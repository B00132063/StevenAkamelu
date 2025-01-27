# Makefile for Serial Program

CC = gcc
CFLAGS = -g -Wall

DEPS =	vars_defs_functions.h timer.h

OBJ = 	serial.o\
	initialiseWorld.o\
	outputDayFBOX.o\
	outputWorld.o\
	countBurningNeighbours.o\
	countBurningNeighbours_ClosedBoundaries.o\
	decide_F_to_B.o\
	decide_B_to_X.o \
	decide_B_to_X_VaryingDays.o

#.SUFFIXES	.c

%.o: %.c $(DEPS)
	$(CC) $(CFLAGS) -c -o $@ $<

serial: $(OBJ)
	$(CC) $(CFLAGS) -o $@ $^

clean: $(OBJ)
	rm *.o
	rm serial
