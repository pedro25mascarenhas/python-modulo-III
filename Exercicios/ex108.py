from Exercicios.utilidadescev.modulos import moeda

p = 500.5

print(f'A metade de {moeda.formatar(p)} é {moeda.formatar(moeda.metade(p))}')
print(f'O dobro de {moeda.formatar(p)} é {moeda.formatar(moeda.dobro(p))}')
print(f'Aumentando 10%: {moeda.formatar(moeda.aumentar(p, 10))}')
print(f'Reduzindo 13%: {moeda.formatar(moeda.diminuir(p, 13))}')