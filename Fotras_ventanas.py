import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
from functools import partial

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
        #Crea el botón comprobar
        self.comprob = tk.Button(self.frame2, height = 2, width = 7, text = "Comprobar", command = self.comprobar)
        self.comprob.config(font = "Arial 9", bg = "#C0DAE2")
        self.comprob.grid(column = 9, row = 4)
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
            
def lose(self):
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
        self.win_msg = ttk.Label(self.frame3, text = "Completaste todas las casillas correctamente y ganaste el juego.", font = "Arial 16", background = "#f1f1f1")
        self.win_msg.grid(column = 1, row = 2)
        self.img = ImageTk.PhotoImage(Image.open("yippe.gif"))
        self.panel = ttk.Label(self.frame3, image = self.img, background = "#f1f1f1")
        self.panel.grid(column = 1, row = 4)
             
