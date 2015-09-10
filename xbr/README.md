xBR Shaders
=======
These shaders uses the xBR algorithm to scale. xBR (scale by rules) works by detecting edges and interpolating pixels along them. It has some empyrical rules developed to detect the edges in many directions. There are many versions implemented and they differs basically by the number of directions considered and the way interpolations are done.

xbr-lvl1-noblend.cg
--------------

The most basic xBR shader. Level 1 means it only detects two edge directions (45º and 135º). The interpolation doesn't blend pixel colors. It uses the most similar color from one of its neighbors. So, the final result uses the original color palette. And because of that, it only works properly at odd scale factors (3x, 5x, 7x...).

Recommended sampling: `Point`
Recommended scale factors: `multiple odd scale factors`

xbr-lvl2-noblend.cg
--------------

An evolution from last shader. Level 2 means it can detect four edge directions, which shows as better rounded objects on screen. The interpolation doesn't blend pixel colors. It uses the most similar color from one of its neighbors. So, the final result uses the original color palette. And because of that, it only works properly at odd scale factors (3x, 5x, 7x...).

Recommended sampling: `Point`
Recommended scale factors: `multiple odd scale factors`

xbr-lvl2.cg
--------------

It can detect four edge directions, which shows as better rounded objects on screen. The interpolation blends pixel colors, so that the final image is smoother than the noblend versions. It works well in any integer scale factor.

Recommended sampling: `Point`
Recommended scale factors: `Integer multiples`

xbr-lvl2-multipass.cg
--------------

It's the same as the last one. But this one divides the calculations among multiple shaders. So, this one is faster than the single versions.

Recommended sampling: `Point`
Recommended scale factors: `Integer multiples`

xbr-lvl2-fast.cg
--------------

This is a simplified lvl2 implementation. Much faster than the standard version, though it sacrifices some quality.

Recommended sampling: `Point`
Recommended scale factors: `Integer multiples`

xbr-lvl3-noblend.cg
--------------

Level 3 means it can detect six edge directions, which shows as better rounded objects on screen. The interpolation doesn't blend pixel colors. It uses the most similar color from one of its neighbors. So, the final result uses the original color palette. And because of that, it only works properly at odd scale factors (3x, 5x, 7x...).

Recommended sampling: `Point`
Recommended scale factors: `multiple odd scale factors`

xbr-lvl3.cg
--------------

It can detect six edge directions, which shows as even better rounded objects on screen than the lvl2. The interpolation blends pixel colors, so that the final image is smoother than the noblend versions. It works well in any integer scale factor.

Recommended sampling: `Point`
Recommended scale factors: `Integer multiples`

xbr-lvl3-multipass.cg
--------------

It's the same as the last one. But this one divides the calculations among multiple shaders. So, this one is faster than the single versions.

Recommended sampling: `Point`
Recommended scale factors: `Integer multiples`

xbr-mlv4-multipass.cg
--------------

This shader is the latest evolution of the standard xBR algorithm. It can can detect eight edge directions, which shows as better rounded objects on screen. Besides, it has a non-greedy selection of edges internally, which means it doesn't automatically chooses to interpolate along the steeper edge. The interpolation blends pixel colors, so that the final image is smoother than the noblend versions. It works well in any integer scale factor.

Recommended sampling: `Point`
Recommended scale factors: `Integer multiples`

xbr-hybrid.cg
--------------

This shader combines xBR with reverse-aa. It's recommended for games with smooth color gradients.

Recommended sampling: `Point`

super-xbr-2p.cg
--------------

Super-xBR uses parts of the xBR algorithm and combines with other linear interpolation ones. It is intended for games with smooth color gradients. Compared to the hybrid ones, Super-xBR provides a much better image, without discontinuities.

Recommended sampling: `Point`
Recommended scale factors: `Integer multiples`

super-xbr-3p-smoother.cg
--------------

The same as the last one with an additional step to increase smoothness. This one provides even better image quality, though a bit slower.

Recommended sampling: `Point`
Recommended scale factors: `Integer multiples`
