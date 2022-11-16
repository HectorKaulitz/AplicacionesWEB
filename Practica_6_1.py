'''
Tema: conjuntos
Fecha: 05 de septiembre del 2022
Autor: Leonardo Martínez González
'''
import string

# 1. Definición. en Python es utilizado para trabajar con conjuntos de elementos.
#    La principal característica de este tipo de datos es que es una colección cuyos elementos
#    no guardan ningún orden y que además son únicos.
#    los principales usos de esta clase se usan para conocer si un elemento pertenece o no
#    a una colección y eliminar duplicados de un tipo secuencial (list, tuple o str).

# 2. Creación. Para crear un conjunto, basta con encerrar una serie de elementos entre llaves {},
#    o bien usar el constructor de la clase set() y pasarle como argumento un objeto iterable
#    (como una lista, una tupla, una cadena …).

conjunto_1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 0}
conjunto_2 = set([1, 2, 3, 4])
conjunto_3 = set(range(10))

#    Usando la función forezenset. es inmutable y su contenido no puede ser modificado
#    una vez que ha sido inicializado

a = frozenset({1, 2, 3})
b = frozenset({3, 4, 5})
a & b
frozenset({3})
a | b
frozenset({1, 2, 3, 4, 5})
a.isdisjoint(b)
print(string.ascii_uppercase)
abc = frozenset(string.ascii_uppercase)
print(abc)

#    Los elementos repetidos se eliminan


# 3. Para acceder a los elementos de un conjunto. Dado que los conjuntos son colecciones
#    desordenadas, en ellos no se guarda la posición en la que son insertados los elementos
#    como ocurre en los tipos list o tuple. Es por ello que no se puede acceder a los elementos
#    a través de un índice.


# 4. Añadir elementos: con el método add() ó con el método update()
#    Agregar el numero 8 al conjunto c
c4 = set()
c4.add(1)
c4.update({3, 5, 7})
print(c4)

#    Agregar varios elementos al conjunto


# 5. Eliminar elementos del conjunto: discard(elemento), remove(elemento), pop() y clear()
#    discard(elemento) y remove(elemento) son muy parecidos, solo que remove lanza una excepcion KeyError
#    en caso de no existir el elemento
c4.discard(5)
c4.discard(100)
print(c4)

#     pop() devuelve un elemento aleatorio y lo elimina, si el conjunto esta vacio lanza una
#     excepcion KeyError.
print(c4.pop())
print(c4)

#    El método clear() elimina todos los elementos del conjunto
c4.clear()
print(c4)

#    Número de elementos en un conlunto con la función len()
c4.update({1, 2, 3, 4})
print(len(c4))

#    Verificar si un elemento esta dentro de un conjunto
print(2 in c4)
print(7 in c4)

# ************************ Operaciones con conjuntos
# 1. Union  ( | )
a = {1, 2, 3, 4}
c = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(a | b)

# 2. Intersección ( & )
print(a & b)

# 3. Diferencia ( - )
print(a - b)

# 4. Diferencia simétrica ( ^ ). es el conjunto que contiene los elementos de A y B
#    que no son comunes.
print(a ^ b)
print(a.symmetric_difference(b))
print(b.symmetric_difference(a))

# 5. Inclusión de conjuntos.  Se utiliza el operador <= para comprobar si un conjunto A
#    es subconjunto de B y el operador >= para comprobar si un conjunto A es superconjunto de B.


# 5. Conjuntos disjuntos. Dos conjuntos A y B son disjuntos si no tienen elementos en común,
#    es decir, la intersección de A y B es el conjunto vacío.
print(a.isdisjoint(b))
print(b.isdisjoint(a))

# 6. Igualdad de conjuntos. En Python dos conjuntos son iguales si y solo si todos los elementos
#    de un conjunto están contenidos en el otro. Esto quiere decir que cada uno es un subconjunto
#    del otro.
print(a == b)
print(a == c)

'''
Crear un programa que utilice los archivos Estudiantes.prn y kardex.txt:

1. Crear un método que regrese un conjunto de tuplas de estudiantes.
'''
archivo = open("Estudiantes.prn", mode="r")
conjuntoEstudiantes = set()
renglones = archivo.readlines()  # arrelego por renglones
i = 0
if (archivo.readable()):
    for ren in renglones:
        # print(ren)
        inf = ren.split("|")
        # print(inf)
        estudiante = (inf[0], inf[1][:-1])
        conjuntoEstudiantes.add(estudiante)
        i += 1
        # print(ren)
    archivo.close()

print(conjuntoEstudiantes)
'''
2. Crear un método que regrese un conjunto de tuplas de materias.
'''
archivo = open("Kardex.txt", mode="r")
conjuntoMaterias = set()
renglones = archivo.readlines()  # arrelego por renglones
i = 0
if (archivo.readable()):
    for ren in renglones:
        # print(ren)
        inf = ren.split("|")
        # print(inf)
        materia = (inf[0], inf[1], inf[2][:-1])
        conjuntoMaterias.add(materia)
        i += 1
        # print(ren)
    archivo.close()

print(conjuntoMaterias)
'''
3. Crear un método que dado un número de control regrese el siguiente formato JSON:
   {
        "Nombre": "Manzo Avalos Diego",
        "Materias":[
            {
                "Nombre":"",
                "Promedio":
            },
            {
                "Nombre":"",
                "Promedio":
            },
            . . . 
        ],
        "Promedio general": 
   }
'''
import json

miJson = open("alumno.json", mode="w")
nc = input("Ingresa numero control")
cadena = {}
materia = []
promedioG = 0
cad = {}
for alumno in conjuntoEstudiantes:
    if str(alumno[0]) == nc:
        cad = {}
        for mat in conjuntoMaterias:
            if str(alumno[0]) == str(mat[0]):
                materia.append({"Nombre": mat[1], " Promedio": mat[2]})
                promedioG += int(mat[2])
        cad = {"Nombre": alumno[1], "Materias": materia, "Promedio general": (promedioG / len(materia))}
json.dump(cad, miJson)
