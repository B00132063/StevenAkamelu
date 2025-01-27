#include <stdio.h>
#include "vars_defs_functions.h"


int countInfectedNeighbours(int row,
			    int col,
			    CELL current[ROWS][COLS]){

  int i, j;

  #if DEBUG_LEVEL > 0
  printf("Cell[%d][%d] is Susceptible:\n", row, col);
  #endif
  
  int local_num_Infected_Neighbours = 0;
  
  //Check neighbours of the candidate cell
  for(i=row-1; i<=row+1; i++)
    for(j=col-1; j<=col+1; j++){
      
      //Don't include the candidate cell
      if(i != row || j != col){

        #if DEBUG_LEVEL > 0
	printf("  Neighbour[%d][%d]\n",(i+ROWS)%ROWS, (j+COLS)%COLS);
	#endif
	
	if(current[(i+ROWS)%ROWS][(j+COLS)%COLS].state == 'I')
	  local_num_Infected_Neighbours++;
	
      }
    }

  return local_num_Infected_Neighbours;

}
  
