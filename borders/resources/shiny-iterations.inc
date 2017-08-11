
// Based on Iterations - shiny Shadertoy - https://www.shadertoy.com/view/MslXz8
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

float4 shiny_iterations(float2 texture_size, float frame_count, float2 uv)
{
	float2 pc = uv * 5.0;

	float2 pa = pc + float2(0.04,0.0);
	float2 pb = pc + float2(0.0,0.04);
	
    // shape (3 times for diferentials)
	float2 zc = pc;
	float3 fc = float3( 0.0, 0.0, 0.0 );
	for( int i=0; i<8; i++ ) 
	{
        // transform		
		zc += cos(zc.yx + cos(zc.yx + cos(zc.yx+frame_count * 0.01 * SPEED) ) );

        // orbit traps		
		float d = dot( zc-pc, zc-pc ); 
		fc.x += 1.0/(1.0+d);
		fc.y += d;
		fc.z += sin(atan2(zc.x-pc.x, zc.y-pc.y));
	}
	fc /= 8.0;
	float3 sc = fc;
	
	float2 za = pa;
	float3 fa = float3( 0.0, 0.0, 0.0 );
		for( int j=0; j<8; j++ ) 
	{
        // transform		
		za += cos(za.yx + cos(za.yx + cos(za.yx+frame_count * 0.01 * SPEED) ) );

        // orbit traps		
		float d = dot( za-pa, za-pa ); 
		fa.x += 1.0/(1.0+d);
		fa.y += d;
		fa.z += sin(atan2(zc.x-pc.x, zc.y-pc.y));
	}
	fa /= 8.0;
	float3 sa = fa;
	
	float2 zb = pb;
	float3 fb = float3( 0.0, 0.0, 0.0 );
		for( int k=0; k<8; k++ ) 
	{
        // transform		
		zb += cos(zb.yx + cos(zb.yx + cos(zb.yx+frame_count * 0.01 * SPEED) ) );

        // orbit traps		
		float d = dot( zb-pb, zb-pb ); 
		fb.x += 1.0/(1.0+d);
		fb.y += d;
		fb.z += sin(atan2(zc.x-pc.x, zc.y-pc.y));
	}
	fb /= 8.0;
	float3 sb = fb;

    // color	
	float3 col = lerp( float3(0.08,0.02,0.15), float3(0.6,1.1,1.6), sc.x );
	col = lerp( col, col.zxy, smoothstep(-0.5,0.5,cos(0.01*frame_count * COL_SHFT)) );
	col *= 0.15*sc.y;
	col += 0.4*abs(sc.z) - 0.1;

    // light	
	float3 nor = normalize( float3( sa.x-sc.x, 0.01, sb.x-sc.x ) );
	float dif = clamp(0.5 + 0.5*dot( nor,float3(0.5773, 0.5773, 0.5773) ),0.0,1.0);
	col *= 1.0 + 0.7*dif*col;
	col += 0.3 * pow(nor.y,128.0);

    // vignetting	
	col *= 1.0 - 0.1*length(pc);
	return float4(col, 1.0);
}

float4 effect_border(float2 texture_size, float2 video_size, float frame_count, float2 tex,
	COMPAT_Texture2D(decal), float2 tex_border, COMPAT_Texture2D(bg))
{
	float4 effect = shiny_iterations(texture_size, frame_count, fragcoord);
	
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
