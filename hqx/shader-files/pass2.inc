/*
* Copyright (C) 2003 Maxim Stepin ( maxst@hiend3d.com )
*
* Copyright (C) 2010 Cameron Zemek ( grom@zeminvaders.net )
*
* Copyright (C) 2014 Jules Blok ( jules@aerix.nl )
*
* This program is free software; you can redistribute it and/or
* modify it under the terms of the GNU Lesser General Public
* License as published by the Free Software Foundation; either
* version 2.1 of the License, or (at your option) any later version.
*
* This program is distributed in the hope that it will be useful,
* but WITHOUT ANY WARRANTY; without even the implied warranty of
* MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
* Lesser General Public License for more details.
*
* You should have received a copy of the GNU Lesser General Public
* License along with this program; if not, write to the Free Software
* Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
*/

/* COMPATIBILITY 
   - HLSL compilers
   - Cg   compilers
   - FX11 compilers
*/

#include "../../compat_includes.inc"
uniform COMPAT_Texture2D(decal) : TEXUNIT0;
uniform COMPAT_Texture2D(LUT)   : TEXUNIT1;
uniform float4x4 modelViewProj;

INITIALIZE_ORIG(0)

struct out_vertex
{
	float4 position : COMPAT_POS;
	float2 texCoord : TEXCOORD0;
	float2 ps       : TEXCOORD1;
#ifndef HLSL_4
	float4 Color    : COLOR;
#endif
};

out_vertex main_vertex(COMPAT_IN_VERTEX)
{
	out_vertex OUT;
#ifdef HLSL_4
	float4 position = VIN.position;
	float2 texCoord = VIN.texCoord;
#else
	OUT.Color = color;
#endif
	OUT.position = mul(modelViewProj, position);
	OUT.ps = 1.0/COMPAT_texture_size;
	OUT.texCoord = texCoord;
	
	return OUT;
}

	//   +----+----+----+
	//   |    |    |    |
	//   | w1 | w2 | w3 |
	//   +----+----+----+
	//   |    |    |    |
	//   | w4 | w5 | w6 |
	//   +----+----+----+
	//   |    |    |    |
	//   | w7 | w8 | w9 |
	//   +----+----+----+

/*    FRAGMENT SHADER    */
float4 hqx(float2 Current_texture_size, float2 Original_texture_size, float2 ps,
	float2 texCoord, COMPAT_Texture2D(Current), COMPAT_Texture2D(Original), COMPAT_Texture2D(LookupTexture))
{
	float2 fp = frac(texCoord * Current_texture_size);
	float2 quad = sign(-0.5 + fp);

	float dx = ps.x;
	float dy = ps.y;

	float3 p1  = COMPAT_SamplePoint(Original, texCoord).rgb;
	float3 p2  = COMPAT_SamplePoint(Original, texCoord + float2(dx, dy) * quad).rgb;
	float3 p3  = COMPAT_SamplePoint(Original, texCoord + float2(dx, 0) * quad).rgb;
	float3 p4  = COMPAT_SamplePoint(Original, texCoord + float2(0, dy) * quad).rgb;
	float4x3 pixels = float4x3(p1, p2, p3, p4);

	float2 index = COMPAT_SamplePoint(Current, texCoord).xy * float2(255.0, 15.0 * (SCALE * SCALE));
	index.y += dot(floor(fp * SCALE), float2(1, SCALE));

	float2 step = 1.0 / float2(256.0, 16.0 * (SCALE * SCALE));
	float2 offset = step / 2.0;
	float4 weights = COMPAT_SamplePoint(LookupTexture, index * step + offset);
	float sum = dot(weights, float4(1,1,1,1));
	float3 res = mul(transpose(pixels), weights / sum);

	return float4(res, 1.0);
}

float4 main_fragment(in orig ORIG : TEXCOORD2, COMPAT_IN_FRAGMENT) : COMPAT_Output
{
	return hqx(COMPAT_texture_size, ORIG_texture_size, VOUT.ps,
		VOUT.texCoord, decal, ORIG_texture, LUT);
}
COMPAT_END
