from math import ceil
from typing import List
#counter = 0
Original_list = []
#Soln-1
def binarySearch(inputList: List, target: int) -> int:
    # iterate through list of elements
    # cmp each elemnet with target elem
    # if matches return its index
    # else if index == (len(list)-1) after searched all elements in the list
    # return -1
    for index,num in enumerate(inputList):
        if num == target:
            print("index=%s" % index)
            return index
        elif index == len(inputList)-1:
            print("index=-1")
            return -1

#Soln-2 # usingBuiltIn-List.index
def usingBuiltIn(inputList: List, target: int) -> int:
    if str(inputList.index(target)).contains("not in list"):
        print("absent-index=-1")
        return -1
    else:
        print("present-index=%s" % inputList.index(target))
        return inputList.index(target)


#Using my BST:

def usingVenuBSTsearch(origList: List,inputList: List, target: int, counter: int)-> int:
    middleElem = ceil(len(inputList)/2)
    counter = counter + middleElem
    print("middleElem%s" % middleElem)
    print("counter%s" % counter)
    print("origList%s" % origList)
    print("--------------")
    if inputList[middleElem] < target:
        # if ME < taret then target will be in second set,repeat the step
        inputList = inputList[inputList.index(middleElem):] # store 2nd set of elements to list
        print("inputList%s" % inputList)
    elif inputList[middleElem] > target:
        inputList = inputList[:inputList.index(middleElem)] # store 1st set of elements to list
    elif inputList[middleElem] == target:
        print("target found & its index:%s" % origList.index(inputList[middleElem]))
        return origList.index(inputList[middleElem])
    usingVenuBSTsearch(origList,inputList, 9, counter) # where 9 is target elem


def usingLeeBSTsearch(inputList: List, target: int)-> int:
    # Find both start n end index & iterate it until start < end [ SI...ME....EI]
    # Find MiddleElement (ME) & its pointer (or) index
    # Compare ME with target
        # If ME == target,then return targer
        # Move StartIndex = ME Index +1   [ ME.SI...EI] --> List size got reduced by moving index from beginning
                # if startIndex Elem < ME, move the start index from current pos to ME index + 1 ,means target > ME ,hence no need to check in lower range
        # Move EndIndex = ME Index -1   [ SI..EI.ME] --> List size got reduced by moving index from ending
                # elif endIndex Elem < ME, move the start index from current pos to ME index + 1 ,means target > ME ,hence no need to check in lower range
    startIndex= 0
    endIndex = len(inputList)-1

    while startIndex < endIndex:
        middleElemPtr = (startIndex+endIndex)//2
        middleElem = inputList[middleElemPtr]

        if ( target == middleElem):
            print("target found & its index:%s" % inputList.index(inputList[middleElem]))
            return middleElem
        elif(inputList[startIndex] < middleElem):
            startIndex = middleElemPtr+1
        elif ( inputList[endIndex] > middleElem):
            endIndex = middleElemPtr-1
    return -1




if __name__ == '__main__':
    input = [-1,0,3,5,9,12]
    Original_list = input
    #binarySearch(input,7)
    #usingBuiltIn(input,7)
    usingLeeBSTsearch(Original_list,9)
