import math

def sumOfDigs(n):
    sum = 0
    while(n!=0):
        sum+=n%10
        n=n//10
    return sum

def isDigPowerSum(n):
    digSum = sumOfDigs(n)
    if(digSum==1):
        return False

    if(digSum%2==0 and n%2!=0):
        return False
    
    if(digSum%2!=0 and n%2==0):
        return False

    for i in range (2,math.floor(math.sqrt(n))+1):
        pow = (digSum**i)
        if(pow==n):
            return True
        elif(pow>=n):
            return False

    return False

count = 10
for a in range(614657,999999999):
    if(isDigPowerSum(a)):
        count+=1
        if(count==30):
            print(a)

print(count)