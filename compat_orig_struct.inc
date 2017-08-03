#ifndef COMPAT_ORIG_STRUCT
	#define COMPAT_ORIG_STRUCT

	#if defined(HLSL_4)
		struct orig
		{
			bool dummy;
		};
		
		cbuffer orig : register(b1)
		{
			float2 video_size;
			float2 texture_size;
			float2 output_size;
		};
		
		#define INITIALIZE_ORIG(c) Texture2D ORIG: register(t##c);
		#define ORIG_Sample(coord) ORIG.Sample(PointSampler, coord)
		#define ORIG_texture ORIG
	#else
		struct orig
		{
			float2 video_size;
			float2 texture_size;
			float2 output_size;
			sampler2D texture;
		};
		#define INITIALIZE_PASSPREV(c) 
		#define ORIG_Sample(coord) tex2D(ORIG, coord)
		#define ORIG_texture ORIG.texture
	#endif
#endif // COMPAT_ORIG_STRUCT