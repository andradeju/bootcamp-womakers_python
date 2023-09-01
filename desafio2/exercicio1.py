#Crie uma classe que modelo o objeto "carro". Um carro tem os seguintes atributos: ligado, cor, modelo, velocidade
#Um carro tem os seguintes comportamentos: liga, desliga, acelera, desacelera.

class Carro:
  def __init__(self, cor, modelo):
    self.cor = cor
    self.modelo = modelo
    self.ligado = False
    self.velocidade = 0
    self.velocidade_max = 220

  def ligar(self):
    self.ligado = True

  def desligar(self):
    self.ligado = False
    self.velocidade = 0

  def acelerar(self):
    if self.ligado == False:
      return   

    if self.velocidade < self.velocidade_max:
      self.velocidade += 10

  def desacelerar(self):
    if self.ligado == False:
      return

    if self.velocidade > 0:
      self.velocidade -= 10

  def __str__(self):
    ligado_str = 'ligado' if self.ligado == True else 'desligado'
    return f'Carro {self.cor} modelo {self.modelo} à velocidade {self.velocidade}'    

carro = Carro('preto', 'Honda Civic')
print(carro)

carro.ligar()

print(f'O carro está ligado? {carro.ligado}')

carro.acelerar()
print(f'Qual é a velocidade atual do carro? {carro.velocidade}')

for _ in range(4):
  carro.acelerar()

print(f'Qual é a velocidade do carro no momento? {carro.velocidade}')

carro.desligar()