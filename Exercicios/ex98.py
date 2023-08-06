from time import sleep

def contador(inicio, fim, passo):
    if passo == 0:
        passo = 1
    else:
        passo = abs(passo)

    while inicio < fim:
        inicio = inicio + passo
        sleep(0.2)
        print(inicio)
        
        if inicio > fim:
            print('FIM')

    while inicio > fim:
        inicio = inicio - passo
        sleep(0.2)
        print(inicio)
        if inicio < fim:
            print('FIM')

contador(10, 100, -8)
print('-'*20)
contador(100,10,10)