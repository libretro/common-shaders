#ifndef COMPAT_ORIG_STRUCT
	#define COMPAT_ORIG_STRUCT

	#if defined(HLSL_4)
		struct orig
		{
			bool dummy;
		};
		
		cbuffer orig : register(b1)
		{
			float2 orig_video_size;
			float2 orig_texture_size;
			float2 orig_output_size;
		};
		
		#define INITIALIZE_ORIG(c) Texture2D ORIGtex: register(t##c);
		#define ORIG_Sample(coord) ORIGtex.Sample(LinearSampler, coord)
		#define ORIG_SamplePoint(coord) ORIGtex.Sample(PointSampler, coord)
		#define ORIG_texture ORIGtex
	#else
		struct orig
		{
			float2 video_size;
			float2 texture_size;
			float2 output_size;
			sampler2D texture;
		};
		#define INITIALIZE_ORIG(c) 
		#define ORIG_Sample(coord) tex2D(ORIG, coord)
		#define ORIG_SamplePoint(coord) tex2D(ORIG, coord)
		#define ORIG_texture ORIG.texture
		#define ORIG_video_size ORIG.video_size
		#define ORIG_texture_size ORIG.texture_size
		#define ORIG_output_size ORIG.output_size
	#endif
#endif // COMPAT_ORIG_STRUCT