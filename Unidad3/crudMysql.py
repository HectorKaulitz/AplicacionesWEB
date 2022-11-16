'''
Tema: Clases y Objetos en Python
Fecha: 29 de septiembre del 2022
Autor: Leonardo Martínez González
'''
from MySQLdb.converters import NoneType

'''
Crear una clase de nombre MySQL que tenga las siguientes propiedades:
    MYSQL_HOST
    MYSQL_USER
    MYSQL_PASSWORD
    MYSQL_DATABASE
    MYSQL_CONNECTION
    MYSQL_CURSOR

y los siguientes métodos:
    constructor (host="localhost",user="root", pwd="", bd="opensource") que recibe parámetros
    con valores por defecto

    conectar_mysql(). se conecta a la Base de datos, 

    desconectar_mysql(). Cerrar la conexion a la Base de Datos

    consulta_sql(sql). Recibe la consulta SQL que ejecutará, desde este método se conectará a la
    Base de Datos y terminando de ejecutar la consulta se deconectará de la BD.



Utilizando la clase MySQL, cargue los datos a la Base de datos de:
    Estudiantes.txt
    Kardex.txt 

Genere las constraseñas a los estudiantes en una tabla llamada Usuarios, utilice la clase Password.

Para ello, cree la Base de Datos y las tablas: Estudiantes, Usuarios y Kardex con los campos que tienen
los archivos mencionados, considere integridad referencial.
Realice el CRUD a la tabla Kardex

Realice algo SIMILAR para MongoDB, considere solo consultas de una tabla.

para instalar mysql: pip install mysql-conector-python
para instalar pymongo: pip install pymongo
'''

import mysql.connector


class MySQL:

    def __init__(self, host="localhost", user="root", pws="", bd="itjestudiantes"):
        self.HOST = host
        self.USER = user
        self.PASSWORD = pws
        self.DATABASE = bd
        self.CONNECTION = None
        # self.MYSQL_CURSOR = None

    def conectar_mysql(self, imprimir =False):
        conecto = False
        try:
            self.CONNECTION = mysql.connector.connect(
                host=self.HOST,
                user=self.USER,
                password=self.PASSWORD,
                database=self.DATABASE)
            conecto = True
        except Exception as error:
            conecto = False
            print("ERROR: ", error)
        return conecto

    def desconectar_mysql(self):
        if self.CONNECTION is not None:
            self.CONNECTION.close()
            self.CONNECTION = None
            # self.MYSQL_CURSOR = None

    def consulta_sql(self, sql, lectura=False, imprimir=False):
        #tieneRegistro = False;
        row = None;
        resultados = []
        if self.CONNECTION is None:
            self.conectar_mysql()
        try:
            CURSOR = self.CONNECTION.cursor(buffered=True)
            CURSOR.execute(sql)
            if lectura:
                for row in CURSOR:
                    resultados.append(row);
                    if imprimir:
                        print(row)
                '''row = CURSOR.fetchone()
                while row is not None:
                    #tieneRegistro = True;
                    print(row)
                    row = CURSOR.fetchone()
                '''
        except mysql.connector.errors.ProgrammingError as e:
            print("Error en la consulta ", e)
        except Exception as error:
            print("ERROR: ", error)

        self.CONNECTION.commit()
        CURSOR.close()
        self.desconectar_mysql()
        return resultados

        # con el método fetchall() del cursor se puede extraer todos los resultados de la consulta
        # respuesta = self.MYSQL_CURSOR.fetchall()
        # print(respuesta)

        # self.MYSQL_CONNECTION.commit()  # Cometer la transaccion

# objMySQL = MySQL()
# objMySQL.consulta_sql("Select * from productos")
