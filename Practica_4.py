'''
# Tema: Tuplas
# Fecha: 31 de agosto del 2022
# Autor: Leonardo Martínez González
'''
# 1. Definición. Es una colección de elementos inmutables.
#             Las tuplas son immutables y normalmente contienen una secuencia heterogénea
#             de elementos que son accedidos al desempaquetar o indizar.

# 2. Crear tuplas
#tupla1 = tuple()
#tupla2 = ()
#tupla3 = (2, 'jose miguel', True, 6)

# 3. Accesar a elementos de la tupla, igual que en las listas
#print(tupla3[1])

#for e in tupla3:
 #   print(e)

# 4. Operaciones.
# 4.A. Son inmutables


# 4.B. Las tuplas pueden ser anidadas
#grupo_a = ('jose miguel','carmen','estela')
#grupo_b = ('luis','karina')
#grupo_c = (grupo_a,grupo_b)
#print(grupo_c)

#numeros = ((3,4),(4,7),(7,90))

#print(numeros)

# 4.C. Las listas se pueden convertir en tuplas  haciendo uso de la función tuple()
#lista = ['A','B','C','D']
#tupla_letras = tuple(lista)
#print(tupla_letras)

# 4.D. Se puede asignar el valor de una tupla con n elementos a n variables
#alumno = (420424,'Hector')
#control,nombre = alumno
#print(control)
#print(nombre)


# 5. Métodos de tuplas
#print(len(alumno))
#print(alumno.count(420424))
#print(grupo_c[1].count('karina'))

# index() Regresa el índice donde se ha encontrado, tambien puede pasarle un segundo
#print(grupo_b.index('karina'))

'''
Escribir un programa que permita procesar datos de pasajeros de viaje en una lista de tuplas
con la siguiente forma:
(nombre, clave, destino)
Ejemplo:
'''
pasajeros =    [("Felipe Gonzalez", 202101, "Guadalajara"),
                ("Gualupe Salazar", 202110, "Zamora"),
                ("Ernesto Sotomayor", 202108, "Guadalajara"),
                ("Nulvy Martinez", 202106, "Leon"),
                ("Jose Luis Bustamante", 202109, "Los Reyes"),
                ("Karina Tello", 202107, "Zamora")
               ]
'''
Además, en otra lista de tuplas se almacenan los datos de cada ciudad y el estado al que pertencen.
Ejemplo:
'''
ciudades = [("Guadalajara","Jalisco"),
            ("Zamora","Michoacan"),
            ("Leon","Guanajuato")]
'''
Hacer un menú interactivo que permita al usuario realizar las siguientes operaciones:
- Agregar pasajeros a la lista de pasajeros
- Agregar ciudades a la lista de ciudades
- Dada la CLAVE de un pasajero, ver a que ciudad viaja
- Dada la CIUDAD, mostrar la cantidad de pasajeros que viajan a esa ciudad
- Dada la CLAVE de un pasajero, ver a que ESTADO viaja
- Dado un Estado, mostrar cuantos pasajeros viajan a ese Estado
- Salir del programa

NOTA: Haga uso de funciones
'''

from practica_4_funciones import  *

salir = False

while(salir == False):

    print("1.-Agregar pasajero 2.-Agregar ciudades 3.-Ver ciudad destino de pasajero 4.-Cantidad pasajero a ciudad \n"
          " 5.-Ver estado destino de pasajero 6.-Cantidad pasajero a estado 7.-Salir")
    try:
        op = int(input("Ingresa la opcion: "))
    except ValueError:
        op = 0
    try:
        match op:
            case 1:
                agregarPasajero(pasajeros)
            case 2:
                agregarCiudad(ciudades)
            case 3:
                ciudadDestino(pasajeros)
            case 4:
                cantidadCiudad(pasajeros)
            case 5:
                estadoDestino(pasajeros,ciudades)
            case 6:
                cantidadEstado(pasajeros,ciudades)
            case 7:
                print("Programa terminado")
                salir = True
            case default:
                print("Opcion no valida")
    except Exception:
        salir = False;


