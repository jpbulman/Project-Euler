#Looks in a hand to see if the card given exists in it
#Can be as specific as KH or 3S, but can also just be S or 3
def handHasA(hand, card):
    for x in hand:
        if(card in x):
            return True
    
    return False

#Swaps out an inputted letter for the correspoding 'number'. Makes the straight function easier
def swapFacesForNum(faceCard):
    return{
        'T':10,
        'J':11,
        'Q':12,
        'K':13,
        'A':14
        #Return the corresponding match to the 0th char in FC, or if it is not in the list, return itself
    }.get(faceCard[0],faceCard)

#Determines if a hand has 10 up to A
def handIsRoyal(hand):
    return (handHasA(hand,'A') and handHasA(hand,'K') and handHasA(hand,'Q') and handHasA(hand,'J') and handHasA(hand,'T'))

#Determines if all of the cards of the same suit
def handIsAFlush(hand):
    #Get the first card's suit
    suit = hand[0][1]
    #See if the rest have the same one
    return (suit==hand[1][1] and suit==hand[2][1] and suit==hand[3][1] and suit==hand[4][1])

#Turns all of the cards into numbers and sorts them
def turnHandIntoOrderedNumberArray(hand):

    arr = [0]*len(hand)

    #Convert all of the cards to numbers
    for a in range(len(hand)):
        #Take each card and replace it with its numeric value
        arr[a]=int(swapFacesForNum(hand[a][0]))

    #Sort the array to see if they are right in a row
    arr.sort()
    return arr

#Determines if a given hand is a straight
def handIsAStraight(hand):
    #Make a number array
    arr = turnHandIntoOrderedNumberArray(hand)

    for i in range(len(arr)):
        #If we are at the end of the list, success!
        if(i==len(arr)-1):
            return True
        #If not, see if the cards are following a straight pattern
        elif(arr[i]+1==arr[i+1]):
            continue
        #If they're not, then the hand is not a straight
        else:
            return False

#Returns false if there is no n-of-a-kind and the number of the card if there is
#WARNING: Function is strict, if you have 4 of something, 2 or 3 of a kind will be false (for making the rest of the program
# easier)
def handHasNOfAKind(hand,n):
    arr = turnHandIntoOrderedNumberArray(hand)
    #13 possible cards
    numOfInstances = [0]*13

    #Counts the number of time each card appears
    for i in arr:
        #2 maps to 0, Ace to 12, etc.
        numOfInstances[i-2]+=1

    #If there are n of something, return the card number
    for j in range(len(numOfInstances)):
        if (numOfInstances[j]==n):
            return j+2
    
    #Otherwise there is no four of a kind
    return False

def fullHouse(hand):
    pairNum = handHasNOfAKind(hand,2)
    threeNum = handHasNOfAKind(hand,3)
    return (pairNum!=threeNum) and (pairNum is not False) and (threeNum is not False)

def twoPairs(hand):
    arr = turnHandIntoOrderedNumberArray(hand)
    #13 possible cards
    numOfInstances = [0]*13

    #Counts the number of time each card appears
    for i in arr:
        #2 maps to 0, Ace to 12, etc.
        numOfInstances[i-2]+=1

    numOfPairs = 0
    
    for j in numOfInstances:
        if (j==2):
            numOfPairs+=1
    
    return numOfPairs==2

def rankHand(hand1):
    if(handIsAFlush(hand1) and handIsRoyal(hand1)):
        return 10
    elif(handIsAStraight(hand1) and handIsAFlush(hand1)):
        return 9
    elif(handHasNOfAKind(hand1,4)):
        return 8
    elif(fullHouse(hand1)):
        return 7
    elif(handIsAFlush(hand1)):
        return 6
    elif(handIsAStraight(hand1)):
        return 5
    elif(handHasNOfAKind(hand1,3)):
        return 4
    elif(twoPairs(hand1)):
        return 3
    elif(handHasNOfAKind(hand1,2)):
        return 2
    else:
        return 1

def highestCardThatsIsNotBlank(hand,notCard):
    arr = turnHandIntoOrderedNumberArray(hand)
    arr=arr[::-1]
    
    for x in arr:
        if(x==notCard):
            continue
        else:
            return x

def handOneWins(hand1, hand2):
    rankH1 = rankHand(hand1)
    rankH2 = rankHand(hand2)

    print(rankH1,rankH2)

    if(rankH1==rankH2):
        if(rankH1 is 9 or rankH1 is 5 or rankH1 is 6):
            return highestCardThatsIsNotBlank(hand1,-1)>highestCardThatsIsNotBlank(hand2,-1)
        if(rankH1==7):
            return handHasNOfAKind(hand1,3)>handHasNOfAKind(hand2,3)

    return rankH1>rankH2

    

test = ['5C', 'AD', '5D', 'AS', '5C']
test1 = ['TC', 'TH', '4D', 'TD', '4S']
print(handOneWins(test1,test))