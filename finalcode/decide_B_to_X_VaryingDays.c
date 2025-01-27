#include <stdio.h>
#include <stdlib.h>
#include "vars_defs_functions.h"

void decide_B_to_X_VaryingDays(int row,
		      int col,
		      CELL current[ROWS][COLS],
		      CELL future[ROWS][COLS]){

    if(current[row][col].counter_B_to_X == 0){

      //Change state to X (Burnt):
      future[row][col].state = 'X';

      numX++;
      numB--;
   
      #if DEBUG_LEVEL > 1
      printf("B -> X\n\n");
      #endif
    }
    else{
      //Decrement B->X counter
      (future[row][col].counter_B_to_X)--;
    
      #if DEBUG_LEVEL > 1
      printf("State stays as B\n\n");
      #endif
    }
}


