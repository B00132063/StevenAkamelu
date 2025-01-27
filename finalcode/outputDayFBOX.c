#include <stdio.h>
#include "vars_defs_functions.h"


void outputDayFBOX(FILE *fp_DayFBOX, int day){

  #if DEBUG_LEVEL > 0
  printf("%d %ld %ld %ld %ld\n", day, numF, numB, numO, numX);
  #endif

  fprintf(fp_DayFBOX, "%d %ld %ld %ld %ld\n", day, numF, numB, numO, numX);

}
