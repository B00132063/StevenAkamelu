#include <stdio.h>
#include <stdlib.h>
#include "vars_defs_functions.h"

void initialiseWorld(CELL current[ROWS][COLS],
		     CELL future[ROWS][COLS]){

  int i, j, randRow, randCol;

  // looping over the rows and colums and set everthing to F
  //it loops over the world and sets the vaalue for i and j
  for(i=0; i<ROWS; i++)
    for(j=0; j<COLS; j++){

      current[i][j].state = 'F';

      //Each cell has a "Burn time" set to a random number of days between MIN_DAYS_B_TO_X and MAX_DAYS_B_TO_X:
      //this sets the timing for how long the world will burn for 
      current[i][j].counter_B_to_X = rand()%(MAX_DAYS_B_TO_X - MIN_DAYS_B_TO_X + 1) + MIN_DAYS_B_TO_X;

     //takes what i have done and drops it into the future world 
      future[i][j] = current[i][j]; //Future and current worlds should be identical at the start
      
      numF++; // Recall that numF is a global variable, initialised to zero in main()
    }

//its getting a random row and col after the loop
  randRow = rand()%ROWS;
  randCol = rand()%COLS;

//provides one random B which will begin to start the fire 
  current[randRow][randCol].state = 'B';
  future[randRow][randCol] = current[randRow][randCol];
  //this increments and decrements our numbers of our fires and burnings
  numF--;
  numB++;


}
