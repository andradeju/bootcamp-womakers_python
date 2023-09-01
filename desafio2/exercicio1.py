#Crie uma classe que modelo o objeto "carro". Um carro tem os seguintes atributos: ligado, cor, modelo, velocidade
#Um carro tem os seguintes comportamentos: liga, desliga, acelera, desacelera.

class Carro:
  def _init_(self):
    self.ligado = False
    self.cor = "Preto"
    self.modelo = "Honda Civic"
    self.velocidade = 0
    self.velocidade_min = 10
    self.velocidade_max = 220

  def ligar(self):
    self.ligado = True

  def desligar(self):
    self.ligado = False
    self.velocidade = 0

  def acelerar(self):
    if not self.ligado:
      return   

    if self.velocidade < self.velocidade_max:
      self.velocidade += 10

  def desacelerar(self):
    if not self.ligado:
      return

    if self.velocidade > self.velocidade_min:
      self.velocidade -= 10

carro = Carro()
carro.ligar()

print(f'O carro está ligado? {carro.ligado}')
carro.acelerar()
print(f'Qual é a velocidade atual do carro? {carro.velocidade}')

for _ in range(4):
  carro.acelerar()

print(f'Qual é a velocidade do carro no momento? {carro.velocidade}')