# O banco Banco Delas é um banco moderno e eficiente, com vantagens exclusivas para clientes mulheres. Modele um sistema orientado a objetos 
# para representar contas correntes do Banco Delas seguindo os requisitos abaixo. Cada conta corrente pode ter um ou mais clientes como titular. 
# O banco controla apenas o nome, o telefone e a renda mensal de cada cliente. A conta corrente apresenta um saldo e uma lista de operações de 
# saques e depósitos. Quando a cliente fizer um saque, diminuiremos o saldo da conta corrente. Quando ela fizer um depósito, aumentaremos o saldo. 
# Clientes mulheres possuem em suas contas um cheque especial de valor igual à sua renda mensal, ou seja, elas podem sacar valores que deixam a sua  
# conta com valor negativo até renda_mensal. Clientes homens por enquanto não têm direito a cheque especial.Para modelar seu sistema, utilize 
# obrigatoriamente os conceitos "classe", "herança", "propriedades", "encapsulamento" e "classe abstrata.

from abc import ABC, abstractmethod

class Cliente(ABC):
    def __init__(self, nome, telefone, renda_mensal):
      self._primeiro_nome = nome.split(" ")[0]
      self._ultimo_nome = nome.split(" ")[-1]
      self._telefone = telefone
      self.__renda_mensal = renda_mensal

    @property
    def nome(self):
        return self._primeiro_nome + " " + self._ultimo_nome

    @nome.setter
    def nome(self, novo_primeiro_nome, novo_ultimo_nome):
        if type(novo_primeiro_nome) != str or type(novo_ultimo_nome) != str:
          raise TypeError('Tipo da variável deve ser str')
        self._primeiro_nome = novo_primeiro_nome  
        self._ultimo_nome = novo_ultimo_nome

    @property
    def telefone(self):
        return self.telefone

    @telefone.setter
    def telefone(self, novo_tel):
        if type(novo_tel) != str:
          raise TypeError('Tipo de ')
        self._telefone = novo_tel   

    @property
    def renda_mensal(self):
        return self.__renda_mensal 

    @abstractmethod
    def tem_cheque_especial(self):
        pass

class ClienteMulher(Cliente):
    def __init__(self, nome, telefone, renda_mensal):
        super().__init__(nome, telefone, renda_mensal)

    def tem_cheque_especial(self):
        return True

class ClienteHomem(Cliente):
    def __init__(self, nome, telefone, renda_mensal):
        super().__init__(nome, telefone, renda_mensal)  

    def tem_cheque_especial(self):
        return False           


class ContaCorrente:
    def __init__(self, titular):
      self.__saldo = 0.0
      self.__operacoes = []
      self.__titulares = []
      self.adicionar_titular(titular)

    def adicionar_titular(self, titular):
      self.__titulares.append(titular)  

    def depositar(self, valor: float):
      self.__saldo += valor
      self.__operacoes.append(f'Depósito de R$ {valor:.2f}')

    def sacar(self, valor: float):
      titular = self.__titulares[0]
      if titular.tem_cheque_especial() == False:
          if valor <= self.__saldo:
            self.__saldo -= valor
            self.__operacoes.append(f'Saque de R$ {valor:.2f}')
          else:
            raise ValueError('Saldo Insuficiente')
      else:
        if valor <= self.__saldo or (self.__saldo - valor) >= - titular.renda_mensal:          
          self.__saldo -= valor
          self.__operacoes.append(f'Saque de R$ {valor:.2f}')
        else:
            raise ValueError('Saldo Insuficiente')

    @property
    def saldo(self):
        return self.__saldo  
    
    @property
    def operacoes(self):
        return self.__operacoes       

cliente_homem = ClienteHomem('Juca Westie', '21123456', 15000)
cliente_mulher = ClienteMulher('Lady Gaga', '21123456', 1356) 

conta1 = ContaCorrente(cliente_mulher)
conta2 = ContaCorrente(cliente_homem)

#ver o saldo da conta
print(conta1.saldo)
print(conta2.saldo)
print()

#fazendo deposito
conta1.depositar(5000)
conta2.depositar(500)

print(conta1.saldo)
print(conta2.saldo)

#fazendo saque
conta1.sacar(100)
conta2.sacar(70)

print(conta1.operacoes)
print()
print(conta2.operacoes)
