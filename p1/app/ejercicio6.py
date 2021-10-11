import re


def expresiones_regulares(frase):
    cadena = "<h1>Reconociemiento de cadenas</h1>"
    cadena += "<h2>Para empezar a funcionar tiene que introducir: </h2>"
    cadena += "<ul> <li>Una palabra seguida de un espacio y una letra mayuscula</li>"
    cadena += "<li>Una dirección de correo válida</li>"
    cadena += "<li>Un número de tarjeta de crédito separada por espacios o guiones</li>"
    cadena += "</ul>"
    cadena += "<h2>Resultado: </h2>"
    if bool(re.match(r"[\w\s]+[A-Z]", frase)):
        cadena += "La cadena es una palabra seguida de un espacio y una letra mayúscula"
    elif bool(re.match(r"^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,3})$", frase)):
        cadena += "La cadena es una dirección de correo válida"
    elif bool(re.match(r"^\d{4}([\ \-]?)\d{4}\1\d{4}\1\d{4}$", frase)):
        cadena += "La cadena es un número de tarjeta de crédito separado por espacios o guiones"
    else:
        cadena += "La cadena no coincide con ninguna de las opciones"

    return cadena