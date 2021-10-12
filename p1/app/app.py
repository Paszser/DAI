from flask import Flask, url_for
from flask import send_from_directory
import codecs

app = Flask(__name__)


import ejercicio2 as ej2
import ejercicio3 as ej3
import ejercicio4 as ej4
import ejercicio5 as ej5
import ejercicio6 as ej6
import opcional as op

@app.route('/')
def root():
    return app.send_static_file('index.html')

# Ejercicio 2
@app.route("/ordena/<lista>")
def ejercicio2(lista):
  return ej2.ordena(lista)

# Ejercicio 3
@app.route('/eratostenes/<int:n>')
def ejercicio3(n):
    return ej3.cribaEratostenes(n)

# Ejercicio 4
@app.route('/fibonacci/<int:n>')
def ejercicio4(n):
    return ej4.ejercicioFibonacci(n)

# Ejercicio 5
@app.route('/balanceados/<cadena>')
def ejercicio5(cadena):
  return ej5.balanceados(cadena)

# Ejercicio 6
@app.route('/expresiones/<frase>')
def ejercicio6(frase):
  return ej6.expresiones_regulares(frase)

# Opcional
@app.route('/svg')
def opcional():
  return op.generate()

@app.errorhandler(404)
def noExistePagina(error):
  return "<h1>La página que intentas buscar no existe.</h1>"

# URL to Static files
with app.test_request_context():
  print(url_for('static', filename='index.html'))