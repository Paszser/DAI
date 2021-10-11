def cribaEratostenes(numero):
    cadena = ""
    string  = "<h1>Criba de Eratostenes</h1>"
    prime = [True for i in range(numero + 1)]
    p = 2
    while p * p <= numero:
        if prime[p] == True:
            for i in range(p * p, numero + 1, p):
                prime[i] = False
        p += 1

    for p in range(0, numero):
        if prime[p]:
            cadena += str(p) + ", "

    cadena = cadena[:-2]

    string += "<h2>Números primos hasta " + str(numero) + "</h2>"
    string += "<div=resultado>" + cadena + "</div>"
    return string