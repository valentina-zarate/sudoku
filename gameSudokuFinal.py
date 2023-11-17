import requests
import tkinter as tk
from tkinter import ttk
import Fventana_dificultad as vent_diff
from Fventana_dificultad import *
from functools import partial
from PIL import ImageTk, Image

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
                self.errors()
            
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
    
    def errors(self):
        #Ventana que aparece cuando se pierde el juego
        self.frame2.destroy()
        self.frame3 = tk.Frame(self.interface)
        self.frame3.pack(fill = "both", expand = True)
        self.frame3.config(bd = 32, relief = "flat", bg = "#f1f1f1")
        self.part_end = ttk.Label(self.frame3, text = "PARTIDA TERMINADA", font = "Arial 22", foreground = "red", background = "#f1f1f1")
        self.part_end.grid(column = 1, row = 1)
        self.err_msg = ttk.Label(self.frame3, text = "Perdiste el juego porque cometiste más de 5 errores.", font = "Arial 16", background = "#f1f1f1")
        self.err_msg.grid(column = 1, row = 2)
        self.img = ImageTk.PhotoImage(Image.open("noyippee.png"))
        self.panel = ttk.Label(self.frame3, image = self.img, background = "#f1f1f1")
        self.panel.grid(column = 1, row = 4)
    
    def win(self):
        #Ventana que aparece al ganar el juego
        self.frame2.destroy()
        self.frame3 = tk.Frame(self.interface)
        self.frame3.pack(fill = "both", expand = True)
        self.frame3.config(bd = 32, relief = "flat", bg = "#f1f1f1")
        self.part_end = ttk.Label(self.frame3, text = "PARTIDA TERMINADA", font = "Arial 22", foreground = "green", background = "#f1f1f1")
        self.part_end.grid(column = 1, row = 1)
        self.err_msg = ttk.Label(self.frame3, text = "Completaste todas las casillas correctamente y ganaste el juego.", font = "Arial 16", background = "#f1f1f1")
        self.err_msg.grid(column = 1, row = 2)
        self.img = ImageTk.PhotoImage(Image.open("yippe.gif"))
        self.panel = ttk.Label(self.frame3, image = self.img, background = "#f1f1f1")
        self.panel.grid(column = 1, row = 4)

    def comprobar(self):
        #"Lee" todos los números uno a uno para asegurarse de que todas las casillas están llenas y sin errores
        for t in range(len(self.sudoku)):
            for l in range(len(self.sudoku[0])):
                text_button = self.tabla[t][l].cget("text")
                fg_button = self.tabla[t][l].cget("fg")
                #Busca por un False y si lo encuentra termina el proceso
                result = []
                if text_button == "" or fg_button == "red":
                    result.append(False)
                    break
                else:
                    result.append(True)
        #Si todas las casillas estáncompletas y sin errores salta la ventana de haber ganado el juego
        if not False in result:
            self.win()
                         
    def crear_sudoku(self, sudoku):
        #Crea la ventana con el sudoku principal
        #Configura el frame, destruye el de la ventana de dificiltad y genera el del juego        
        self.frame.destroy()
        self.frame2 = tk.Frame(self.interface)
        self.frame2.pack(fill = "both", expand = True)
        self.frame2.config(bd = 35, relief = "flat", bg = "#f1f1f1")
        #Cuadro de texto que te dice la dificultad que estás jugando
        self.dificultad = ttk.Label(self.frame2, text = self.dificultad, font = "Arial 15", background = "#f1f1f1")
        self.dificultad.grid(column = 9, row = 9)
        #Cuadro de texto que te dice los errores que llevas
        self.cont_err = ttk.Label(self.frame2, text = "Errores: 0/5", font = "Arial 15", background = "#f1f1f1")
        self.cont_err.grid(column = 9,row = 10)
        #Crea la fila de botones para seleccionar número
        for h in range(len(sudoku[0])):
            self.select_btn = tk.Button(self.frame2, height = 2, width = 2, text = str(h+1), bg = "#C0DAE2", command = lambda n=h+1: self.save_button(n))
            self.select_btn.grid(column = h, row = 11)
        self.selection = ttk.Label(self.frame2, text= "Nro seleccionado: ", font = "Arial 11", background = "#f1f1f1")
        self.selection.grid(column = 9, row = 11)
            #Crea los botones del cuadro de sudoku
        self.tabla = []
        for i in range(len(sudoku)):
            self.lista = []
            for j in range(len(sudoku[0])):
                if sudoku[i][j] == 0:
                    sudoku[i][j] = ""
                btn = tk.Button(self.frame2, height = 2, width = 2, text = sudoku[i][j], command = partial(self.click_button, i, j))
                color=self.get_color(i,j)
                btn.config(bg=color)
                if sudoku[i][j]:
                    btn.config(fg = "#032e4d")
                btn.grid(column = j, row = i)
                self.lista.append(btn)
            self.tabla.append(self.lista)
        #Crea el botón comprobar
        self.comprob = tk.Button(self.frame2, height = 2, width = 7, text = "Comprobar", command = self.comprobar)
        self.comprob.config(font = "Arial 9", bg = "#C0DAE2")
        self.comprob.grid(column = 9, row = 4)

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