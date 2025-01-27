#include <stdio.h>
#include <stdlib.h>
#include "vars_defs_functions.h"

void decide_F_to_B(int row,
		   int col,
		   int num_Burning_Neighbours,
		   CELL future[ROWS][COLS]){

  float chance;
  
  switch(num_Burning_Neighbours){

  case 0:  // 0 Burning Neighbours
    #if DEBUG_LEVEL > 1
    printf("State stays as F\n\n");
    #endif

    break;
    
  case 1: // 1 Burning Neighbour
    // Generate a random "chance" between 0.0 and 1.0
    chance = (float)rand() / (float)RAND_MAX;
  
    #if DEBUG_LEVEL > 1
    printf("chance = %f\n", chance);
    printf("PROB_F_TO_B_1 = %f\n", PROB_F_TO_B_1);
    #endif

    if(chance <= PROB_F_TO_B_1){
      future[row][col].state = 'B'; // Future cell changes from Fuel to Burning

      #if DEBUG_LEVEL > 1
      printf("F -> B\n\n");
      #endif

      numB++;
      numF--;
    }
    else{
      #if DEBUG_LEVEL > 1
      printf("State stays as F\n\n");
      #endif
    }
    
    break;
    
    
  case 2: // 2 Burning Neighbours
    // Generate a random "chance" between 0.0 and 1.0
    chance = (float)rand() / (float)RAND_MAX;
  
    #if DEBUG_LEVEL > 1
    printf("chance = %f\n", chance);
    printf("PROB_F_TO_B_2 = %f\n", PROB_F_TO_B_2);
    #endif

    if(chance <= PROB_F_TO_B_2){
      future[row][col].state = 'B';

      #if DEBUG_LEVEL > 1
      printf("F -> B\n\n");
      #endif

      numB++;
      numF--;
    }
    else{
      #if DEBUG_LEVEL > 1
      printf("State stays as F\n\n");
      #endif
    }
    
    break;
    
    
  case 3: // 3 Burning Neighbours
    // Generate a random "chance" between 0.0 and 1.0
    chance = (float)rand() / (float)RAND_MAX;
  
    #if DEBUG_LEVEL > 1
    printf("chance = %f\n", chance);
    printf("PROB_F_TO_B_3 = %f\n", PROB_F_TO_B_3);
    #endif

    if(chance <= PROB_F_TO_B_3){
      future[row][col].state = 'B';

      #if DEBUG_LEVEL > 1
      printf("F -> B\n\n");
      #endif

      numB++;
      numF--;
    }
    else{
      #if DEBUG_LEVEL > 1
      printf("State stays as F\n\n");
      #endif
    }
        
    break;
    
    
  case 4: // 4 Burning Neighbours
    // Generate a random "chance" between 0.0 and 1.0
    chance = (float)rand() / (float)RAND_MAX;
  
    #if DEBUG_LEVEL > 1
    printf("chance = %f\n", chance);
    printf("PROB_F_TO_B_4 = %f\n", PROB_F_TO_B_4);
    #endif

    if(chance <= PROB_F_TO_B_4){
      future[row][col].state = 'B';

      #if DEBUG_LEVEL > 1
      printf("F -> B\n\n");
      #endif

      numB++;
      numF--;
    }
    else{
      #if DEBUG_LEVEL > 1
      printf("State stays as F\n\n");
      #endif
    }
        
    break;
    
    
  case 5: // 5 Burning Neighbours
    // Generate a random "chance" between 0.0 and 1.0
    chance = (float)rand() / (float)RAND_MAX;
  
    #if DEBUG_LEVEL > 1
    printf("chance = %f\n", chance);
    printf("PROB_F_TO_B_5 = %f\n", PROB_F_TO_B_5);
    #endif

    if(chance <= PROB_F_TO_B_5){
      future[row][col].state = 'B';

      #if DEBUG_LEVEL > 1
      printf("F -> B\n\n");
      #endif

      numB++;
      numF--;
    }
    else{
      #if DEBUG_LEVEL > 1
      printf("State stays as F\n\n");
      #endif
    }
      
    break;
    

  case 6: // 6 Burning Neighbours
    // Generate a random "chance" between 0.0 and 1.0
    chance = (float)rand() / (float)RAND_MAX;
  
    #if DEBUG_LEVEL > 1
    printf("chance = %f\n", chance);
    printf("PROB_F_TO_B_6 = %f\n", PROB_F_TO_B_6);
    #endif

    if(chance <= PROB_F_TO_B_6){
      future[row][col].state = 'B';

      #if DEBUG_LEVEL > 1
      printf("F -> B\n\n");
      #endif

      numB++;
      numF--;
    }
    else{
      #if DEBUG_LEVEL > 1
      printf("State stays as F\n\n");
      #endif
    }
    
    break;
    
    
  case 7: // 7 Burning Neighbours
    // Generate a random "chance" between 0.0 and 1.0
    chance = (float)rand() / (float)RAND_MAX;
  
    #if DEBUG_LEVEL > 1
    printf("chance = %f\n", chance);
    printf("PROB_F_TO_B_7 = %f\n", PROB_F_TO_B_7);
    #endif

    if(chance <= PROB_F_TO_B_7){
      future[row][col].state = 'B';

      #if DEBUG_LEVEL > 1
      printf("F -> B\n\n");
      #endif

      numB++;
      numF--;
    }
    else{
      #if DEBUG_LEVEL > 1
      printf("State stays as F\n\n");
      #endif
    }
    
    break;
    
    
  case 8: // 8 Burning Neighbours
    // Generate a random "chance" between 0.0 and 1.0
    chance = (float)rand() / (float)RAND_MAX;
  
    #if DEBUG_LEVEL > 1
    printf("chance = %f\n", chance);
    printf("PROB_F_TO_B_8 = %f\n", PROB_F_TO_B_8);
    #endif

    if(chance <= PROB_F_TO_B_8){
      future[row][col].state = 'B';

      #if DEBUG_LEVEL > 1
      printf("F -> B\n\n");
      #endif

      numB++;
      numF--;
    }
    else{
      #if DEBUG_LEVEL > 1
      printf("State stays as F\n\n");
      #endif
    }
    
    break;
    
  }


}
  
