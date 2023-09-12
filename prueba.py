import requests
import tkinter as tk
from tkinter import ttk

class Generator(ttk.Frame):
    sudoku=[[0, 6, 0, 2, 0, 0, 9, 0, 0], [0, 0, 9, 0, 0, 0, 0, 0, 0], [0, 0, 0, 4, 0, 0, 2, 0, 0], [5, 0, 0, 1, 0, 4, 0, 0, 8], [0, 0, 0, 0, 0, 0, 0, 5, 6], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 9, 0, 0, 0, 7, 0, 0, 0], [0, 0, 0, 0, 0, 0, 5, 3, 9], [0, 0, 1, 0, 0, 0, 0, 7, 0]]
    dificultad=""
    url="https://sudoku-api.vercel.app/api/dosuku"
    
    def crear_sudoku(self, interface1, sudoku):
        self.frame2=tk.Frame(interface1)
        self.frame2.pack(fill="both", expand=True)
        self.frame2.config(bd=24, relief="sunken", bg="#f1f1f1")
        self.dificultad=ttk.Label(self.frame2, text= "Diffculty: Hard", font="Arial 15")
        self.dificultad.pack()
        self.tabla = []
        self.fila= [0,1,2,3,4,5,6,7,8]
        self.columna= [0,1,2,3,4,5,6,7,8]
        for i in self.fila:
            lista = []
            for j in self.columna:
                if sudoku[i][j] == 0:
                    sudoku[i][j]=""
                self.btn = tk.Button(self.frame2,height=2,width=2, text=sudoku[i][j])
                self.btn.grid()
                rR = i//3
                cC = j//3
                if not (rR+cC) % 2:
                    self.btn.config(bg='lightblue')
                self.btn.grid(column=j, row=i)
                self.lista.append(self.btn)
            self.tabla.append(lista)
    
    def __init__(self,interface):
        self.crear_sudoku(interface, self.sudoku)
        
        
'''class Game(ttk.Frame, Generator):
    
    def __init__(self,interface):
        self.dificultad=ttk.Label(interface, text= "Hard")
        self.dificultad.place(x=10, y=10)'''
        
    
vent=tk.Tk()
vent.title("Sudoku Zarate-Vargas")
vent.resizable(False, False)
vent.geometry("600x600")
vent.config(background="#f1f1f1")
eq=Generator(vent)
vent.mainloop()