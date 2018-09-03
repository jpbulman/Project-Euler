import math

#Returns the number of digits in a given num
def numberOfDigits(num):
    count = 0
    #While the number exists, take off it's rightmost digit, add 1 to the number of digits, and go to the remaining part of
    #the number
    while(num>0):
        count+=1
        num=math.floor(num//10)
    
    return count


numerator = 3
denominator = 2
count = 0

for x in range(1000):
    #Increase the count of the number of digits in the num. is greater than denom.
    if(numberOfDigits(numerator)>numberOfDigits(denominator)):
        count+=1
    #Placeholder
    actDenom = denominator
    #In the problem, the sqaure root expansions show the next denominator is the sum of the previous denom. and num.
    denominator=denominator+numerator
    #The next numerator is double the denominator plus the previous numerator
    numerator=(actDenom*2)+numerator

print(count)