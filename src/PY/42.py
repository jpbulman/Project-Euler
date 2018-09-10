def letterVal(letter):
    alph = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    for i in range(len(alph)):
        if(alph[i]==letter):
            return i+1

def wordVal(word):
    sum = 0
    for letter in word:
        sum+=letterVal(letter)
    return sum

triangs = [0]*99999

for a in range(1,99999):
    triangs[a]=(a*(a+1))//2

def isTriang(n):
    for a in triangs:
        if(a==n):
            return True
        elif(a >= n):
            return False

file = open("p042_words.txt","r")

string1 = file.readline()
string2 = string1.replace("\",\""," ").replace("\"","")

numTriangWords = 0

currWord = ""
print(string2)
for c in string2:
    if(c==" "):
        print("word:"+currWord)
        val = wordVal(currWord)
        if(isTriang(val)):
            numTriangWords+=1
        currWord=""
    else:
        currWord+=string2[0]
    
    string2=string2[1:]

print(numTriangWords)