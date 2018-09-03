import java.math.BigInteger;

public class Problem25 {

    public static void main(String[] args) {

        BigInteger[] list = new BigInteger[9999];

        for(int i=0;i<9999;i++){
            list[i] = BigInteger.ZERO;
        }

        list[0]=BigInteger.ZERO;//Burn the first
        list[1]=BigInteger.ONE;
        list[2]=BigInteger.ONE;

        for(int i=1;i<9999;i++){
            if(list[i].equals(BigInteger.ZERO)){
                list[i] = list[i-1].add(list[i-2]);
            }

            if(list[i].toString().length()==1000){System.out.println(i);System.exit(0);}
        }

    }

} 