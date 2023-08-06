# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário
# No final, mostre o conteúdo da estrutura na tela

data_dict = {}

data_dict['Nome'] = input('Digite o nome: ')
data_dict['Média'] = float(input('Digite a média: '))
data_dict['Situação'] = 'Aprovado' if 10 >= data_dict['Média'] >= 7 else 'Reprovado'

for k, v in data_dict.items():
    print(f'{k}: {v}')
