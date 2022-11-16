import json
import random

from MongoDb import *
from Unidad3.crudMysql import MySQL

mongoDB = MongoDb()


def AgregarAlumnos():
    mySql = MySQL(bd="ItjEstudiantes");
    if mySql.conectar_mysql():
        estudiantes = mySql.consulta_sql("select * from Estudiante", True)
        kardex = mySql.consulta_sql("select * from Kardex", True)
        usuarios = mySql.consulta_sql("select * from Usuario", True)

        if mongoDB.conectar_mongoDb():
            for estudiante in estudiantes:
                res = mongoDB.consulta_mongoDb('Estudiante', {'IDEstudiante': estudiante[0]})
                if len(res) < 1:
                    e = {}
                    e = {'IDEstudiante': estudiante[0],
                         'NumeroControl': estudiante[1],
                         'NombreEstudiante': estudiante[2]
                         }
                    mongoDB.insertar('Estudiante', e)

            for karde in kardex:
                res = mongoDB.consulta_mongoDb('Kardex', {'IDEstudiante': karde[1]})
                if len(res) < 1:
                    k = {}
                    k = {
                        'IDKardex': karde[0],
                        'IDEstudiante': karde[1],
                        'Materia': karde[2],
                        'Calificacion': float(karde[3])
                    }
                    mongoDB.insertar('Kardex', k)

            for usuario in usuarios:
                res = mongoDB.consulta_mongoDb('Usuario', {'IDEstudiante': usuario[1]})
                if len(res) < 1:
                    u = {}
                    u = {
                        'IDUsuario': usuario[0],
                        'IDEstudiante': usuario[1],
                        'Clave': usuario[2],
                        'ClaveCifrada': usuario[3]
                    }
                    mongoDB.insertar('Usuario', u)
        else:
            print("No se pudo establecer conexion a la base de datos en MongoDB");
    else:
        print("No se pudo establecer conexion a la base de datos en MySql");
    mySql.desconectar_mysql();
    mongoDB.desconectar_mongoDb();


def AgregarEstudiante():
    correcto = False;
    e = {}
    mySql = MySQL()

    if mongoDB.conectar_mongoDb():
        if mySql.conectar_mysql():
            while not correcto:
                print("--------AGREGAR ESTUDIANTE---------")
                no_control = input("Ingresa el numero de control del nuevo estudiante")

                if len(no_control) <= 8:
                    res = mySql.consulta_sql("select * from Estudiante where NumeroControl=" + no_control, True)
                    if len(res) > 0:  # Existe en la base de datos en Mysql
                        res2 = mongoDB.consulta_mongoDb('Estudiante',
                                                        {'IDEstudiante': res[0][0]})  # ver si tambien existe en Mongo

                        if len(res2) < 1:  # no existe en Mongo
                            e = {'IDEstudiante': res[0][0],
                                 'NumeroControl': res[0][1],
                                 'NombreEstudiante': res[0][2]
                                 }
                            mongoDB.insertar('Estudiante', e)  # se inserta con ,os datos de Mysql
                        else:  # Ya existe en Mongo
                            correcto = False;
                            print("Ya existe un estudiante con el numero de control " + no_control)
                    else:  # No existe en Mysql
                        res2 = mongoDB.consulta_mongoDb('Estudiante',
                                                        {'IDEstudiante': res[0][0]})  # ver si tambien existe en Mongo

                        if len(res2) < 1:  # no existe en Mongo
                            e = {'IDEstudiante': res[0][0],
                                 'NumeroControl': res[0][1],
                                 'NombreEstudiante': res[0][2]
                                 }
                            mongoDB.insertar('Estudiante', e)  # se inserta con ,os datos de Mysql
                        else:  # Ya existe en Mongo
                            correcto = False;
                            print("Ya existe un estudiante con el numero de control " + no_control)
                        nomEstudiante = input("Ingresa el nombre del nuevo estudiante")
                        if nomEstudiante != "":
                            mySql.consulta_sql(
                                f"insert into Estudiante(NumeroControl,NombreEstudiante) values('{no_control}','{nomEstudiante}')");
                            correcto = True;
                        else:
                            correcto = False;
                            print("El nombre de estudiante no puede estar vacio");
                else:
                    correcto = False
                    print("Numero control no puede pasar de 8 caracteres");
        else:
            print("No se pudo establecer conexion a la base de datos de MySql");
    else:
        print("No se pudo establecer conexion a la base de datos de MongoDB");
    mySql.desconectar_mysql();


