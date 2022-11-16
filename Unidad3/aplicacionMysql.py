'''
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
import this
from random import random

from crudMysql import *

asc = []
num = 65;
while (num <= 90):
    asc.append(num);
    num += 1;

num = 97;
while (num <= 122):
    asc.append(num);
    num += 1;

mySql = MySQL();


def ObtenerArrayAlumnos():
    # se obtienen los archivos
    estudiantes = []
    archivo = open("Estudiantes.prn", mode="r")
    if archivo.readable():
        for est in archivo.read().split("\n"):
            if len(est) > 0:
                estudiantes.append((est[0:8], est[9:]))
    archivo.close()
    return estudiantes;


def ObtenerArrayKardex():
    materias = []
    archivo = open("Kardex.txt", mode="r")
    if archivo.readable():
        for kar in archivo.read().split("\n"):
            if len(kar) > 0:
                datos = kar.split("|")
                materias.append((datos[0], datos[1], datos[2]))
    archivo.close()
    return materias;


def GenerarContrasena():
    i = 0;
    while i < 1:
        cont = "";
        while len(cont) < 11:
            cont += '' + chr(asc[random.randint(0, (len(asc) - 1))]);
        cont += str(generar_numeros())
        i += 1;
    return cont


def generar_numeros():
    return random.randint(0, 9)


def AgregarAlumnos():
    # mySql = MySQL(bd="ItjEstudiantes");
    estudiantes = ObtenerArrayAlumnos();
    materias = ObtenerArrayKardex();

    if mySql.conectar_mysql():
        for i in range(0, len(estudiantes)):  # se recorre el txt
            no_control = estudiantes[i][0];  # se obtiene el numero de control
            nomEstudiante = estudiantes[i][1]

            # print(consulta)
            res = mySql.consulta_sql("select * from Estudiante where NumeroControl=" + no_control, True)
            if len(res) < 1:
                mySql.consulta_sql(
                    f"insert into Estudiante(NumeroControl,NombreEstudiante) values('{no_control}','{nomEstudiante}')");
                if estudiantes[i][0] == no_control:  # if existe coincidencia
                    for j in range(0, len(materias)):  # recorremos buscando sus materias
                        nombreMateria = ""
                        calificacion = 0
                        if materias[j][0] == no_control:  # si coincide alguna materia
                            nombreMateria = materias[j][1];  # se saca el nombre de la materia
                            calificacion = materias[j][2];  # se saca la calificacion
                            idAlumno = \
                                mySql.consulta_sql("select * from Estudiante where NumeroControl=" + no_control, True)[
                                    0][0];
                            mySql.consulta_sql(
                                f"insert into Kardex (IDEstudiante,Materia,Calificacion) values({idAlumno},'{nombreMateria}','{calificacion}')")

    else:
        print("No se pudo establecer conexion a la base de datos");
    mySql.desconectar_mysql();


def AgregarEstudiante():
    # mySql = MySQL(bd="ItjEstudiantes");
    correcto = False;
    if mySql.conectar_mysql():
        while not correcto:
            print("--------AGREGAR ESTUDIANTE---------")
            no_control = input("Ingresa el numero de control del nuevo estudiante")

            if len(no_control) <= 8:
                res = mySql.consulta_sql("select * from Estudiante where NumeroControl=" + no_control, True)
                if len(res) < 1:
                    nomEstudiante = input("Ingresa el nombre del nuevo estudiante")
                    if nomEstudiante != "":
                        mySql.consulta_sql(
                            f"insert into Estudiante(NumeroControl,NombreEstudiante) values('{no_control}','{nomEstudiante}')");
                        correcto = True;
                    else:
                        correcto = False;
                        print("El nombre de estudiante no puede estar vacio");
                else:
                    correcto = False;
                    print("Ya existe un estudiante con el numero de control " + no_control)

            else:
                correcto = False;
                print("Numero control no puede pasar de 8 caracteres");
    else:
        print("No se pudo establecer conexion a la base de datos");
    mySql.desconectar_mysql();


def ActualizarCalificacion():
    # mySql = MySQL(bd="ItjEstudiantes");
    correcto = False;
    if mySql.conectar_mysql():
        while not correcto:
            print("--------ACTUALIZAR CALIFICACION---------")
            no_control = input("Ingresa el numero de control del estudiante")

            if len(no_control) <= 8:
                res = mySql.consulta_sql("select * from Estudiante where NumeroControl=" + no_control, True)
                if len(res) > 0:
                    idAlumno = \
                        mySql.consulta_sql("select * from Estudiante where NumeroControl=" + no_control, True)[0][0];
                    materias = mySql.consulta_sql(f"select * from Kardex where IDEstudiante = {idAlumno}", True);
                    if materias is not None:
                        idMateria = -1;
                        while idMateria < 1 or idMateria > len(materias):
                            ind = 1;
                            for materia in materias:
                                print(str(ind) + ".-Nombre materia: ", materia[2])
                                ind += 1;
                            try:
                                idMateria = int(input("Ingresa el numero de materia para actualizar la calificacion"));
                            except ValueError:
                                idMateria = -1;

                            if idMateria < 1 or idMateria > len(materias):
                                print("Materia no valida");
                            else:
                                print("Nombre materia seleccionada: ", str(materias[(idMateria - 1)][2]));
                                print("Calificacion actual: ", str(materias[(idMateria - 1)][3]));
                                cali = -1;
                                while cali <= 0 or cali > 100:
                                    try:
                                        cali = float(input("Ingresa la nueva calificacion"));
                                        if cali <= 0 or cali > 100:
                                            print("La calificacion no puede ser menor a 0 ni mayor a 100");
                                        else:
                                            mySql.consulta_sql(
                                                f"update Kardex set Calificacion = {cali} where IDKardex = {materias[(idMateria - 1)][0]}");
                                            # print(cali)
                                    except ValueError:
                                        cali = -1;


                    else:
                        print("No se encontraron materias para este alumno");
                    correcto = True;

                else:
                    correcto = False;
                    print("No existe un estudiante con el numero de control " + no_control)

            else:
                correcto = False;
                print("Numero control no puede pasar de 8 caracteres");
    else:
        print("No se pudo establecer conexion a la base de datos");
    mySql.desconectar_mysql();


def ConsultarMateriaEstudiante():
    # mySql = MySQL(bd="ItjEstudiantes");
    correcto = False;
    if mySql.conectar_mysql():
        while not correcto:
            print("--------CONSULTAR MATERIA ESTUDIANTE---------")
            no_control = input("Ingresa el numero de control del estudiante")

            if len(no_control) <= 8:
                res = mySql.consulta_sql("select * from Estudiante where NumeroControl=" + no_control, True)
                if len(res) > 0:
                    idAlumno = \
                        mySql.consulta_sql("select * from Estudiante where NumeroControl=" + no_control, True)[0][0];
                    materias = mySql.consulta_sql(f"select * from Kardex where IDEstudiante = {idAlumno}", True);
                    if materias is not None:
                        print("Las materias del estudiante :", res[0][2])
                        ind = 1;
                        for materia in materias:
                            print(str(ind) + ".-Nombre materia: ", materia[2], " calificacion: ", str(materia[3]))
                            ind += 1;
                    else:
                        print("No se encontraron materias para este alumno");
                    correcto = True;

                else:
                    correcto = False;
                    print("No existe un estudiante con el numero de control " + no_control)

            else:
                correcto = False;
                print("Numero control no puede pasar de 8 caracteres");
    else:
        print("No se pudo establecer conexion a la base de datos");
    mySql.desconectar_mysql();


def EliminarEstudiante():
    # mySql = MySQL(bd="ItjEstudiantes");
    correcto = False;
    if mySql.conectar_mysql():
        while not correcto:
            print("--------ElIMINAR ESTUDIANTE---------")
            no_control = input("Ingresa el numero de control del estudiante")

            if len(no_control) <= 8:
                res = mySql.consulta_sql("select * from Estudiante where NumeroControl=" + no_control, True)
                if len(res) > 0:
                    idAlumno = \
                        mySql.consulta_sql("select * from Estudiante where NumeroControl=" + no_control, True)[0][0];
                    mySql.consulta_sql(f"delete from Kardex where IDEstudiante = {idAlumno}");
                    mySql.consulta_sql(f"delete from Usuario where IDEstudiante = {idAlumno}");
                    mySql.consulta_sql(f"delete from Estudiante where IDEstudiante = {idAlumno}");
                    correcto = True;

                else:
                    correcto = False;
                    print("No existe un estudiante con el numero de control " + no_control)

            else:
                correcto = False;
                print("Numero control no puede pasar de 8 caracteres");
    else:
        print("No se pudo establecer conexion a la base de datos");
    mySql.desconectar_mysql();


def Menu(self):
    salir = False;
    while not salir:
        print("------Bases de datos disponibles---------")
        print("1.-MySql Local");
        print("2.-MySql clever cloud");
        print("3.-MySql google cloud")
        try:
            op = int(input("Ingresa la base de datos a utilizar"));
        except ValueError:
            op = 0;

        match op:
            case 1:
                mySql = MySQL();
                salir = True;
            case 2:
                mySql = MySQL(host="bhq08rbad6sn9hcddbnp-mysql.services.clever-cloud.com", user="uvxb0tj6a5ay6lgz",
                              pws="xhbCRb5TpvJVWHw3WIHR", bd="bhq08rbad6sn9hcddbnp");
                salir = True;
            case 3:
                mySql = MySQL(host="34.68.69.88", user="root",
                              pws="kaulitz354", bd="");
                salir = True;
            case default:
                print("Opcion no valida")

    AgregarAlumnos();
    salir = False;
    while not salir:
        print("---------------Menu Opciones: ----------------");
        print("1.- Insertar estudiante");
        print("2.- Actualizar calificacion");
        print("3.- Consultar materias por estudiante");
        print("4.- Consulta general de estudiante");
        print("5.- Eliminar estudiante");
        print("6.- Salir");
        try:
            op = int(input("Ingrese la operacion a realizar: "));
        except ValueError:
            op = 0

        match op:
            case 1:
                AgregarEstudiante();
            case 2:
                ActualizarCalificacion();
            case 3:
                ConsultarMateriaEstudiante();
            # case 4:

            case 5:
                EliminarEstudiante();

            case 6:
                salir = True
            case default:
                print("Opcion no valida")


Menu();
