#Returns the nth triangle number
def triangle(n):
    return (n*(n+1))//2

numberOfDivisors = [1]*999999999

#Returns the number of divisors a number has
def numDivs(n):
    if(n==1):
        return 1
    elif(numberOfDivisors[n]!=1):
        return numberOfDivisors[n]
    else:
        for i in range(2,(n//2)+1):
            if(n%i==0):
                return numDivs(n//i)-1+(numDivs(i)-1)

currBest = 0
for i in range(1,900):
    divs = numDivs(triangle(i))
    if(divs>=currBest):
        currBest=divs

print(currBest)