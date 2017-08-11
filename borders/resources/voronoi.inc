// Based on Voronoi - smooth Shadertoy - https://www.shadertoy.com/view/ldB3zc
// Created by inigo quilez - iq/2014
// License Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License.

#include "../../compat_includes.inc"

uniform COMPAT_Texture2D(decal) : TEXUNIT0;
uniform COMPAT_Texture2D(bg) : TEXUNIT1;
uniform float4x4 modelViewProj;

struct out_vertex{
   float4 position : COMPAT_POS;
   float2 texCoord : TEXCOORD;
   float2 tex_border : TEXCOORD1;
};

out_vertex main_vertex(COMPAT_IN_VERTEX)
{
#ifdef HLSL_4
	float4 position = VIN.position;
	float2 texCoord = VIN.texCoord;
	float2 t1 = VIN.t1;
#endif
   out_vertex OUT;

   OUT.position = mul(modelViewProj, position);
   
   float2 out_res = float2(out_res_x, out_res_y);
   float2 corrected_size = float2(in_res_x, in_res_y) * (box_scale / box_scale);
   float2 scale = (COMPAT_output_size / corrected_size) / box_scale;
   float2 middle = location * COMPAT_video_size / COMPAT_texture_size;
   float2 diff = texCoord.xy - middle;
   OUT.texCoord = middle + diff * scale;

   middle = float2(0.49999, 0.49999);
   float2 dist = t1 - middle;
   OUT.tex_border = middle + dist * COMPAT_output_size / out_res;
   return OUT;
}

#define fragcoord (tex.xy * (texture_size.xy/video_size.xy))

float4 conv_background(float4 back, float2 coord, float frame_count)
{
   return float4(back.rgb, back.a);
}

float hash1( float n )
{
	return frac(sin(n)*43758.5453);
}

float2 hash2( float2  p )
{
	p = float2( dot(p,float2(127.1,311.7)), dot(p,float2(269.5,183.3)) );
	return frac(sin(p)*43758.5453);
}

float4 voronoi( in float2 x, float w, float frame_count )
{
    float2 n = floor( x );
    float2 f = frac( x );

	float4 m = float4( 8.0, 0.0, 0.0, 0.0 );
    for( int j=-1; j<=2; j++ )
    for( int i=-1; i<=2; i++ )
    {
        float2 g = float2( float(i),float(j) );
        float2 o = hash2( n + g );
		
		// animate
        o = 0.5 + 0.5*sin( 0.01 * frame_count + 6.2831*o );

        // distance to cell		
		float d = length(g - f + o);
		
        // do the smooth min for colors and distances		
		float3 col = 0.5 + 0.5*sin( hash1(dot(n+g,float2(7.0,113.0)))*2.5 + 3.5 + float3(2.0,3.0,0.0));
		float h = smoothstep( 0.0, 1.0, 0.5 + 0.5*(m.x-d)/w );
		
	    m.x   = lerp( m.x,     d, h ) - h*(1.0-h)*w/(1.0+3.0*w); // distance
		m.yzw = lerp( m.yzw, col, h ) - h*(1.0-h)*w/(1.0+3.0*w); // cioloe
    }
	
	return m;
}

float4 voronoi_bg(float2 texture_size, float frame_count, float2 uv)
{
    float2 p = uv * float2(2.0,1.0);
	
	float k = 2.0 + 70.0 * pow( 0.5 + 0.5*sin(0.25*6.2831*0.03 * frame_count), 4.0 );
	k = 0.5 - 0.5*cos(0.25*6.2831*0.01 * frame_count);
    float4 c = voronoi( 6.0*p, k, frame_count );

    float3 col = c.yzw;
	
	col *= 1.0 - 0.8*c.x*step(p.y,0.33);
	col *= lerp(c.x,1.0,step(p.y,0.66));
	
	col *= smoothstep( 0.005, 0.007, abs(p.y-0.33) );
	col *= smoothstep( 0.005, 0.007, abs(p.y-0.66) );
	
	return float4( col, 1.0 );
}

float4 effect_border(float2 texture_size, float2 video_size, float frame_count, float2 tex,
	COMPAT_Texture2D(decal), float2 tex_border, COMPAT_Texture2D(bg))
{
	float4 effect = voronoi_bg(texture_size, frame_count, fragcoord);
	
	float4 frame = COMPAT_SamplePoint(decal, tex);
	float4 background = conv_background(COMPAT_SamplePoint(bg, tex_border), tex_border, frame_count);
	if (fragcoord.x < 1.0 && fragcoord.x > 0.0 && fragcoord.y < 1.0 && fragcoord.y > 0.0 && border_on_top > 0.5)
		background.a *= 0.0;
	
	return lerp(frame, effect, background.a);
}

float4 main_fragment(COMPAT_IN_FRAGMENT) : COMPAT_Output
{
	return effect_border(COMPAT_texture_size, COMPAT_video_size, COMPAT_frame_count,
		VOUT.texCoord, decal, VOUT.tex_border, bg);
}
COMPAT_END