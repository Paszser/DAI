
def guess(rand, user_number):
    msg = ""
    alert = ""
    if user_number < rand:
        msg = "El número a encontrar es mayor que el introducido"
        alert = "alert alert-danger"
    elif user_number > rand:
        msg = "El número a encontrar es menor que el introducido"
        alert = "alert alert-danger"
    elif user_number == rand:
        msg = "¡¡Correcto!!"
        alert = "alert alert-success"
    
    return msg, alert
