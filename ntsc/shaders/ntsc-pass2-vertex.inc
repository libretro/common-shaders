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
	OUT.texCoord = texCoord - float2(0.5 / COMPAT_texture_size.x, 0.0); // Compensate for decimate-by-2.
	
	return OUT;
}