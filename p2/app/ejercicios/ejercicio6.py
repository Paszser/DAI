import re

def exp_reg(string):
    if bool(re.match(r"[\w\s]+[A-Z]", string)):
        str = "La cadena es una palabra seguida de un espacio y una letra mayúscula"
    elif bool(re.match(r"^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,3})$", string)):
        str = "La cadena es una dirección de correo válida"
    elif bool(re.match(r"^\d{4}([\ \-]?)\d{4}\1\d{4}\1\d{4}$", string)):
        str = "La cadena es un número de tarjeta de crédito separado por espacios o guiones"
    else:
        str = "La cadena no coincide con ninguna de las opciones"

    return str