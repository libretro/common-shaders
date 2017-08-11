
// Snowy Border Cg shader, based on Andrew Baldwin's 'Just Snow' shadertoy, licensed below:
// Copyright (c) 2013 Andrew Baldwin (twitter: baldand, www: http://thndl.com)
// License = Attribution-NonCommercial-ShareAlike (http://creativecommons.org/licenses/by-nc-sa/3.0/deed.en_US)

// "Just snow"
// Simple (but not cheap) snow made from multiple parallax layers with randomly positioned 
// flakes and directions. Also includes a DoF effect. Pan around with mouse.

#define LAYERS 15.0
#define DEPTH 1.0
#define WIDTH 0.5
#define SPEED -.03

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

float4 snow(float2 texture_size, float frame_count, float2 uv)
{
	const float3x3 p = float3x3(13.323122,21.1212,21.8112,23.5112,28.7312,14.7212,21.71123,11.9312,61.3934);
	float3 acc = float3(R, G, B);
	float dof = 5.*sin(frame_count*.1);
	for (int i=0;i<LAYERS;i++) {
		float fi = float(i);
		float2 q = uv*(1.+fi*DEPTH);
		q += float2(q.y*(WIDTH*fmod(abs(fi*7.238917),1.)-WIDTH*.5),SPEED*frame_count/(1.+fi*DEPTH*.03));
		float3 n = float3(floor(q),31.189+fi);
		float3 m = floor(n)*.00001 + frac(n);
		float3 mp = (31415.9+m)/frac(mul(p,m));
		float3 r = frac(mp);
		float2 s = abs(fmod(abs(q),1.)-.5+.9*r.xy-.45);
		s += .01*abs(2.*frac(10.*q.yx)-1.); 
		float d = .6*max(s.x-s.y,s.x+s.y)+max(s.x,s.y)-.01;
		float edge = .05+.05*min(.5*abs(fi-5.-dof),1.);
		float acc_mod = smoothstep(edge,-edge,d)*(r.x/(1.+.02*fi*DEPTH));
		acc += float3(acc_mod, acc_mod, acc_mod);
	}
	return float4(float3(acc),1.0);
}

float4 effect_bg(float2 texture_size, float2 video_size, float frame_count, float2 tex,
	COMPAT_Texture2D(decal), float2 tex_border, COMPAT_Texture2D(bg))
{
	float4 effect = snow(texture_size, frame_count, fragcoord);
	
	float4 frame = COMPAT_SamplePoint(decal, tex);
	float4 background = conv_background(COMPAT_SamplePoint(bg, tex_border), tex_border, frame_count);
	if (fragcoord.x < 1.0 && fragcoord.x > 0.0 && fragcoord.y < 1.0 && fragcoord.y > 0.0 && border_on_top > 0.5)
		background.a *= 0.0;
	
	return lerp(frame, effect, background.a);
}

float4 main_fragment(COMPAT_IN_FRAGMENT) : COMPAT_Output
{
	return effect_bg(COMPAT_texture_size, COMPAT_video_size, COMPAT_frame_count,
		VOUT.texCoord, decal, VOUT.tex_border, bg);
}
COMPAT_END