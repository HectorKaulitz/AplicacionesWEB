'''
Tema: Diccionarios, archivos y formato JSON
Fecha: 02 de septiembre del 2022
Autor: Leonardo Martínez González
'''
import random

# 1. Definición. Colección no ordenada de objetos. Está formada por un PAR clave: valor.
#    Las claves pueden ser números, cadenas o cualquier otro tipo inmutable.
#    Los valores pueden ser de cualquier tipo, incluso otros diccionarios.

# 2. Crear diccionarios
diccionario1 = {"valor1": 1, "valor2": 2}
prueba_deportiva = {'Jorge': 500, 'Diana': 600, 'Rodrigo': 800, 'Julia': 750, 'Li': 900}

clientes = ["Alex", "Bob", "Carol", "Dave", "Flow", "Katie", "Nate"]
diccionario_descuentos = {cliente: random.randint(1, 100) for cliente in clientes}

dicc = dict()

# 3. Acceder a sus valores. Se accede igual que las listas pero por su clave en lugar del indice
#    Si no existe la clave se lanza la excepcion KeyError
try:
    print(diccionario1["valor5"])
except KeyError:
    print("No existe clave")
print(diccionario_descuentos)

# 4. Recorrer un diccionario por su clave.
for eleme in diccionario_descuentos:
    print(eleme)
    print()

# 5. Recorrer un diccionario por su valor
for eleme in diccionario_descuentos.values():
    print(eleme)

# 6. Recorrer un diccionario por clave: valor
for eleme in diccionario_descuentos.items():
    print(eleme)
for clave, valor in diccionario_descuentos.items():
    print(clave, valor)
# 7. Agregar elementos a un diccionario
diccionario1["valor3"] = 3
print(diccionario1)
# 8. Eliminar elementos con del
del diccionario1["valor2"]
print(diccionario1)
# 9. Modificar, accesando directo a la posición
diccionario1["valor1"] = "era 1"
print(diccionario1)
# 10. Algunas operaciones comunes
#     Contar elementos
print(len(diccionario1))
#     Saber si existe un elemento dentro de un diccionario (solo por clave)
print("valor4" in diccionario1)
#     Para vaciar un diccionario
diccionario1.clear()
print(diccionario1)
#     Unir o actualizar dos diccionarios
d1 = {"uno": 1, "dos": 2, "tres": 3, "cuatro": 4}
d2 = {"cinco": 5, "seis": 6}
d1.update(d2)
print(d1)
#     Sacar un elemento del diccionario con pop() muy parecido a get(), pero pop(),
#     regresa el elemento y lo elimina del diccionario
print(d1.pop("seis"))
print(d1)
#      Tambien acepta devolver un valor por defecto pop(clave, "valor por defecto)

#      popitem() regresa el ultimo  elemento (par clave:valor) y lo remueve
#      si no existe genera una excepción KeyError
print(d1.popitem())
print(d1)

#      generar un diccionario a partir de una lista con el metodo fromkeys() con valores
#      por defecto con valor None o 0 (CERO)
pares = [i for i in range(2, 101, 2)]
dicPares = dict.fromkeys(pares, 2)
print(dicPares)
'''
Defina un diccionario Estudiantes, que:
Almacene datos personales y todas las materia que ha cursado con sus promedios.
Las actividades complemetarias que ha tomado.
'''
estudiantes = {
    "estudiante1": {"materias": {"Poo": 70, "Automatas": 70, "Web": 70, "Teleocmunicaciones": 70},
                    "personales": {"sexo": "masculino", "edad": 21, "nombre": "brian"},
                    "actividades": {"activida1": "musica"}
                    },
    "estudiante2": {"materias": {"Poo": 80, "Automatas": 80, "Web": 80, "Teleocmunicaciones": 80},
                    "personales": {"sexo": "masculino", "edad": 22, "nombre": "Hector"},
                    "actividades": {"activida1": "musica"}
                    }
}
for est in estudiantes.items():
    print(est)

'''
El directorio de los clientes de una empresa está organizado en una cadena de texto como la de
más abajo, donde cada línea contiene la información: nombre, email, teléfono, nss, y el descuento
que se le aplica.
 Las líneas se separan con el carácter de cambio de línea \n 
y la primera línea contiene los nombres de los campos con la información contenida en el directorio.

"NSS;nombre;email;teléfono;descuento\n01234567L;Luis González;luisgonzalez@mail.com;656343576;12.5\n71476342J;Macarena Ramírez;macarena@mail.com;692839321;8\n63823376M;Juan José Martínez;juanjo@mail.com;664888233;5.2\n98376547F;Carmen Sánchez;carmen@mail.com;667677855;15.7"

'''
cadena = "NSS;nombre;email;teléfono;descuento\n01234567L;Luis González;luisgonzalez@mail.com;656343576;12.5\n71476342J;Macarena Ramírez;macarena@mail.com;692839321;8\n63823376M;Juan José Martínez;juanjo@mail.com;664888233;5.2\n98376547F;Carmen Sánchez;carmen@mail.com;667677855;15.7"
cad = cadena.split("\n")
indice = 0
dicc = {}
keys = []
#print(cad)
for c in cad:
    if indice == 0:
        keys = c.split(";")
    else:
        cl = "cliente"+str(indice)
        dicc[cl] ={}
        clien = {}
        indInterno = 0
        for k in keys:
            dicc[cl] = {k: c[indInterno]}
            indInterno += 1

    indice += 1

