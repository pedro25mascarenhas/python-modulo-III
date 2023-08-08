import cadastro
import validador
def iniciar():
    while True:
        show_menu()
        opcao = validador.validar_opcao()
        if opcao == 2:
            nome = input('Digite o nome: ').capitalize()
            idade = validador.validar_idade()
            cadastro.cadastrar_pessoa(nome,idade)

        if opcao == 3:
            print('Você saiu do sistema.')
            quit()

        if opcao == 1:
            cadastro.ver_pessoas_cadastradas()

def show_menu():
    print('MENU PRINCIPAL')
    print('1 - Ver pessoas cadastradas')
    print('2 - Cadastrar nova pessoa')
    print('3 - Sair do sistema')
    print('-'*30)

if __name__ == '__main__':
    menu()
