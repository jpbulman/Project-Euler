import java.math.BigInteger;

public class Problem15 {

    //1 is to go right, 0 is down
    public static boolean validPath(BigInteger path){

        int i = 0;
        int j = 0;

        while (path.compareTo(BigInteger.ZERO)>0){

            int end  = path.mod(BigInteger.TEN).intValue();

            if(end==1){j++;}
            else if(end==0){i++;}

            path=path.divide(BigInteger.TEN);
        }

        return i==19&&j==19;
    }

    public static BigInteger toBinary(BigInteger n){

        BigInteger num = BigInteger.ZERO;
        int pow = 0;

        while (n.compareTo(BigInteger.ZERO)>0){
            BigInteger val = n.mod(BigInteger.valueOf(2));
            num = num.add(val.multiply(BigInteger.TEN.pow(pow++)));

            n=n.divide(BigInteger.valueOf(2));
        }
        return num;
    }

    public static void main(String[] args) {

        int[][] board = new int[20][20];

        BigInteger path = BigInteger.ZERO;

        int numPaths = 0;

        BigInteger max = toBinary(BigInteger.valueOf(2).pow(40).subtract(BigInteger.ONE)).add(BigInteger.ONE);

        for(;toBinary(path).compareTo(max)<0;path=path.add(BigInteger.ONE)){
            if(validPath(toBinary(path))){numPaths++;}
        }
        System.out.println(numPaths);
    }

} 