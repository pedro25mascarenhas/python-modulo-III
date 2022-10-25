pessoas_cadastradas = list()
pessoas_mais_pesadas = list()
pessoas_mais_leves = list()

pessoa = list()

peso_pessoa_pesada = 0
peso_pessoa_leve = 1000000

while True:
  pessoa.append(input('Nome: '))
  pessoa.append(float(input('Peso: ')))

  quer_continuar = input('Quer continuar S/N? ').upper()

  if pessoa[1] > peso_pessoa_pesada:
    pessoas_mais_pesadas.clear()
    peso_pessoa_pesada = pessoa[1]
    pessoas_mais_pesadas.append(pessoa[0])
  elif pessoa[1] == peso_pessoa_pesada:
    pessoas_mais_pesadas.append(pessoa[0])

  if pessoa[1] < peso_pessoa_leve:
    pessoas_mais_leves.clear()
    peso_pessoa_leve = pessoa[1]
    pessoas_mais_leves.append(pessoa[0])
  elif pessoa[1] == peso_pessoa_leve:
    pessoas_mais_leves.append(pessoa[0])
    
  if quer_continuar[0] == 'N':
    break
  pessoas_cadastradas.append(pessoa[:])
  
  pessoa.clear()

quantidade_pessoas_cadastradas = len(pessoas_cadastradas)
print(f'Ao todo você cadastrou {quantidade_pessoas_cadastradas} pessoas.' )


print(f'O maior peso foi de {peso_pessoa_pesada}kg. Peso de {pessoas_mais_pesadas}')
print(f'O maior peso foi de {peso_pessoa_leve}kg. Peso de {pessoas_mais_leves}')