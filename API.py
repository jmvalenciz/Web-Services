from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
from datetime import datetime, timedelta
from jsonschema import validate
import random

app = Flask(__name__)
CORS(app)

mediciones = []

now = datetime.now()
dateFormat = '%Y-%m-%d %H:%M:%S'
schema = {  # formato de como debe estar el json que se reciba
    "type": "object",
    "properties": {
        "fecha": {"type": "string"},
        "sensor": {"type": "string"},
        "variable": {"type": "string"},
        "unidades": {"type": "string"},
        "valor": {"type": "number"}
    },
}


def view(route):
    return render_template(route)


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
        **tipo_medicion,
        'valor': random.randint(40000, 80000)
    })


@app.route('/', methods=['GET'])
def index():
    return view('index.html')


@app.route('/mediciones/', methods=['GET'])
def getAll():
    return jsonify(mediciones)


@app.route('/mediciones/', methods=['POST'])
def addDato():
    d = request.get_json()
    try:
        validate(instance=d, schema=schema)
    except Exception:
        return jsonify({'error': 'formato del dato erroneo'})
    d['fecha'] = datetime.strptime(d['fecha'], dateFormat)

    if d['sensor'] != tipo_medicion['sensor']:
        return jsonify({'error': 'Tipo de sensor diferente al esperado'})
    if d['variable'] != tipo_medicion['variable']:
        return jsonify({'error': 'Tipo de variable diferente a la esperada'})
    if d['unidades'] != tipo_medicion['unidades']:
        return jsonify({'error': 'Tipo de unidad diferente a la esperada'})
    mediciones.append(d)
    return d


@app.route('/mediciones/fecha', methods=['GET'])
def getByFecha():
    fecha = request.get_json()['fecha']
    if fecha is not None:
        date = datetime.strptime(fecha, dateFormat)
        result = []
        for med in mediciones:
            if med['fecha'] > date:
                result.append(med)
        return jsonify(result)
    else:
        return jsonify({'error': 'Se requiere una fecha'})


@app.route('/update/', methods=['PUT'])
def updateDato():
    dato = request.get_json()
    for i in range(0, len(mediciones)):
        if mediciones[i]['fecha'] == dato['fecha']:
            mediciones[i] = dato
            break


@app.route('/delete/', methods=['DELETE'])
def deleteDato():
    index = request.get_json()['index']
    try:
        mediciones.remove(index)
    except IndexError:
        return jsonify({'error': str(IndexError)})


if(__name__ == '__main__'):
    app.run()
