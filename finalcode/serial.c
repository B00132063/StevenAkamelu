#include <stdio.h>
#include <stdlib.h>
#include <time.h>
//defines the time and how we get the time in our worlds
#include "timer.h"
//to define or create the variables
#include "vars_defs_functions.h"

//Global Variables

//The quantity of F, B, O, X cz
// F = Fuel, 
//B = Burning 
//O = Not Burnt
//X = Burnt
//the int numf f, b, o, x is used to store fires and the numbers of burnings that happened
//unsigned means positive number
unsigned long int numF; 
unsigned long int numB;
unsigned long int numO;
unsigned long int numX;


int main(){
  

  //start = is used to log the start time
  //finish = is used to log the end time
  //elapsed = is used to see the times in between 
  double start, finish, elapsed;

//where we actually get the time 
//defined in the timer.h file 
  GET_TIME(start);




  // Initial values for #F, #B, #O, #X have to be zero
  //sets all the variables below to zero
  numF = 0;
  numB = 0;
  numO = 0;
  numX = 0;
  
  

//this is our two worlds
//rows and cols gets its value from the vars and defs file with our matrix being 20 rows and cols
//our world is a 2 dimension array 
  CELL current[ROWS][COLS]; 
  CELL future[ROWS][COLS]; 
  







  int day = 0; //Current day
  int i, j;
  int row, col;
  int num_Burning_Neighbours;
  
  //File handle for DayFBOX.dat
  FILE *fp_DayFBOX;
  

  fp_DayFBOX = fopen("data/DayFBOX.dat", "w");








  // Generate random seed
  srand((unsigned int)time(NULL));

  // Create the initial world and give each cell a state
  //this gives the value to the world
  //comes from the initaliseWorld file with a lot of for loops
  initialiseWorld(current, future);

  // Output the day, #F, #B, #O, #X to file
  outputDayFBOX(fp_DayFBOX, day);

  // Output the day and the 2-dim array of the current world
  outputWorld(day, current);
  


  #if DEBUG_LEVEL > 0
  printf("numF = %ld, numB = %ld\n\n", numF, numB);
  #endif

 







  for(day=1; day <= TOTAL_DAYS; day++){ // 50 days

  
        // loop over the chess board for each day
        for(row=0; row<ROWS; row++){
          for(col=0; col<COLS; col++){
                          // what is the current cell
                          switch(current[row][col].state){
                            
                          case 'F':
                            //num_Burning_Neighbours = countBurningNeighbours(row, col, current);
                            //here would look for fires
                            num_Burning_Neighbours = countBurningNeighbours_ClosedBoundaries(row, col, current);
                            
                          //here would decide who turns from (F to B ) fire to burning
                            decide_F_to_B(row, col, num_Burning_Neighbours, future);
                            break;

                            
                          case 'B':
                                  
                            
                          
                            decide_B_to_X_VaryingDays(row, col, current, future);

                            break;
	  
	                       }//switch
      } // cols
    }// rows










	
    //Overwrite the current world with the future world
    for(i=0; i<ROWS; i++){
      for(j=0; j<COLS; j++) {
	      current[i][j] = future[i][j];
      }
    }

    // Output the day, #F, #B, #O, #X to file
    outputDayFBOX(fp_DayFBOX, day);

    // Outputting the day of the current world
    outputWorld(day, current);
  }
  
 






  fclose(fp_DayFBOX);
  
  GET_TIME(finish);
  elapsed = finish - start;
  printf("Elapsed time = %lf\n\n", elapsed);

  return 0;
}
