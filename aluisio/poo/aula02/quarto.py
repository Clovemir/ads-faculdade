class Quarto:
    def __init__(self, numero, preco_por_noite):
        self.numero = numero
        self.preco_por_noite = preco_por_noite
        self.reservado = False
    
    def reservar(self):
        if not self.reservado:
            self.reservado = True
            print(f"O quarto {self.numero} foi reservado.")
        else:
            print(f"O quarto {self.numero} já está reservado.")
    
    def liberar(self):
        if self.reservado:
            self.reservado = False
            print(f"O quarto {self.numero} foi liberado.")
        else:
            print(f"O quarto {self.numero} já está disponível.")
    
    def __str__(self):
        status = "Reservado" if self.reservado else "Disponível"
        return f"Quarto Número: {self.numero}\nPreço por Noite: R$ {self.preco_por_noite:.2f}\nStatus: {status}"

quarto1 = Quarto(101, 150.00)

quarto1.reservar()
quarto1.reservar()
quarto1.liberar()

print(quarto1)
