listOfCombos = []

def populateCombos(n):

    if len(n) == 40 :
        listOfCombos.append(n)
    else:
        one_count = n.count("1")
        zero_count = n.count("0")

        if one_count == 20:
            populateCombos(n+"0")
        elif zero_count == 20:
            populateCombos(n+"1")
        else:
            populateCombos(n+"0")
            populateCombos(n+"1")

digHash = {}
digsUsed = ([0]*20)+([1]*20)
def popCombs(n, nums):
    if len(nums) == 0:
        print(1)

print(digsUsed)
