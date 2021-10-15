def ordena(lista):
    return burbuja(lista) #+ insercion(lista)
    
def burbuja(A):
    M = A.split(',')
    tam = len(M)
    for i in range(tam):
        for j in range(0, tam - i - 1):
            if M[j] > M[j + 1]:
                M[j], M[j + 1] = M[j + 1], M[j]

    cadena = "<h1>Ordenación por burbuja</h1>"
    cadena += "<h2>Lista inicial: " + A + "</h2>"
    cadena += "<h2>Lista ordenada: "

    for i in range(0, tam):
        cadena += M[i]
        if i != tam - 1:
            cadena += ", "
    cadena += "</h2>"
    return cadena
    

'''def insercion(matrix):
    m = matrix
    for i in range(len(matrix)):
        for j in range(i,0,-1):
            if(matrix[j-1] > matrix[j]):
                aux=matrix[j];
                matrix[j]=matrix[j-1];
                matrix[j-1]=aux;

    cadena = "<h1> Ordenación por inserción</h1>"
    cadena2 = cadena + "<h2>Lista Inicial: " + m + "</h2>"
    cadena3 = cadena2 + "<h2>Lista Ordenada: " + matrix + "</h2>"

    return cadena3'''

