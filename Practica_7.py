"""
Tema: Aplicación de estructuras de Python: archivos, JSON, cifrado de contraseñas
Fecha: 06 de septiembre del 2022
Autor: Leonardo Martínez González
Continuación de la práctica 6
Crear un programa que utilice los archivos Estudiantes.prn y kardex.txt:
1. Crear un método que regrese un conjunto de tuplas de estudiantes. (5) 10 min.
2. Crear un método que regrese un conjunto de tuplas de materias.
3. Crear un método que dado un número de control regrese el siguiente formato JSON:
   {
        "Nombre": "Manzo Avalos Diego",
        "Materias":[
            {
                "Nombre":"Base de Datos",
                "Promedio":85
            },
            {
                "Nombre":"Inteligencia Artificial",
                "Promedio":100
            },
            . . .
        ],
        "Promedio general": 98.4
   }
4. Regresar una lista de JSON con las materias de un estudiante, el formato es el siguiente:
[
    {"Nombre": "Contabilidad Financiera"},
    {"Nombre": "Dise\u00f1o UX y UI"},
    {"Nombre": "Base de datos distribuidas"},
    {"Nombre": "Finanzas internacionales IV"},
    {"Nombre": "Analisis y dise\u00f1o de sistemas de informacion"},
    {"Nombre": "Microservicios"},
    {"Nombre": "Algoritmos inteligentes"}
]
5. Generar un archivo de usuarios que contenga el numero de control, éste será el usuario
   y se generará una contraseña de tamaño 10 la cual debe tener:
   A. Al menos una letra mayúscula
   B. Al menos una letra minúscula
   C. Numeros
   D. Al menos UN carácter especial, considere ( @, #, $,%,&,_,?,! )
   Considere:
    - Crear un método para generar cada caracter
    - El codigo ascii: https://elcodigoascii.com.ar/
    - Encriptar la contraseña con bcrypt, se utiliza con node.js, react, etc. Para ello:
        * Descargue la libreria bcrypt con el comando: "pip install bcrypt" desde la terminal o desde PyCharm
        * Página: https://pypi.org/project/bcrypt/
        * Video:Como Cifrar Contraseñas en Python     https://www.youtube.com/watch?v=9tEovDYSPK4
   El formato del archivo usuarios.txt será:
   control contrasena contraseña_cifrada
6. Crear un método "autenticar_usuario(usuario,contrasena)" que regrese una bandera que
   indica si se pudo AUTENTICAR, el nombre del estudiante y un mensaje, regresar el JSON:
   {
        "Bandera": True,
        "Usuario": "Leonardo Martínez González",
        "Mensaje": "Bienvenido al Sistema de Autenticación de usuarios"
   }
   ó
   {
        "Bandera": False,
        "Usuario": "",
        "Mensaje": "No existe el Usuario"
   }
   ó
    {
        "Bandera": False,
        "Usuario": "Leonardo Martínez González",
        "Mensaje": "Contraseña incorrecta"
   }
"""

import json
import random
import bcrypt


def obtener_alumnos():
    # Obtenemos los alumnos
    estudiantes = []
    archivo = open("Estudiantes.prn", mode="r")
    if archivo.readable():
        for est in archivo.read().split("\n"):
            if len(est) > 0:
                estudiantes.append((est[0:8], est[9:]))
    archivo.close()
    return estudiantes


def obtener_materias():
    # Obtenemos las materias
    kardex = []
    archivo = open("Archivos/Kardex.txt", mode="r")
    if archivo.readable():
        for kar in archivo.read().split("\n"):
            if len(kar) > 0:
                datos = kar.split("|")
                kardex.append((datos[0], datos[1], datos[2]))
    archivo.close()
    return kardex


def obtener_alumno_no_control():
    # Obtenemos el numero de control por el usuario
    datos_alumno = {}
    materias_alumno = []
    promedio = 0

    no_control = input("Dame un numero de control")

    estudiantes = obtener_alumnos()
    materias = obtener_materias()

    for i in range(0, len(estudiantes)):
        if estudiantes[i][0] == no_control:
            for j in range(0, len(materias)):
                if materias[j][0] == no_control:
                    materias_alumno.append({"Nombre": materias[j][1], "Promedio": materias[j][2]})
                    promedio += int(materias[j][2])
            datos_alumno = {"Nombre": estudiantes[i][1], "Materias": materias_alumno, "Promedio General": (promedio / len(materias))}

    print(json.dumps(datos_alumno))


def generar_materias_estudiante():
    estudiantes = obtener_alumnos()
    materias = obtener_materias()
    materias_alumno = []

    no_control = input("Dame un numero de control")
    for i in range(0, len(estudiantes)):
        if estudiantes[i][0] == no_control:
            for j in range(0, len(materias)):
                if materias[j][0] == no_control:
                    materias_alumno.append({"Nombre": materias[j][1]})
            break
        print(json.dumps(materias_alumno))


def generar_letra_mayuscula():
    return chr(random.randint(65, 90))


def generar_letra_minuscula():
    return chr(random.randint(97, 122))


def generar_numero_aleatorio():
    return chr(random.randint(48, 57))


def generar_caracter_aleatorio():
    caracteres = ("@", "#", "$", "%", "&", "_", "?", "!")
    return caracteres[random.randint(0, len(caracteres) - 1)]


def generar_contrasena():
    contrasena = ""
    for i in range(1, 10):
        accion = random.randint(1, 5)
        if accion == 1:
            contrasena += generar_letra_mayuscula()
        elif accion == 2:
            contrasena += generar_letra_minuscula()
        elif accion == 3:
            contrasena += generar_caracter_aleatorio()
        else:
            contrasena += generar_numero_aleatorio()
    return contrasena


def generar_contrasena_encriptada(contrasena):
    salt = bcrypt.gensalt()
    password = bcrypt.hashpw(contrasena.encode('utf-8'), salt)
    return password


def generar_archivo_usuario():
    archivo = open("usuarios.txt", mode="w")
    alumnos = obtener_alumnos()
    for alumno in alumnos:
        contrasena = generar_contrasena()
        contrasena2 = generar_contrasena_encriptada(contrasena)
        archivo.write(alumno[0] + "|" + alumno[1] + "|" + contrasena + "|" + str(contrasena2, "utf-8") + "\n")
    archivo.close()


def autenticarUsuario(usuario, contrasena):
    resultado = {}

    if usuario != "":
        archivo = open("usuarios.txt", mode="r")
        alumnos = archivo.read().split("\n")

        for alumno in alumnos:
            datos = alumno.split("|")
            if len(datos) > 0:
                if datos[0] == usuario:
                    if bcrypt.checkpw(contrasena.encode('utf-8'), datos[3].encode('utf-8')):
                        resultado = {"Bandera": True, "Usuario": datos[1], "Mensaje": "Bienvenido al Sistema de Autenticación de usuarios"}
                    else:
                        resultado = {"Bandera": False, "Usuario": datos[1], "Mensaje": "Contraseña incorrecta"}
                    break

    if len(resultado) == 0:
        resultado = {"Bandera": False, "Usuario": "", "Mensaje": "No existe el Usuario"}

    print(resultado)



#try:
#generar_archivo_usuario()
#except ValueError:

autenticarUsuario("18420427", "_bHA6#B29")
autenticarUsuario("18420427", "5Aucv__94")