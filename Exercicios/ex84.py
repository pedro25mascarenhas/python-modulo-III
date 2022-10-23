from operator import itemgetter

nome_peso = list()
lista_pessoas = list()
while True:
  nome_peso = input().split()
  lista_pessoas.append(nome_peso[:])
  continuar = input('Quer continuar S/N? ').strip().upper()
  if continuar == 'N':
    break
print('\n')

print(f'A) Pessoas cadastradas: {len(lista_pessoas)}')
lista_pessoas.sort(key=itemgetter(1), reverse=True)

print('B) Mais pesados: ', end='')
for c in range(len(lista_pessoas)//2):
  if c == len(lista_pessoas)//2:
    print(f'{lista_pessoas[c][0]} com {lista_pessoas[c][1]}kg')
  else:
    print(f'{lista_pessoas[c][0]} com {lista_pessoas[c][1]}kg', end=' | ')


lista_pessoas.sort(key=itemgetter(1), reverse=False)

print('C) Mais leves: ', end='')
for c in range(len(lista_pessoas)//2):
  print(f'{lista_pessoas[c][0]} com {lista_pessoas[c][1]}kg', end=' | ')


