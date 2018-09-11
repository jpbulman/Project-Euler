#Returns the number value of a letter (eg A-1, Z-26)
def letterVal(letter):
    alph = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    for i in range(len(alph)):
        if(alph[i]==letter):
            return i+1

#Returns the sum of the value of the letters for a given word
def wordVal(word):
    sum = 0
    #Iterate through each character in the word and add its value to the sum
    for letter in word:
        sum+=letterVal(letter)
    return sum

#Make a list of a lot of triangle numbers
triangs = [0]*99999

#Populate the array
for a in range(1,99999):
    triangs[a]=(a*(a+1))//2

#Returns if a given number is a triangle number
def isTriang(n):
    #If it is in the array, return true
    for a in triangs:
        if(a==n):
            return True
        #If we've gone too far, it's not there, so terminate
        elif(a >= n):
            return False

file = open("p042_words.txt","r")

string1 = file.readline()
string2 = string1.replace("\",\""," ").replace("\"","")

numTriangWords = 0

currWord = ""
for c in string2:
    #If we reach a new word
    if(c==" "):
        #Get the numeric value of the word
        val = wordVal(currWord)
        #If it is a triangle number, then add one to the current count
        if(isTriang(val)):
            numTriangWords+=1
        #Reset the current word
        currWord=""
    else:
        #Take the left character and add it to the current fragment of a word
        currWord+=string2[0]
    #Take the leftmost character off
    string2=string2[1:]

print(numTriangWords)