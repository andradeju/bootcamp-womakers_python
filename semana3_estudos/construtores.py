#Construtor padrão
class MinhaClasse1:
  def __init__(self):
    print('MinhaClasse1: Chamou o construtor padrão')

#Construtor implícito - o interpretador python cria o construtor padrão por debaixo dos panos
class MinhaClasse2:
  pass #não faz nada

#construtor parametrizado
class MinhaClasse3:
  def __init__(self, param):
    print(f'MinhaClasse3: Chamou o construtor parametrizado com o parâmetro {param}')

objeto1 = MinhaClasse1()
objeto2 = MinhaClasse2()
objeto3 = MinhaClasse3('juca')    

