import java.util.* ;
import java.io.* ;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;
/*
Question URL
https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/seating-arrangement-1/description



Level - Very Easy
*/

//Pbm -1

class TrainSolution {

    public static void main( String args[] ) throws IOException {

        System.setIn( new FileInputStream( new File("input.txt") ) ) ;
        System.setOut( new PrintStream( new File("output.txt") ) ) ;

        Scanner sc = new Scanner(System.in);
        int number = sc.nextInt();
        if (1 <= number && number <= Math.pow(10, 5)) {
            for (int i = 1; i <= number; i++) {
                int n = sc.nextInt();
                getSeatNumber(n);

            }
        } else {
            System.out.println("Invalid Entry ");
        }
    }

    public static void getSeatNumber(int number) {
        if (1 <= number && number <= 108) {
            int remainder = number % 12;
            switch (remainder) {
            case 0:
                number -= 11;
                System.out.println(number + " WS");
                break;
            case 1:
                number += 11;
                System.out.println(number + " WS");
                break;
            case 2:
                number += 9;
                System.out.println(number + " MS");
                break;
            case 3:
                number += 7;
                System.out.println(number + " AS");
                break;
            case 4:
                number += 5;
                System.out.println(number + " AS");
                break;
            case 5:
                number += 3;
                System.out.println(number + " MS");
                break;
            case 6:
                number += 1;
                System.out.println(number + " WS");
                break;
            case 7:
                number -= 1;
                System.out.println(number + " WS");
                break;
            case 8:
                number -= 3;
                System.out.println(number + " MS");
                break;
            case 9:
                number -= 5;
                System.out.println(number + " AS");
                break;
            case 10:
                number -= 7;
                System.out.println(number + " AS");
                break;
            case 11:
                number -= 9;
                System.out.println(number + " MS");
                break;
            }
        } else {
            System.out.println("invalid Seat number " + number);
        }

    }
}
