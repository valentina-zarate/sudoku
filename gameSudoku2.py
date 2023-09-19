import requests
import tkinter as tk
from tkinter import ttk
import Fventana_dificultad as vent_diff
from Fventana_dificultad import ventana_dificultad
from functools import partial

class JuegoSudoku(ttk.Frame):
    sudoku = []
    solucion = []
    dificultad = ""
    url = "https://sudoku-api.vercel.app/api/dosuku"
    interface = ""
    
    def __init__(self,interface):
        self.interface = interface
        vent_diff.ventana_dificultad(self)
        
    def click_button(self, fila, col):
        print(fila, col)
        num = self.tabla[fila][col].cget("text")
        fgColor = self.tabla[fila][col].cget("fg")
        if fgColor != "#0b334f":
            if not num or num == "9":
                numero = "1"
            else:
                numero = str(int(num)+1)
            if self.check_number(numero,fila,col):
                color = self.get_color(fila, col)
            else:
                color = "red"
            self.tabla[fila][col].config(text = numero, bg = color)
            
    def check_number(self, number, row, col):
        result=[]
        for r in range(len(self.tabla)):
            cuadradito = str(self.tabla[r][col].cget("text"))
            if cuadradito == str(number):
                self.tabla[r][col].config(bg = "red")
                result.append(False)
            else:
                color=self.get_color(r, col)
                self.tabla[r][col].config(bg = color)
        for c in range(len(self.tabla)):
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
                return False      
        return True
                        
    def comprobar(self):
        for a in self.solucion:
            for b in a:
                pass
                        
    def crear_sudoku(self, sudoku):
        print(sudoku)
        print(self.solucion)
        self.frame.destroy()
        self.frame2 = tk.Frame(self.interface)
        self.frame2.pack(fill = "both", expand = True)
        self.frame2.config(bd = 22, relief = "flat", bg = "#f1f1f1")
        self.dificultad = ttk.Label(self.frame2, text = self.dificultad, font = "Arial 15", background = "#f1f1f1")
        self.dificultad.grid(column = 9, row = 9)
        self.tabla = []
        for i in range(len(sudoku)):
            self.lista = []
            for j in range(len(sudoku[0])):
                if sudoku[i][j] == 0:
                    sudoku[i][j] = ""
               
                btn = tk.Button(self.frame2, height = 2, width = 2, text=sudoku[i][j], command = partial(self.click_button, i, j))
                color=self.get_color(i,j)
                btn.config(bg=color)
                if sudoku[i][j]:
                    btn.config(fg = '#032e4d')
                btn.grid(column = j, row = i)
                self.lista.append(btn)
            self.tabla.append(self.lista)
        self.comprob = tk.Button(self.frame2, height = 2, width = 7, text = "Comprobar", command = self.comprobar)
        self.comprob.config(font = "Arial 9")
        self.comprob.grid(column = 9, row = 4)
        
    def get_color(self, i, j):
        rR = i // 3
        cC = j // 3
        if not (rR + cC) % 2:
            return 'lightblue'
        else:
            return 'gainsboro'
        
    def easy(self):
        resp = "504"
        while self.dificultad != "Easy" or "504" in resp:
            resp = requests.get(self.url)
            if "200" in str(resp):
                self.json = resp.json()
                self.dificultad = self.json["newboard"]["grids"][0]["difficulty"]
        self.sudoku = self.json["newboard"]["grids"][0]["value"]
        self.solucion = self.json["newboard"]["grids"][0]["solution"]
        self.dificultad = " Dificultad:\n  Fácil"
        self.crear_sudoku(self.sudoku)
        
    def medium(self):
        resp = "504"
        while self.dificultad != "Medium" or "504" in resp:
            resp = requests.get(self.url)
            if "200" in str(resp):
                self.json = resp.json()
                self.dificultad=self.json["newboard"]["grids"][0]["difficulty"]
        self.sudoku = self.json["newboard"]["grids"][0]["value"]
        self.solucion = self.json["newboard"]["grids"][0]["solution"]
        self.dificultad = " Dificultad:\n  Medio"
        self.crear_sudoku(self.sudoku)
        
    def hard(self):
        resp = "504"
        while self.dificultad != "Hard" or "504" in resp:
            resp = requests.get(self.url)
            if "200" in str(resp):
                self.json = resp.json()
                self.dificultad=self.json["newboard"]["grids"][0]["difficulty"]
        self.sudoku = self.json["newboard"]["grids"][0]["value"]
        self.solucion = self.json["newboard"]["grids"][0]["solution"]
        self.dificultad = " Dificultad: Difícil"
        self.crear_sudoku(self.sudoku)   
    
vent = tk.Tk()
vent.title("Sudoku Zarate-Vargas")
vent.resizable(False, False)
vent.config(background = "#f1f1f1")
eq=JuegoSudoku(vent)
vent.mainloop()