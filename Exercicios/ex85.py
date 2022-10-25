## Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente. ##

lista_numeros = [[], []]

for c in range(7):
  numero = int(input(f'Digite o {c+1} valor: '))
  if numero % 2 == 0:
    lista_numeros[0].append(numero)
  else:
    lista_numeros[1].append(numero)

print(f'Os valores pares digitados foram: {lista_numeros[0]}')
print(f'Os valores ímpares digitados foram: {lista_numeros[1]}')