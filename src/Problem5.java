public class Problem5 {

    /*2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?*/

    //Only need to check 11-20, 1-10 is automatic if they are divisible 11-20
    public static boolean isDivisOneTwenty(int n){

        return (n%20==0)&&(n%19==0)&&(n%18==0)&&(n%17==0)&&(n%16==0)&&(n%15==0)&&(n%14==0)&&(n%13==0)&&(n%12==0)&&(n%11==0);

    }

    public static void main(String[] args) {

        boolean hasFound = false;
        int count = 1;

        while (!hasFound){

            if(isDivisOneTwenty(count)){hasFound=true;}

            if(!hasFound)count++;
        }

        System.out.println(count);

    }

} 