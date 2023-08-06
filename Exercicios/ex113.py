def leiaInt(string):

    while True:
        try:
            n = int(input(string))
            break
        except ValueError:
            print("ERRO! por favor, digite um número inteiro válido: ")

    print(f"Você acabou de digitar o número {n}")

def leiaFloat(string):

    while True:
        try:
            n = float(input(string))
            break
        except ValueError:
            print("ERRO! por favor, digite um número real válido: ")

    print(f"Você acabou de digitar o número {n}")


leiaInt('Digite um número inteiro: ')
leiaFloat('Digite um número real: ')