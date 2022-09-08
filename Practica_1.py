# Tipos de dato UNIDAD 1
# 24/agosto/2022
# El hector

# Datos primitivos python
"""
Numerico: float,int
Cadenas:
Boleanos:
"""
import math

producto = "Computadora gamer"
precio = 5000.50
oferta = False
descuento = 10
# precio_oferta= precio-(precio*descuento/100)

# print(producto+" $ ", precio, " "+str(oferta))

"""
Condicionales
1.-If
2.-If-else
3.-Aninado
"""
"""if (oferta):
    precio_oferta = precio - (precio * descuento / 100)
else:
    precio_oferta = precio

    print(producto + " $ ", precio_oferta, )
"""

# dia = input("Ingrese el numero del dia")
# print(dia)
""" 
dia = 0
match int(dia):
    case 1:
        print("Lunes")
    case 2:
        print("Martes")
    case 3:
        print("Miercoles")
    case 4:
        print("Jueves")
    case 5:
        print("Viernes")
    case 6:
        print("Sabado")
    case 7:
        print("Domingo")

num = int(input("Ingresa un numero "))
if num < 0:
    num *= -1

print("Absoluto: ", num)

primerNombre = input("Primer nombre")
segundoNombre = input("Segundo nombre")

if primerNombre[0] == segundoNombre[0]:
    print("Coincidencia primera letra")
else:
    print("Sin coincidencia primera letra")

if primerNombre[len(primerNombre)-1] == segundoNombre[len(segundoNombre)-1]:
    print("Coincidencia ultima letra")
else:
    print("Sin coincidencia ultima letra")
"""
"""
print("--------------------Partidos disponibles:--------------")
print("A = Partido ROJO \n B = Partido VERDE \n C = Partido AZUL ")

candidato = input("Elija el candidato al que dara su voto ").upper()

match candidato:
    case "A" :
        print("Usted ha votado por el partido Rojo")
    case "B" :
        print("Usted ha votado por el partido Verde")
    case "C":
        print("Usted ha votado por el partido Azul")
    case default:
        print("Opcion no valida")
"""
"""
letra = input("Ingresa una letra").upper()
if len(letra)==1:
    if letra in "AEIOU":
        print("Letra es una vocal")
    else:
        print("Letra no es una vocal")
else:
    print("Solo debe ser 1 letra")
"""
"""
mes = -1
while mes < 1 or mes > 12:
    mes = input("Ingresa un numero del 1 al 12 (correspondiente a los meses del año) \n")
    try:
        mes = int(mes)
    except:
        mes = -1

match int(mes):
    case -1:
        print("Solo numeros enteros del 1 al 12")
    case 1:
        print("Enero")
    case 2:
        print("Febrero")
    case 3:
        print("Marzo")
    case 4:
        print("Abril")
    case 5:
        print("Mayo")
    case 6:
        print("Junio")
    case 7:
        print("Julio")
    case 8:
        print("Agosto")
    case 9:
        print("Septiembre")
    case 10:
        print("Octubre")
    case 11:
        print("Noviembre")
    case 12:
        print("Dicembre")
    case default:
        print("No valido")
        """

"""
for x in range(0,102,2):
    print(x)
"""
"""
for x in range (500,1001):
    if(x %3 ==0 ):
        print(x)
"""
"""
for x in range (100,0,-1):
        print(x)
"""
"""
num = 10
while num>0 :
    print(num)
    num-=1
"""
"""
num = -1
while num != 0:
    num = int(input("Ingresa un numero"))
    if num != 0:
        print(num)
    else:
        print("Termino")
 """

while True:
    num = int(input("Ingresa un numero"))
    if num != 0:
        print(num)
    else:
        print("Termino")
        break;