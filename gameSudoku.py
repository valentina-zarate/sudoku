import requests
import tkinter
url1="https://sudoku-api.vercel.app/api/dosuku"
entrada=input("fácil=f\n medio=m\n dificil=d\n\nINGRESE UNA DIFICULTAD: ")
dificultad= ""
sudoku=[]
if entrada == "f":
    while dificultad != "Easy":
        resp=requests.get(url1)
        json=resp.json()
        dificultad=json["newboard"]["grids"][0]["difficulty"]
    sudoku=json["newboard"]["grids"][0]["value"]
    print(sudoku)
elif entrada == "m":
    while dificultad != "Medium":
        resp=requests.get(url1)
        json=resp.json()
        dificultad=json["newboard"]["grids"][0]["difficulty"]
    sudoku=json["newboard"]["grids"][0]["value"]
    print(sudoku)
elif entrada == "d":
    while dificultad != "Hard":
        resp=requests.get(url1)
        json=resp.json()
        dificultad=json["newboard"]["grids"][0]["difficulty"]
    sudoku=json["newboard"]["grids"][0]["value"]
    print(sudoku)
    

vent = tkinter.Tk()
tabla = []
lista = []
fila= [0,1,2,3,4,5,6,7,8]
columna= [0,1,2,3,4,5,6,7,8]
for i in fila:
    for j in columna:
        if sudoku[i][j] == 0:
            sudoku[i][j]=""
        btn = tkinter.Button(vent,height=2,width=2, text=sudoku[i][j])
        rR = i//3
        cC = j//3
        if not (rR+cC) % 2:
            btn.config(bg='lightblue')
        btn.grid(column=j, row=i)
        lista.append(btn)
    tabla.append(lista)
vent.mainloop()
    
    
