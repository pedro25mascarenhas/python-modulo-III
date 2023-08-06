def leiaInt(n):
    if type(n) is int:
        return f"Você acabou de digitar o número {n}"
    else:
        return "ERRO! Digite um número inteiro válido"

print(leiaInt('0'))