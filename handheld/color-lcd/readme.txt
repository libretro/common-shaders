LUT Shaders and Textures are based from Aybe's CMYK shaders.
Used to create the GBA (Original and SP AGS-001) and NDS (PHAT) to output the same color matrix display as the real hardware.
Must have at least 512 MB of your GPU and update to the latest Retroarch builds and drivers. Opengl is the only backend to support LUT Textures.
Standard represents the actual view from the console that mimics the backlight and brightness of the handheld consoles.
Fullrange outputs it with 0-255 value.
XBR includes the XBR-LV3 shader for scaling.
Lcdmotion adds the LCD and Motion Blur to the output.

PSP Shader is only a .cgp that uses the image-adjustment.cg shader to adjust the image that mimics the display of PSP 1000 or 2000 models.
Didn't need the LUT texture for this. May work for D3D backend but tested in Opengl.
LCD .cgp is also included in the package using LCD shader and Motion Blur.