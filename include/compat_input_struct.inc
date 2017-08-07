#ifndef COMPAT_INPUT_STRUCT
	#define COMPAT_INPUT_STRUCT

	#if defined(HLSL_4)
		struct input
		{
			bool dummy;
		};
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
	#if defined(HLSL_4)
		#define COMPAT_video_size video_size
		#define COMPAT_texture_size texture_size
		#define COMPAT_output_size output_size
		#define COMPAT_frame_count frame_count
		#define COMPAT_frame_direction frame_direction
	#else
		#define COMPAT_video_size IN.video_size
		#define COMPAT_texture_size IN.texture_size
		#define COMPAT_output_size IN.output_size
		#define COMPAT_frame_count IN.frame_count
		#define COMPAT_frame_direction IN.frame_direction
	#endif
#endif // COMPAT_INPUT_STRUCT