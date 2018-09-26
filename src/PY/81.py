def printArr(arry):
    for i in arry:
        print(i)


n = 80
massiveArray = [[0]*n for i in range(n)]

file = open("p081_matrix.txt","r")

X = 0
Y = 0
for line in file:
    arrayOfNumbers = line.split(",")
    arrayOfNumbers = list(map(lambda a: int(a), arrayOfNumbers))
    while X < n:
        massiveArray[Y][X] = arrayOfNumbers[X]
        X += 1
    X = 0
    Y += 1


def minPath(array, x, y):
    if x is len(array)-1 and y is len(array) - 1:
        return array[y][x]
    elif x is len(array)-1:
        return array[y][x]+minPath(array, x, y+1)
    elif y is len(array)-1:
        return array[y][x]+minPath(array, x+1, y)
    else:
        pathdown = minPath(array, x, y+1)
        pathright = minPath(array, x+1, y)

        if pathdown < pathright:
            return pathdown
        else:
            return pathright


printArr(minPath(massiveArray, 0, 0))

printArr(massiveArray)
