#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira, e calcule quanto poderia comprar de cada moeda estrangeira. Considere a tabela de conversão abaixo:
#Dólar Americano: R$4,91
#Peso Argentino: R$0,02
#Dólar Australiano: R$3,18
#Dólar Canadense: R$3,64
#Franco Suiço: R$0,42
#Euro: R$5,36
#Libra esterlina: R$6,212.
def cambio():
  valor_carteira = float(input('Digite o valor que você tem em reais R$: '))

  for moeda, valor_moeda in moedas.items():
    valor_convertido = valor_moeda / valor_carteira
    print(f'{moeda}: {valor_convertido}')

moedas = {
  'Dolar Americano': 4.91,
  'Peso Argentino': 0.02,
  'Dólar Australiano': 3.18,
  'Dólar Canadense': 3.64,
  'Franco Suiço': 0.42,
  'Euro': 5.36,
  'Libra esterlina': 6.212
}
cambio()


#Escreva um programa que pergunte a quantidadede km percorridos por um carro alugado e a quantidadede dias pelos 
#quais ele foi alugado.#Calcule o preço a pagar,sabendo que o carro custa R$80,00 por dia e R$0,20 por km rodado.
km_percorridos = float(input('Digite a quantidade de Km percorridos: '))
dias_alugados = int(input('Digite a quantidade de dias alugado: '))

custo_km = 0.20
custo_dia = 80

preco_a_pagar = (km_percorridos * custo_km) + (dias_alugados * custo_dia)
print(f'O valor a pagar do carro é {preco_a_pagar}')


#3.Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário. Se o salário for até R$1000,00 o funcionário terá
#20% de aumento.Entre R$1001,00 até R$2800,00 o funcionário terá 10% de aumento.Acima de R$2801,00 o funcionário terá 5% de aumento.

salario_func = float(input('Digite seu salario: '))

if salario_func <= 1000:
  aumento = salario_func * 0.2
elif salario_func <= 2800:
  aumento = salario_func * 0.1
else:
  aumento = salario_func * 0.05

salario_reajustado = salario_func + aumento   
print(f'Você teve um aumento seu salário agora é: {salario_reajustado:.2f}')
