Data-Dependent Triangulation Shaders
=======
These shaders consider the square plane formed by the four nearest neighbors. They divide the square plane in two triangle planes. The pixels are bilinear interpolated using only the three points of triangles they belong.

ddt.cg
--------------

The classical ddt implementation. It works in any scale factor above 1x. It is a good last pass filter too.

Recommended sampling: `Point`


ddt-extended.cg
--------------

It has a better edge detection than the standard ddt, though a bit slower. It works in any scale factor above 1x. It is a good last pass filter too.

Recommended sampling: `Point`

