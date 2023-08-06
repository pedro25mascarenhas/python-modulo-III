import json

def cadastrar_pessoa(nome, idade):
    with open('pessoas_cadastradas.json', 'w+') as arquivo:
        try:
            data = json.load(arquivo)
        except json.decoder.JSONDecodeError:
            data = {'lista': []}
        data['lista'].append([nome,idade])

        json.dump(data['lista'], arquivo, ensure_ascii=False)

def menu():
    while True:
        show_menu()

        opcao = 0
        while opcao not in [1,2,3]:
            opcao = int(input('Sua Opção: '))
            if opcao not in [1,2,3]:
                print("Houve um erro, escolha uma opção correta")

        if opcao == 2:
            nome = input('Digite o nome: ').capitalize()

            while True:
                try:
                    idade = int(input('Digite a idade: '))
                    break
                except ValueError:
                    print('Digite um numero inteiro para a idade')
            cadastrar_pessoa(nome,idade)

        if opcao == 3:
            print('Você saiu do sistema.')
            quit()

        if opcao == 1:
            ver_pessoas_cadastradas()

def show_menu():
    print('MENU PRINCIPAL')
    print('1 - Ver pessoas cadastradas')
    print('2 - Cadastrar nova pessoa')
    print('3 - Sair do sistema')
    print('-'*30)

def ver_pessoas_cadastradas():
    with open('pessoas_cadastradas.json', 'r') as arquivo:
        data = json.load(arquivo)
        print(data)

if __name__ == '__main__':
    cadastrar_pessoa('pedro', 20)


