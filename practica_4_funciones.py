

def imprimirPasajeros(pasajeros):
    print(pasajeros)

def imprimirCiudades(ciudades):
    print(ciudades)


def agregarPasajero(pasajeros):
    try:
        print(pasajeros)
        print("\n")
        nom = input("Ingresa el nombre del pasajero")
        cla = int(input("Ingrea la clave del pasajero"))
        dest = input("Ingresa la ciudad destino del pasajero")
        pasajeros.append((nom, cla, dest))
    except:
        print("Error datos no validos")


def agregarCiudad(ciudades):

    try:
        print(ciudades)
        print("\n")
        ciud = input("Ingresa el nombre de la ciudad")
        est = input("Ingrea el estado de la ciudad")
        ciudades.append((ciud, est))
    except:
        print("Error datos no validos")



def ciudadDestino(pasajeros):

        salir = False
        encontro = False
        while(salir == False):
            try:
                print("\n")
                clv = int(input("Ingresa la clave del pasajero"))
                for pas in pasajeros:
                    if(pas[1] == clv):
                        encontro=True
                        print("Pasajero: ",pas[0]," viaja a ciudad :",pas[2])
                if(encontro == False):
                    print("No existe pasajero con esa clave \n")
                salir = True
            except:
                salir = False
                print("Error dato no valido")

def cantidadCiudad(pasajeros):
    try:
        cont = 0
        print("\n")
        ciu = input("Ingres la ciudad").upper()
        for pas in pasajeros:
            if(str(pas[2]).upper() == ciu):
                cont +=1
        print("La cantidad de pasajeros a la ciudad: ",ciu ," es: ",cont )
        print("\n")
    except:
        print("Dato no valido")



def estadoDestino(pasajeros,ciudades):
    salir = False
    encontro = False
    encontroCiud = False
    while (salir == False):
        try:
            print("\n")
            clv = int(input("Ingresa la clave del pasajero"))
            for pas in pasajeros:
                if (pas[1] == clv):
                    encontro = True
                    for ci in ciudades:
                        if(str(pas[2]).upper() == str(ci[0]).upper()):
                            encontroCiud = True
                            print("Pasajero: ", pas[0], " viaja a estado :", ci[1])

            if (encontro == False):
                print("No existe pasajero con esa clave \n")
            else:
                if(encontroCiud == False):
                    print("Pasajero encontrado,pero la ciudad y estado al que viaja no esta registrado")
            print("\n")
            salir = True
        except ValueError:
            salir = False
            print("Error dato no valido")


def cantidadEstado(pasajeros,ciudades):
    try:
        cont = 0
        encontroEstado = False
        print("\n")
        est = input("Ingresa el estado").upper()
        for ci in ciudades:
            if(str(ci[1]).upper() == est):
                encontroEstado = True
                for pas in pasajeros:
                    if (str(pas[2]).upper() == str(ci[0]).upper()):
                        cont += 1
                print("La cantidad de pasajeros al estado : ", est, " es: ", cont)
                print("\n")

        if(encontroEstado == False):
            print("Estado no encontrado")
        print("\n")
    except:
        print("Dato no valido")