from tkinter import *    

def command(d):
   print(d)

a = Tk()
b = []

for c in range(0, 5):
    x = Button(a, text=c, command=lambda j=c: command(j))
    x.pack()
    b.append(x)

a.mainloop()