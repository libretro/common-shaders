Bicubic Shaders
=======
These shaders uses sixteen nearest neighbors to interpolate. Four samples are used at a time and the resampling is calculated by using cubic functions horizontally and vertically.

bicubic-fast.cg
--------------

A fast bicubic implementation. It has a normal sharpness.

Recommended sampling: `Point`

bicubic-normal.cg
--------------

A classical bicubic implementation. It has a normal sharpness.

Recommended sampling: `Point`

bicubic-sharp.cg
--------------

A classical bicubic implementation. It has good sharpness.

Recommended sampling: `Point`


bicubic-sharper.cg
--------------

A classical bicubic implementation. It's very sharp.

Recommended sampling: `Point`

