'''
Tema: Entrada y Salida
Fecha: 12 de septiembre del 2022
Autor: Leonardo Martínez González

'''
import json

# Python soporta múltiples formas de formatear una cadena de caracteres. A continuación se describen:
# 1. Formateo %. operador de interpolación
# 2. format(). devuelve una versión formateada de una cadena de caracteres, usando substituciones desde argumentos
# 3. formateo avanzado. Este método soporta muchas técnicas de formateo
# 4. formateo por tipo


# 1. Formateo %. operador de interpolación
# %s - Cadena (O cualquier objeto, como los números al representarlos en una cadena de texto)
# %d - Integrales
# %f - Números de punto flotante
# %.<numero de digitos>f - Números de punto flotante con una cantidad de números fijos a la derecha del punto.
# %x/%X - Integral con representacion hex (minúscula/mayúscula)

nombre = "Hector"
materia = "Aplicaciones web open source"
# print('Soy %s ' % nombre);
# print('Soy %s y esta es la materia de %s' % (nombre, materia));

# formato con salida %.2


#    Con esta sintaxis hay que determinar el tipo del objeto:

#    %c = str, simple carácter.
#    %s = str, cadena de carácter.
milista = [1, 2, 3]
# print("Una lista: %s" % milista)

#    %d = int, enteros.
#    %f = float, coma flotante.
#    %o = octal.
#    %x = hexadecimal.
x = 10 * 3.25
y = 200 * 200
# print('El valor de X es ' + repr(x) + ', & Y es ' + repr(y) + '')

# 2. format(). devuelve una versión formateada de una cadena de caracteres,
#     usando substituciones desde argumentos


# print('Tenemos {0} y {1}'.format('Jugos', 'Refrescos'))
# print('A esta {food} le doy {calf}.'.format(food='Pizza', calf='5/10'))

# 3. fromateo avanzado. Este método soporta muchas técnicas de formateo
#    A) Alinear una cadena de caracteres a la derecha en 30 caracteres
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
# print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; ''Dcab: {0[Dcab]:d}'.format(table))

myNum = -1234
myStr = "Right Aligned Number with length 10 is: {:>10}".format(myNum)
# print(myStr)
cadena = "una cadena muy cadena de prueba"

# print("Right Aligned: {:>30}".format(cadena))

#    B) Alinear una cadena de caracteres a la izquierda en 30 caracteres
#        (crea espacios a la derecha), con la siguiente sentencia
# print("{cadena:<30}".format(cadena="una cadena muy cadena de prueba"))

#    C) Alinear una cadena de caracteres al centro en 30 caracteres.
# print("{cadena:^30}".format(cadena="una cadena muy cadena de prueba"))

#    D) Truncamiento a 9 caracteres.
cad = "Me encanta el lenguaje Python diria yo si en realidad fuera"
# print(cad[0:9])

stringTrun = cad.rsplit(" ")[9]

# print(stringTrun)
import textwrap

str = textwrap.shorten(cad, width=15, placeholder='.')
# print(str)
# 4. Formateo por tipo
#    s para cadenas de caracteres (tipo str).
#    d para números enteros (tipo int).
#    f para números de coma flotante (tipo float).

# Formateo de numeros enteros rellenados con espacios


# Formateo de numeros rellenados con ceros


# Formateo de números flotantes, rellenados con espacios


'''
# Carrito de compra:
#    nombre_producto
#    precio
#    cantidad
#    descuento


#    NOMBRE PRODUCTO     PRECIO      CANTIDAD        SUBTOTAL
'''
carrito = {1: ['Monitor Samsumng 27 pulgadas     ', 4589.98, 1, 3],
           2: ['Tableta 10 pulgadas marca X      ', 2500.9, 1, 3],
           3: ['Mouse gamer 3d                   ', 3400.5, 1, 3],
           4: ['Computadora de escritorio lenovo ', 1589.98, 1, 3],
           5: ['Renovación Antivirus X           ', 1057, 2, 3]
           }

# 1. Mostrar el contenido del carrito alineado
renglones = []
def ObtenerRenglones():
    renglones.clear()
    try:
        for ren in carrito:
            # renglones.append(carrito[int(ren)]);
            p = carrito[int(ren)];
            renglones.append([ren, p[0], p[1], p[2], p[3]]);
    except Exception:
        print("")
    return (len(renglones))

# print(renglones)

# productos = []
# ind = 0
def ImprimirProductos():
    import json
    TieneProductos = open("TieneProductos.json", mode="w")
    cad = {}
    if ObtenerRenglones() > 0:
        for prod in renglones:
            id = "ID:%d" % prod[0]
            nom = "Nombre:%s" % prod[1];
            prec = "$:%f" % prod[2]
            cant = "Cantidad: %f" % prod[3]
            sub = "Subtotal: %f" % prod[4]
            print("{key:^0} {sombre:>20} {precio:^25}  {cant:>32}  {sub:>38}  ".format(key=id, sombre=nom, precio=prec,
                                                                                       cant=cant, sub=sub));
        cad = {"Bandera":True}
        json.dump(cad, TieneProductos)
        return True;
    else:
        cad = {"Bandera": False}
        print("No hay productos en el carrito");
        json.dump(cad, TieneProductos)
        return False;


'''
2. Eliminar un producto del carrito
'''
salir = False;
while (salir == False):
    print("\n");

    if ImprimirProductos():
        print("\n")
        try:
            key = int(input("Ingresa el ID del producto a eliminar"));
            try:
                del carrito[key]
                ImprimirProductos();
            except KeyError:
                print("ID no valido")
        except ValueError:
            print("Solo numeros enteros");
    else:
        salir = True;
'''
3. Regresar un JSON con una bandera si el carrito tiene productos
'''
