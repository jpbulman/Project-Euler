def toBin(n):
	num = ""
	
	while(n!=0):
		num=str(n%2)+num
		n=n//2
	
	return num

def isPal(n):
	n=str(n)
	return n==n[::-1]

sum = 0

for x in range(1000000):
	if(isPal(x) and isPal(toBin(x))):
		sum+=x

print(sum)
