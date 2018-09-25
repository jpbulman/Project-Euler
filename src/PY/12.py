#Returns the nth triangle number
def triangle(n):
    return (n*(n+1))//2

numberOfDivisors = {
    2:0,
    3:0,
    4:1
}

#Returns the number of divisors a number has
def numDivs(n):
    if numberOfDivisors.get(n) is None:
        start = n//2
        for i in range(start,1,-1):
            if(n%i==0):
                num = numDivs(start)
                numberOfDivisors[n] = 1+num
                return 1+1+1+num
    else:
        return 1+numberOfDivisors[n]

# currBest = 0
# for i in range(1,800):
#     divs = numDivs(triangle(i))
#     #print(str(divs)+" "+str(triangle(i)))
#     if(divs>=currBest):
#         currBest=divs

print(numDivs(7))