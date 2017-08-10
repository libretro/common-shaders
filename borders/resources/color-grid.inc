
// Based on Color Grid Shadertoy - https://www.shadertoy.com/view/4dBSRK
// Created by inigo quilez - iq/2014
// License Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License.

#include "../../compat_includes.inc"

uniform COMPAT_Texture2D(decal) : TEXUNIT0;
uniform COMPAT_Texture2D(bg) : TEXUNIT1;
uniform float4x4 modelViewProj;

struct out_vertex{
   float4 position : COMPAT_POS;
   float2 tex : TEXCOORD;
   float2 tex_border : TEXCOORD1;
};

out_vertex main_vertex(COMPAT_IN_VERTEX)
{
#ifdef HLSL_4
	float4 position = VIN.position;
	float2 tex = VIN.texCoord;
	float2 tex_border = VIN.t1;
#else
	float2 tex = texCoord;
	float2 tex_border = t1;
#endif
   out_vertex OUT;

   OUT.position = mul(modelViewProj, position);
   
   float2 out_res = float2(out_res_x, out_res_y);
   float2 corrected_size = float2(in_res_x, in_res_y) * (box_scale / box_scale);
   float2 scale = (COMPAT_output_size / corrected_size) / box_scale;
   float2 middle = location * COMPAT_video_size / COMPAT_texture_size;
   float2 diff = tex.xy - middle;
   OUT.tex = middle + diff * scale;

   middle = float2(0.49999, 0.49999);
   float2 dist = tex_border - middle;
   OUT.tex_border = middle + dist * COMPAT_output_size / out_res;
   return OUT;
}

float4 conv_background(float4 back, float2 coord, float frame_count)
{
   return float4(back.rgb, back.a);
}

float4 main_fragment(COMPAT_IN_FRAGMENT) : COMPAT_Output
{
#ifdef HLSL_4
	float4 position = VOUT.position;
	float2 tex = VOUT.tex;
	float2 tex_border = VOUT.tex_border;
#else
	float4 position = VOUT.position;
	float2 tex = VOUT.tex;
	float2 tex_border = VOUT.tex_border;
#endif

    float2  px = 1000.0 *(-COMPAT_texture_size.xy + 2.0 * ZOOM * (tex.xy*(COMPAT_texture_size.xy/COMPAT_video_size.xy)).xy) / COMPAT_texture_size.y;
	
    float id = 0.5 + 0.5*cos(COMPAT_frame_count * 0.01 * SPEED + sin(dot(floor(px+0.5),float2(113.1,17.81)))*43758.545);
    
    float3  co = 0.5 + 0.5*cos(COMPAT_frame_count * 0.01 + 3.5*id + float3(0.0,1.57,3.14) );
    
    float2  pa = smoothstep( 0.0, 0.2, id*(0.5 + 0.5*cos(6.2831*px)) );

	float4 colorgrid = float4( co*pa.x*pa.y, 1.0 );
	
   float4 frame = COMPAT_SamplePoint(decal, tex);
   float2 fragcoord = tex.xy * (COMPAT_texture_size.xy/COMPAT_video_size.xy);
   float4 background = conv_background(COMPAT_SamplePoint(bg, tex_border), tex_border, COMPAT_frame_count);
   if (fragcoord.x < 1.0 && fragcoord.x > 0.0 && fragcoord.y < 1.0 && fragcoord.y > 0.0 && border_on_top > 0.5)
   background.a *= 0.0;
   return lerp(frame, colorgrid, background.a);
}
COMPAT_END