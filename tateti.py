#Proyecto final juego ta-te-ti


import tkinter as tk
from tkinter import messagebox
import pickle

class TatetiGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Tateti")

        self.tablero = [[" " for _ in range(3)] for _ in range(3)]
        self.turno_actual = 0
        self.jugadores = ["X", "O"]
        self.marcador = {"X": 0, "O": 0}
        self.primer_turno_actual = "X"



        self.crear_interfaz()
        self.mostrar_mensaje_turno()

    def reiniciar_juego(self):
        self.tablero = [[" " for _ in range(3)] for _ in range(3)]
        self.turno_actual = 0
        self.actualizar_tablero()
        self.guardar_estado()
        self.mostrar_mensaje_turno()

    def reiniciar_marcador(self):
        self.marcador = {"X": 0, "O": 0}
        self.actualizar_marcador()

    def verificar_ganador(self, jugador):
        # Verificar filas
        for fila in self.tablero:
            if all(cell == jugador for cell in fila):
                return True

        # Verificar columnas
        for columna in range(3):
            if all(self.tablero[fila][columna] == jugador for fila in range(3)):
                return True

        # Verificar diagonales
        if all(self.tablero[i][i] == jugador for i in range(3)) or all(self.tablero[i][2 - i] == jugador for i in range(3)):
            return True

        return False

    def hacer_movimiento(self, fila, columna):
        if self.tablero[fila][columna] == " ":
            jugador_actual = self.jugadores[self.turno_actual % 2]
            self.tablero[fila][columna] = jugador_actual

            if self.verificar_ganador(jugador_actual):
                self.marcador[jugador_actual] += 1
                self.actualizar_marcador()
                self.mostrar_mensaje(f"¡{jugador_actual} ha ganado!")
                self.reiniciar_juego()
            elif all(cell != " " for row in self.tablero for cell in row):
                self.mostrar_mensaje("¡Empate!")
                self.reiniciar_juego()
            else:
                self.turno_actual += 1
                self.actualizar_tablero()
                self.guardar_estado()

    def mostrar_mensaje(self, mensaje):
        messagebox.showinfo("¡Fin del juego!", mensaje)

    def mostrar_mensaje_turno(self):
        jugador_actual="X"
        self.mostrar_mensaje(f"Turno de {jugador_actual}")

    def crear_interfaz(self):
        for fila in range(3):
            for columna in range(3):
                btn = tk.Button(self.root, text=" ", font=("Helvetica", 24), width=4, height=2,
                                command=lambda f=fila, c=columna: self.hacer_movimiento(f, c))
                btn.grid(row=fila, column=columna)

        reiniciar_partida_btn = tk.Button(self.root, text="Reiniciar Partida", command=self.reiniciar_juego)
        reiniciar_partida_btn.grid(row=3, column=0, columnspan=3)

        reiniciar_marcador_btn = tk.Button(self.root, text="Reiniciar Marcador", command=self.reiniciar_marcador)
        reiniciar_marcador_btn.grid(row=4, column=0, columnspan=3)

        self.marcador_label = tk.Label(self.root, text="Marcador:\nX: 0\nO: 0", font=("Helvetica", 12))
        self.marcador_label.grid(row=5, column=0, columnspan=3)

        self.actualizar_tablero()
        self.cargar_estado()

    def actualizar_tablero(self):
        for fila in range(3):
            for columna in range(3):
                texto = self.tablero[fila][columna]
                btn_text = " " if texto == " " else f" {texto} "
                self.root.grid_slaves(row=fila, column=columna)[0].config(text=btn_text)

    def actualizar_marcador(self):
        marcador_text = f"Marcador:\nX: {self.marcador['X']}\nO: {self.marcador['O']}"
        self.marcador_label.config(text=marcador_text)

    def guardar_estado(self):
        with open("tateti_guardado.pkl", "wb") as archivo:
            pickle.dump((self.tablero, self.turno_actual, self.marcador, self.primer_turno_actual), archivo)

    def cargar_estado(self):
        try:
            with open("tateti_guardado.pkl", "rb") as archivo:
                self.tablero, self.turno_actual, self.marcador, self.primer_turno_actual = pickle.load(archivo)
                self.actualizar_tablero()
                self.actualizar_marcador()
        except FileNotFoundError:
            pass  # No hay un estado guardado

if __name__ == "__main__":
    root = tk.Tk()
    tateti_gui = TatetiGUI(root)
    root.mainloop()