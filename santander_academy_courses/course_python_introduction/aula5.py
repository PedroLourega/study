"""
### ESTRUTURAS DE CONTROLE

# Estruturas condicionais
As estruturas condicionais nos permitem executar diferentes blocos de código segundo se cumpra ou não uma determinada condição. Em Python, as estruturas condicionais mais utilizadas são if, if-else e if-elif-else.

IF
A estrutura if é utilizada para executar um bloco de código se uma condição for verdadeira. A sintaxe básica é a seguinte:

if condicao:

   # Bloco de código a executar se a condição for verdadeira
   instruções
Exemplo:

idade = 18


if idade >= 18:
   print ("Você é maior de idade.")
Neste exemplo, se a variável idade for maior ou igual a 18, será executado o bloco de código dentro do if e será impressa a mensagem "Você é maior de idade."

"""

"""
IF-ELSE
A estrutura if-else nos permite especificar um bloco de código alternativo que será executado se a condição do if for falsa. A sintaxe básica é a seguinte:

idade = 15


if idade >= 18:
   print ("Você é maior de idade.")

else:
   print ("Você é menor de idade.")
Neste exemplo, se a variável idade for maior ou igual a 18, será executado o bloco de código dentro do if e será impressa a mensagem "Você é maior de idade." Caso contrário, será executado o bloco de código dentro do else e será impressa a mensagem "Você é menor de idade."

"""

"""
IF-ELIF-ELSE
A estrutura if-elif-else nos permite especificar múltiplas condições e blocos de código alternativos. A sintaxe básica é a seguinte:

if condicao1:

   # Bloco de código a executar se a condicao1 for verdadeira
   instruções

elif condicao2:

   # Bloco de código a executar se a condicao2 for verdadeira
   instruções

else:

   # Bloco de código a executar se nenhuma condição anterior for verdadeira
   instruções
Exemplo:

nota = 85


if nota >= 90:
   print ("Excelente")

elif nota >= 80:
   print ("Muito bom")

elif nota >= 70:
   print ("Bom")

else:
   print ("Precisa melhorar")

Neste exemplo, são avaliadas múltiplas condições em ordem. Se a variável nota for maior ou igual a 90, será impresso "Excelente". Se não se cumprir a primeira condição, mas nota for maior ou igual a 80, será impresso "Muito bom". Se não se cumprirem as condições anteriores, mas nota for maior ou igual a 70, será impresso "Bom". Se nenhuma das condições anteriores for verdadeira, será executado o bloco else e será impresso "Precisa melhorar".

"""

idade = int(input("Digite sua idade:"))

if idade < 18:
    print("Você é menor de idade!")
elif idade >= 18 and idade < 60:
    print("Você é adulto!")
elif idade > 15:
    print("Maior de 15 anos!")
elif idade == 60:
    print("Feliz 60 anos!!!!")
else:
    print("Você é um idoso")