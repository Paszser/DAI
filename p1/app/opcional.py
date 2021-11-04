import random
def generate():
    cadena = "<h1>Ejercicio opcional</h1>"
    opcion = random.randint(0,3)
    cadena += f'<h2>La opción escogida ha sido la {opcion}:</h2>'

    if opcion == 0:
        rect = '<svg width="1000" height="1000" viewBox="0 0 1000 1000" xmlns="https://www.w3.org/2000/svg">\
                    <style>\
                        rect {\
                            fill: #f33;\
                        }\
                    </style>\
                    <rect x="100" y="200" width="75" height="50" />\
                </svg>'
        cadena += rect

    if opcion == 1:
        ellipse = '<svg height="1000" width="1000">\
                    <ellipse cx="900" cy="80" rx="100" ry="50"\
                    style="fill:yellow;stroke:purple;stroke-width:2" />\
                  </svg>'
        cadena += ellipse

    if opcion == 2:
        circle = '<svg width="1000" height="1000" viewBox="0 0 1000 1000" xmlns="https://www.w3.org/2000/svg">\
                    <circle cx="300" cy="300" r="75" />\
                    style="fill:purple;stroke:pink;Stroke-width:3" />\
                    <circle x="900" y="600" />\
                  </svg>'
        cadena += circle

    if opcion == 3:
        circle = '<svg height="1000" width="1000">\
                    <polyline points="20,20 40,25 60,40 80,120 120,140 200,180"\
                    style="fill:none;stroke:blue;stroke-width:3" />\
                  </svg>'
        cadena += circle    

    return cadena
