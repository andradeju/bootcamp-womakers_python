#1-Faça um Programa que peça dois números e imprima o maior deles
number1 = int(input('Digite o primeiro número: '))
number2 = int(input('Digite o primeiro número: '))

if number1 > number2:
  print(f'{number1} é o maior número')
else:
  print(f'{number2} é o maior número')  

#2-Faça um Programa que pergunte em que turno você estuda.Peça para digitar M-matutino ou V-Vespertino ou N-Noturno.
# Imprima a mensagem "Bom Dia!","Boa Tarde! "ou" Boa Noite! "ou" Valor Inválido!", conforme o caso
pergunta = input('Digite o turno que você estuda, sendo M-matutino, V-vespertino ou N-noturno: ')
pergunta = pergunta.upper()

if pergunta == "M":
  print('Bom dia!')
elif pergunta == "V":
  print('Boa tarde!')
elif pergunta == "N":
  print('Boa noite!')  
else:
  print('Valor Inválido!')

#3.Faça um programa que peça uma nota, entre zero e dez.Mostre uma mensagem caso o valor seja inválido e continue
#pedindo até que o usuário informe um valor válido.
nota = 0
while nota < 0 or nota > 10:
  nota = int (input('Digite uma nota entre zero e dez: '))

print(f'Boa! A nota digitada foi {nota}')


