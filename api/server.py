from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
from datetime import datetime, timedelta
from controllers.tipoSensores import tipoSensor
import random

app = Flask(__name__)
CORS(app)

mediciones = []

now = datetime.now()
dateFormat = '%Y-%m-%d %H:%M:%S'

def getDate():
    start = datetime.strptime('2016-7-12 00:00:00', dateFormat)
    end = datetime.strptime(datetime.strftime(now, dateFormat), dateFormat)
    delta = timedelta(
        seconds=random.randint(0, int((end - start).total_seconds())),
    )
    return start + delta


tipo_medicion = {
    'sensor': 'TSL2561',
    'variable': 'Luz Solar',
    'unidades': 'Lux'
    }


for i in range(0, 7):
    mediciones.append({
        'fecha': getDate(),
        'origen': " ",
        'valor': random.randint(40000, 80000),
        'codigoSensor': random.randint(1,4),
        'observacion': "nada"
    })

@app.route("/tipoSensor/", methods=['GET'])
def getAll():
    return (tipoSensor.list())

@app.route("/tipoSensor/", methods=['POST'])
def postOne():
    body = request.json
    return (tipoSensor.create(body))

if(__name__ == '__main__'):
    app.run()
