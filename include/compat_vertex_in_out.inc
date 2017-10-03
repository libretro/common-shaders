#ifndef COMPAT_VERTEX_IN_OUT
	#define COMPAT_VERTEX_IN_OUT
	
	#ifdef HLSL_4	
		struct in_vertex
		{
			float4 position : COMPAT_POS;
			float2 texCoord : TEXCOORD0;
			float2 t1 : TEXCOORD1;
		};

		#define COMPAT_IN_VERTEX in_vertex VIN
		#define COMPAT_IN_FRAGMENT out_vertex VOUT
	#else
		struct in_vertex
		{
			bool dummy;
		};
		
		#define COMPAT_IN_VERTEX in_vertex VIN, uniform input IN, float4 color : COLOR, float4 position : COMPAT_POS, float2 texCoord : TEXCOORD0, float2 t1 : TEXCOORD1
		#define COMPAT_IN_FRAGMENT out_vertex VOUT, uniform input IN
	#endif
#endif // COMPAT_VERTEX_IN_OUT