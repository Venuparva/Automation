import collections
import string

'''def longestPali(inputString: string) -> string:
  To return Longest palindrome for given string

    Input : abccccdd -> mix of both even n odd num charcs
    O/p : dccaccd -> 7

     Input : abcccaacdd -> mix of both even n odd num charcs --> a-3,b-1,c-4,d-2 => a-2,b-1,c-4,d-2 => aabccccdd
    O/p : dccabaccd -> 9 -->

    case-2 : a -> just single
    O/p : 1

    Case-3: '' -> empty str
    O/p : -1

    case-2 : bb -> no uniq case
    O/p : 2

    My Algm:
    1. Count the chars in string both odd n even
    2. Handle both edge n negative cases
    3. take even cnt as it is ,if more than 1 odd count,like b=1 a=1 ,then pick only 1
    4. if odd > 1 ,then convert it into even by minus-1 like c=3 ,then consider only c=3-1=2
    5.count the total values
    '''

#Algm:
'''1.count number of each characs  
2.split number of odd & even chars count
3. odd count : 
        a. case-1 : only 1 odd char --> a:1-->count as it is
        b. case-2 : more than 1 odd chars exists --> c:3,e:5--> reduce c-1 & e-1
        c. case-3 : both 1 & more than one odd chars count--> a:1,c:3,e:5
        Reduce 1 from odd char count  if odd count > 1 & also more than 1 odd char count
4.total count = odd + even
-----------
learnings : use AND for multiple cnds compare

'''

import string
charCount_dict = {}
def longestPalidrom(inputString : string) -> string:
    ''' This function used to find longest palindrom available in given string'''
    evenCharCount = ""
    oddCharCount = ""
    uniqCharCount = ""
    pali_start_str = pali_end_str = longestPali = ""
    totalFinalCount = 0
    for char in inputString:
        print("inputChar:%s" % char)
        # Step-1 : count number of each chars -> done
        if char in charCount_dict:
            charCount_dict[char] = charCount_dict[char]+1
        else:
             charCount_dict[char] = 1
    print("charCount: %s" %(charCount_dict))
    # Step-2 : split number of odd & even chars
    for charcount in charCount_dict:
        print("incoming iteration:%s:count:%s" % (charcount,charCount_dict[charcount]))
        if charCount_dict[charcount]%2 == 0:
            totalFinalCount = totalFinalCount + charCount_dict[charcount]
            evenCharCount = evenCharCount + (charCount_dict[charcount])*charcount
            evenSplitCount = charCount_dict[charcount]//2 * charcount
            pali_start_str = pali_start_str + evenSplitCount
            pali_end_str = pali_end_str + evenSplitCount
        elif (charCount_dict[charcount]%2 != 0 and charCount_dict[charcount] > 1):
            totalFinalCount = totalFinalCount + charCount_dict[charcount]-1
            oddCharCount = oddCharCount + (charCount_dict[charcount]-1)*charcount
            evenSplitCount = charCount_dict[charcount] // 2 * charcount
            pali_start_str = pali_start_str + evenSplitCount
            pali_end_str = pali_end_str + evenSplitCount
        elif (charCount_dict[charcount] == 1 and charcount not in uniqCharCount):
            uniqCharCount = uniqCharCount + charcount
        else:
            print("final else enter")
        print("totalFinalCount count:%s:after char:%s:iteration" % (totalFinalCount,charcount))
        print("-----------")
    if len(uniqCharCount) >= 1:
        totalFinalCount = totalFinalCount + 1
        longestPali = pali_start_str + uniqCharCount[0] + pali_end_str[::-1]
    print("pali_start_str count:%s" % (pali_start_str))
    print("pali_end_str count:%s" % (pali_end_str))
    print("Longest-Pali count:%s" % (longestPali))
    print("totalFinalCount count:%s" % (totalFinalCount))


def longestPalindrome(s):
    ans = 0
    print("count:%s" % collections.Counter(s).items())
    for v in collections.Counter(s).items():   # this will give each char n its count
        ans += v[1] / 2 * 2  # equals to => Math.floor(value / 2) * 2
        print("char:%s:ans:%s" % v,ans)
        if ans % 2 == 0 and v[1] % 2 == 1: # take only 1 char one time
            print("if stmt true")
            ans += 1
        else:
            print("else stmt true")
    print("answer:%s" %ans)
    return ans

#longestPalidrom("bananas")
longestPalindrome("bccfccdd")


