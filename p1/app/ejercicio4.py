def ejercicioFibonacci(n):
    cadena = "<h1>Sucesión de Fibonacci</h1>"
    cadena += "<h2>El número en la posición "+str(n)+" de la sucesión es: </h2>"
    cadena += "<div=resultado>"
    cadena += str(fibonacci(n))
    cadena += "</div>"
    return cadena

def fibonacci(n):
  if n<=0:
    return "El número debe ser mayor que 0."
  elif n==1:
    return 0
  elif n==2:
    return 1
  else:
    return fibonacci(n-1)+fibonacci(n-2)