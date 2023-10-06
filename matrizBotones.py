import tkinter
from tkinter import ttk

vent = tkinter.Tk()
tabla = []
for i in range(9):
    lista = []
    for j in range(9):
        btn = ttk.Entry(vent, width=2, text="")
        btn.grid(column=j, row=i)
        lista.append(btn)
    tabla.append(lista)
vent.mainloop()