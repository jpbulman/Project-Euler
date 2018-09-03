public class Problem19 {

    public static boolean monthIsOver(int day,int month,boolean isLeapYear){

        switch (month){
            case 1:return day==31;
            case 2:if(isLeapYear)return day==29;else return day==28;
            case 3:return day==31;
            case 4:return day==30;
            case 5:return day==31;
            case 6:return day==30;
            case 7:return day==31;
            case 8:return day==31;
            case 9:return day==30;
            case 10:return day==31;
            case 11:return day==30;
            case 12:return day==31;
            default:return false;
        }

    }

    public static void main(String[] args) {

        //1 monday, 7 Sunday
        int currDay = 1;

        int currYear = 1900;

        int numFirstSundays = 0;

        //Need <= to cycle through the year 1900, but don't count it and still reach all through the end of 2000
        for(int years = 0;years<=100;years++){

            int numDays = 365;
            int month = 1;
            int currNumDay = 1;
            boolean isLeapYear = false;

            if(currYear%4==0&&currYear%100!=0){
                numDays=366;
                isLeapYear=true;
            }
            if(currYear%100==0&&currYear%400==0){
                numDays=366;
                isLeapYear=true;
            }

            for(int i=0;i<numDays;i++){

                if(currYear!=1900&&currNumDay==1&&currDay==7){numFirstSundays++;}

                if(monthIsOver(currNumDay,month,isLeapYear)){
                    currNumDay=1;
                    month++;
                    if(currDay==7){currDay=1;}
                    else {currDay++;}
                }
                else {
                    currNumDay++;
                    if(currDay==7){currDay=1;}
                    else {currDay++;}
                }


            }

            currYear++;
        }

        System.out.println(numFirstSundays);

    }

} 