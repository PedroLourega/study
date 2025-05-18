#nome = input("Qual seu nome?") # função input sempre tem como resultado string, então é necessário fazer a conversão

#print(f'O seu nome é: {nome=}')

numero1 = input("Digite um número:")
numero2 = input("Digite o segundo número: ")

int_numero1 = int(numero1) # forma correta de fazer a conversão de numeros sem dar problemas no codigo
int_numero2 = int(numero2)

print(f"A soma dos numeros é: {int_numero1 + int_numero2}")