from collections import Counter
import sys
def slidingWindowStrPrbm(s,t):
    ''' To find longest substring from given string'''
    table = {}
    for char in t:
        table[char] = 1
    print(table)
    counter = len(table)
    print("counter:%s" % (counter))

    startChar = ""
    begin = end = 0
    ansLen = sys.maxsize
    ans = ""

    # start sliding window
    while end < len(s):

        #————————————
        #Section - 0: print current sliding window substring ….Just for debug purpose..you can ignore if you want
        #————————————
        currStrRange = s[begin:end]
        print("currStrRange", currStrRange)  # string value '4chb' after set like this a-0->1

        #————————————
        #Section - 1: Update table for available char from 1 to 0 means a:1->0
        #————————————
        endChar = s[end]  # endIndex moved from b to a..hence update a:1->0 back again

        if endChar in table:
            table[endChar] = 0
            counter = counter - 1
        end = end + 1

        print("table", table)

        #————————————
        # Section-2: Before move into below while..at this time { a:0,b:0,c:0} and also counter = 3 -> 0 means all 3 required values found in current substring
        #————————————
        
        while counter == 0:  # means we found an answer, now try to trim that window by sliding begin to right. Here 'a' will be missing after start index moved from f --> 4..hence a->1,b->0 ,c -> 0..we need to expand endIndex to find a again
            #————————————
            # Section-3: Stroing the o/p if length of new found substring is less than length of previous one
            #————————————-
            if end - begin < ansLen:
                ansLen = end - begin
                ans = s[begin:end]  # 'fa4chb','a4chb','chba', --> still 1 more exits --> ba4c..since len(chba) == len(ba4c)..we are ignoring last 'ba4c' o/p n return chba itself
            #————————————
            #Section - 4: print current sliding window substring ….Just for debug purpose..you can ignore if you want
            #————————————-
            currStrRange = s[begin:end]
            print("New currStrRange after shrink n expand",currStrRange)  # string value 'a4chb' after set like this a-1->0 back
            #————————————
            #Section - 5: Update table for available char from 0 to 1 means a:0->1(just viceversa of section - 1..since required chars are removed from table)
            #————————————
            startChar = s[begin]
            
            if startChar in table:
                table[startChar] = 1
                counter = counter + 1
            begin = begin + 1
    print("ans",ans)
        
#slidingWindowStrPrbm("ADOBECODEBANC","ABC")
slidingWindowStrPrbm("fa4chba4c","abc")


