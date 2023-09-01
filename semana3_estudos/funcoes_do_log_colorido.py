import colorama

colorama.init()

nome_de_usuario = 'Juca'

def imprimir_no_log(texto, nivel='info'):
  if nivel.lower() == 'info':
    print(colorama.Fore.LIGHTBLUE_EX + f'Info: ', end='')
    print(colorama.Style.RESET_ALL + texto)
  elif nivel.lower() == 'aviso':
    print(colorama.Fore.YELLOW + f'Aviso: ', end='')
    print(colorama.Style.RESET_ALL + texto)
  elif nivel.lower() == 'erro':
    print(colorama.Fore.RED + f'Erro: ', end='')
    print(colorama.Style.RESET_ALL + texto)
  else:
    print(colorama.Fore.RED + 'Erro interno - nível desconhecido de mensagem' + colorama.Style.RESET_ALL)      