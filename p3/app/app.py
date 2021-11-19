#Pruebas realizadas con httpie
#http -v http://0.0.0.0:5000/api/friends    GET, muestra todos los pokémon
#http -f POST http://0.0.0.0:5000/api/friends name=prueba season=2021.0 number=2021.0 airdate=2021/11/10 airtime=10:00 summary="RESUMEN"       POST, añade un Pokémon
#http -v http://0.0.0.0:5000/api/friends/618012220814c9b1b4f5d582   En el caso de añadir otro capitulo copiar el id que se genera cuando se hace POST      GET con id
#http -f PUT http://0.0.0.0:5000/api/friends/618012220814c9b1b4f5d582 name=prueba_editado season=2021.1 number=2021.1 airdate=2021/11/11 airtime=11:00 summary="RESUMEN EDITADO"
#http DELETE http://0.0.0.0:5000/api/friends/618012220814c9b1b4f5d582

from flask import Flask, url_for, render_template, session, flash, request, jsonify
from pymongo import MongoClient
from bson import ObjectId
#from flask_restful import Resource, Api, reqparse
import codecs, model, re, random, itertools

app = Flask(__name__, static_url_path='/static')
app.secret_key = '1234'

client = MongoClient("mongo", 27017) # Conectar al servicio (docker) "mongo" en su puerto estandar
db = client.SampleCollections        # Elegimos la base de datos de ejemplo

#####################################################
############# Formulario de Búsquedas ###############
#####################################################

# Ruta Index
@app.route('/')
def home():
    return render_template('index.html')

# Ruta paginada que muestra los Pokémon
@app.route('/pokemon/<int:pag>', methods=['GET', 'POST'])
def busqueda(pag):
	# Obtenemos la lista de todos los pokémons con su id
	lista_pkms = []
	lista_pkms = obtener_pokemons(pag)
	# Encontramos los documentos de la coleccion "samples_pokemon"
	if request.method == 'POST':
		busqueda_pkmns = []
		# Si no se busca nada
		if request.form['pokemon'] is "":
			msg = "Por favor introduzca el nombre de un Pokémon"
			alert = "alert alert-warning"
			flash(msg)
			return render_template('pokemon.html', pokemons=busqueda_pkmns, Alert=alert, lista_completa = lista_pkms, pag=pag)
		
		# Se realiza la búsqueda
		else:
			pokemon_a_buscar = request.form['pokemon']
			pokemons = db.samples_pokemon.find({"name": pokemon_a_buscar},{"_id": 0, "num": 1, "name": 1, "img": 1, "type": 1, 'height': 1,
												'weight': 1, 'weaknesses': 1});
						
			for pokemon in pokemons:
				busqueda_pkmns += ([{'name': pokemon.get("name"), 'id': pokemon.get("num"), 'type': pokemon.get("type"), 
									 'height': pokemon.get("height"), 'weight': pokemon.get("weight"), 'img': pokemon.get("img"),
									 'weaknesses': pokemon.get("weaknesses")}])

			return render_template('pokemon.html', pokemons=busqueda_pkmns, lista_completa = lista_pkms, pag=pag)
			# a los templates de Jinja hay que pasarle una lista, no el cursor	
	else:
		return render_template("pokemon.html", lista_completa = lista_pkms, pag=pag)

#Manejador de Error
@app.errorhandler(404)
def noExistePagina(error):
    return "<h1>La página que intentas buscar no existe.</h1>"

# URL to Static files
with app.test_request_context():
    print(url_for('static', filename='index.html'))

# Obtiene la parte de la lista de Pokémon que se va a mostrar en la página correspondiente 
def obtener_pokemons(npag):
	pokemons = db.samples_pokemon.find({},{"_id": 0, "num": 1, "name": 1});
	lista = []
	stop = npag * 10
	start = stop - 10
	if stop == 150:
		stop = 151
	for pokemon in itertools.islice(pokemons , start, stop):
		lista += ([{'name': pokemon.get("name"), 'id': pokemon.get("num")}])
	return lista

###########################################
######## API RESTFULL usando FLASK ########
###########################################

@app.route('/api/pokemon', methods=['GET', 'POST'])
def api_get_post():
	if request.method == 'POST':
		try:
			pokemon = {'name': request.form['name'],
						'type': request.form['type'],
						'height': request.form['height'],
						'weight': request.form['weight'],
						'img': request.form['img'],
						'weaknesses': request.form['weaknesses']}
			db.samples_pokemon.insert_one(pokemon)
			return jsonify({'id': str(pokemon['_id'])})
		except Exception:
			return jsonify({'error': 'No se ha podido añadir el Pokémon'}), 400
	elif request.method == 'GET':
		lista_get = []
		if request.args.get('name') is not None:
			nombre = str(request.args.get('name'))
			pokemons = db.samples_pokemon.find({'name': nombre})
		elif request.args.get('type') is not None:
			type = str(request.args.get('type'))
			pokemons = db.samples_pokemon.find({'type': type})
		elif request.args.get('height') is not None:
			height = float(request.args.get('height'))
			pokemons = db.samples_pokemon.find({'height': height})
		elif request.args.get('weight') is not None:
			weight = float(request.args.get('weight'))
			pokemons = db.samples_pokemon.find({'type': weight})
		elif request.args.get('img') is not None:
			img = str(request.args.get('img'))
			pokemons = db.samples_pokemon.find({'img': img})
		elif request.args.get('weaknesses') is not None:
			weaknesses = float(request.args.get('weaknesses'))
			pokemons = db.samples_pokemon.find({'weaknesses': weaknesses})
		else:
			pokemons = db.samples_pokemon.find()
		for pokemon in pokemons:
			lista_get.append({
				'id': str(pokemon.get('_id')),
				'name': pokemon.get('name'),
				'type': pokemon.get('type'),
				'weight': pokemon.get('weight'),
				'height': pokemon.get('height'),
				'weaknesses': pokemon.get('weaknesses'),
				'img': pokemon.get('img'),
			})
		return jsonify(lista_get)

@app.route('/api/pokemon/<id>', methods=['GET', 'PUT', 'DELETE'])
def api_get_put_delete(id):
	if request.method == 'GET':
		try:
			pokemon = db.samples_pokemon.find_one({'_id': ObjectId(id)})
			return jsonify({
                'id': id,
                'name': pokemon.get('name'),
                'type': pokemon.get('type'),
                'height': pokemon.get('height'),
                'weight': pokemon.get('weight'),
                'img': pokemon.get('img'),
                'weaknesses': pokemon.get('weaknesses')
            })
		except Exception:
			return jsonify({'error': 'No se ha encontrado el Pokémon'}), 404

	if request.method == 'PUT':
		try:
			db.samples_pokemon.find_and_modify(query={'_id':ObjectId(id)},
			update={"$set": {
				'name': request.form['name'],
				'type': request.form['type'],
				'height': request.form['height'],
				'weight': request.form['weight'],
				'img': request.form['img'],
				'weaknesses': request.form['weaknesses']
			}}, upsert=False, full_response= True)
			
			return jsonify({"Editado": id})
		except Exception:
			return jsonify({'Error': 'Pokémon no encontrado'}), 404

	if request.method == 'DELETE':
		try:
			pokemon = db.samples_pokemon.delete_one({'_id': ObjectId(id)})
			return jsonify({'Borrado': id})
		except Exception:
			return jsonify({'error': 'No se ha podido eliminar el Pokémon'}), 400
			