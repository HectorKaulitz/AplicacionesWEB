'''
Tema: Gestión de excepciones
Fecha: 19 de septiembre del 2022
Autor: Leonardo Martínez González
'''
import sys

import _mysql_connector

#    En algunas ocasiones nuestros programas pueden fallar ocasionando su detención.
#    Ya sea por errores de sintaxis o de lógica, tenemos que que ser capaces de detectar esos
#    momentos y tratarlos debidamente para prevenirlos.

#    Los errores detienen la ejecución del programa y tienen varias causas. Para poder estudiarlos
#    vamos a provocar algunos intencionadamente.
#    Tipos: Errores de sintaxis, de nombre y semánticos.

# 1. Excepciones: Las excepciones son bloques de código que nos permiten continuar
#    con la ejecución de un programa pese a que ocurra un error.

#    Se trata de una forma de controlar el comportamiento de un programa
#    cuando se produce un error.

# 2. Sintaxis:
'''
    try:
        # Intenta ejecutar la instrucion(es)
    except:
        # Si ocurre un error aqui se trata
    else:
        # Si entra al bloque try se ejecuta este bloque de código
    finally: 
        # Siempre se ejecutara este código
'''

# Los ejemplos más comunes que podemos nombrar de excepciones:
#
# 1. Tratar de convertir a entero un string que no contiene valores numéricos. (ValueError)
# 2. Tratar de dividir por cero.
# 3. Abrir un archivo de texto inexistente o que se encuentra bloqueado por otra aplicación.
# 4. Conectar con un servidor de bases de datos que no se encuentra activo.
# 5. Acceder a subíndices de listas o tuplas inexistentes.

'''
# Ejemplo 1: Calcular si un  numero es PAR o IMPAR, introducir el dato desde teclado
'''
numero = -1;
while (numero == -1):
    try:
        numero = int(input("Ingresa un numero"));
        if (numero % 2 == 0):
            print("Numero par");
        else:
            print("Numero impar");

    except ValueError:
        print("Caracter invalido");
        numero = -1;

'''
# 2. Tratar de dividir por cero. (ZeroDivisionError)
'''
numero = -1;
while (numero == -1):
    try:
        numero = int(input("Numero division entre 0: "));
        res = numero / 0;
    except ValueError:
        numero = -1;
    except ZeroDivisionError:
        print("No se puede dividir entre 0 :)");
    else:
        print(res)
    finally:
        print("Resultado es 0 por lo tanto")

'''
# 3. Abrir un archivo de texto inexistente.
#    (FileNotFoundError)
'''

try:
    sudoku = open("Kardexx.txt", 'r')
except FileNotFoundError:
    print("Archivo no encontrado para lectura")
else:
    print(sudoku.readlines())
    sudoku.close();

'''
# 4. Conectar con un servidor de bases de datos de MySQL que no se encuentra activo.
#      Importar mysql-connector
#      pip install mysql-connector
'''
import mysql.connector

try:
    mydb = mysql.connector.connect(
        host="localhost",
        user="yourusername",
        password="yourpassword"
    )
except Exception:
    print("No se pudo establecer coneccion")
else:
    print(mydb)

'''
# 5. Acceder a subíndices de listas o tuplas inexistentes.
#    Utilizar el mismo ejemplo anterior
'''
lista = [1, 2, 3, 4, 5, 6]
try:
    print(lista[7]);
except IndexError:
    print("Indice no valido");

'''
# ========== Generación manual de excepciones con la declaración raise en Python ==========
Podemos usar la declaración raise dentro de una declaración if
para generar una excepción específica si ocurre una condición específica. 
'''

'''
#1. Generar una excepción ZeroDivisionError
'''

num1 = 7;
num2 = 0;
try:
    if num1 == 0 or num2 == 0:
        raise ZeroDivisionError("No se puede dividir entre zero :)")
    else:
        print(num1 / num2);
except ZeroDivisionError:
    print("")

'''
# 2. Generar una excepción TypeError si var no es una variable de tipo entero.
'''
try:
    var = input("Ingresa un numero entero")
    if not type(var) is int:
        raise TypeError("Solo numeros enteros")
except TypeError:
    print("")

'''
# 3. Generar una excepción ValueError si month es mayor que 12
'''
mes = 13;
try:
    if (mes < 1 or mes > 12):
        raise Exception("Numero mes no valido")
except Exception:
    print("")

'''
# ERRORES PERSONALIZADOS CON assert
'''
try:
    x = "Hola"
    # if condition returns True, then nothing happens:
    assert x == "Hola"
    # x = "Holaa"
    x = "adios"
    # if condition returns False, AssertionError is raised:
    assert x == "adios"
except AssertionError:
    print("No coincide la cadena");


def calcula_media(lista):
    return sum(lista) / len(lista)


try:
    assert (calcula_media([5, 10, 7.5]) == 7.5)
    assert (calcula_media([4, 8]) == 6)
except AssertionError:
    print("No es igual la division");
'''
# PROPAGACIÓN DEL ERROR con raise
'''
var = "a"


def error():
    if not type(var) is int:
        raise TypeError('No es entero:', var)


def catch_error_modify_message():
    try:
        error()
    except TypeError:
        error_type, error_instance, traceback = sys.exc_info()
        error_instance.args = (error_instance.args[0] + ' <modification>',)
        raise error_type(error_instance).with_traceback(traceback)

catch_error_modify_message();