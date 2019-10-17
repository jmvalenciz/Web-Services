from flask import jsonify, request
from db.db import cnx

class tipoSensor():
    global cur
    cur = cnx.cursor()

    def list():
        lista = []
        cur.execute("SELECT * FROM tipo_sensores, sensores, origen WHERE tipo_sensores.codigoSensor = sensor.id AND tipo_sensores.origen = origen.id")
        rows = cur.fetchall()
        columns = [i[0] for i in cur.description]
        for row in rows:
            registro = zip(columns,row)
            json = dict(registro)
            lista.append(json)
        cnx.close
        return jsonify(lista)

    def create(body):
        data = (body["fecha"], body["origen"], body["valor"], body["codigoSensor"], body["observacion"])
        sql = "insert into tipo_sensores(fecha, origen, valor, codigoSensor, observacion) values(%s,%s,%s,%s;%s)"
        cur.execute(sql,data)
        cnx.commit()
        cnx.close
        return {"estado", "insertado"},200
