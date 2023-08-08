def cadastrar_pessoa(nome, idade):
    with open('pessoas_cadastradas.txt', 'r+') as arquivo:
        linhas = arquivo.readlines()
        idade = f'{idade}'
        nova_linha = f'{nome.ljust(35)}{idade.rjust(10)}\n'
        linhas.append(nova_linha)
        arquivo.writelines(nova_linha)

def ver_pessoas_cadastradas():
    with open('pessoas_cadastradas.txt', 'r') as arquivo:
        print(arquivo.read())
