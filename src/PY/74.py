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

#Returns the sum of the factorials of the digits
#Eg f(145) = 1! + 4! + 5!
def digFacts(n):
    sum=0
    #Make it a string
    strn = str(n)
    #Iterate over it and add the factorial of each digit to the sum
    for i in strn:
        intForm = int(i)
        sum+=factorial(intForm)
    
    return sum

#Returns if the chain has length 60 or not
def sixtyChainLength(n):
    #List of the numbers so far
    numsSoFar = []
    #Insert n as the first one
    numsSoFar.insert(0,n)

    #Since we already did the first number, we only need to do 59 more to get 60
    for i in range(59):
        #Get the digfacts of the most recent item in the list
        next = digFacts(numsSoFar[-1])
        #If it is a repeat, the chain is over, and it is false
        if(next in numsSoFar):
            return False
        #Otherwise, insert and keep going
        else:
            numsSoFar.insert(len(numsSoFar),next)
    #If we went through the loop and no repeats came up, then we got a chain of 60 in length
    return True

numOf = 0
for a in range(1000000):
    if(sixtyChainLength(a)):
        numOf+=1

print(numOf)