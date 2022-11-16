import pymongo


class MongoDb:
    import pymongo

    def __init__(self, host="localhost", port="27017", timeout=1000, user="root", pws="", bd="itjestudiantes"):
        # Crear cadena de conexión
        self.MONGO_DATABASE = bd;
        self.MONGO_TIMEOUT = timeout;
        self.MONGO_URI = 'mongodb://' + host + ':' + str(port)
        # self.MONGO_URI = "mongodb+srv://usuario1:<password>@cluster0.iib6cxn.mongodb.net/?retryWrites=true&w=majority"
        self.Conexion = None

    def conectar_mongoDb(self):
        conecto = False;
        try:
            self.Conexion = pymongo.MongoClient(self.MONGO_URI, serverSelectionTimeoutMS=self.MONGO_TIMEOUT)
            # print(self.Conexion.test)
            conecto = True
        except Exception as error:
            print("ERROR: ", error)
        return conecto;

    def desconectar_mongoDb(self):
        try:
            if self.Conexion:
                self.Conexion.close()
        except Exception as error:
            print("ERROR: ", error)

    def consulta_mongoDb(self, tabla='', filtro={}, campos={}):
        MONGO_RESPUESTA = None
        resultados = []
        try:
            MONGO_RESPUESTA = self.Conexion[self.MONGO_DATABASE][tabla].find(filtro, campos)
            if MONGO_RESPUESTA:
                for reg in MONGO_RESPUESTA:
                    resultados.append(reg)
                # print(reg)
        except Exception as error:
            print("ERROR: ", error)
        return resultados

    def Agregracion_mongoDb(self, tabla='', query=[]):
        MONGO_RESPUESTA = None
        resultados = []
        try:
            print(self.Conexion[self.MONGO_DATABASE][tabla].aggregate(query))
            if MONGO_RESPUESTA:
                for reg in MONGO_RESPUESTA:
                    resultados.append(reg)
                # print(reg)
        except Exception as error:
            print("ERROR: ", error)
        return resultados

    def insertar(self, tabla, documento):
        MONGO_RESPUESTA = None
        try:
            MONGO_RESPUESTA = self.Conexion[self.MONGO_DATABASE][tabla].insert_one(documento)
            if MONGO_RESPUESTA:
                for reg in MONGO_RESPUESTA:
                    print(reg)
        except Exception as error:
            print("ERROR: ", error)

    def Eliminar(self, tabla, documento):
        MONGO_RESPUESTA = None
        try:
            MONGO_RESPUESTA = self.Conexion[self.MONGO_DATABASE][tabla].delete_one(documento)
            print(MONGO_RESPUESTA.deleted_count)
            print(documento)
        except Exception as error:
            print("ERROR: ", error)

    def EliminarVarios(self, tabla, campo, condicion):
        MONGO_RESPUESTA = None
        try:
            query = {campo: {"$gt": condicion}}
            MONGO_RESPUESTA = self.Conexion[self.MONGO_DATABASE][tabla].delete_many(query)
            print(query)
            print(MONGO_RESPUESTA.deleted_count)

        except Exception as error:
            print("Error en la consulta: ", error)

# mongo = MongoDb()
# print(str(mongo.conectar_mongoDb()) + "")
# mongo.consulta_mongoDb('PRODUCTOS')
