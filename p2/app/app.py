from flask import Flask, url_for, send_from_directory, render_template, session, flash, request
from ejercicios import ejercicio1 as ejer1, ejercicio2 as ejer2, ejercicio3 as ejer3, ejercicio4 as ejer4, ejercicio5 as ejer5, ejercicio6 as ejer6
import codecs, model, re, random

app = Flask(__name__, static_url_path='/static')
app.secret_key = '1234'

@app.route('/')
def home():
    enlaces = Enlaces(url_for('home'), "Home")
    return render_template('index.html', enlaces=enlaces)

@app.route('/login', methods=['GET', 'POST'])
def login():
    enlaces = Enlaces(url_for('login'), "Login")
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        if model.login_bd_email(email):
            if model.login_bd_password(email, password):
                flash('Se ha iniciado sesión correctamente')
                session['email'] = email
                session['password'] = password
                app.logger.debug('%s logged in successfully', email)
                app.logger.debug('%s logged from', request.remote_addr)
                return render_template('index.html', Alert="alert alert-success", enlaces=enlaces, emailLog=email)
            else:
                flash('La contraseña es incorrecta.')
                return render_template('login.html', Alert="alert alert-danger", enlaces=enlaces)
        else:
            flash('El usuario no existe')
            return render_template('login.html', Alert="alert alert-danger", enlaces=enlaces)
    else:
        return render_template('login.html', enlaces=enlaces)

@app.route('/register', methods=['GET', 'POST'])
def register():
    enlaces = Enlaces(url_for('register'), "Registro")
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        if model.login_bd_email(email):
            flash('Ya existe ese usuario.')
            return render_template('login.html', Alert="alert alert-danger")
        else:
            model.add_user(email, password)
            flash('Se ha completado correctamente el registro. Puede proceder a iniciar sesión')
            return render_template('login.html', Alert="alert alert-success", enlaces=enlaces)
    else:
        return render_template('register.html', enlaces=enlaces)

@app.route("/logout")
def logout():
  enlaces = Enlaces(url_for('home'), "Home")
  session.pop('email')
  session.pop('password')
  session.clear()
  flash('Se ha cerrado la sesión.')
  return render_template('index.html', Alert="alert alert-success" ,enlaces=enlaces)

@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    enlaces = Enlaces(url_for('ejercicio1'), "Ejercicio 1")
    if request.method == 'POST':
        if not 'rand_num' in session:
            session['rand_num'] = random.randint(1,100)
            session['num_tries'] = 0
        if request.form['number'] is "":
            msg = "Por favor introduzca un número."
            alert = "alert alert-warning"
        else:
            number_user = int(request.form['number'])
            msg, alert = ejer1.guess(session['rand_num'], number_user)
            session['num_tries'] += 1
            if session['num_tries'] > 10:
                session.pop('rand_num')
                session.pop('num_tries')
                msg = "Has perdido por superar el número de intentos permitido :("
            elif msg != "":
                if alert == "alert alert-danger":
                    msg += f". Llevas {session['num_tries']} intentos."
                elif alert == "alert alert-success":
                    msg += f" Lo conseguiste en {session['num_tries']} intentos."
            flash(msg)
    
        if alert == "alert alert-success":
            session.pop('rand_num', None)
            session.pop('num_tries', None)

        return render_template('ejer1.html', Alert=alert, enlaces=enlaces)
    else:
        return render_template('ejer1.html', enlaces=enlaces)

@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    enlaces = Enlaces(url_for('ejercicio2'), "Ejercicio 2")
    if request.method == 'POST':
        if request.form['text'] is "":
            msg = "Por favor introduzca un conjunto de números."
            alert = "alert alert-warning"
        else:
            lista = request.form['text']
            time_bubble, time_sort, list_sort, list_bubble = ejer2.ordena(lista)
            msg = f"La lista por burbuja ordenada es: {list_bubble}, con un tiempo de {time_bubble}s. La lista por sort es: {list_sort}, con un tiempo de {time_sort}s."
            alert = "alert alert-success"
        flash(msg)

        return render_template('ejer2.html', Alert=alert, enlaces=enlaces)
    else:
        return render_template('ejer2.html', enlaces=enlaces)

@app.route('/ejercicio3', methods=['GET', 'POST'])
def ejercicio3():
    enlaces = Enlaces(url_for('ejercicio3'), "Ejercicio 3")
    if request.method == 'POST':
        if request.form['number'] is "":
            msg = "Por favor introduzca un número."
            alert = "alert alert-warning"
        else:
            if request.form['number'] == '0':
                msg = "El número debe ser mayor que 0"
                alert = "alert alert-warning"
            else:
                number_user = int(request.form['number'])
                primes = ejer3.cribaEratostenes(number_user)
                msg = f"La criba de Erastótenes hasta {request.form['number']} es: {primes}."
                alert = "alert alert-success"
            flash(msg)

        return render_template('ejer3.html', Alert=alert, enlaces=enlaces)
    else:
        return render_template('ejer3.html', enlaces=enlaces)

