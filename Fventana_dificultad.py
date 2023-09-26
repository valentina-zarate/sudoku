import tkinter as tk
import requests
from tkinter import ttk

def ventana_dificultad(self):
        self.frame=tk.Frame(self.interface)
        self.frame.pack(fill="both", expand=True)
        self.frame.config(bd=24, relief="sunken", bg="#f1f1f1")
        self.text=ttk.Label(self.frame, text="Seleccione la dificultad")
        self.text.pack(padx=10, pady=60)
        self.text.config(font="Arial 20 bold", background="#f1f1f1")
        self.facil=tk.Button(self.frame, text="Fácil", height=3, width=15, command=self.easy)
        self.facil.pack(padx=10, pady=6)
        self.facil.config(font="Arial 15", background="lightgreen")
        self.medio=tk.Button(self.frame, text="Medio", height=3, width=15, command=self.medium)
        self.medio.pack(padx=10, pady=6)
        self.medio.config(font="Arial 15", background="#7feac0")
        self.dificil=tk.Button(self.frame, text="Difícil", height=3, width=15, command=self.hard)
        self.dificil.pack(padx=10, pady=6)
        self.dificil.config(font="Arial 15", background="#7ce3e2")

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