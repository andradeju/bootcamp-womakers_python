#1-Faça um programa, com uma função que necesseite de três argumentos, e que forneça a soma desses três 
#argumentos.

def soma(num1, num2, num3):
  calculo = num1 + num2 + num3
  print(f'O resultado dos números digitados é {calculo}')

num1 = int(input('Digite o primeiro nº: '))
num2 = int(input('Digite o primeiro nº: '))
num3 = int(input('Digite o primeiro nº: '))
soma(num1, num2, num3)

#2-Reverso do número. Faça uma função que retorne o reverso de um número inteiro informado. Por exemplo: 127 > 721
def reverso(numero):
    numero_str = str(numero)
    reverso_str = numero_str[::-1]
    reverso_int = int(reverso_str)
    print("O reverso do número é:", reverso_int)

numero = int(input("Informe um número inteiro: "))
reverso(numero)

#3-Escreva um script que pergunta ao usuário se ele deseja converter uma temperatura de grau Celsius para Fahrenheit 
#ou vice-versa.Para cada opção, crie uma função. Crie uma terceira, que é um menu para o usuário escolher a opção 
#desejada, onde esse menu chama a função de conversão correta.
def celsiusFahre(celsius):
  fahrenheit = celsius * 1.8 + 32
  return fahrenheit

def fahreCelsius(fahrenheit):
  celsius = (fahrenheit - 32)/ 1.8
  return celsius

def menu():
  print('Escolha uma opção')
  print('1 se deseja converte de CELSIUS para FAHRENHEIT: ')
  print('2 se deseja converte de FAHRENHEIT para CELSIUS : ')

  opcao = int(input('Digite o nº da opção escolhida: '))

  if opcao == 1:
    celsius = float(input('Digite a temperatura em graus Celsius: '))
    fahrenheit = celsiusFahre(celsius)
    print(f'[Celsius para Fahrenheit] A temperatura em Fahrenheit é {fahrenheit}°F')

  elif opcao == 2:
    fahrenheit = float(input('Digite a temperatura em graus Celsius: '))
    celsius = fahreCelsius(fahrenheit)
    print(f'[Fanrenheit para Celsius]A temperatura em Celsius é {celsius}°C')  

  else:
    print('Opção inválida')

menu()      
