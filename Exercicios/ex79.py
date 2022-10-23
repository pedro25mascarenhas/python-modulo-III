lista = []
while True:
    valor = int(input('Digite um valor: '))
    if valor not in lista:
        lista.append(valor)
    continuar = input('Quer continuar S/N? ').upper()
    if continuar == 'N':
        break
lista.sort()
print(lista)