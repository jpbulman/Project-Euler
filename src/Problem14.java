import java.math.BigInteger;
import java.util.LinkedList;

public class Problem14 {

    public static BigInteger collatzStep(BigInteger i){

        if(i.mod(BigInteger.valueOf(2)).equals(BigInteger.ZERO)){return i.divide(BigInteger.valueOf(2));}
        else{return (BigInteger.valueOf(3).multiply(i)).add(BigInteger.ONE);}
    }

    public static int numSteps(BigInteger n){

        int numSteps = 1;

        while (!n.equals(BigInteger.ONE)){
            numSteps++;
            n=collatzStep(n);
        }

        return numSteps;
    }

    public static void main(String[] args) {
        int maxSteps = 0;
        int maxI = 0;
        for(int i=2;i<1000000;i++){
            int steps = numSteps(BigInteger.valueOf(i));
            if(steps>maxSteps){maxSteps=steps;maxI=i;}
        }
        System.out.println(maxI);
    }

} 