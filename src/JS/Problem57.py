import math

def numberOfDigits(num):
    count = 0
    while(num>0):
        count+=1
        num=math.floor(num//10)
    
    return count


numerator = 3
denominator = 2
count = 0

for x in range(1000):
    if(numberOfDigits(numerator)>numberOfDigits(denominator)):
        count+=1
    actDenom = denominator
    denominator=denominator+numerator
    numerator=(actDenom*2)+numerator

print(count)