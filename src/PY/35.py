# Returns the index of the first character
def findFirstCharacter(n):
    string = str(n)

    for i in range(len(string)-2,-1,-1):
        if int(string[i]) < int(string[i+1]):
            return i

    return -1

# Returns the index of the ceiling character
def findCeilChar(indexOfFirstCharacter,n):
    string = str(n)
    firstChar = int(string[indexOfFirstCharacter])

    listOfGreaterNums = {}
    right = string[indexOfFirstCharacter:]

    pos = indexOfFirstCharacter+1

    for i in right:
        if int(i) > firstChar:
            listOfGreaterNums[i]=pos
        pos+=1

    return listOfGreaterNums[min(listOfGreaterNums)]

def swap(indI, indJ, n):
    l = list(str(n))
    i, j = l[indI], l[indJ]
    l[indI], l[indJ] = j, i
    return int(''.join(l)) 

listOfPermutations = [123]

while findFirstCharacter(listOfPermutations[-1]) > 0:
    currNum = listOfPermutations[-1]
    firstCharIndex = findFirstCharacter(currNum)
    secondCharIndex = findCeilChar(firstCharIndex,currNum)
    
    nextNum = swap(firstCharIndex,secondCharIndex,currNum)
    rightSub = ''.join(list(str(nextNum)[firstCharIndex:]).sort)
    nextNum = ((str(nextNum)[:firstCharIndex])+rightSub)
    list.append(nextNum)

print(listOfPermutations)