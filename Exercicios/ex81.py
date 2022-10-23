cinco = 'Essa lista não tem o número 5'
lista = []
while True:
  n = int(input('Digite um número: '))
  continuar = input('Quer continuar? ').upper()
  lista.append(n)
  if n == 5:
    cinco = 'Essa lista tem o número 5'
  if continuar[0] != 'S':
    break
lista.sort(reverse=True)
print(lista)
print(cinco)
print(f'Você digitou {len(lista)} valores')
