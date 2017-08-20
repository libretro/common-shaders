#ifndef COMPAT_MACROS
	#define COMPAT_MACROS

	#if defined(HLSL_4)
		SamplerState LinearSampler { Filter = MIN_MAG_LINEAR_MIP_POINT; AddressU = Clamp; AddressV = Clamp; };
		SamplerState PointSampler { Filter = MIN_MAG_MIP_POINT; AddressU = Clamp; AddressV = Clamp; };
		#define mod(x,y) (x - y * trunc(x/y))
		#define fract(x) (frac(x))
		#define COMPAT_Texture2D(tex) Texture2D tex
		#define COMPAT_TexturePass2D(tex) tex
		#define COMPAT_SampleLevelZero(tex, coord) tex.SampleLevel(LinearSampler, coord, 0)
		#define COMPAT_SampleLevelZeroPoint(tex, coord) tex.SampleLevel(PointSampler, coord, 0)
		#define COMPAT_SampleLevelZeroOffset(tex, coord, offset) tex.SampleLevel(LinearSampler, coord, 0, offset)
		#define COMPAT_Sample(tex, coord) tex.Sample(LinearSampler, coord)
		#define COMPAT_SamplePoint(tex, coord) tex.Sample(PointSampler, coord)
		#define COMPAT_SampleOffset(tex, coord, offset) tex.Sample(LinearSampler, coord, offset)
		#define COMPAT_FLATTEN [flatten]
		#define COMPAT_BRANCH [branch]
		#define COMPAT_Texture2DMS2(tex) Texture2DMS<float4, 2> tex
		#define COMPAT_Load(tex, pos, sample) tex.Load(pos, sample)
		#define COMPAT_Output SV_Target
		#define half float
		#define half2 float2
		#define half3 float3
		#define half4 float4
		#define half3x3 float3x3
		#define half2x2 float2x2
		#define half4x4 float4x4
		#define half4x3 float4x3
		#define COMPAT_POS SV_POSITION
	#else
		#define COMPAT_Texture2D(tex) sampler2D tex
		#define COMPAT_TexturePass2D(tex) tex
		#define COMPAT_SampleLevelZero(tex, coord) tex2Dlod(tex, float4(coord, 0.0, 0.0))
		#define COMPAT_SampleLevelZeroPoint(tex, coord) tex2Dlod(tex, float4(coord, 0.0, 0.0))
		#define COMPAT_SampleLevelZeroOffset(tex, coord, offset) tex2Dlod(tex, float4(coord + offset, 0.0, 0.0))
		#define COMPAT_Sample(tex, coord) tex2D(tex, coord)
		#define COMPAT_SamplePoint(tex, coord) tex2D(tex, coord)
		#define COMPAT_SampleOffset(tex, coord, offset) tex2D(tex, coord + offset)
		#define COMPAT_FLATTEN [flatten]
		#define COMPAT_BRANCH [branch]
		#define COMPAT_Output COLOR
		#define COMPAT_POS POSITION
	#endif
	#if defined(HLSL_FX)
		#define COMPAT_END \
			technique11 TEQ \
			{ \
			  pass P0 \
			  { \
				SetVertexShader( CompileShader( vs_4_0, main_vertex() ) ); \
				SetPixelShader( CompileShader( ps_4_0, main_fragment() ) ); \
			  } \
			};
	#else
		#define COMPAT_END
	#endif
#endif // COMPAT_MACROS