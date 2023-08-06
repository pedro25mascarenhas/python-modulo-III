data_dict = {}

nome_jogador = input('Nome do Jogador: ')
qnt_partidas = int(input('Quantas partidas ele jogou? '))

lista_quantidade_gols = []

for n in range(qnt_partidas):
    lista_quantidade_gols.append(int(input(f'Quantos gols na partida {n}? ')))

data_dict['nome'] = nome_jogador
data_dict['gols'] = lista_quantidade_gols
data_dict['total'] = sum(lista_quantidade_gols)

print('=-' * 20)
print(data_dict)
print('=-' * 20)

for k,v in data_dict.items():
    print(f'{k}: {v}.')

print('=-' * 20)

print(f'O jogador {nome_jogador} jogou {qnt_partidas} partidas.')

for idx, qnt_gols in enumerate(data_dict['gols']):
    print(f'         => Na partida {idx}, fez {qnt_gols} gols')

print(f'Fez um total de {data_dict["total"]}')