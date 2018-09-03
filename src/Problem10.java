import java.math.BigInteger;

public class Problem10 {

    /*
    The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
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

        BigInteger sum = BigInteger.ZERO;
        for(int i=2;i<2000000;i++){
            if(isPrime(i)){
                sum=sum.add(BigInteger.valueOf(i));
            }
        }

        System.out.println(sum);

    }

} 