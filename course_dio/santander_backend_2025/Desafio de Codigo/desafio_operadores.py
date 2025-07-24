# Entrada do usuário
email = input().strip()

# Verifica as regras do e-mail
if " " in email:
    print("E-mail inválido")
elif email.startswith("@") or email.endswith("@"):
    print("E-mail inválido")
elif "@" not in email:
    print("E-mail inválido")
else:
    print("E-mail válido")