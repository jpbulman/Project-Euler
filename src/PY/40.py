#Burn an index for ease later on
p = "-"

underAMil = True
currNum = 1

#Keep adding numbers until the string is over a million+1 (since we burned an index) in length
while(underAMil):
    p+=str(currNum)
    currNum+=1
    if(len(p)>1000001):
        underAMil=False

#Since we burned an index, we can just get the numbers as is
nums = [p[1],p[10],p[100],p[1000],p[10000],p[100000],p[1000000]]
ints = [0]*7

#Convert the strings to numbers
for i in range(len(nums)):
    ints[i] = int(nums[i])

prod = 1

#Multiply them out
for i in ints:
    prod = prod*i

print(prod)