data_list = []

soma_idades = 0

mulheres_cadastradas = []

while True:
    data_dict = {

        'nome': input('Nome: '),
        'sexo': (input('Sexo: [M/F] ').upper())[0],
        'idade': int(input('Idade: ')),
    }
    soma_idades += data_dict['idade']

    data_list.append(data_dict)

    if data_dict['sexo'] == 'F':
        mulheres_cadastradas.append(data_dict['nome'])
    if input('Quer continuar? (S/N) ').upper() == 'N':
        break

print('=-' * 20)

qnt_pessoas = len(data_list)
media_idades = soma_idades/qnt_pessoas


print(f'- O grupo tem {qnt_pessoas} pessoas')
print(f'- A média de idade é de {media_idades}')
print(f'- As mulheres cadastradas foram: {mulheres_cadastradas}')
print('- Lista das pessoas que estão acima da média: ')
print('')

for dicionario in data_list:
    if dicionario['idade'] > media_idades:
        print(f"nome = {dicionario['nome']}; sexo = {dicionario['sexo']}; idade = {dicionario['idade']}")
        print('')
