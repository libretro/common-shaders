#ifndef COMPAT_MACROS
	#define COMPAT_MACROS

	#if defined(HLSL_4)
		SamplerState LinearSampler { Filter = MIN_MAG_LINEAR_MIP_POINT; AddressU = Clamp; AddressV = Clamp; };
		SamplerState PointSampler { Filter = MIN_MAG_MIP_POINT; AddressU = Clamp; AddressV = Clamp; };
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
	
	// common helper macros
	#define COMPAT_START_SHADER1(t1,v1) t1 v1=IN.v1;
	#define COMPAT_START_SHADER2(t1,v1,t2,v2) t1 v1=IN.v1;t2 v2=IN.v2;
	#define COMPAT_START_SHADER3(t1,v1,t2,v2,t3,v3) t1 v1=IN.v1;t2 v2=IN.v2;t3 v3=IN.v3;
	#define COMPAT_START_SHADER4(t1,v1,t2,v2,t3,v3,t4,v4) t1 v1=IN.v1;t2 v2=IN.v2;t3 v3=IN.v3;t4 v4=IN.v4;
	#define COMPAT_START_SHADER5(t1,v1,t2,v2,t3,v3,t4,v4,t5,v5) t1 v1=IN.v1;t2 v2=IN.v2;t3 v3=IN.v3;t4 v4=IN.v4;t5 v5=IN.v5;
	#define COMPAT_START_SHADER6(t1,v1,t2,v2,t3,v3,t4,v4,t5,v5,t6,v6) t1 v1=IN.v1;t2 v2=IN.v2;t3 v3=IN.v3;t4 v4=IN.v4;t5 v5=IN.v5;t6 v6=IN.v6;
	#define COMPAT_START_SHADER7(t1,v1,t2,v2,t3,v3,t4,v4,t5,v5,t6,v6,t7,v7) t1 v1=IN.v1;t2 v2=IN.v2;t3 v3=IN.v3;t4 v4=IN.v4;t5 v5=IN.v5;t6 v6=IN.v6;t7 v7=IN.v7;
	#define COMPAT_START_SHADER8(t1,v1,t2,v2,t3,v3,t4,v4,t5,v5,t6,v6,t7,v7,t8,v8) t1 v1=IN.v1;t2 v2=IN.v2;t3 v3=IN.v3;t4 v4=IN.v4;t5 v5=IN.v5;t6 v6=IN.v6;t7 v7=IN.v7;t8 v8=IN.v8;
	#define COMPAT_START_SHADER9(t1,v1,t2,v2,t3,v3,t4,v4,t5,v5,t6,v6,t7,v7,t8,v8,t9,v9) t1 v1=IN.v1;t2 v2=IN.v2;t3 v3=IN.v3;t4 v4=IN.v4;t5 v5=IN.v5;t6 v6=IN.v6;t7 v7=IN.v7;t8 v8=IN.v8;t9 v9=IN.v9;
	#define COMPAT_START_SHADER10(t1,v1,t2,v2,t3,v3,t4,v4,t5,v5,t6,v6,t7,v7,t8,v8,t9,v9,t10,v10) t1 v1=IN.v1;t2 v2=IN.v2;t3 v3=IN.v3;t4 v4=IN.v4;t5 v5=IN.v5;t6 v6=IN.v6;t7 v7=IN.v7;t8 v8=IN.v8;t9 v9=IN.v9;t10 v10=IN.v10;
	#define COMPAT_START_SHADER_DEFAULT COMPAT_START_SHADER3(float4, position, float2, texCoord, float2, t1)
	
	#define COMPAT_DEFAULT_VS_SHADER \
		out_vertex main_vertex(out_vertex IN) \
		{ \
		  COMPAT_START_SHADER_DEFAULT \
		  out_vertex OUT; \
		  OUT.position = mul(modelViewProj, position); \
		  OUT.texCoord = texCoord; \
		  OUT.t1 = t1; \
		  return OUT; \
		}
#endif // COMPAT_MACROS