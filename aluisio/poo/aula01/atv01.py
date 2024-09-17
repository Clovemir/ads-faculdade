class Produto:
    def __init__(self, nome, preco, qtd_estoque):
        self.nome = nome
        self.preco = preco
        self.qtd_prod = qtd_estoque
    def adicionar(self):
        self.qtd_estoque = self.qtd_estoque + 1
        print(f"O produto{self.nome} Foi adicionado")
        
    def remover(self):
        self.qtd_estoque = self.qtd_estoque - 1
        print(f"O produto{self.nome} Foi removido")
        
    def calcular (self):
        return self.qtd_estoque * self.preco
        
produto1 = Produto("cafe", 3, 2)
produto2 = Produto("leite", 4, 1)
produto3 = Produto("sal", 2, 5)

produto1.calcular()
produto2.calcular()
produto3.calcular()