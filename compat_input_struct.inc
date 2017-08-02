#ifndef COMPAT_INPUT_STRUCTS
	#define COMPAT_INPUT_STRUCTS

	#if defined(HLSL_4)
		cbuffer input : register(b0)
	#else
		struct input
	#endif
		{
			float2 video_size;
			float2 texture_size;
			float2 output_size;
			float  frame_count;
			float  frame_direction;
		};

#endif // COMPAT_INPUT_STRUCTS