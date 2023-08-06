
import datetime

ano_atual = datetime.datetime.now().year

data_dict = {}

data_dict['nome'] = input('Nome: ')

data_dict['idade'] = ano_atual - int(input('Ano de Nascimento: '))

data_dict['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))

if data_dict['ctps'] > 0:

    data_dict['contratacao'] = int(input('Ano de contratação: '))

    data_dict['salario'] = float(input('Salário: R$ '))

    idade_aposentadoria = 35 - (ano_atual - data_dict['contratacao']) + data_dict['idade']
    data_dict['aposentadoria'] = idade_aposentadoria

# data_dict['aposentadoria'] = 
print('-=' * 20)

print(data_dict)

for k,v in data_dict.items():
    print(f'{k}: {v}')
