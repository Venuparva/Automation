import itertools
from typing import List

input_iter = [8,1,2,2,3]

#Expected o/p : outputlist-[4, 0, 1, 1, 3] --> how many numbers less than current number ex. (1,2,2,3) < 8 => 4 numbers ,llly 1=> 0 , 2 => 1 ,3 => 2 (1,2)
#------my Solun-------
outputlist = []
cmp_list = []
# iter0, iter1 = itertools.tee(input_iter, 2)
'''for item in input_iter:
    result = list(map(lambda x: x<item, input_iter))
    result.count(True)
    outputlist.append(result.count(True))
print("outputlist-%s"%(outputlist))'''
# print("Itr-%s"%(iter0.__next__()))
# print("Itrnew-%s"%(iter1.__next__()))
# len_gen = itertools.accumulate(map(lambda x: 1, iter0))
# print("%s"%(len_gen))

#------my 2nd Solun-------
# 1.sort the list and count number less than current number
#[8,1,2,2,3]
#[4,0,1,1,3] => expected o/p
# Sort it
# [8, 3, 2, 2, 1]
#[1, 2, 2, 3, 8]
#count from current index till startIndex (backwards) only if values are different,by storing compared list in done list
# If values are same,check in done list and move on to next value

#--------------His logic----------
#things learned:
# 1. To avoid index OOR (out of range) error using range(len(sorted_list_reverse)-1)
# 2. Handling Current_item n next_item iteration is possible due to above range under same iteration
# 3. Store 0 for last item since its already in reverse order

def countNums(input_list: List[int]) -> List[int]:
    count_dict = {}
    for curr_index in range(len(sorted_list_reverse)-1): # To avoid OOR (out of range)error # memorize sorted & reverse=True
        # pick curr & nxt item for comparison
        curr_item = sorted_list_reverse[curr_index] # 8 # Handling Current_item  under same  iteration
        next_item = sorted_list_reverse[curr_index+1] # 3 Handling next_item  under same  iteration
        # compare curr & nxt element
        if curr_item > next_item:
            remaining_values_cnt = len(sorted_list_reverse) - (curr_index+1) # 8 > 3 ( minus total length - next item index)
            count_dict[curr_item] = remaining_values_cnt # Store that value in dict { 8: 4 } -> Since 4 elements are smaller than 8
        else:
            print("looks like same number came")
        count_dict[sorted_list_reverse[-1]] = 0 # store last value count is zero ,since its already sorted list
        # and no element possible after last one
        print("sorted-1:%s" % count_dict)
    for num in input_iter:
        outputlist.append(count_dict[num]) # This is needed to print the given list order count - input_iter = [8,1,2,2,3]
    print("outputlist:%s" % outputlist)

sorted_list_reverse = sorted(input_iter,reverse=True) # memorize sorted & reverse=True
countNums(sorted_list_reverse)