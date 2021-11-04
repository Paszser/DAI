def balanced(str):
    open_bracket = "["
    close_bracket = "]"
    stack = []
    for i in str:
        if i == open_bracket:
            stack.append(i)
        elif i == close_bracket:
            if len(stack) > 0:
                stack.pop()
            else:
                return "no están"
    if len(stack) == 0:
        return "están"
    else:
        return "no están"
