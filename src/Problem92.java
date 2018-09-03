public class Problem92 {

    public static int chainRes(int n){

        int sum = 0;

        while (n>0){
            sum+=Math.pow((n%10),2);
            n=n/10;
        }

        return sum;
    }

    public static boolean goesToEN(int n){

        while (true){
            if (n==1){return false;}
            else if(n==89){return true;}
            else {n=chainRes(n);}
        }

    }

    public static void main(String[] args) {

        int count = 0;

        for(int i=2;i<10000000;i++){
            if(goesToEN(i))count++;
        }

        System.out.println(count);

    }

} 