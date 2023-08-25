""" #1-Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene numa lista a média de cada aluno,imprima 
#o número de alunos com média maior ou igual a 7.0
medias_alunos = []
aluno_num = 0
for aluno_num in range(10):
  aluno_num += 1
  print(f'Notas do Aluno {aluno_num}')

  nota1 = float(input('Digite a primeira nota: '))
  nota2 = float(input('Digite a segunda nota: '))
  nota3 = float(input('Digite a terceira nota: '))
  nota4 = float(input('Digite a quarta nota: '))

  media = (nota1 + nota2 + nota3 + nota4)/4
  medias_alunos.append(media)

aprovados = 0
for media in medias_alunos:
    if media >= 7:
      aprovados +=1
      print(f'Esses são os alunos com media maior ou igual a 7: {aprovados}')



#2-Faça um programa que permita ao usuário digitar o seu nome e em seguida mostre o nome do usuário de trás para
#frente utilizando somente letras maiúsculas. Dica: lembre-se que ao informar o nome o usuário pode digitar 
#letras maiúsculas ou minúsculas.
nome = input('Digite seu nome(pode ser em maiuscula ou em minuscula: ')
print(nome.upper()[::-1]) """



#3-Escreva um programa em Python que onde todos os valores em um dicionário são emitidos. Se sim, imprima True. 
#caso contrário, imprima Falso.
#dicionario = {'Chave':'Valor'}
def verifica_dicionario():
  dicionario = {'uva':'É uma fruta', 'carro' : 'É um veículo', 'cachorro' : 'É um animal', 'boneca' : ''}
  print(dicionario)

  valores_emitidos = all(valor for valor in dicionario.values())

  if valores_emitidos:
    print("True")
  else:
    print("False")

verifica_dicionario()    






#4-Utilizando listas, faça um programa que faça 5 perguntas para uma pessoa sobre um crime. 
#As perguntas são: "Telefonou para a vítima?" "Esteve no local do crime?" "Mora perto da vítima?" "Devia 
#para a vítima?" "Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a 
#participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões, ela deve ser classificada 
#como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ela será classificada como 
#"Inocente".
""" def investigacao():
  respostas= []

  respostas.append(input('[Responda sim ou não] - Telefonou para a vítima? ').lower())
  respostas.append(input('[Responda sim ou não] - Esteve no local do crime? ').lower())
  respostas.append(input('[Responda sim ou não] - Mora perto da vítima? ').lower())
  respostas.append(input('[Responda sim ou não] - Devia para a vítima? ').lower())
  respostas.append(input('[Responda sim ou não] - Já trabalhou com a vítima? ').lower())

  respostas_positivas = respostas.count("sim")

  if respostas_positivas == 2:
    print("Suspeita")
  elif 3 <= respostas_positivas <= 4:
    print("Cúmplice")  
  elif respostas_positivas == 5:
    print("Assassino!")
  else:
    print("Inocente")    

investigacao()
 """