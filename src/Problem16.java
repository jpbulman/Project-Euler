import java.math.BigInteger;

public class Problem16 {

    public static BigInteger digSum(BigInteger n){
        BigInteger sum = BigInteger.ZERO;
        while (!n.equals(BigInteger.ZERO)){
            sum=sum.add(n.mod(BigInteger.TEN));
            n=n.divide(BigInteger.TEN);
        }
        return sum;
    }

    public static void main(String[] args) {

        BigInteger n = BigInteger.ONE;

        for(int i=0;i<1000;i++){
            n=n.multiply(BigInteger.valueOf(2));
        }

        System.out.println(digSum(n));

    }

} 