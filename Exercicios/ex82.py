lista_geral = []
lista_par = []
lista_impar = []
while True: 
  n = int(input(f'Digite um número: '))
  lista_geral.append(n)
  if n%2 == 0:
    lista_par.append(n)
  else:
    lista_impar.append(n)
  continuar = input('Quer continuar S/N?').strip().upper()
  if continuar[0] == 'N':
    break

lista_geral.sort()
lista_par.sort()
lista_impar.sort()

print(f'Lista geral: {lista_geral}')
print(f'Lista par: {lista_par}')
print(f'Lista ímpar: {lista_impar}')
