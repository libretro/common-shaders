
/*
   Author: Themaister
   License: Public domain
*/

// Border shader :)

struct input
{
   float2 video_size;
   float2 texture_size;
   float2 output_size;
   float frame_count;
   float frame_direction;
   float frame_rotation;
};

void main_vertex
(
   float4 position : POSITION,
   out float4 oPosition : POSITION,
   uniform float4x4 modelViewProj,

   float4 color : COLOR,
   out float4 oColor : COLOR,

   float2 tex : TEXCOORD,
   out float2 oTex : TEXCOORD,

   float2 tex_border : TEXCOORD1,
   out float2 otex_border : TEXCOORD1,

   uniform input IN
)
{
   oPosition = mul(modelViewProj, position);
   oColor = color;

   float2 out_res = float2(out_res_x, out_res_y);   
   float2 corrected_size = float2(in_res_x, in_res_y);
   float2 scale = (IN.output_size / corrected_size) / box_scale;
   float2 middle = location * IN.video_size / IN.texture_size;
   float2 diff = tex.xy - middle;
   oTex = middle + diff * scale;

   middle = float2(0.5, 0.5);
   float2 dist = tex_border - middle;
   otex_border = middle + dist * IN.output_size / out_res;
}

float4 conv_background(float4 back, float2 coord, float frame_count)
{
   return float4(back.rgb, back.a);
}

float4 main_fragment (
   float2 tex : TEXCOORD0, float2 tex_border : TEXCOORD1,
   uniform sampler2D s0 : TEXUNIT0,
   uniform sampler2D bg,
   uniform input IN) : COLOR
{
   float4 frame = tex2D(s0, tex);
   float2 fragcoord = tex.xy * (IN.texture_size.xy/IN.video_size.xy);
   float4 background = conv_background(tex2D(bg, tex_border), tex_border, IN.frame_count);
   background.a *= opacity / 100.0;
   if (fragcoord.x < 1.0 && fragcoord.x > 0.0 && fragcoord.y < 1.0 && fragcoord.y > 0.0 && border_on_top < 0.5)
   background.a *= 0.0;
   return lerp(frame, background, background.a);
}
