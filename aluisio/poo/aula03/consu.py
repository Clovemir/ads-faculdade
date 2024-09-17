class Paciente:
    def __init__ (self, nome, idade, doencas, consultas):
        self.nome = nome 
        self.idade = idade
        self.doencas = doencas
        self.consultas = consultas
        
    def adicionar_consultas(self, consulta):
        self.consultas.append(consulta)
        
    def __str__(self):
        doencas_str = ', '.join(self.doencas)
        consultas_str = '\n' .join(self.doencas)
        return (f"Nome: {self.nome}\n"
                f"idade:  {self.idade}\n"
                f"Doencas:  {doencas_str}\n"
                f"Histórico de consultas:  {consultas_str}")

class SistemaDeGerenciamento:
    def __init__(self):
        self.pacientes = []
    
    def adicionar_pacientes(self,paciente):
        self.pacientes.append(paciente)
        
    def exibir_pacientes(self):
        for paciente in self.pacientes:
            print(paciente)
            print('-------')
            
#função principal
def main():
    sistema = SistemaDeGerenciamento()

    #cria a condição para a exibição dos menus
    while True:
        print('1. Adicionar Paciente')
        print('2. Exibir Pacientes')
        print('3. sair')
        opcao = input('Escolha uma opção...')

        if opcao == '1':
            nome = input('Informe o nome do paciente: ')
            idade = int(input('Informe a idade do paciente: '))
            doencas = input('Informe as doenças do paciente (separadas por vírgula): ').split(',')
            doencas = [doencas.strip() for doencas in doencas]
            consultas = []

            paciente = Paciente(nome,idade,doencas,consultas)
            sistema.adicionar_pacientes(paciente)
            print('Paciente Adicionado com sucesso')
            print('---------------------------------------')
        
        elif opcao == '2':
            sistema.exibir_pacientes()
        
        elif opcao == '3':
            print('Saindo...')
            break
            
        else:
            print('Opção inválida. \n Tente novamente...')
            
if __name__ == "__main__":
    main()
            
            
            
            
            
            
            
            
            
            
            
            

        