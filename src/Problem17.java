public class Problem17 {

    public static String singNumToWord(int i){
        switch (i){
            case 1:return "one";
            case 2:return "two";
            case 3:return "three";
            case 4:return "four";
            case 5:return "five";
            case 6:return "six";
            case 7:return "seven";
            case 8:return "eight";
            case 9:return "nine";
            default:return "";
        }
    }

    public static String tensToWord(int n){
        int i = n/10;
        switch (i){
            case 1:return teens(n);
            case 2:return "twenty-"+singNumToWord(n%10);
            case 3:return "thirty-"+singNumToWord(n%10);
            case 4:return "forty-"+singNumToWord(n%10);
            case 5:return "fifty-"+singNumToWord(n%10);
            case 6:return "sixty-"+singNumToWord(n%10);
            case 7:return "seventy-"+singNumToWord(n%10);
            case 8:return "eighty-"+singNumToWord(n%10);
            case 9:return "ninety-"+singNumToWord(n%10);
            default:return singNumToWord(n%10);
        }
    }

    public static String teens(int i){
        switch (i){
            case 10:return "ten";
            case 11:return "eleven";
            case 12:return "twelve";
            case 13:return "thirteen";
            case 14:return "fourteen";
            case 15:return "fifteen";
            case 16:return "sixteen";
            case 17:return "seventeen";
            case 18:return "eighteen";
            case 19:return "nineteen";
            default:return "";
        }
    }

    public static String threeDigToString(int n){
        if(n%100==0){return singNumToWord(n/100)+" hundred";}
        else return singNumToWord(n/100)+" hundred and "+tensToWord(n%100);
    }

    public static void main(String[] args) {

        int sum = 0;

        for(int i=1;i<1001;i++){

            if(i<10){sum+=singNumToWord(i).length();}
            else if(i<100){sum+=tensToWord(i).replaceAll(" ","").replaceAll("-","").length();}
            else if(i<1000){sum+=threeDigToString(i).replaceAll(" ","").replaceAll("-","").length();}
            else if(i==1000){sum+="onethousand".length();}

        }

        System.out.println(sum);

    }

} 