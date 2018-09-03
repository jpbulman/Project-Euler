import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.util.Arrays;

public class Problem22 {

    public static int strnVal(String s){
        int sum = 0;
        while (!s.equals("")){
            String curr = s.substring(0,1);

            switch (curr){
                case "A":sum+=1;break;
                case "B":sum+=2;break;
                case "C":sum+=3;break;
                case "D":sum+=4;break;
                case "E":sum+=5;break;
                case "F":sum+=6;break;
                case "G":sum+=7;break;
                case "H":sum+=8;break;
                case "I":sum+=9;break;
                case "J":sum+=10;break;
                case "K":sum+=11;break;
                case "L":sum+=12;break;
                case "M":sum+=13;break;
                case "N":sum+=14;break;
                case "O":sum+=15;break;
                case "P":sum+=16;break;
                case "Q":sum+=17;break;
                case "R":sum+=18;break;
                case "S":sum+=19;break;
                case "T":sum+=20;break;
                case "U":sum+=21;break;
                case "V":sum+=22;break;
                case "W":sum+=23;break;
                case "X":sum+=24;break;
                case "Y":sum+=25;break;
                case "Z":sum+=26;break;
            }

            s=s.substring(1,s.length());
        }
        return sum;
    }

    public static void main(String[] args)throws Exception {

        File file = new File("p022_names.txt");

        BufferedReader br = new BufferedReader(new FileReader(file));

        String allNames = br.readLine();
        int numWords = 0;

        for(int i=0;i<allNames.length();i++){
            if(allNames.substring(i,i+1).equals("\"")){numWords++;}
        }
        numWords/=2;

        allNames = allNames.replaceAll("\",\"" , " ").replaceAll("\"","");

        String[] names = new String[numWords];

        int index = 0;
        while (allNames.length()>0){

            String name = "";

            while (!allNames.substring(0,1).equals(" ")){
                name+=allNames.substring(0,1);
                allNames=allNames.substring(1,allNames.length());
                if(allNames.length()==0){break;}
            }
            if(allNames.length()!=0)allNames=allNames.substring(1,allNames.length());

            names[index++]=name;
        }

        Arrays.sort(names);

        int ind = 1;
        int sum = 0;
        for (String s:names){
            sum += strnVal(s)*ind++;
        }

        System.out.println(sum);

    }

} 