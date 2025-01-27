#include <stdio.h>
#include "vars_defs_functions.h"


void outputWorld(int day, CELL current[ROWS][COLS]){

  //int i,j;
  //  char worldfilenamebuf[20];

  //  snprintf(worldfilenamebuf, sizeof(worldfilenamebuf), "data/world%d.dat", day);
  //  FILE *fp_world = fopen(worldfilenamebuf, "w");

  int i,j,t,m;
  char name[20];

  FILE *fp_world;

  i = day;

//opening a connection and printing out 
  sprintf(name, "data/worldTTTTT.dat");
  for(t=14; t>=10; t--)
  {
    m = i%10;
    
    name[t] = (char) (48+m);
    i = i/10;
  }
  //defining the name of the folder
  fp_world = fopen(name,"w");

  
  for(i=0; i<ROWS; i++){ 
    for(j=0; j<COLS; j++){

      #if DEBUG_LEVEL > 0
      printf("%c ", current[i][j].state);
      #endif
      
      fprintf(fp_world, "%c ", current[i][j].state);

    }

    #if DEBUG_LEVEL > 0
    printf("\n");
    #endif
    
    fprintf(fp_world,"\n");

  }

  fclose(fp_world);

}
