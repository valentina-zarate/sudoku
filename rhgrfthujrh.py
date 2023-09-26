'''        for a in self.solucion:
            for b in a:
                for c in self.tabla:
                    for d in c:
                        if b != d:
                            self.tabla[col][fila].config(background="red")
                        else:
                            self.tabla[col][fila].config(background="green")'''
'''     self.frame2 = tk.Frame(self.interface)
        self.frame2.pack(fill = "both", expand = True)'''
        
#functools partial, enviando a la función comprobar i y j (columna y fila) como para la función test_button