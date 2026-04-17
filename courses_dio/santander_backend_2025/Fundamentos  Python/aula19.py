###Trabalhando com strings em python
curso1 = "    Python  "
curso2 = "Python"
curso = "pYtHon"

###Maiusculas e minusculas

#maisculas
print(curso.upper())

#minusculas
print(curso.lower())

#primeira letra maiuscula apenas
print(curso.title())

###Trabalhando com espaços em strings

#Tira espaços
print(curso1.strip())

#Tira espaços do inicio
print(curso1.lstrip())

#tira espaços do final
print(curso1.rstrip())

### Juncoes e centralizações

#...
print(curso2.center(10, "#"))

print(".".join(curso))

menu = "Python"

print("####", menu, "####")
print(menu.center(14))
print(menu.center(20, "#"))
print("-".join(menu))