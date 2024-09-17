# class Termostato:
#     def __init__(self, temp_atual, temp_desejada):
#         self.temp_atual = temp_atual
#         self.temp_desejada = temp_desejada
        
#     def ajustar(self, nova_temperatura):
#         #ajusta a temperatura
#         self.temp_atual = nova_temperatura
#         print(f'temperatura desejada ajustada para {self.temp_atual}°C')
        
#     def temp_segura(self, max=25, min=18):
#         #compara a temperatura e informa se é segura ou não
#         if (self.temp_atual < min or self.temp_atual > max):
#             print(f'A temperatura: {self.temp_atual}°C Não é segura')
#         else:
#             print(f'A temperatura: {self.temp_atual}°C è segura')
            
# temperatura1 = Termostato (30,20)

# temperatura1.temp_segura()
# temperatura1.ajustar(23)
# temperatura1.temp_segura()

#---------------------------------------------------------------------

#define o objeto e os itens dele
class Paciente:
    def __init__(self, nome, idade, doencas, consultas):
        self.nome = nome
        self.idade = idade
        self.doencas = doencas
        self.consultas = consultas

    def adicionar_consulta(self, consulta):
        self.consultas.append(consulta)
        #append adiciona itens a lista

    def __str__(self):
        doencas_str = ', '.join(self.doencas)
        consultas_str = '\n'.join(self.consultas)
        return (f"Nome: {self.nome}\n"
                f"Idade: {self.idade}\n"
                f"Doenças: {doencas_str}\n"
                f"Histórico de Consultas:\n{consultas_str}")

#cria uma lista de pacientes
class SistemaDeGerenciamento:
    def __init__(self):
        self.pacientes = []

    def adicionar_paciente(self, paciente):
        self.pacientes.append(paciente)

    def exibir_pacientes(self):
        for paciente in self.pacientes:
            print(paciente)
            print('---')

# Função principal
def main():
    sistema = SistemaDeGerenciamento()
    
    #abre um laço com condição
    while True:
        print("1. Adicionar paciente")
        print("2. Exibir pacientes")
        print("3. Sair")
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            nome = input("Nome do paciente: ")
            idade = int(input("Idade do paciente: "))
            doencas = input("Doenças do paciente (separadas por vírgula): ").split(',')
            doencas = [doencas.strip() for doencas in doencas]
            consultas = []
            
            paciente = Paciente(nome, idade, doencas, consultas)
            sistema.adicionar_paciente(paciente)
            print("Paciente adicionado com sucesso!")
            print("---------------------------------------------")
        
        elif opcao == '2':
            sistema.exibir_pacientes()
        
        elif opcao == '3':
            print("Saindo...")
            break
        
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main() 
        

    


        