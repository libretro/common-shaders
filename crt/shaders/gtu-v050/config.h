//#undef PARAMETER_UNIFORM

#ifdef PARAMETER_UNIFORM
uniform float compositeConnection;
#endif

#ifndef PARAMETER_UNIFORM
#define compositeConnection   0.0
#define noScanlines           0.0

#define signalResolution      256.0
#define signalResolutionI     83.0
#define signalResolutionQ     25.0
#define tvVerticalResolution  250.0

#define blackLevel            0.0875
#define contrast              1.0
#endif

#define FIXNUM 6
