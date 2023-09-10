#o programa abaixo deve calcular a média dos valores digitados
#pelo usuário. No entanto, ele não está funcionando corretamente. Você pode conserta-lo 

def calcular_media(valores):
    tamanho = 0
    soma = 0.0
    for _, valor in enumerate(valores):
        soma += valor
        tamanho += 1
    media = soma / tamanho
    return media
    
continuar = True
valores = []
while continuar:
    valor = input('Digite um número para calcular a sua média ou "ok" para calcular o valor: ')
    if valor.lower() == 'ok':
        continuar = False 
    else:
        valores.append(float(valor))
media = calcular_media(valores)
print(f'A média calculada para os valores {valores} foi de {media}')        