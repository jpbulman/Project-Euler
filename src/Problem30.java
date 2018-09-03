public class Problem30 {

    public static boolean digfthpow(int n){
        String s = String.valueOf(n);

        int sum = 0;

        for(int i=0;i<s.length();i++)
            sum+=Math.pow(Integer.valueOf(s.substring(i,i+1)),5);

        return sum==n;
    }

    public static void main(String[] args) {

        int sum  = 0;

        for(int i=2;i<999999;i++){

            if(digfthpow(i))sum+=i;

        }

        System.out.println(sum);

    }

} 