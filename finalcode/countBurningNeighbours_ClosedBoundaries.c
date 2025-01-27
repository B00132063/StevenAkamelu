#include <stdio.h>
#include "vars_defs_functions.h"


int countBurningNeighbours_ClosedBoundaries(int row,
			   int col,
			   CELL current[ROWS][COLS]){

  int i, j;

  #if DEBUG_LEVEL > 1
  printf("Cell[%d][%d] is Fuel:\n", row, col);
  #endif
  
  int local_num_Burning_Neighbours = 0;
  
  //Check neighbours of the candidate cell

  if(row > 0 && row < ROWS-1 && col > 0 && col < COLS-1){ // Candidate cell is an interior cell
    
    for(i=row-1; i<=row+1; i++)
      for(j=col-1; j<=col+1; j++){
	
	//Don't include the candidate cell
	if(i != row || j != col){
	  
          #if DEBUG_LEVEL > 1
	  printf("  Neighbour[%d][%d]\n",(i+ROWS)%ROWS, (j+COLS)%COLS);
          #endif
	  
    //if our current cell is b that will go back and go up
	  if(current[i][j].state == 'B')
	    local_num_Burning_Neighbours++;
	  
	}
      }
  }
  else if(row > 0 && row < ROWS-1){
    // Candidate on Left OR Right edge, but not a corner
    // => Five nearest neighbours
    
    // TWO vertical Neighbours of the Left or Right edge:
    if(current[row-1][col].state == 'B')
      local_num_Burning_Neighbours++;
    
    if(current[row+1][col].state == 'B')
      local_num_Burning_Neighbours++;
    
    // Candidate is Left edge
    if(col == 0){
      // THREE diagonal neighbours of the Left edge:
      if(current[row-1][col+1].state == 'B')
	local_num_Burning_Neighbours++;
      
      if(current[row+1][col+1].state == 'B')
	local_num_Burning_Neighbours++;
      
      if(current[row][col+1].state == 'B')
	local_num_Burning_Neighbours++;
    }
    else
      // Candidate is Right edge
      if(col == COLS-1){
	// THREE diagonal neighbours of Right edge:
	if(current[row-1][col-1].state == 'B')
	  local_num_Burning_Neighbours++;
	
	if(current[row+1][col-1].state == 'B')
	  local_num_Burning_Neighbours++;
	
	if(current[row][col-1].state == 'B')
	  local_num_Burning_Neighbours++;
      }
  }
  else if(col > 0 && col < COLS-1 ){
    // Candidate on Top edge OR Bottom edge, but not a corner
    // => Five nearest neighbours
    if(current[row][col-1].state == 'B')
      local_num_Burning_Neighbours++;
    
    if(current[row][col+1].state == 'B')
      local_num_Burning_Neighbours++;
    
    // Candidate is Top edge
    if(row == 0){
      // THREE diagonal neighbours
      if(current[row+1][col-1].state == 'B')
	local_num_Burning_Neighbours++;
      
      if(current[row+1][col+1].state == 'B')
	local_num_Burning_Neighbours++;
      
      if(current[row+1][col].state == 'B')
	local_num_Burning_Neighbours++;
    }
    else
      // Candidate is Bottom edge
      if(row == ROWS-1){
	// THREE diagonal neighbours
	if(current[row-1][col-1].state == 'B')
	  local_num_Burning_Neighbours++;
	
	if(current[row-1][col+1].state == 'B')
	  local_num_Burning_Neighbours++;
	
	if(current[row-1][col].state == 'B')
	  local_num_Burning_Neighbours++;
      }
  }
  else if(row == 0){
    // Top Corner cell (we have accounted for Top edge cells already)
    // Vertical neighbour below:
    if(current[row+1][col].state == 'B')
      local_num_Burning_Neighbours++;
    
    if(col == 0){
      // Top-Left Corner: ONE diagonal neighbour & ONE right neighbour
      if(current[row+1][col+1].state == 'B')
	local_num_Burning_Neighbours++;
      
      if(current[row][col+1].state == 'B')
	local_num_Burning_Neighbours++;
    }
    else
      if(col == COLS-1){
	//Top-Right Corner: ONE diagonal neighbour & ONE left neighbour
	if(current[row+1][col-1].state == 'B')
	  local_num_Burning_Neighbours++;
	
	if(current[row][col-1].state == 'B')
	  local_num_Burning_Neighbours++;
      }
  }
  else if(row == ROWS-1){
    // Bottom Corner cell (we have accounted for Bottom edge cells already)
    // Vertical neighbour below:
    if(current[row-1][col].state == 'B')
      local_num_Burning_Neighbours++;
    
    if(col == 0){
      // Bottom-Left Corner: ONE diagonal neighbour & ONE right neighbour
      if(current[row-1][col+1].state == 'B')
	local_num_Burning_Neighbours++;
      
      if(current[row][col+1].state == 'B')
	local_num_Burning_Neighbours++;
    }
    else
      if(col == COLS-1){
	//Bottom-Right Corner: ONE diagonal neighbour & ONE left neighbour
	if(current[row-11][col-1].state == 'B')
	  local_num_Burning_Neighbours++;
	
	if(current[row][col-1].state == 'B')
	  local_num_Burning_Neighbours++;
      }
  }
  
  return local_num_Burning_Neighbours;
  
}
  
