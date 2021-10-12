def ordena(lista):
    return burbuja(lista) + insercion(lista)

def burbuja(A):
    m = A
    for i in range(1,len(A)):
        for j in range(0,len(A)-i):
            if(A[j+1] < A[j]):
                aux=A[j];
                A[j]=A[j+1];
                A[j+1]=aux;
    
    cadena = "<h1> Ordenación por burbuja</h1>"
    cadena += "<h2>Lista Inicial: " + m + "</h2>"
    cadena += "<h2>Lista Ordenada: " + A + "</h2>"
    

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

