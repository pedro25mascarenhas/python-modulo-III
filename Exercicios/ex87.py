# Aprimore o desafio anterior mostrando no final:

#A) A soma de todos os valores pares digitados.
#B) A soma dos valores da terceira coluna.
#C) O maior valor da segunda linha. 

soma_pares = 0
soma_terceira_coluna = 0
maior_valor_segunda_linha = 'Não existe'
matriz = list()

for c in range(3):
  
  numeros = list(map(int, input(f'Digite a {c+1} linha: ').split()))
  matriz.append(numeros[:])
  soma_terceira_coluna += numeros[2]
  if c == 1:
    maior_valor_segunda_linha = max(numeros)

for l in matriz:
  print(l)
  for n in l:
    if n % 2 == 0:
      soma_pares += n

print(soma_pares)
print(soma_terceira_coluna)
print(maior_valor_segunda_linha)