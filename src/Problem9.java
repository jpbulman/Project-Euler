public class Problem9 {

    /*
    A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
     */

    public static boolean isPyag(int a,int b,int c){
        return (Math.pow(a,2))+Math.pow(b,2)==Math.pow(c,2);
    }

    public static void main(String[] args) {

        for (int a=1;a<999;a++){
            for(int b=1;b<999;b++){
                for(int c=1;c<999;c++){

                    if(isPyag(a,b,c)&&a+b+c==1000){System.out.println(a*b*c);System.exit(0);}

                }
            }
        }

    }

} 