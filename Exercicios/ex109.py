from Exercicios.utilidadescev.modulos import moeda

p = 500.5

print(f'A metade de {moeda.formatar(p)} é {moeda.metade(p, True)}')
print(f'O dobro de {moeda.formatar(p)} é {moeda.dobro(p, True)}')
print(f'Aumentando 10%: {moeda.aumentar(p, 10, True)}')
print(f'Reduzindo 13%: {moeda.diminuir(p, 13, True)}')