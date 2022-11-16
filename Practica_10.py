'''
Tema: Esquema de registro de errores o LOG
Fecha: 21 de septiembre del 2022
Autor: Leonardo Martínez González
'''
from unicodedata import decimal

'''
1. Abrir una Base de Datos de MySQL, realizar una consulta y aplicar excepciones
2. Abrir una Base de Datos de MongoDB, realizar una consulta y aplicar excepciones
3. Crear un diseño, esquema para guardar cada uno de los errores que ocurren en un
   archivo LOG o en una Base de Datos.
'''
import mysql.connector;
import json;
try:
    conexion = mysql.connector.connect(host="localhost",user="root",password="",database="opensource")
except Exception as error:
    print(error)
else:
    cursor = conexion.cursor();
    try:
        cursor.execute("select id,Nombre,Precio from Productos");
    except mysql.connector.errors.ProgrammingError as e:
        print(e)
    else:
        cad = {}
        producto = {}
        miJson = open("productosBD.json", mode="w")
        indice = 1;
        for reg in cursor:
            producto = {"ID": reg[0], "Nombre": reg[1], "Precio":str(reg[2])}
            cad[indice] = producto;
            indice += 1;
            #print(reg)
    print(cad)
    json.dump(cad, miJson)
    cursor.close()
    conexion.close()


