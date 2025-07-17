MAIOR_IDADE = 18
IDADE_ESPECIAL = 17

idade = int(input("Informe a sua idade: "))

if idade >= MAIOR_IDADE:
    print("Pode tirar a CNH, usuário maior de idade. Dirija-se ao balcão principal!")

if idade < MAIOR_IDADE:
    print("Ainda não pode tirar a CNH. ")


if idade >= MAIOR_IDADE:
    print("Pode tirar a CNH, usuário maior de idade. Dirija-se ao balcão principal!")
elif idade >= IDADE_ESPECIAL:
    print("Você ainda não pode fazer a CNH, mas já pode assistir as aulas teóricas!")
else:
    print("Ainda não, você é menor de idade, espere até completar 18 anos")
 