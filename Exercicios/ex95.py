from prettytable import PrettyTable

data_dict = {}
data_list = []
tabela = PrettyTable()
tabela.field_names =['Cod', 'Nome', 'Gols', 'Total']
cod = 0


while True:

    print('-'*30)
    nome_jogador = input('Nome do Jogador: ')
    qnt_partidas = int(input('Quantas partidas ele jogou? '))

    lista_quantidade_gols = []

    for n in range(qnt_partidas):
        lista_quantidade_gols.append(int(input(f'Quantos gols na partida {n}? ')))
    
    data_dict['nome'] = nome_jogador
    data_dict['gols'] = lista_quantidade_gols
    data_dict['total'] = sum(lista_quantidade_gols)

    data_list.append(data_dict)

    tabela.add_row([cod, nome_jogador, lista_quantidade_gols, sum(lista_quantidade_gols)])

    cod += 1

    if input('Quer continuar? S/N ')[0].upper() == 'N':
        break

print('')
print('=-' * 21)
print(tabela)


escolher_jogador = 0
while escolher_jogador != 999:

    print('-' * 30)
    escolher_jogador = int(input('Mostrar dados de qual jogador? ')[0].upper())
    if escolher_jogador == 999:
        break

    if len(data_list) >= escolher_jogador >= 0 :
        print(f"O jogador {data_list[escolher_jogador]['nome']} jogou {data_list[escolher_jogador]['total']} partidas.")
        for idx, qnt_gols in enumerate(data_dict['gols']):
            print(f'         => Na partida {idx}, fez {qnt_gols} gols')
        print(f'Fez um total de {data_dict["total"]} gols')
        print('')
    else:
        print(f'Erro, não existe jogador com o código {escolher_jogador}')