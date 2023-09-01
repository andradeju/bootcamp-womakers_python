""" def cardapio():
  comida = 'hamburguer'
  print(comida) """

bebida = 'refrigerante'
def cardapio():
  global bebida
  comida = 'hamburguer'
  bebida = 'suco'
  print('comida:', comida)
  print('bebida:', bebida)

cardapio()
print('bebida:', bebida)