print(dicc)


'''
Escribir un programa que genere un diccionario con la información del directorio, 
donde cada elemento corresponda a un cliente y tenga por clave su NSS y por valor otro diccionario
con el resto de la información del cliente. Los diccionarios con la información de cada cliente
tendrán como claves los nombres de los campos y como valores la información de cada cliente
correspondientes a los campos. Es decir, un diccionario como el siguiente:

{'01234567L': {'nombre': 'Luis González', 'email': 'luisgonzalez@mail.com', 'teléfono': '656343576', 'descuento': 12.5}, '71476342J': {'nombre': 'Macarena Ramírez', 'email': 'macarena@mail.com', 'teléfono': '692839321', 'descuento': 8.0}, '63823376M': {'nombre': 'Juan José Martínez', 'email': 'juanjo@mail.com', 'teléfono': '664888233', 'descuento': 5.2}, '98376547F': {'nombre': 'Carmen Sánchez', 'email': 'carmen@mail.com', 'teléfono': '667677855', 'descuento': 15.7}}
{'01234567L': {'Nombre': 'Luis González', 'Email': 'luisgonzalez@mail.com', 'Telefono': '656343576', 'Descuento': 12.5}, '71476342J': {'Nombre': 'Macarena Ramírez', 'Email': 'macarena@mail.com', 'Telefono': '692839321', 'Descuento': 8.0}, '63823376M': {'Nombre': 'Juan José Martínez', 'Email': 'juanjo@mail.com', 'Telefono': '664888233', 'Descuento': 5.2}, '98376547F': {'Nombre': 'Carmen Sánchez', 'Email': 'carmen@mail.com', 'Telefono': '667677855', 'Descuento': 15.7}}
considere el método de cadena split() que separa una cadena de acuerdo al caracter que se le pase
'''

'''
Ejercicio: Crear un diccionario con los códigos postales y su localidad del estado de San Luis Potosi,
           para ello descargue la tabla de códigos postales de la siguiente dirección: 
           https://www.correosdemexico.gob.mx/SSLServicios/ConsultaCP/CodigoPostal_Exportar.aspx
           
           el formato del diccionario  tendra la forma:
           {109159: {'CP': '78000', 'Municipio': 'San Luis Potosí', 'Estado': 'San Luis Potosí'}, 
            109160: {'CP': '78037', 'Municipio': 'San Luis Potosí', 'Estado': 'San Luis Potosí'}, . . . }
           
           Genere una lista con los VALORES del diccionario anterior.
           Guarde en un archivo con formato JSON los resultados
           
           Consideraciones:
           1. El método split regresa un arreglo al separar una cadena en subcadenas.
           2. El municipio se encuentra en la posición 4.
           3. El estado se llama: "San Luis Potosí"
'''
import json

codigosPostales = {}
municipios = []

archivo = open("San Luis Potosí.txt", mode="r")
mJson = open("San Luis Potosí.json", mode="w")
#El Catálogo Nacional de Códigos Postales, es elaborado por Correos de México y se proporciona en forma gratuita para uso particular, no estando permitida su comercialización, total o parcial, ni su distribución a terceros bajo ningún concepto.
#d_codigo|d_asenta|d_tipo_asenta|D_mnpio|d_estado|d_ciudad|d_CP|c_estado|c_oficina|c_tipo_asenta|c_mnpio|id_asenta_cpcons|d_zona|c_cve_ciudad|c_CP

if archivo.readable():
    municipios = archivo.read().split("\n")
    indice = 0
    for mun in municipios[2:]:
        municipio = {}
        indice += 1
        datos = mun.split("|")
        if len(datos) > 4:
            municipio["CP"] = datos[0]
            municipio["Municipio"] = datos[3]
            municipio["Estado"] = datos[4]
            codigosPostales[indice] = municipio
    json.dump(codigosPostales, mJson)
else:
    print("No se pudo abrir el archivo")

mJson.close()
archivo.close()

'''
Formto  JSON
Formato ligero de intercambio de datos
medio de comunicación estadarizado entre lenguajes de programación

en Python se leen facilmente archivos JSON 
import json #libreria que maneja este formato
with open("Nombre_archivo", 'w') as archivo:
        json.dump( Lista_de_diccionario, archivo) # dump es disparar

Las lineas anteriores graban un archivo y su contenido es en formato JSON



'''
