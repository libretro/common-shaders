# mdapt v2.7 - merge dithering and pseudo transparency

## Introduction

In many old arcade or console games you will find dithering effects which are there to compensate for platform weaknesses like missing transparency support or small color palettes. This works well since back then the monitors (CRTs) had scanline bleeding and other certain features which merged the dithering through the display technology. But nowadays every pixel will displayed perfectly so dithering won't look like it should be.

There are already shaders out there who are trying to simulate how a CRT displays an image. mdapt though goes a different way and tries to detect dithering patterns by analyzing the relation between neighbored pixels. This way only these specific parts of the image are blended. The resulting image (still in the original resolution) is now a good base for further scaling with advanced algorithms (like xBR) which on there own usually have a hard time with dithering.

## Algorithm

mdapt can detect two basic dithering patterns. Checkerboard (CB) and vertical lines (VL). It actually doesn't matter of how many colors the pattern consists and mdapt doesn't use difference thresholds to determinie similarity at all. The algorithm just looks for regular "up and downs" between the pixels. There will always be errors though since the dithering process itself is lossy and not invertible. But mdapt tries to balance it by checking if there are enough detections in one local area.

## Usage

In RetroArch's shader options load one of the provided .cgp files. There are a few configuration options throughout the .cg files in the `dithering/mdapt-v2.7/passes/` directory. Here's a list of configuration options and their default values:

+ `dithering/mdapt-v2.7/passes/mdapt-pass0.cg`

 + `//#define strict // Strict neighbor analysis, only allows 2 different colors.`
<br><br>
+ `dithering/mdapt-v2.7/passes/mdapt-pass2.cg`

 + `const static float2 thresh = float2(2.0, 6.0); // Threshold values for VL, CB. Valid range: ([0.0, 10.0], [0.0, 25.0])`
<br><br>
+ `dithering/mdapt-v2.7/passes/mdapt-pass4.cg`

 + `//#define VL // vertical line handling`
 + `#define CB // checkerboard handling`
