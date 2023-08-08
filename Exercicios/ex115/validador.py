def validar_opcao():
    global opcao
    opcao = 0

    while True:
        try:
            while opcao not in [1, 2, 3]:
                opcao = int(input('Sua Opção: '))
                if opcao in [1, 2, 3]:
                    return opcao
                else:
                    print("Houve um erro, escolha uma opção correta")

        except ValueError:
            print("Houve um erro, escolha uma opção correta")



def validar_idade():
    global idade
    while True:
        try:
            idade = int(input('Digite a idade: '))
            return idade
        except ValueError:
            print('Digite um numero inteiro para a idade')


