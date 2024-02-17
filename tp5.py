#1)Hacer un programa que gestione datos para una escuela         
class Escuela:
    def __init__(self):
        self.datos = {"Alumnos": []}

    def agregar_alumno(self, alumno):
        if self.validar_dni(alumno["DNI"]):
            self.datos["Alumnos"].append(alumno)
        else:
            print("Error: El número de DNI es inválido.")

    def validar_dni(self, dni):
        return dni.isdigit() and len(dni) == 8

    def mostrar_alumnos(self):
        for i, alumno in enumerate(self.datos["Alumnos"], 1):
            print(f"\nAlumno {i}:\n")
            for key, value in alumno.items():
                print(f"{key}: {value}")
                
    def modificar_alumno(self, indice, campo, nuevo_valor):
        try:
            alumno = self.datos["Alumnos"][indice - 1]
            if campo in alumno:
                alumno[campo] = nuevo_valor
            else:
                print(f"Error: El campo '{campo}' no existe para este alumno.")
        except IndexError:
            print("Error: El índice especificado está fuera de rango.")

    def expulsar_alumno(self, indice):
        try:
            expulsado = self.datos["Alumnos"].pop(indice - 1)
            print(f"\nAlumno expulsado:\n{expulsado}")
        except IndexError:
            print("Error: El índice especificado está fuera de rango.")


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

alumno3 = {
    "Nombre": "Pedro",
    "Apellido": "Lopez",
    "DNI": "1234abc",  # DNI inválido
    "Fecha de nacimiento": "20/03/2001",
    "Tutor": "Ana Fernandez",
    "Notas": [7, 8, 9],
    "Faltas": 0,
    "Amonestaciones": 0
}

escuela.agregar_alumno(alumno1)
escuela.agregar_alumno(alumno2)
escuela.agregar_alumno(alumno3)

escuela.mostrar_alumnos()

escuela.modificar_alumno(1,"Nombre","pablo")
escuela.modificar_alumno(1,"Tutor","Franco Lopez")

escuela.mostrar_alumnos()

escuela.expulsar_alumno(2)

escuela.mostrar_alumnos()

#Castrillo Santiago