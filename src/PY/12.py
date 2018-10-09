listOfFactors = {}

def factorize(num):
    if num not in listOfFactors:
        # iterate from 2 to half of the number, since no factor is bigger than half the number
        for i in range(2, (num // 2)):
            # if num is divisible by i, we found a factor
            if (num % i) == 0:
                # if we found a factor, our answer is to prime factorize both factors and combine
                lOF = factorize(i) + factorize(num // i)
                lOF.sort()
                listOfFactors[num] = lOF
                return lOF

        # if we didn't find any factors, it's a prime, so we'll just return the number itself as the only factor
        listOfFactors[num] = [num]
        return [num]
    else:
        return listOfFactors[num]

def numberOfFactors(n):
    factors = factorize(n)
    uniqueFactors = list(set(factorize(n)))

    totalProd = 1
    for i in uniqueFactors:
        count = factors.count(i)
        count += 1
        totalProd *= count

    return totalProd

def triang(n):
    return (n*(n+1))//2


i = 2
while True:
    triangle = triang(i)
    numberOfFacts = numberOfFactors(triangle)
    if numberOfFacts >= 500:
        print(triangle)
        print(i)
        break
    i += 1