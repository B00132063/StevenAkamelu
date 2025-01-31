//Write a program that simulates rolling of a fair four-sided dice. The program should roll a single dice 1000 times. Keep track of the number of each potential
//result (1 - 4) and display it as a percentage of the total number of rolls at the end.

import java.util.Scanner;
    
    public class Question2{
        public static void main(String[] args){

        int one = 0;
        int two = 0;
        int three = 0;
        int four = 0;
        int five = 0;
        int six = 0;
        int seven = 0;
        int eight = 0;


        int rolls = 100;
        int dice;


        Scanner in = new Scanner(System.in);

        for (int x = 0; x < 100; x++) {
          dice = (int)(Math.random () * 8 + 1);
          if (dice == 1)
          	one = one + 1;
          else if (dice == 2)
          	two = two + 1;
         else  if (dice == 3)
          	three = three + 1;
         else if (dice == 4)
          	four = four + 1;
          else if (dice == 5)
          	five = five + 1;
          else if (dice == 6)
          	six = six + 1;
          else if (dice == 7)
          	seven = seven + 1;
          else if (dice == 8)
          	eight = eight + 1;

        }
        System.out.printf("1 was %5.2f%% " + "of times\n", (float) (one) / rolls * 100);
        System.out.printf("2 was %5.2f%% " + "of times\n", (float) (two) / rolls * 100);
        System.out.printf("3 was %5.2f%% " + "of times\n", (float) (three) / rolls * 100);
        System.out.printf("4 was %5.2f%% " + "of times\n", (float) (four) / rolls * 100);
        System.out.printf("5 was %5.2f%% " + "of times\n", (float) (five) / rolls * 100);
        System.out.printf("6 was %5.2f%% " + "of times\n", (float) (six) / rolls * 100);
        System.out.printf("7 was %5.2f%% " + "of times\n", (float) (seven) / rolls * 100);
        System.out.printf("8 was %5.2f%% " + "of times\n", (float) (eight) / rolls * 100);

    }
}