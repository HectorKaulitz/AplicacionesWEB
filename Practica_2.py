# Listas UNIDAD 2
# 26/agosto/2022

# lista = []
# listaDinamica = list()

"""lista = [2,4,6,8]

for i in lista:
    print(i)

lista = ["shiro","brian","hector"]
for nombre in lista:
    print(nombre)
"""
import os
import random

list = [424, "Hector", "Sistemas", "Masculino", True]

"""

for alumno in list:
    print(alumno)
    """
"""
print(list)
print(list[0:5])

numeros = []
index = 1
while index <= 2:
    try:
        num = int(input("Ingresa un numero"))
        numeros.append(num)
        index += 1
    except ValueError as ex:
        print(f"Dato no valido: {ex=},{type(ex)=} ")

numeros.extend(random.randint(1, 100) for i in range(10))
numeros.sort()
print(numeros[0:len(numeros)])
print("Tamaño", len(numeros))
print(numeros.pop())"""

#alumnos=[[144205,"Fernando"] , [144203,"Hector"] , [144202,"Brian"] ,[144201,"Pedro"]]
#print(alumnos)
#print(alumnos.pop())
#print(alumnos[2])
#print(alumnos[-2::])

"""promedio=[60,65,70,75]
ind=0
for prom in promedio:
    alumnos[ind].append(prom)
    ind += 1
print(alumnos)

promediosSacados = []
for alum in alumnos:
    promediosSacados.append(alum[2])
print(promediosSacados)
"""

"""
#Menu principal insertar,eliminar,actualizar,imprimir ,salir
def insertar():
    inse = input("Inserta el dato: ")
    lista.append(inse)

def eliminar():
    if len(lista) <= 0:
        print("Lista vacia,no hay datos para eliminar")
    else:
        imprimir()
        elim = input("Escriba el dato a eliminar")
        try:
            lista.remove(elim)
            imprimir()
        except ValueError:
            print("Dato no encontrado")


def actualizar():
    imprimir()
    act = input("Dato a actualizar")

def imprimir():
    if len(lista)<=0:
        print("Lista vacia")
    else:
        print(lista)

salir = False
lista = []
while(salir==False):
    print("\n Operaciones:  1.-Insertar  2.-Eliminar  3.-Actualizar  4.-Imprimir  5.-Salir")
    try:
        op = int(input("Elija la operacion: "))
    except ValueError:
        op = 0
    match op:
        case 1:
            insertar()
        case 2:
            eliminar()
        case 3:
            actualizar()
        case 4:
            imprimir()
        case 5:
            salir = True
        case  default:
            print("Opcion no valida")
    """
#f = open('uni.txt','r') #lee el archivo si no existe da error
f = open('uni.txt','r') #abre el archivo para escritura si no existe lo crea
#men = f.read() lee todooo el archivo
#men = f.read(5) soloo lee 5 caracteres
renglones = f.readlines() #arrelego por renglones
for ren in renglones:
    print(ren)
f.close()






