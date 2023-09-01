#while enquanto a condição for verdadeira, esta condição será executada
numero = -1
while numero < 0:
  numero = int(input('Você precisa digitar um numero positivo: '))

print("Número positivo inserido com sucesso")

#for uva in fruts: -> para cada item na lista de futas, será executada essa condição
frutas = ['uva', 'banana', 'laranja'] #declarando uma lista
for fruta in frutas:
  print(fruta)

artistas = ['Gal', 'Marilia Mendonça', 'Luedji Luna', 'Rachel Reis', 'Duda Beat']

for artista in artistas:
  print(artista)
else:
  print('Todas as artistas foram listadas')  

for i in range(0,10):
  print(i)  
else:
  print('Esses são os nº de 0 a 9')  

nomes = ['Juca', 'Nath']

for nome in nomes:
  print('Olá, ' + nome)


l = [1, 2, 3, 4, 5]  
for n in l:
  print(5 + n)