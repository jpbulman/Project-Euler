import math

#Gets the sum of all the digits in a number
def digSum(num):
    count = 0
    while num>0:
        count+=num%10
        num=math.floor(num//10)
    return count

sum = 0

#Finds the biggest digital sum in 0 <= a,b, < 100 in a^b
for a in range(100):
    for b in range(100):
        big = digSum(a**b)
        if(big>sum):
            sum=big

print(sum)