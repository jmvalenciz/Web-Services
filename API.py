from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
from time import sleep
from datetime import datetime
import random

now = datetime.now()

def render(view):
    return render_template(view)

def getDate():
    #sleep(random.randint(1,4))
    return now.strftime('%Y-%m-%d %H:%M:%S')

app = Flask(__name__)
CORS(app)

tipo_medicion = {'sensor':'PH0-14', 'variable':'PH', 'unidades':'Nivel de PH'}

mediciones=[
    {'fecha':getDate(),**tipo_medicion,'valor':random.randint(5,11)},
    {'fecha':getDate(),**tipo_medicion,'valor':random.randint(5,11)},
    {'fecha':getDate(),**tipo_medicion,'valor':random.randint(5,11)},
    {'fecha':getDate(),**tipo_medicion,'valor':random.randint(5,11)},
    {'fecha':getDate(),**tipo_medicion,'valor':random.randint(5,11)},
    {'fecha':getDate(),**tipo_medicion,'valor':random.randint(5,11)}
]

@app.route('/', methods=['GET'])
def index():
    return render('index.html')

@app.route('/mediciones', methods=['GET'])
def getAll():
    return jsonify(mediciones)

@app.route('/mediciones/<int:id>', methods=['GET'])
def getById(id):
    return jsonify(mediciones[id])

@app.route('/mayoresque/<string:date>', methods=['GET'])
def getMayoresA(date):
    data = request.get_json()
    return date;

@app.route('/update/<int:dato>', methods=['PUT'])
def updateDato(dato):
    pass

if(__name__=='__main__'):
    app.run()
