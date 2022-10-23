lista = []
p_maior = []
p_menor = []
for p in range(0,5):
    n = int(input(f'Digite o {p+1}º valor: '))
    lista.append(n)
    if p == 0:
        maior = n
        menor = n
    if n >= maior:
        maior = n
        p_maior.append(p)
    elif n <= menor:
        menor = n
        p_menor.append(p)

print(f'Maior: {maior} Posição: {p_maior}\nMenor: {menor} Posição: {p_menor}')