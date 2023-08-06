from Exercicios.utilidadescev.modulos import moeda

p = 500.0

print(f'A metade de {p} é {moeda.metade(p)}')
print(f'O dobro de {p} é {moeda.dobro(p)}')
print(f'Aumentando 10%: {moeda.aumentar(p, 10)}')
print(f'Reduzindo 13%: {moeda.diminuir(p, 13)}')
