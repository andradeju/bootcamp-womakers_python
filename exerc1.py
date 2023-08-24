#1-peça um numero e então mostre a msg: O nº informado foi ...
numero = int (input('Digite um número inteiro qualquer: '))
print(f'O número informado foi {numero}')

#2-peça 2 numeros e imprima a soma
num1 = int (input('Digite o primeiro número: '))
num2 = int (input('Digite o segundo número: '))
soma = num1 + num2
print(f'A soma dos números digitados é {soma}')

#3-Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
tempEmCelsius = int (input('Digite a temperatura em Celsius: '))
conversao = tempEmCelsius * 1.8 + 32
print(f'A temperatura {tempEmCelsius}º convertida para Fahrenheit é {conversao}')


#4-Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
#Calcule e mostre o total do seu salário no referido mês.
valorHr = float(input('Digite quanto você ganha por hora: '))
horaMes = float(input('Digite o número de horas trabalhadas no mês: '))
calculoSal = valorHr * horaMes
print(f'De acordo com os dados o seu salário no mês é {calculoSal} ')