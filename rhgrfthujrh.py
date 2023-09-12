'''        for a in self.solucion:
            for b in a:
                for c in self.tabla:
                    for d in c:
                        if b == d:
                            self.tabla[col][fila].config(background="red")
                        else:
                            self.tabla[col][fila].config(background="green")'''
        
        
#functools partial, enviando a la función comprobar i y j (columna y fila) como para la función test_button