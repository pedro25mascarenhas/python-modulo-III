from random import randint

def somar_aleatorio(qnt):
    
    numeros = [randint(1, 10) for _ in range(qnt)]
    soma_pares = sum([num for num in numeros if num % 2 == 0])
    print(numeros)
    print(soma_pares)

somar_aleatorio(100)