@app.route('/ejercicio4', methods=['GET', 'POST'])
def ejercicio4():
    enlaces = Enlaces(url_for('ejercicio4'), "Ejercicio 4")
    if request.method == 'POST':
        if request.form['number'] is "":
            msg = "Por favor introduzca un número."
            alert = "alert alert-warning"
        else:
            number_user = int(request.form['number'])
            num_fibonacci, msg = ejer4.fibonacci(number_user)
            if number_user == 0:
                alert = "alert alert-warning"
            else:
                msg = f"El número en la posición {request.form['number']} es: {num_fibonacci}."
                alert = "alert alert-success"
        flash(msg)

        return render_template('ejer4.html', Alert=alert, enlaces=enlaces)
    else:
        return render_template('ejer4.html', enlaces=enlaces)

@app.route('/ejercicio5', methods=['GET', 'POST'])
def ejercicio5():
    enlaces = Enlaces(url_for('ejercicio5'), "Ejercicio 5")
    if request.method == 'POST':
        if request.form['text'] is "":
            msg = "Por favor introduzca los corchetes."
            alert = "alert alert-warning"
        else:
            corchetes = request.form['text']

            '''for i in corchetes:
                if (i != "[") or (i != "]"):
                    msg = "Por favor, introduce solamente corchetes"
                    flash(msg)
                    alert = "alert alert-danger"
                    return render_template('ejer5.html', Alert=alert, enlaces=enlaces)'''

            balanced = ejer5.balanced(corchetes)
            msg = f"Los corchetes {balanced} balanceados."
            alert = "alert alert-success"
        flash(msg)

        return render_template('ejer5.html', Alert=alert, enlaces=enlaces)
    else:
        return render_template('ejer5.html', enlaces=enlaces)

@app.route('/ejercicio6', methods=['GET', 'POST'])
def ejercicio6():
    enlaces = Enlaces(url_for('ejercicio6'), "Ejercicio 6")
    if request.method == 'POST':
        if request.form['text'] is "":
            msg = "Por favor introduzca una frase"
            alert = "alert alert-warning"
        else:
            str = request.form['text']
            cadena = ejer6.exp_reg(str)
            msg = cadena
            alert = "alert alert-success"
        flash(msg)

        return render_template('ejer6.html', Alert=alert, enlaces=enlaces)
    else:
        return render_template('ejer6.html', enlaces=enlaces)
    
with app.test_request_context():
    print(url_for('home'))
    print(url_for('login'))
    print(url_for('register'))
    print(url_for('ejercicio1'))
    print(url_for('ejercicio2'))
    print(url_for('ejercicio3'))
    print(url_for('ejercicio4'))
    print(url_for('ejercicio5'))
    print(url_for('ejercicio6'))

#Manejador de Error
@app.errorhandler(404)
def noExistePagina(error):
  return "<h1>La página que intentas buscar no existe.</h1>"

# URL to Static files
with app.test_request_context():
  print(url_for('static', filename='index.html'))

def Enlaces(url, nom_pagina):
    enlaces = []

    if not 'ult_url' in session:
        session['ult_url'] = url
        session['ult_nom_pagina'] = nom_pagina
        enlaces = [{'url': session['ult_url'], 'nom_pagina': session['ult_nom_pagina']}]
    elif not 'penultima_url' in session:
        session['penultima_url'] = session['ult_url']
        session['penultima_nom_pagina'] = session['ult_nom_pagina']
        session['ult_url'] = url
        session['ult_nom_pagina'] = nom_pagina
        enlaces = [{'url': session['ult_url'], 'nom_pagina': session['ult_nom_pagina']},
                    {'url': session['penultima_url'], 'nom_pagina': session['penultima_nom_pagina']}]
    else:
        session['antepenultima_url'] = session['penultima_url']
        session['antepenultima_nom_pagina'] = session['penultima_nom_pagina']
        session['penultima_url'] = session['ult_url']
        session['penultima_nom_pagina'] = session['ult_nom_pagina']
        session['ult_url'] = url
        session['ult_nom_pagina'] = nom_pagina
        enlaces = [{'url': session['ult_url'], 'nom_pagina': session['ult_nom_pagina']},
                    {'url': session['penultima_url'], 'nom_pagina': session['penultima_nom_pagina']},
                    {'url': session['antepenultima_url'], 'nom_pagina': session['antepenultima_nom_pagina']}]
    return enlaces