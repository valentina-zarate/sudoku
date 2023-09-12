import tkinter

vent = tkinter.Tk()
tabla = []
for i in range(9):
    lista = []
    for j in range(9):
        btn = tkinter.Button(vent,height=2,width=2, text=)
        btn.grid(column=j, row=i)
        lista.append(btn)
    tabla.append(lista)
vent.mainloop()