def ConsultaGeneral():
    if mongoDB.conectar_mongoDb():
        alumnos = mongoDB.consulta_mongoDb("Estudiante", {})
        resultado = []
        for alumno in alumnos:
            prom = 0;
            promedio = 0.0
            materias = mongoDB.consulta_mongoDb("Kardex", {"IDEstudiante": alumno["IDEstudiante"]})
            for materia in materias:
                promedio += float(materia["Calificacion"])
            if len(materias) > 0:
                promedio /= len(materias)
            mongoDB.Agregracion_mongoDb("Kardex", [
                "{$match:{IDEstudiante:" + str(alumno["IDEstudiante"]) + ",AverageValue: {$avg:$Calificacion }}"])
            print(str("" + alumno["NumeroControl"]) + " " + str(alumno["NombreEstudiante"]) + " " + str(
                round(promedio, 2)))
    else:
        print("No se pudo establecer conexion a la base de datos de MongoDB");

    mongoDB.desconectar_mongoDb();


def EliminarEstudiante():
    correcto = False;
    if mongoDB.conectar_mongoDb():
        while not correcto:
            print("--------ElIMINAR ESTUDIANTE---------")
            no_control = input("Ingresa el numero de control del estudiante")

            if len(no_control) <= 8:
                res = mongoDB.consulta_mongoDb('Estudiante',
                                               {'NumeroControl': no_control})
                if len(res) > 0:
                    idAlumno = res[0]['IDEstudiante']

                    mongoDB.EliminarVarios("Kardex ", "IDEstudiante", idAlumno);
                    mongoDB.Eliminar("Usuario ", {"IDEstudiante": str(idAlumno)});
                    mongoDB.Eliminar("Estudiante ", {"IDEstudiante": str(idAlumno)});
                    correcto = True;

                else:
                    correcto = False;
                    print("No existe un estudiante con el numero de control " + no_control)

            else:
                correcto = False;
                print("Numero control no puede pasar de 8 caracteres");
    else:
        print("No se pudo establecer conexion a la base de datos");
    mongoDB.desconectar_mongoDb();


def ObtenerPromedioEstudiante():
    mySql = MySQL()
    miJson = open("alumnoPromedio.json", mode="w")
    cad = {}
    if mongoDB.conectar_mongoDb():
        no_control = input("Ingresa el numero de control del estudiante")

        res = mySql.consulta_sql("select * from Estudiante where NumeroControl=" + no_control, True)
        if len(res) > 0:  # Existe en la base de datos en Mysql
            alumnos = mongoDB.consulta_mongoDb('Estudiante',
                                            {'IDEstudiante': res[0][0]})  # ver si tambien existe en Mongo

            if len(alumnos) > 0:
                for alumno in alumnos:
                    promedio = 0.0
                    materias = mongoDB.consulta_mongoDb("Kardex", {"IDEstudiante": alumno["IDEstudiante"]})
                    for materia in materias:
                        promedio += float(materia["Calificacion"])
                    if len(materias) > 0:
                        promedio /= len(materias)
                    #print(str("" + alumno["NumeroControl"]) + " " + str(alumno["NombreEstudiante"]) + " " + str(
                     #   round(promedio, 2)))
                    cad = {"Nombre": str(alumno["NombreEstudiante"]), "Promedio general": round(promedio, 2)}
                    print(cad)

        else:
            print("No existe el estudiante con numero de control", str(no_control))
    else:
        print("No se pudo establecer conexion a la base de datos de MongoDB");
    json.dump(cad, miJson)
    mongoDB.desconectar_mongoDb();


def Menu():
    AgregarAlumnos();
    salir = False;
    while not salir:
        print("---------------Menu Opciones: ----------------");
        print("1.- Insertar estudiante");
        print("2.- Actualizar calificacion");
        print("3.- Consultar materias por estudiante");
        print("4.- Consulta general de estudiante");
        print("5.- Eliminar estudiante");
        print("6.- Promedio estudiante");
        print("7.- Salir");
        try:
            op = int(input("Ingrese la operacion a realizar: "));
        except ValueError:
            op = 0

        match op:
            case 1:
                AgregarEstudiante();
            case 2:
                # ActualizarCalificacion();
                print("")
            case 3:
                # ConsultarMateriaEstudiante();
                print("")
            case 4:
                ConsultaGeneral();

            case 5:
                EliminarEstudiante();
            case 6:
                ObtenerPromedioEstudiante();
            case 7:
                salir = True
            case default:
                print("Opcion no valida")


Menu()
