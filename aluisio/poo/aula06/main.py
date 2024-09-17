from abc import ABC, abstractmethod

class Veiculo(ABC):
    def __init__(self, rodas, capacidade, nome):
        self.rodas = rodas
        self.capacidade = capacidade
        self.nome = nome
    
    @abstractmethod
    def ligarMotor(self):
        pass
        return (f'O {self.nome} teve o motor ligado')
    
    @abstractmethod
    def mover(self):
        pass
        return (f'O {self.nome} se moveu por 30km')

    @abstractmethod
    def desligarMotor(self):
        pass
        return (f'O {self.nome} parou e foi desligado')

class Moto(Veiculo):
    def ligarMotor(self):
        return super().ligarMotor()
   
    def mover(self):
        return super().mover()

    def desligarMotor(self):
        return super().desligarMotor()

class Onibus(Veiculo):
    def ligarMotor(self):
        return super().ligarMotor()
   
    def mover(self):
        return super().mover()

    def desligarMotor(self):
        return super().desligarMotor()

class Carro(Veiculo):
    def ligarMotor(self):
        return super().ligarMotor()
   
    def mover(self):
        return super().mover()

    def desligarMotor(self):
        return super().desligarMotor()
    
    
m = Moto(2, "2 pessoas","shineray")
o = Onibus(6,"32 pessoas", "scania")
c = Carro(4,"3 pessoas","civic type r")
print(m.ligarMotor())
print(m.mover())
print(m.desligarMotor() )

print(o.ligarMotor())
print(o.mover())
print(o.desligarMotor())

print(c.ligarMotor())
print(c.mover())
print(c.desligarMotor())

