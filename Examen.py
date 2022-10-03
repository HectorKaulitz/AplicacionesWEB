import json;


class Examen:

    def ObtenerEstudiantes(self, Lista_alumnos=[]):

        alumnos = []

        JsonDatosAlumno = open("JsonDatosAlumno.json", mode="w")
        # se obtienen los archivos
        estudiantes = []
        archivo = open("Estudiantes.prn", mode="r")
        if archivo.readable():
            for est in archivo.read().split("\n"):
                if len(est) > 0:
                    estudiantes.append((est[0:8], est[9:]))
        archivo.close()

        materias = []
        archivo = open("Kardex.txt", mode="r")
        if archivo.readable():
            for kar in archivo.read().split("\n"):
                if len(kar) > 0:
                    datos = kar.split("|")
                    materias.append((datos[0], datos[1], datos[2]))
        archivo.close()
        # inicializamos variables
        alumno = {}
        materias_alumno = []
        promedio = 0

        if len(Lista_alumnos) > 0:  # esta buscando estudinte especifico
            for alum in Lista_alumnos:  # se recorre la lista
                no_control = alum;  # se obtiene el numero de control
                for i in range(0, len(estudiantes)):  # se recorre el txt
                    alumno = {}
                    promedio = 0
                    if estudiantes[i][0] == no_control:  # if existe coincidencia
                        materias_alumno = []
                        for j in range(0, len(materias)):  # recorremos buscando sus materias
                            if materias[j][0] == no_control:  # si coincide alguna materia
                                materias_alumno.append({"Nombre": materias[j][1], "Promedio": materias[j][2]})
                                promedio += int(materias[j][2])

                        alumno = {"Nombre": estudiantes[i][1], "Materias": materias_alumno,
                                  "Promedio General": (promedio / len(materias))}
                        alumnos.append(alumno)
            # print(json.dumps(alumnos))
            json.dump(alumnos, JsonDatosAlumno)
        else:  # lee todos
            for i in range(0, len(estudiantes)):  # se recorre el txt
                no_control = estudiantes[i][0];  # se obtiene el numero de control
                alumno = {}
                promedio = 0
                if estudiantes[i][0] == no_control:  # if existe coincidencia
                    materias_alumno = []
                    for j in range(0, len(materias)):  # recorremos buscando sus materias
                        if materias[j][0] == no_control:  # si coincide alguna materia
                            materias_alumno.append({"Nombre": materias[j][1], "Promedio": materias[j][2]})
                            promedio += int(materias[j][2])

                    alumno = {"Nombre": estudiantes[i][1], "Materias": materias_alumno,
                              "Promedio General": (promedio / len(materias))}
                    alumnos.append(alumno)
            json.dump(alumnos, JsonDatosAlumno)


# Tomar en cuneta que la letra ñ la toma como otro tipo de caracteres
obe = Examen()
#obe.ObtenerEstudiantes(["18420097", "18420100", "18420493", "18420495"]);
obe.ObtenerEstudiantes();
