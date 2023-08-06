# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
# Guarde esses resultados em um dicionário. No final, coloque esse dicionário em ordem, sabendo
# que o vencedor tirou o maior numero no dado

from random import randint

dicionario_resultados = {}

for c in range(10):
    dicionario_resultados[f'Jogador_{c+1}'] = randint(1, 6)

dicionario_resultados = dict(
    sorted(dicionario_resultados.items(), key=lambda item: item[1]))

for k, v in dicionario_resultados.items():
    print(k, v)
