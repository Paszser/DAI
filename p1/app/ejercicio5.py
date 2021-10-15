def balanceados(cadena):
    string = "<h1>Corchetes balanceados</h1>"
    string += "<h2>¿Están estos corchetes balanceados? Corchetes: " + cadena + "</h2>"
    open_bracket = "["
    close_bracket = "]"
    stack = []
    for i in cadena:
        if i == open_bracket:
            stack.append(i)
        elif i == close_bracket:
            if len(stack) > 0:
                stack.pop()
            else:
                return string + "No lo están"
    if len(stack) == 0:
        return string + "Lo están"
    else:
        return string + "No lo están"
