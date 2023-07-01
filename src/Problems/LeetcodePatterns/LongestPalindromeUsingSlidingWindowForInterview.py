
def longestPalindrome(s):
    output = ""
    def isPalindrome(inputString):
        print("Orig-Str", inputString)
        print("Rev-Str", inputString[::-1])
        if inputString == inputString[::-1]:
            print("return True")
            return True
        else:
            print("return False")
            return False

    # output = ""
    def slidewindow(s, output=""):
        begin = 0
        end = 0
        print("incoming string", s)
        while end < len(s): # VERY -IMPORTANT ..for moving begin n end indexes..1 HR wasted
            windowString = str(s[begin:end])
            print("windowString", windowString)
            print("output Str-1", output)
            if isPalindrome(windowString) and len(windowString) > len(output):
                output = windowString
                print("output Str", output)
            else:
                print("not palindrome or len is small")
                print("windowString", len(windowString))
                print("output", len(output))
            if end != len(s) - 1:
                end = end + 1
            else:
                print("end reached last char")
                print("-------")
                begin = begin + 1
                end = begin
        print("final-output",output)
        return output

    return slidewindow("babad", output)

longestPalindrome("cbba")

