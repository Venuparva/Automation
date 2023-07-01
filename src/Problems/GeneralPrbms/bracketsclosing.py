def isValid(s: str) -> bool:
    stack = []
    mapping_dict = {
        '(': ')',
        '[': ']',
        '{': '}'
    }
    # for char in s:
    #     if char in mapping_dict.keys():
    #         stack.append(mapping_dict[char])
    #     elif not stack or stack[-1] != char:
    #         print(False)
    #     else:
    #         stack.pop()
    # print(len(stack) == 0)

    for char in s:
        # check whether incoming char is key (open bracket) of mapping_dict
        # please insert it into stack
        if char in mapping_dict.keys():
            stack.append(char)
        # if incoming char is value (closing bracket) of mapping_dict,then check whether last element of stack is its own key
        # if its yes,then pop ,else return false
        elif char in mapping_dict.values():
            if char == mapping_dict.get(stack[-1]):
                stack.pop()
            else:
                return False
        elif not stack:
            print("Empty stack")
            return False
    print(bool(len(stack) == 0))
    return bool(len(stack) == 0)

isValid("()")