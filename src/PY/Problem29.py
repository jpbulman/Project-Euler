#Make a list of the unique numbers
currList = []

for a in range(2,101):
    for b in range(2,101):
        currNum = a**b
        #If it is not in the list, add it
        if(currNum not in currList):
            currList.insert(len(currList),currNum)

#Print the number of els in the list
print(len(currList))