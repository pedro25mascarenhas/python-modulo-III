import json
def carregar_arquivo(path):

    with open(path, 'r+') as arquivo:
        dados_json = json.load(arquivo)
        print(dados_json)

if __name__ == '__main__':
    carregar_arquivo('pessoas_cadastradas.json')
