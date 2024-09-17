class Pessoa:
    def __init__(self, nome, idade):
        self._nome = nome
        self.__idade = idade
        
    def get_idade(self):
        return self.__idade
    def set_idade(self, idade):
        if idade > 0:
            self.__idade = idade
        else:
            print("Idade inválida")   
            
class Aluno(Pessoa):
    def __init__(self, nome, idade, resultado, faltas):
        super().__init__(nome,idade)
        self.resultado = resultado
        self.faltas = faltas
    def aprovado(self, faltas):
        if faltas < 6:
            print("aluno reprovado")
        else:
            print("aluno aprovado")    
        
        
pessoa1 = Aluno("Clóvis", 22, "aprovado", 12)
print(f"O Aluno {pessoa1._nome} tem: {pessoa1.get_idade()} anos, \nFoi: {pessoa1.resultado}, Tendo: {pessoa1.faltas} faltas")
pessoa1.aprovado()

