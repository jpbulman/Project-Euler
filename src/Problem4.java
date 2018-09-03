import java.util.Stack;

public class Problem4 {

    /*A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.*/

    public static boolean isPal(String n){

        Stack<String> forward = new Stack<String>();

        for(int i=0;i<n.length();i++){
            String sub = n.substring(i,i+1);
            forward.push(sub);
        }

        Stack<String> back = new Stack<String>();

        for(int i=n.length();i>0;i--){
            String sub = n.substring(i-1,i);
            back.push(sub);
        }

        while(!back.isEmpty()&&!forward.isEmpty()){
            if(!back.pop().equals(forward.pop())){return false;}
        }

        return true;
    }


    public static void main(String[] args) {

        int max = 0;
        int first = 0;
        int second = 0;

        for(int i=100;i<1000;i++){

            for(int j=100;j<1000;j++){

                int mult = i*j;
                if(isPal(String.valueOf(mult))&&mult>max){
                    max=mult;
                    first=i;
                    second=j;
                }

            }

        }

        System.out.println(max+" = "+first+" x "+second);

    }

} 