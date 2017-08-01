#if defined(HLSL_4) || defined(HLSL_4_1)
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
#endif
#if defined(HLSL_4_1)
#define COMPAT_Gather(tex, coord) tex.Gather(LinearSampler, coord, 0)
#endif