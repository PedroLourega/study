"""
Faça um programa que pergunte a gora ao usuário e, baseando-se no horário descrito, exiba a saudação apropriada. Ex:
Bom dia 0 - 11, boa tarde - 12-17 boa noite 18-23
"""

# entrada = input('Digite um horário (0 a 23 | em horas):')

# try:
#     horario = int(entrada)
#     if 0 <= horario <= 11:
#         print('Bom dia!')
#     elif 12 <= horario <= 17:
#         print('Boa tarde!')
#     elif 18 <= horario <= 23:
#         print('Boa noite!!')
#     else:
#         print('Horário inválido! Digite um número entre 0 a 23.')
# except ValueError:
#     print('Entrada inválida! Digite um número inteiro.')


entrada = input('Digite a hora em números inteiros:')

try:
    hora = int(entrada)

    if hora >= 0 and hora <= 11:
        print('Bom dia!!')
    elif hora >= 12 and hora <= 17:
        print('Boa tarde!!')
    elif hora >= 18 and hora <= 23:
        print('Bom dia!')
    else:
        print('Nao conheço essa hora')
except:
    print('Digite um número inteiro!')