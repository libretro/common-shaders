// Animated Border Cg shader
// Copyright (c) 2014 Mudlord licensed under the WTFPL.

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

float4 mudscape(float2 texture_size, float frame_count, float2 uv)
{
	float2 sp = uv;
	float2 p = sp*PARAM1 - float2(PARAM2, PARAM2);
	float2 i = p;
	float c = 1.0;
	float inten = PARAM6;//0.01;
	float t = 0.01 * PARAM3 * frame_count* (1.0 - (3.0 / float(0+1)));
	i = p + float2(cos(t - i.x) + sin(t + i.y), sin(t - i.y) + cos(t + i.x));
	c += 1.2/length(float2(p.x / (sin(i.x+t)/inten),p.y / (cos(i.y+t)/inten)));
	c /= PARAM5;//1.5;
	c = PARAM4-sqrt(c);
	float4 color = float4(R,G,B,1.0);

	return float4(float3(c*c*c*c, c*c*c*c, c*c*c*c), 9999.0) + color;;
}

float4 effect_border(float2 texture_size, float2 video_size, float frame_count, float2 tex,
	COMPAT_Texture2D(decal), float2 tex_border, COMPAT_Texture2D(bg))
{
	float4 effect = mudscape(texture_size, frame_count, fragcoord);
	
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
