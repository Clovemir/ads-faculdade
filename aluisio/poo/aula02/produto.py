class Produto:
    def __init__(self, nome, preco, quantidade_estoque):
        self.nome = nome
        self.preco = preco
        self.quantidade_estoque = quantidade_estoque
    
    def adicionar_estoque(self, quantidade):
        self.quantidade_estoque += quantidade
        print(f"{quantidade} unidades adicionadas ao estoque. Estoque atual: {self.quantidade_estoque}")
    
    def remover_estoque(self, quantidade):
        if quantidade <= self.quantidade_estoque:
            self.quantidade_estoque -= quantidade
            print(f"{quantidade} unidades removidas do estoque. Estoque atual: {self.quantidade_estoque}")
        else:
            print(f"Quantidade insuficiente em estoque para remover {quantidade} unidades.")
    
    def valor_total_estoque(self):
        return self.preco * self.quantidade_estoque
    
    def __str__(self):
        return (f"Produto: {self.nome}\n"
                f"Preço: R$ {self.preco:.2f}\n"
                f"Quantidade em Estoque: {self.quantidade_estoque}\n"
                f"Valor Total em Estoque: R$ {self.valor_total_estoque():.2f}")
    

produto1 = Produto("Camiseta", 50.00, 100)
produto2 = Produto("Calça", 80.00, 50)

produto1.adicionar_estoque(20)
produto1.remover_estoque(50)

print(produto1)
