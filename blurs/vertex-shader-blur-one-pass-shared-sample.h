#ifndef VERTEX_SHADER_BLUR_ONE_PASS_SHARED_SAMPLE_H
#define VERTEX_SHADER_BLUR_ONE_PASS_SHARED_SAMPLE_H

/////////////////////////////////  MIT LICENSE  ////////////////////////////////

//  Copyright (C) 2014 TroggleMonkey
//
//  Permission is hereby granted, free of charge, to any person obtaining a copy
//  of this software and associated documentation files (the "Software"), to
//  deal in the Software without restriction, including without limitation the
//  rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
//  sell copies of the Software, and to permit persons to whom the Software is
//  furnished to do so, subject to the following conditions:
//
//  The above copyright notice and this permission notice shall be included in
//  all copies or substantial portions of the Software.
//
//  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
//  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
//  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
//  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
//  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
//  FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
//  IN THE SOFTWARE.


/////////////////////////////  SETTINGS MANAGEMENT  ////////////////////////////

//  PASS SETTINGS:
//  Pass settings should be set by the .cg file that #includes this one.


//////////////////////////////////  INCLUDES  //////////////////////////////////

#include "../include/gamma-management.h"
#include "../include/blur-functions.h"


/////////////////////////////////  STRUCTURES  /////////////////////////////////

struct input
{
    float2 video_size;
    float2 texture_size;
    float2 output_size;
    float frame_count;
    float frame_direction;
    float frame_rotation;
};

struct out_vertex
{
    float4 position         : POSITION;
    float4 tex_uv           : TEXCOORD0;
    float4 output_pixel_num : TEXCOORD1;
    float2 blur_dxdy        : TEXCOORD2;
};


////////////////////////////////  VERTEX SHADER  ///////////////////////////////

out_vertex main_vertex
(
	float4 position : POSITION,
	float4 color    : COLOR,
	float2 tex_uv   : TEXCOORD0,
	uniform float4x4 modelViewProj,
	uniform input IN
)
{
	out_vertex OUT;
    const float4 out_position = mul(modelViewProj, position);
	OUT.position = out_position;

	//  Get the uv sample distance between output pixels.  Blurs are not generic
    //  Gaussian resizers, and correct blurs require:
    //  1.) IN.output_size == IN.video_size * 2^m, where m is an integer <= 0.
    //  2.) mipmap_inputN = "true" for this pass in .cgp preset if m < 0
    //  3.) filter_linearN = "true" for all one-pass blurs
    //  4.) #define DRIVERS_ALLOW_TEX2DLOD for shared-sample blurs
    //  Gaussian resizers would upsize using the distance between input texels
    //  (not output pixels), but we avoid this and consistently blur at the
    //  destination size.  Otherwise, combining statically calculated weights
    //  with bilinear sample exploitation would result in terrible artifacts.
    const float2 dxdy_scale = IN.video_size/IN.output_size;
	OUT.blur_dxdy = dxdy_scale/IN.texture_size;

    //  Get the output pixel number in ([0, xres), [0, yres)) with respect to
    //  the uv origin (.xy components) and the screen origin (.zw components).
    //  Both are useful.  Don't round until the fragment shader.
    const float2 video_uv = tex_uv * (IN.texture_size / IN.video_size);
    OUT.output_pixel_num.xy = IN.output_size * float2(video_uv.x, video_uv.y);
    OUT.output_pixel_num.zw = IN.output_size *
        (out_position.xy * 0.5 + float2(0.5));

    //  Set the mip level correctly for shared-sample blurs (where the
    //  derivatives are unreliable):
    const float mip_level = log2(IN.video_size/IN.output_size).y;
    OUT.tex_uv = float4(tex_uv, 0.0, mip_level);

	return OUT;
}


#endif  //  VERTEX_SHADER_BLUR_ONE_PASS_SHARED_SAMPLE_H

