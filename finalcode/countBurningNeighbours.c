#include <stdio.h>
#include "vars_defs_functions.h"


int countBurningNeighbours(int row,
			   int col,
			   CELL current[ROWS][COLS]){

  int i, j;

  #if DEBUG_LEVEL > 1
  printf("Cell[%d][%d] is Fuel:\n", row, col);
  #endif
  
  int local_num_Burning_Neighbours = 0;
  
  //Check neighbours of the candidate cell
  for(i=row-1; i<=row+1; i++)
    for(j=col-1; j<=col+1; j++){
      
      //Don't include the candidate cell
      if(i != row || j != col){

        #if DEBUG_LEVEL > 1
	printf("  Neighbour[%d][%d]\n",(i+ROWS)%ROWS, (j+COLS)%COLS);
	#endif
	
	if(current[(i+ROWS)%ROWS][(j+COLS)%COLS].state == 'B')
	  local_num_Burning_Neighbours++;
	
      }
    }

  return local_num_Burning_Neighbours;

}
  
