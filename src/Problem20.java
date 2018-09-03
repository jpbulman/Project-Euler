import java.math.BigInteger;

public class Problem20 {

    public static BigInteger factorial(BigInteger n){
        if(n.equals(BigInteger.ONE)){return BigInteger.ONE;}
        else {return n.multiply(factorial(n.subtract(BigInteger.ONE)));}
    }

    public static void main(String[] args) {

        BigInteger oneHund = factorial(BigInteger.valueOf(100));

        System.out.println(Problem16.digSum(oneHund));

    }

} 