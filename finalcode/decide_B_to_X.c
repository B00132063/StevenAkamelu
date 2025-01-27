#include <stdio.h>
#include <stdlib.h>
#include "vars_defs_functions.h"

void decide_B_to_X(int row,
		      int col,
		      CELL current[ROWS][COLS],
		      CELL future[ROWS][COLS]){
  
  //Change state to X (Burnt):
  future[row][col].state = 'X';
  
  #if DEBUG_LEVEL > 1
  printf("B -> X\n\n");
  #endif
  
  numX++;
  numB--;
}


