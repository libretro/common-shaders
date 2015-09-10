# HQx-shader

Cg shader version of the [HQx pixel art upscaling filter](https://code.google.com/p/hqx/).

## How to use

Load the preset files for the desired upscale factor  in an emulator that supports it
such as [RetroArch](http://www.libretro.com/).

## Integration

If you want to implement support for this shader in an emulator you will need to
support loading an additional texture for the shader besides the game output texture.
The texture that needs to be loaded can be found in the `resources` directory.

After you have added support for additional textures you can integrate the single-pass
shader which can be found in the `single-pass/shader-files` directory.

Additionally, for better performance you can support multi-pass shaders that will
reduce redundant computation and thus preform a lot faster than the single-pass
variant. The multi-pass variant can be found in the `shader-files` directory and are
used by the preset files by default.

## Implementation

Like the original HQx filter this shader requires a lookup table. In HQx this lookup table
contains the weights used for interpolating the pixels through a weighted average. More
information on the original algorithm can be found [in the documentation](https://code.google.com/p/hqx/wiki/ReadMe).

The HQx algorithm interpolates the original pixel (w5) with its 8 neighbours.

	//   +----+----+----+
	//   |    |    |    |
	//   | w1 | w2 | w3 |
	//   +----+----+----+
	//   |    |    |    |
	//   | w4 | w5 | w6 |
	//   +----+----+----+
	//   |    |    |    |
	//   | w7 | w8 | w9 |
	//   +----+----+----+
	
All pixels are compared in the YUV color space and the weights for the detected pattern
are retrieved from the look-up texture. The pixels we want to use for the interpolation
are also selected by these weights (the weights of the other pixels are set to zero).

Each entry in the look-up texture has four components to store the weights. The weights
are then applied through a simple matrix-vector multiplication. The pixels in this matrix
will differ based on which upscaled pixel we're processing relative to the original pixel.
For example, if we're in the top-left quadrant relative to the original pixel we will only
ever need to interpolate the pixels w1, w2, w4 and w5.

## Credits

Maxim Stepin and Cameron Zemek for the original C implementation.

Hyllian (author of xBR) for helping me out during the implementation.

[Hunter K.](http://filthypants.blogspot.com/) for his support.
