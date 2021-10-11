def ordena(lista):
    return burbuja(lista) + insercion(lista)

def burbuja(matrix):
    m = matrix
    for i in range(len(matrix)-1,0,-1):
        for j in range(i):
            if matrix[j]>matrix[j+1]:
                temp = matrix[j]
                matrix[j] = matrix[j+1]
                matrix[j+1] = temp
    
    cadena = "<h1> Ordenación por burbuja</h1>"
    cadena += "<h2>Lista Inicial: " + m + "</h2>"
    cadena += "<h2>Lista Ordenada: " + matrix + "</h2>"
    

def insercion(matrix):
    m = matrix
    for i in range(len(matrix)):
        for j in range(i,0,-1):
            if(matrix[j-1] > matrix[j]):
                aux=matrix[j];
                matrix[j]=matrix[j-1];
                matrix[j-1]=aux;

    cadena = "<h1> Ordenación por inserción</h1>"
    cadena += "<h2>Lista Inicial: " + m + "</h2>"
    cadena += "<h2>Lista Ordenada: " + matrix + "</h2>"

