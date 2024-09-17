class Caneta:
    def __init__(self, cor, marca, tipo):
        self.cor = cor
        self.marca = marca
        self.tipo = tipo
    
    def escrever(self):
        print(f"a caneta de cor {self.cor} escreveu ")
        
    def __str__(self):
        return(f"{self.cor} - {self.marca} - {self.tipo}")
    

caneta1 = Caneta ("azul", "BIC", "Esfergráfica")
caneta2 = Caneta ("Vermelha", "Compactor", "Esferográfica")

caneta1.escrever()
caneta2.escrever()

print(caneta1)
print(caneta2)
