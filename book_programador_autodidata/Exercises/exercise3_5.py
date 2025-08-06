Crianca = "Você ainda é criança!"
Jovem = "Você não é mais criança, mas ainda NÃO é um adulto."
Adulto = "Você é um adulto!"
Velho = "Você é velho"

age = int(input("Digite sua idade: "))

if age < 13:
    print(Crianca)
elif age >= 14 and age < 18:
    print(Jovem)
elif age >= 18 and age < 60:
    print(Adulto)
else:
    print(Velho)