struct out_vertex
{
	float4 position : COMPAT_POS;
	float2 texCoord : TEXCOORD0;
	float2 pix_no   : TEXCOORD1;
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
	OUT.pix_no = texCoord * COMPAT_texture_size * (COMPAT_output_size / COMPAT_video_size);
	
	return OUT;
}