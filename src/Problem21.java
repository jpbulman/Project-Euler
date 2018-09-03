public class Problem21 {

    public static boolean isAnAmicableNum(int n){

        int sum = 0;

        for(int i=1;i<n;i++){
            if(n%i==0){sum+=i;}
        }

        if(sum==n){return false;}

        int altSum = 0;

        for(int j=1;j<sum;j++){
            if(sum%j==0){altSum+=j;}
        }

        return n==altSum;
    }

    public static void main(String[] args) {

        int sum = 0;

        //System.out.println(isAnAmicableNum(2));

        for (int i=1;i<10001;i++){
            if(isAnAmicableNum(i)){System.out.println(i);sum+=i;}
        }

        System.out.println(sum);

    }

} 