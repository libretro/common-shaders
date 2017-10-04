/* COMPATIBILITY
   - HLSL compilers
   - Cg   compilers
   - FX11 compilers
*/

#include "../../compat_includes.inc"
uniform COMPAT_Texture2D(decal) : TEXUNIT0;
uniform float4x4 modelViewProj;

struct out_vertex
{
	float4 position : COMPAT_POS;
	float2 texCoord : TEXCOORD0;
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
	OUT.texCoord = texCoord;
	return OUT;
}

float4 crt_nes_mini(float2 texture_size, float2 co, COMPAT_Texture2D(tex))
{
    float3 texel = COMPAT_Sample(tex, co).rgb;
    float3 pixelHigh = (1.2 - (0.2 * texel)) * texel;
    float3 pixelLow  = (0.85 + (0.1 * texel)) * texel;
    float selectY = fmod(co.y * 2 * texture_size.y, 2.0);
    float selectHigh = step(1.0, selectY);
    float selectLow = 1.0 - selectHigh;
    float3 pixelColor = (selectLow * pixelLow) + (selectHigh * pixelHigh);

    return float4(pixelColor, 1.0);
}

float4 main_fragment(COMPAT_IN_FRAGMENT) : COMPAT_Output
{
	return crt_nes_mini(COMPAT_texture_size, VOUT.texCoord, decal);
}
COMPAT_END
