
public class Problem23 {

    public static boolean isAbundant(int n){
        int sum = 0;

        for(int i=1;i<n;i++){
            if(n%i==0){sum+=i;}
        }

        return sum>n;
    }

    public static void main(String[] args) {

        int size = 0;
        for(int i=12;i<28123;i++){
            if(isAbundant(i))size++;
        }

        int index = 0;
        int[] abd = new int[size];
        int sum = 0;

        bob:
        for(int i=1;i<=28123;i++){
            if(isAbundant(i)){
                abd[index++]=i;
            }

            for(int j:abd) {
                for (int k : abd) {
                    if (j + k == i&&j!=0&&k!=0) {
                        continue bob;
                    }
                }
            }
            sum+=i;
        }

            System.out.println(sum);
    }

}