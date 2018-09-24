n = 1001
arr = [[0] * n for i in range(n)]

def printArr(arry):
    for i in arry:
        print(i)

def sumDiags(array):
    x = 0
    y = 0
    sum = 0

    while(x<len(array) and y<len(array)):
        sum+=array[y][x]
        x+=1
        y+=1

    x=len(array)-1
    y=0

    while(x>=0 and y<len(array)):
        sum+=array[y][x]
        x-=1
        y+=1

    return sum-1

#0 is east, 1 is south, 2 is west, 3 is north
direction = 0
X = ((len(arr))//2)
Y = X

arr[Y][X]=1
currNumToAdd = 2

while(X <= len(arr) - 1 and Y <= len(arr)-1):

    if(direction is 0):
        X+=1
    elif(direction is 1):
        Y+=1
    elif(direction is 2):
        X-=1
    elif(direction is 3):
        Y-=1

    if(X >=len(arr) or Y >= len(arr)):
        break

    arr[Y][X] = currNumToAdd
    currNumToAdd+=1

    testX = X
    testY = Y
    testDirection = direction+1
    if(testDirection>3):
        testDirection=0

    if(testDirection is 0):
        testX+=1
    elif(testDirection is 1):
        testY+=1
    elif(testDirection is 2):
        testX-=1
    elif(testDirection is 3):
        testY-=1

    if(arr[testY][testX] is 0):
        direction+=1

    if(direction > 3):
        direction=0

print(sumDiags(arr))