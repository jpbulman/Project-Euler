primes = [0]*999999

def prime(n):
    if primes[n] != 0:
        return primes[n]
    else:
        for i in range(2,n//2):
            if n % i == 0:
                primes[n] = False
                return False
        primes[n] = True
        return True

max = 0
maxA = 0
maxB = 0
for a in range(-999,1000):
    for b in range(-1000,1001):
        fun = lambda x: (x**2)+(a*x)+b
        n = 0
        while prime(fun(n)):
            n+=1
        if n > max:
            max = n
            maxA = a
            maxB = b

print(a,b,a*b,max)

