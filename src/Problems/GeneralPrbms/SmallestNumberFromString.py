# Python program for the above approach
def removeKdigits(num, k):
    n = len(num)
    mystack = []

    # Store the final string in stack
    for c in num:
        while (len(mystack) > 0 and k > 0 and ord(mystack[len(mystack) - 1]) > ord(c)):
            mystack.pop()
            k -= 1

        if len(mystack) > 0 or c != '0':
            mystack.append(c)

    # Now remove the largest values from the top of the
    # stack
    while len(mystack) > 0 and k:
        mystack.pop()
        k -= 1
    if len(mystack) == 0:
        return "0"

    # Now retrieve the number from stack into a string
    # (reusing num)
    while (len(mystack) > 0):
        num = num.replace(num[n - 1], mystack[len(mystack) - 1])
        mystack.pop()
        n -= 1
    return num[n:]


# driver code
str = "765028321"
k = 5
print(removeKdigits(str, k))

# This code is contributed by shinjanpatra

