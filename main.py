# chat conversation
import json
import pymysql
import requests
import http.client
import os
from datetime import datetime
from dotenv import load_dotenv
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

from itertools import cycle

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/", methods=["POST"])
@cross_origin()
def function(self):
    load_dotenv()
    DB_HOST = os.getenv("DB_HOST")
    DB_USER = os.getenv("DB_USER")
    DB_PASS = os.getenv("DB_PASS")
    DB_DDBB = os.getenv("DB_DDBB")
    #try:
    connection = pymysql.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASS,
        database=DB_DDBB)
    cursor = connection.cursor()

    print("conexión exitosa")
    print("REQUEST: "+str(request.json))

    try:
        cursor = connection.cursor()
        
        profesional_id = str(request.json['profesional_id'])
        alumno_id = str(request.json['alumno_id'])
        fecha = str(request.json['fecha'])
        hora = str(request.json['hora'])
        estado = str(request.json['estado'])
        modalidad = str(request.json['modalidad'])
        campus = str(request.json['campus'])
        notas = str(request.json['notas'])
        motivo = str(request.json['motivo'])
        como = str(request.json['como'])
        derivado_desde = str(request.json['derivado_desde'])
        tratamiento = str(request.json['tratamiento'])
        diagnostico_previo = str(request.json['diagnostico_previo'])
        
        sql_insertar = 'INSERT INTO '+DB_DDBB+'.citas'+'''
                        (profesional_id, alumno_id, fecha, hora, estado, modalidad, campus, notas, motivo, como, derivado_desde, tratamiento, diagnostico_previo)
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
                        '''
        print('INSERT:'+sql_insertar)
        print(profesional_id, alumno_id, fecha, hora, estado, modalidad, campus, notas, motivo, como, derivado_desde, tratamiento, diagnostico_previo)
        cursor.execute(sql_insertar,(profesional_id, alumno_id, fecha, hora, estado, modalidad, campus, notas, motivo, como, derivado_desde, tratamiento, diagnostico_previo))
        connection.commit()

        retorno = {
                "estado":True,
                "detalle":"success!!"
            }

    except Exception as e:
        print('Error: '+ str(e))
        retorno = {
            "estado":False,
            "detalle":"fail!!"
        }
    return retorno

if __name__ == "__main__":
    app.run(debug=True, port=8002, ssl_context='adhoc')