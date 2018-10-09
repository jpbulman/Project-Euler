# Just uses 5th grade style division
def lenOfRepeat(dividend, divisor):
    
    #List of the divisors we have seen, if there are any repeats, we know that will start a loop and we can stop
    divs = []

    # As long as the division is going
    while dividend != 0:

        # Add the leading 0's until the number is big enough
        # E.g     __      __
        #       8|1  -> 8|10
        #
        while dividend // divisor == 0:
            dividend *= 10

        # If we reach a duplicate divisor, we go into a repeat cycle
        if divs.__contains__(dividend):
            # The length of the cycle is the number of unique divisors in the sequences
            return len(divs)
        else:
            # Otherwise, we have not repeated yet and can continue
            divs.append(dividend)

        # The next dividend is itself minus the closest multiple of the divisor
        dividend = dividend - ((dividend//divisor)*divisor)

    #If there is no repeated digit, then return -1
    return -1

# Go from 2-999 and see which produces the biggest repeat      
num = 0
maxLen = 0
for i in range(2,1000):
    curr = lenOfRepeat(1,i)
    if curr > maxLen:
        maxLen = curr
        num = i
    
print(num, maxLen)