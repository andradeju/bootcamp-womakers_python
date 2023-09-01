def multiplicacao():
  mult = 20 * 2
  file = 'arquivo.txt'

#open
  arquivo_escrita = open(file, 'w') #open p/ escrita
  arquivo_escrita.write(f'O resultado da multiplicação é {mult}') 
  arquivo_escrita.close()

  arquivo_leitura = open(file, 'r') #open somente p/ leitura
  leitura = arquivo_leitura.read()
  print(leitura)
  arquivo_leitura.close()

#escrita
#leitura

multiplicacao()  
