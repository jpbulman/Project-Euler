facts = [1]*99999

def factorial(n):
    if(n is 0):
        return 1
    elif(facts[n]!=1):
        return facts[n]
    else:
        num = n*factorial(n-1)
        facts[n]=num
        return num

def digFact(n):
    sum = 0
    numStr = str(n)

    for a in range(len(numStr)):
        sum+=factorial(int(numStr[a]))

    return sum==n

sum = 0
for a in range(3,999999):
    if(digFact(a)):
        print(a)
        sum+=a

print(sum)