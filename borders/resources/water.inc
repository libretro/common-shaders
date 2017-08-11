/*
   Author: Themaister
   License: Public domain
*/

// Border shader :)

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

float apply_wave(float2 pos, float2 src, float cnt)
{
   float2 diff = pos - src;
   float dist = 300.0 * sqrt(dot(diff, diff));
   dist -= 0.15 * cnt;
   return sin(dist);
}

const float2 src0 = float2(0.6, 0.7);
const float2 src1 = float2(0.9, 0.9);
const float2 src2 = float2(-0.6, 0.3);
const float2 src3 = float2(0.1, 0.4);
const float2 src4 = float2(0.1, 0.4);
const float2 src5 = float2(0.5, 0.5);
const float2 src6 = float2(-1.0, 1.0);

float4 conv_background(float4 back, float2 coord, float frame_count)
{
   float cnt = frame_count;
   float res = apply_wave(coord, src0, cnt);
   res +=      apply_wave(coord, src1, cnt);
   res +=      apply_wave(coord, src2, cnt);
   res +=      apply_wave(coord, src3, cnt);
   res +=      apply_wave(coord, src4, cnt);
   res +=      apply_wave(coord, src5, cnt);
   res +=      apply_wave(coord, src6, cnt);

   return float4(back.rgb * (0.7 + 0.05 * res), back.a);
}

float4 effect_border(float2 texture_size, float2 video_size, float frame_count, float2 tex,
	COMPAT_Texture2D(decal), float2 tex_border, COMPAT_Texture2D(bg))
{
	float4 frame = COMPAT_SamplePoint(decal, tex);
	float4 background = conv_background(COMPAT_SamplePoint(bg, tex_border), tex_border, frame_count);
	if (fragcoord.x < 1.0 && fragcoord.x > 0.0 && fragcoord.y < 1.0 && fragcoord.y > 0.0 && border_on_top > 0.5)
		background.a *= 0.0;
	
	return lerp(frame, background, background.a);
}

float4 main_fragment(COMPAT_IN_FRAGMENT) : COMPAT_Output
{
	return effect_border(COMPAT_texture_size, COMPAT_video_size, COMPAT_frame_count,
		VOUT.texCoord, decal, VOUT.tex_border, bg);
}
COMPAT_END