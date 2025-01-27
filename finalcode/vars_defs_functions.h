
//
// Global Variables and Definitions
//

#ifndef VARS_AND_DEFS
#define VARS_AND_DEFS

#define DEBUG_LEVEL 1

//our matrix is 20 rows and 20 cols
#define ROWS 20
#define COLS 20

//if i change this to 35 days by day 30 to 34 it should show everything being burnt
#define TOTAL_DAYS 35



//Probabilities for transition: Fuel --> Burning, for 1 Burning Neighbour,
// 2 Burning Neighbours, 3 Burning Neighbours, etc.
#define PROB_F_TO_B_1 0.50
#define PROB_F_TO_B_2 0.6
#define PROB_F_TO_B_3 0.7
#define PROB_F_TO_B_4 0.75
#define PROB_F_TO_B_5 0.8
#define PROB_F_TO_B_6 0.85
#define PROB_F_TO_B_7 0.9
#define PROB_F_TO_B_8 1.0

//Burning to Burnt Parameters: Each Burning (B) cell will burn for a number of days,
//before change to Burnt (X). This wll be a random number between Min and Max here:
#define MIN_DAYS_B_TO_X 1
#define MAX_DAYS_B_TO_X 7








//Cell Datatype-definition
typedef struct cell {
  
  char state; // state can be one of: F for Fuel, B for Burning, O for Not Fuel, X for Burnt
  
  int counter_B_to_X; // Counter used to determine when a Burning cell gets changed to Burnt
  
} CELL;







//Global Variables.
extern unsigned long int numF; 
extern unsigned long int numB;
extern unsigned long int numO;
extern unsigned long int numX;












//Function Prototypes

void initialiseWorld(CELL current[ROWS][COLS],
		     CELL future[ROWS][COLS]);


void outputWorld(int day,
		 CELL current[ROWS][COLS]);


void outputDayFBOX(FILE *fp_DayFBOX, int day);


int countBurningNeighbours(int row,
			    int col,
			    CELL current[ROWS][COLS]);


int countBurningNeighbours_ClosedBoundaries(int row,
			    int col,
			    CELL current[ROWS][COLS]);


void decide_F_to_B(int row,
		   int col,
		   int num_Burning_Neighbours,
		   CELL future[ROWS][COLS]);

void decide_B_to_X(int row,
		   int col,
		   CELL current[ROWS][COLS],
		   CELL future[ROWS][COLS]);


void decide_B_to_X_VaryingDays(int row,
		   int col,
		   CELL current[ROWS][COLS],
		   CELL future[ROWS][COLS]);


#endif
