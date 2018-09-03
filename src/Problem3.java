import java.math.BigInteger;
import java.util.LinkedList;

public class Problem3 {

    /*The prime factors of 13195 are 5, 7, 13 and 29.

    What is the largest prime factor of the number 600851475143 ?*/

    public static LinkedList<BigInteger> distinctFactors(BigInteger n){
        LinkedList<BigInteger> factors = new LinkedList<BigInteger>();

        //Biggest possible factor
        BigInteger bpf = n.divide(BigInteger.valueOf(2));

        for(int i=2;bpf.compareTo(BigInteger.valueOf(i))>=0;i++){
            if(isPrime(i)&&n.mod(BigInteger.valueOf(i)).equals(BigInteger.ZERO)){
                factors.add(BigInteger.valueOf(i));
            }
            if(product(factors).compareTo(n)==0){return factors;}
        }

        return factors;
    }

    public static BigInteger product(LinkedList<BigInteger> facts){

        BigInteger prod = BigInteger.ONE;

        for(BigInteger n:facts){
            prod = prod.multiply(n);
        }
        return prod;
    }

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
        long time1 = System.currentTimeMillis();
        BigInteger i = new BigInteger("600851475143");
        LinkedList<BigInteger> factors = distinctFactors(i);

        BigInteger currMax = BigInteger.ZERO;
        for(BigInteger n:factors){
            if(n.compareTo(currMax)>0){currMax=n;}
        }
        long time2 = System.currentTimeMillis();
        System.out.println(currMax + " Completed in: " + (time2-time1)+" ms");
    }

} 