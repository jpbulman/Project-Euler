public class Problem7 {

    /*
    By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
     */

    public static boolean isPrime(int n){

        if(n==2){return true;}

        //Biggest possible factor
        int bpf = (int)Math.ceil(Math.sqrt((double) n));

        for(int i=2;i<=bpf;i++){
            if(n%i==0){return false;}
        }

        return true;
    }

    public static void main(String[] args) {

        int countOfPrimes=0;
        int currNum = 1;

        while (countOfPrimes!=10001){
            currNum++;
            if (isPrime(currNum)){countOfPrimes++;}
        }

        System.out.println(currNum);

    }

} 