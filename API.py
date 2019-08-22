from flask import Flask, jsonify, request
from flask_cors import CORS
import datetime
import random

app = Flask(__name__)
CORS(app)

tipo_medicion = {'sensor':'PH0-14', 'variable':'PH', 'unidades':'Nivel de PH'}

mediciones=[
    {'fecha':datetime.datetime.now(), **tipo_medicion, 'valor':random.randint(5,11)},
    {'fecha':datetime.datetime.now(), **tipo_medicion, 'valor':random.randint(5,11)},
    {'fecha':datetime.datetime.now(), **tipo_medicion, 'valor':random.randint(5,11)},
    {'fecha':datetime.datetime.now(), **tipo_medicion, 'valor':random.randint(5,11)},
    {'fecha':datetime.datetime.now(), **tipo_medicion, 'valor':random.randint(5,11)},
    {'fecha':datetime.datetime.now(), **tipo_medicion, 'valor':random.randint(5,11)}
]

@app.route('/', methods=['GET'])
def getAll():
    return jsonify(mediciones)

@app.route('/mayoresque/<string:date>', methods=['GET'])
def getMayoresA(date):
    return date;

@app.route('/', methods=[''])
app.run(port=80, debug=True)
