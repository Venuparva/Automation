'''

Write a function to divide an array into n parts such that each part is evenly divided as much as possible

Ex 1: Array of 10 items, divided in 5 sub-arrays = 5 sub-arrays with 2 items in each
Ex 2: Array of 10 items, divided in 3 sub-arrays = 2 sub-arrays of 3 items each & 1 sub-array of 4 items

return array of arrays divided above

k = 2

index % 2 == 0 , 2, 4, 6 => [ 0,1]


[1,2,3,4,5,6,7,8,9,10] = [[1,2],[3,4],[5,6],[7,8],[9,10]]

k = 3
[1,2,3,4,5,6,7,8,9,10] = [ [1,2,3],[4,5,6],[7,8,9,10]]


Negative test cases:

1. if list is empty => return 0

2.if list is not numbers => return 0 or invalid input

positive test case:

1. for vali K input, divide array into sub arrays

Algm:

1. Iterate through list of items

2. if index == K , and store the result in resArray

3.reset the index = 0 for next iteration

[1 2 3 4 5 6 7 8 9 10]

K = 2

n/k = [ 1 2 ]

1. Iterate through input array

2. index,item => index and value of items

3. 1,2,3,...10-->range Index

4. range index  == K

    resArra1.append[1,2] [ 3,4] [4,5]

5.Iterate once again


'''

def divideSubArrays(inputList: list,k : int):
    resArray = []
    for index in range(len(inputList)-1): # Range analysis - To avoid oob error
        startIndex = index # useful variable names - Always use like this n put reasonable names for understanding
        endIndex = index+k # resonable names for better iteration
        print(inputList[startIndex:endIndex])
        print("startIndex:%sendIndex:%s" % (startIndex,endIndex))
        if inputList[startIndex:endIndex]: # Condition check
            resArray.append(inputList[startIndex:endIndex]) # store result
        del inputList[startIndex:endIndex-1] # feed correct input for next iteration
    print(resArray)

def divideSubArraysNew(inputList: list, k: int):
    for i in range(0,len(inputList),k):
        print(inputList[i:i+k])
divideSubArraysNew([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],2)




