from itertools import permutations
maxSum = 0
windowSum = 0
k = 5
input = [100,200,100,400,500,2,600]
#windowSum = map(lambda x,y: x+y,input)
print("done")
#print(list(map(int,windowSum)))

for x in range(k):
    windowSum += input[x]
    print("windowSum:",windowSum)

#WindowSum = 1300 ( sum of first K elements )

i= k
max_sum = 0
while i < len(input):
    windowSum += input[i] - input[i-k]
    max_sum = max(max_sum,windowSum)
    print("maxsum",max_sum)
    i = i+1

#SlidingWindow technique: ->
"""
100,200,100,400,500,2,600
|-----old sum----| for given k = 5
    |---new-sum1----| => new_sum = old_sum(sum from 0 to 4 ) - first_elem(input[0]) + 6th elem(input[5]) => 1300 - 100 + 2 = 1202
        |----new-sum2---| => new-sum2 = new_sum - second_elem(input[0]) + 7th elem(input[6]) => 1202 - 200 + 600 = 1002+600 = 1602
"""

'''
# Find Shortest substring contains desired characters

input : "fa4chba4c"

o/p : abc

'''

input = "fa4chba4c"
expected = "abc"
result = [''.join(p) for p in permutations(input)]
print(result)

for word in result:
    if expected in str(word):
      print("Item found",word)



