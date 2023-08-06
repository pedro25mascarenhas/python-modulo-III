def maior(*tupla_numeros):
    maior_numero = None

    print('Analisando Valores')
    for numero in tupla_numeros:
        if maior_numero is None or numero > maior_numero:
            maior_numero = numero

    print(f'Foram passados {len(tupla_numeros)} valores ao todo.')
    print(f'O maior número é: {maior_numero}')


maior(3, 2, 100, 2, 3010)
