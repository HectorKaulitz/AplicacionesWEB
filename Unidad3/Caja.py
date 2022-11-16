'''
Unidad 3: Programación Orientada a objetos
Tema: 1.1 Clases y objetos
Fecha: 28 de septiembre del 2022
Autor: Leonardo Martínez González

Clases y objetos en Python : https://www.youtube.com/watch?v=aj4PEXq0zuc
'''
from fernet import Fernet

'''
Sumar y restar dias a la fecha: https://j2logo.com/operaciones-con-fechas-en-python/
'''
import datetime

ahora = datetime.datetime.utcnow()
# print(ahora)

# print((ahora - datetime.timedelta(days=1)))

'''
Generar numeros aleatorios: https://j2logo.com/python/generar-numeros-aleatorios-en-python/
'''
import random

# for i in range(10):
#   print(random.randrange(5, 27, 4))
'''
Código ASCII:  https://elcodigoascii.com.ar/
Convertir un INT a ASCII: https://www.delftstack.com/es/howto/python/python-int-to-ascii/
Descargue la libreria bcrypt con el comando: "pip install bcrypt"
'''
asc = []
num = 65;
while (num <= 90):
    asc.append(num);
    num += 1;

num = 97;
while (num <= 122):
    asc.append(num);
    num += 1;
# print(asc);
# for i in range(0,(len(asc)-1),1):
#   print(chr(asc[i]));
print(chr(asc[random.randrange(0, (len(asc) - 1), 1)]));

'''

Realizar una clase llamada Password que siga las siguientes condiciones:
▪ Que tenga los atributos longitud, contraseña y fecha_expiracion. Por defecto, la longitud sera de 8, la contraseña
  será los números del 1 al 8 y la fecha_expiración será de UN día.
'''


def Password(longitud=8, contrasena='12345678', expiracion='2022-09-28'):
    print("La longitud es de " + str(longitud) + " la contraseña es " + contrasena + " y expira " + expiracion)


# Password()
'''
▪ Un constructor con la contraseña y fecha_expiracion que nosotros le pasemos, se calculará la longitud de la contrasena
'''


class CajaClase:
    aleatoria = "";
    key = "";
    longitud = 8;

    def __init__(self, con, expiracion):
        self.key = Fernet.generate_key();
        self.longitud = len(con)
        print("Longitud contraseña es de:" + str(self.longitud))
        self.GenerarContrasena()

    def GenerarContrasena(self):
        longitude = self.longitud;
        while len(self.aleatoria) < longitude:
            # caracter = ;
            self.aleatoria += '' + chr(asc[random.randint(0, (len(asc) - 1))]);

    # self.aleatoria += '#';

    def Fuerte(self):
        esFuerte = False;
        numeroMayusculas = 0;
        numeroMinusculas = 0;
        numeroCaracter = 0;

        for caracter in self.aleatoria:
            if (ord(caracter) > 64 and ord(caracter) < 91):  # si es maysucula
                numeroMayusculas += 1;
            else:  # si no es minuscula
                if (ord(caracter) > 96 and ord(caracter) < 123):
                    numeroMinusculas += 1;
                else:  # es cualquier otro caracter
                    numeroCaracter += 1;

        if numeroMayusculas > 2 and numeroMinusculas > 0 and numeroCaracter > 0:
            esFuerte = True;

        return esFuerte;

    def cifraPassword(self):
        contrasenaEncritada = Fernet(self.key).encrypt(self.aleatoria);
        return contrasenaEncritada;

    def decifraPassword(self, conCi):
        contrasenaDesencriptada = Fernet(self.key).decrypt(conCi).decode();
        return contrasenaDesencriptada;

    def setLongitud(self, long):
        self.longitud = long;

    def getLongitud(self):
        return self.longitud;

    def getContrasena(self):
        return self.aleatoria;


'''
obj = CajaClase("HectorContra", datetime.datetime.now())
print(obj.Fuerte());
cifrada = obj.cifraPassword()
print(cifrada);
print(obj.decifraPassword(cifrada));

obj.setLongitud(15);
obj.GenerarContrasena();
print(obj.getContrasena())
print(obj.getLongitud())
cifrada = obj.cifraPassword()
print(cifrada);

print(obj.decifraPassword(cifrada));
print(obj.Fuerte());
'''

'''
Generará una contraseña aleatoria con esa longitud.

▪ Los métodos que implementa serán:
▪ esFuerte(): devuelve un booleano si es fuerte o no, para que sea fuerte debe tener mas de 2 mayúsculas, al menos una
minúscula y al menos  1 caracter.

▪ generarPassword(): genera la contraseña del objeto con la longitud que tenga.

▪ cifraPassword(): cifra la contraseña del objeto.

▪ verificarClave: regresará verdadero si la contrasena es correcta.

▪ Método get para contraseña y longitud.

▪ Método set para longitud.

Ahora, crea una clase clase ejecutable(main):
▪ Crea un array de Passwords con el tamaño que tu le indiques por teclado.
▪ Crea un bucle que cree un objeto para cada posición del array.
▪ Indica también por teclado la longitud de los Passwords (antes de bucle).
▪ Crea otro array de booleanos donde se almacene si el password del array de Password es o no fuerte (usa el bucle anterior).
▪ Al final, muestra la contraseña y si es o no fuerte (usa el bucle anterior). Usa este simple formato:
contraseña1 valor_booleano1
contraseña2 valor_bololeano2
'''


class Ejecutable:
    cantidadPassword = 0;
    arrayPassword = [];
    arrayPasswordSeguridad = [];
    longitudPassword = 0;

    def __init__(self):
        while (True):
            continuar = False;
            while continuar == False:
                try:
                    self.cantidadPassword = int(input("Ingresa el numero de contraseñas a generar: "));
                    continuar = True;
                except ValueError:
                    continuar = False;

            continuar = False;
            while continuar == False:
                try:
                    self.longitudPassword = int(input("Ingresa la longitud de las contraseñas: "));
                    continuar = True;
                except ValueError:
                    continuar = False;

            self.GenerarContrasena();
            print(self.arrayPassword)
            print(self.arrayPasswordSeguridad)

    def GenerarContrasena(self):
        i = 0;
        while i < self.cantidadPassword:
            cont = "";
            while len(cont) < self.longitudPassword:
                cont += '' + chr(asc[random.randint(0, (len(asc) - 1))]);
            cont += str(self.generar_numeros())
            self.arrayPassword.append(cont);
            self.arrayPasswordSeguridad.append(self.Fuerte(cont))
            i += 1;

    def generar_numeros(self):
        return random.randint(0, 9)

    def Fuerte(self,contra):
        esFuerte = False;
        numeroMayusculas = 0;
        numeroMinusculas = 0;
        numeroCaracter = 0;

        for caracter in contra:
            if ord(caracter) > 64 and ord(caracter) < 91:  # si es maysucula
                numeroMayusculas += 1;
            else:  # si no es minuscula
                if ord(caracter) > 96 and ord(caracter) < 123:
                    numeroMinusculas += 1;
                else:  # es cualquier otro caracter
                    numeroCaracter += 1;

        if numeroMayusculas > 2 and numeroMinusculas > 0 and numeroCaracter > 0:
            esFuerte = True;

        return esFuerte;


objE = Ejecutable();
