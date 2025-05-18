salario = float(input("Informe o salário: "))


#IF/ELIF/ELSE em Python
if salario <= 3000:
    print("programador junior")
#AND Adciona mais uma condição     
elif salario > 3000 and salario <= 6000:
    print("programador pleno")
elif salario > 6000 and salario <= 15000:        
    print("programador senior")
else:
    print("gerente de projetos")    