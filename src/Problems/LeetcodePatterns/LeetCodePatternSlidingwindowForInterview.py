from collections import Counter
import sys


def slidingWindowStrPrbm(s, t):
    ''' To find longest substring from given string'''
    table = {}
    for char in t:
        table[char] = 1
    print(table)
    counter = len(table)
    print("counter:%s" % (counter))

    begin = end = 0
    ansLen = sys.maxsize
    ans = ""

    # start sliding window
    while end < len(s):
        currStrRange = s[begin:end]
        print("currStrRange", currStrRange)

        # endChar = s[end]
        # if endChar in table:
        #     table[endChar] = 0
        #     counter = counter - 1
        # end = end + 1
        print("table", table)
        while counter == 0:
            if end - begin < ansLen:
                ansLen = end - begin
                ans = s[begin:end]
            # startChar = s[begin]
            # if startChar in table:
            #     table[startChar] = 1
            #     counter = counter + 1
            # begin = begin + 1

    print("ans", ans)


# slidingWindowStrPrbm("ADOBECODEBANC","ABC")
slidingWindowStrPrbm("fa4chba4c", "abc")