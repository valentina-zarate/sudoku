import tkinter as tk
from tkinter import ttk
import Fventana_dificultad as vent_diff
import Fotras_ventanas as vent_othr
from Fventana_dificultad import *
from Fotras_ventanas import *

class JuegoSudoku(ttk.Frame):
    sudoku = []
    dificultad = ""
    url = "https://sudoku-api.vercel.app/api/dosuku"
    interface = ""
    errores = 0
    select = 0
    
    def __init__(self,interface):
        self.interface = interface
        #La función de la ventana de selección de dificultad se encuentra en un archivo aparte
        vent_diff.ventana_dificultad(self)

    def save_button(self, n):
        self.select = n
        self.selection.config(text = f"Nro seleccionado: {self.select}")    

    def click_button(self, fila, col):
        #Lo que pasa cuando se hace click en una casilla
        fgColor = self.tabla[fila][col].cget("fg")
        if fgColor != "#032e4d":
            #Detecta si el número no es uno de los que te da el propio sudoku tomando el color de la fuente
            numero = self.select
            if self.check_number(numero,fila,col):
                color = self.get_color(fila, col)
            else:
                color = "red"
            if numero != 0:
                self.tabla[fila][col].config(text = numero, bg = color)
                self.cont_err.config(text = f"Errores: {self.errores}/5")
            if self.errores > 5:
                self.lose()
            
    def check_number(self, number, row, col):
        result=[]
        for r in range(len(self.tabla)):
            #Comprueba la fila del sudoku con el número puesto
            cuadradito = str(self.tabla[r][col].cget("text"))
            if cuadradito == str(number):
                self.tabla[r][col].config(bg = "red")
                result.append(False)
            else:
                color=self.get_color(r, col)
                self.tabla[r][col].config(bg = color)
        for c in range(len(self.tabla)):
            #Comprueba la columna del sudoku con el numero puesto
            cuadradito = str(self.tabla[row][c].cget("text"))
            if cuadradito == str(number):
                self.tabla[row][c].config(bg = "red")
                result.append(False)
            else:
                color=self.get_color(row, c)
                self.tabla[row][c].config(bg = color)
        rowCua = (row // 3)
        colCua = (col // 3)
        mcol = colCua * 2 + colCua
        mrow = rowCua * 2 + rowCua
        for a in range(3):
            #Comprueba el cuadrante del sudoku con el número puesto
            for b in range(3):
                cuadradito = str(self.tabla[mrow + a][mcol + b].cget("text"))
                if cuadradito == str(number):
                    self.tabla[mrow+a][mcol+b].config(bg = "red")
                    result.append(False)
                else:
                    color=self.get_color(mrow+a, mcol+b)
                    self.tabla[mrow+a][mcol+b].config(bg = color)
        for i in result:
            if i == False:
                self.errores += 1
                return False      
        return True

    def comprobar(self):
        #"Lee" todos los números uno a uno para asegurarse de que todas las casillas están llenas y sin errores
        for t in range(len(self.sudoku)):
            for l in range(len(self.sudoku[0])):
                text_button = self.tabla[t][l].cget("text")
                bg_button = self.tabla[t][l].cget("bg")
                #Busca por un False y si lo encuentra termina el proceso
                result = []
                if text_button == "" or bg_button == "red":
                    result.append(False)
                    break
                else:
                    result.append(True)
        #Si todas las casillas estáncompletas y sin errores salta la ventana de haber ganado el juego
        if not False in result:
            self.win()
              
    def lose(self):
        #Ventana que aparece cuando se pierde el juego
        vent_othr.lose(self)
        
    def win(self):
        #Ventana que aparece al ganar el juego
        vent_othr.win(self)        
                         
    def crear_sudoku(self, sudoku):
        #Crea la ventana con el sudoku principal
        vent_othr.crear_sudoku(self, sudoku)

    def get_color(self, i, j):
        #Colorea los cuadrantes
        rR = i // 3
        cC = j // 3
        if not (rR + cC) % 2:
            return 'lightblue'
        else:
            return 'gainsboro'
        
    def easy(self):
        #Genera un sudoku de dificultad fácil
        vent_diff.easy(self)
        
    def medium(self):
        #genera un sudoku de dificultad media
        vent_diff.medium(self)
        
    def hard(self):
        #genera un sudoku de dificultad difícil
        vent_diff.hard(self)   
    
vent = tk.Tk()
vent.title("Sudoku Zarate-Vargas")
vent.resizable(False, False)
vent.config(background = "#f1f1f1")
eq = JuegoSudoku(vent)
vent.mainloop()