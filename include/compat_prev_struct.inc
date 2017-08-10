#ifndef COMPAT_PREV_STRUCT
	#define COMPAT_PREV_STRUCT

	#if defined(HLSL_4)
		struct prev
		{
			bool dummy;
		};
		
		cbuffer prev : register(b1)
		{
			float2 prev_video_size;
			float2 prev_texture_size;
			float2 prev_output_size;
		};
		
		#define INITIALIZE_PASSPREV(c, d) Texture2D PASSPREV##c: register(t##d);
		#define PASSPREV_Sample(c, coord) PASSPREV##c.Sample(LinearSampler, coord)
		#define PASSPREV_SamplePoint(c, coord) PASSPREV##c.Sample(PointSampler, coord)
		#define PASSPREV_texture(c) PASSPREV##c
	#else
		struct prev
		{
			float2 video_size;
			float2 texture_size;
			float2 output_size;
			sampler2D texture;
		};
		#define INITIALIZE_PASSPREV(c, d) 
		#define PASSPREV_Sample(c, coord) tex2D(PASSPREV##c, coord)
		#define PASSPREV_SamplePoint(c, coord) tex2D(PASSPREV##c, coord)
		#define PASSPREV_texture(c) PASSPREV##c.texture
	#endif
#endif // COMPAT_PREV_STRUCT