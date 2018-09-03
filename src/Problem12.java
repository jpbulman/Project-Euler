import java.math.BigInteger;
import java.util.LinkedList;

public class Problem12 {

    public static BigInteger triangleNumber(BigInteger n){
        return (n.multiply(n.add(BigInteger.ONE))).divide(BigInteger.valueOf(2));
    }

    public static int allFactors(BigInteger n){
        int size = 1;
        for(int i=1;n.divide(BigInteger.valueOf(2)).compareTo(BigInteger.valueOf(i))>=0;i++){
            if(n.mod(BigInteger.valueOf(i)).equals(BigInteger.ZERO)){size++;}
        }
        return size;
    }

    public static void main(String[] args) {

        for(int i=99999;i<999999;i++){
            BigInteger tri = triangleNumber(BigInteger.valueOf(i));
            int size = allFactors(tri);
            System.out.println(i+" "+size);
            if(size>=500){System.out.println(tri);System.exit(0);}
        }

    }

} 