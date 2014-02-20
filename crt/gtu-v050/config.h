
 #define compositeConnection
// #define noScanlines

#define signalResolution		256.0
#define signalResolutionI		83.0
#define signalResolutionQ		25.0
#define tvVerticalResolution	250.0

#define blackLevel 0.0875
#define contrast 1.0

// uncomment the following line to fix the shader on AMD/Ati GPUs
//#define ATIFIX
#define FIXNUM 6 // this should be a value between 2 and 12. Lower values will have less vibrant color when 'compositeConnection' is enabled, but higher values will be slower.
