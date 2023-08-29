def soma(num1, num2): #definição da função soma
  calculo = num1 + num2
  print(f'O resultado da soma é {calculo}')

def subtracao(num1, num2):
  sub = num1 - num2
  print(f'O resultado da subtração é {sub}')

def multiplicacao(num1, num2):
  mult = num1 * num2
  print(f'O resultado da multiplicação é {mult}')  

num1 = int(input('Digite o primeiro nº '))
num2 = int(input('Digite o segundo nº '))

soma(num1, num2) #chamada da função  
subtracao(num1, num2) #chamada da função  
multiplicacao(num1, num2) #chamada de função dentro de uma função

