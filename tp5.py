#1)Hacer un programa que gestione datos para una escuela         

class Escuela:
    def __init__(self):
        self.datos = {"Alumnos": []}

    def agregar_alumno(self, alumno):
        self.datos["Alumnos"].append(alumno)

    def mostrar_alumnos(self):
        for i, alumno in enumerate(self.datos["Alumnos"], 1):
            print(f"\nAlumno {i}:\n")
            for key, value in alumno.items():
                print(f"{key}: {value}")
                
    def modificar_alumno(self, indice, campo, nuevo_valor):
        self.datos["Alumnos"][indice - 1][campo] = nuevo_valor

    def expulsar_alumno(self, indice):
        expulsado = self.datos["Alumnos"].pop(indice - 1)
        print(f"\nAlumno expulsado:\n{expulsado}")


escuela = Escuela()

alumno1 = {
    "Nombre": "Juan",
    "Apellido": "Perez",
    "DNI": "12345678",
    "Fecha de nacimiento": "01/01/2000",
    "Tutor": "Maria Rodriguez",
    "Notas": [8, 7, 9],
    "Faltas": 2,
    "Amonestaciones": 1
}

alumno2 = {
    "Nombre": "Ana",
    "Apellido": "Gomez",
    "DNI": "87654321",
    "Fecha de nacimiento": "15/05/2002",
    "Tutor": "Carlos Martinez",
    "Notas": [6, 5, 9],
    "Faltas": 1,
    "Amonestaciones": 0
}

escuela.agregar_alumno(alumno1)
escuela.agregar_alumno(alumno2)

escuela.mostrar_alumnos()

escuela.modificar_alumno(1, "Nombre", "Pablo")
escuela.modificar_alumno(1,"Tutor","Franco Lopez")

escuela.mostrar_alumnos()

escuela.expulsar_alumno(2)

escuela.mostrar_alumnos()

#Castrillo Santiago