#Returns the nth triangle number
def triangle(n):
    return (n*(n+1))//2

numberOfDivisors = [1]*999999999

#Returns the number of divisors a number has
def numDivs(n):
    total = 0

    if(n==1):
        return 1

    for b in range((n//2)+1,1,-1):
        if(numberOfDivisors[b]!=1):
            return numberOfDivisors[b]+numDivs(n/b)
        else:
            for a in range(1,(n//2)+1):
                if(n%a==0):
                    total+=1
                    #The plus one is to include itself
                    return total+1

currBest = 0
for i in range(1,900):
    divs = numDivs(triangle(i))
    if(divs>=currBest):
        currBest=divs

print(currBest)