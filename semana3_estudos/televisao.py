class Televisao:
  def __init__(self):
    self.ligada = False
    self.canal = 3
    self.canal_min = 1
    self.canal_max = 99
    self.volume = 30
    self.volume_min = 0
    self.volume_max = 100

  def ligar(self):
    self.ligada = True
  
  def desligar(self):
    self.ligada = False

  def mudar_canal_para_cima(self):
    if not self.ligada:
      return    
    
    if self.canal < self.canal_max:
      self.canal += 1 

  def mudar_canal_para_baixo(self):
    if not self.ligada:
      return    

    if self.canal > self.canal_min:
      self.canal -= 1

  def aumentar_volume(self):
    if not self.ligada:
      return

    if self.volume < self.volume_max:
      self.volume += 10    

  def reduzir_volume(self):
    if not self.ligada:
      return      

    if self.volume > self.volume_min:
      self.volume -= 10

  def __str__(self) -> str:
    return f'Televisao - ligada {self.ligada} - canal {self.canal} - volume {self.volume}'

#criando instâncias das class Televisao
tv_sala = Televisao()
tv_quarto = Televisao()    


tv_sala.ligar()
print(f'tv_sala está ligada? {tv_sala.ligada}')
print(f'tv_quarto está ligada? {tv_quarto.ligada}')

#usa _ quando não usar a variável do loop 
for _ in range(3):
  tv_sala.aumentar_volume()   

print(f'tv_sala volume {tv_sala.volume}')
print(f'tv_quarto volume {tv_quarto.volume}')  
print()

print('tv_sala:', tv_sala)
print('tv_quarto:', tv_quarto)
print()

#Dia é um objeto, ou seja, uma instância da classe date
from datetime import date
dia = date(1989, 4, 23) #YYYY M D  
print('Dia da semana:', dia.weekday()) #começa do zero na segunda


