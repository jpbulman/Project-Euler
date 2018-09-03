//Returns an array of size 10 that contains the number of times the index is in the parameter
//Eg arrDigits(33045) -> [1,0,0,2,1,1,0,0,0,0]
function arrDigits(num){
    //Make an empty array
    digits = [0,0,0,0,0,0,0,0,0,0];

    //Takes the end digit off each time, counts it into the array, and moves onto the rest of the number
    while(num>0){
        //Right most digit
        var current_digit = num%10;
        //Count it into the array
        digits[current_digit]+=1;
        //Take off the right digit
        num/=10;
        //Take off decimal because JS is dumb
        num=Math.floor(num);
    }

    //Give back the array
    return digits;
}

//Checks if arrays are equal
function arrayEq(ar1, ar2){
    if(ar1.length!=ar2.length){
        return false;
    }
    
    for(var i=0;i<ar1.length;i++){
        if(ar1[i]!=ar2[i])
            return false;
    }

    return true;
}

//Main part of the problem, see https://projecteuler.net/problem=52
for(var x=10;x<999999;x++){

    one = arrDigits(x);
    two = arrDigits(2*x);
    three = arrDigits(3*x);
    four = arrDigits(4*x);
    five = arrDigits(5*x);
    six = arrDigits(6*x);

    if(arrayEq(one,two)){
        if(arrayEq(two,three)){
            if(arrayEq(three,four)){
                if(arrayEq(four,five)){
                    if(arrayEq(five,six)){
                        console.log(x);
                        return;
                    }
                }
            }
        }
    }

}
