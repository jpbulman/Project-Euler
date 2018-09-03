import java.math.BigInteger;

public class Problem48 {

    public static void main(String[] args) {

        BigInteger sum = BigInteger.ZERO;

        for(BigInteger i=BigInteger.ONE;i.compareTo(BigInteger.valueOf(1000))<0;i=i.add(BigInteger.ONE))
            sum=sum.add(i.pow(i.intValue()));

        System.out.println(sum);

    }

} 