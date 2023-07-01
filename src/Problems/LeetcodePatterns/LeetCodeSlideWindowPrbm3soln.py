def longestSubStrwithoutRepeatChar(s : str):
    """To find the longest Sub str without Repeat chars"""

    begin = end = 0
    length = 0
    seen = {}
    for char in s:
        seen[char] = 0
    print(seen)

    ans = ""
    print(s)
    while end < len(s):
        current = s[end]
        print("---------")
        print("current",current)
        print("before begin",begin)
        print("before end", end)
        if seen[current] == 1 and seen[current] >= begin:
            print("repeat found")
            begin = seen[current] + 1
        else:
            print("repeat not found")
            seen[current] = end
            end = end + 1
        print("after begin", begin)
        print("after end", end)
        if (end - begin) > length:
            length = end - begin
            ans = s[begin:length+1]

    print("ans",ans)
    print("len(ans)", len(ans))
    return len(ans)

longestSubStrwithoutRepeatChar("abcabcbb")