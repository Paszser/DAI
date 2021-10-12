import math 
def cribaEratostenes(sieveSize):
    cadena = ""
    string  = "<h1>Criba de Eratostenes</h1>"
    #creating Sieve.
    sieve = [True] * (sieveSize+1)
    # 0 and 1 are not considered prime.
    sieve[0] = False
    sieve[1] = False
    for i in range(2,int(math.sqrt(sieveSize))+1):
        if sieve[i] == False:
            continue
        for pointer in range(i**2, sieveSize+1, i):
            sieve[pointer] = False
    # Sieve is left with prime numbers == True
    primes = []
    for i in range(sieveSize+1):
        if sieve[i] == True:
            primes.append(i)
    string += "<h2>Números primos hasta " + str(sieveSize) + "</h2>"
    string += "<div=resultado>" + str(primes) + "</div>" 
    return string