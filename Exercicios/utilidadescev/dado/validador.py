def validarDinheiro(string):

    n = input(string)

    if type(n) in [int, float]:
        return n

    frase = 'Digite um valor numérico por favor: '

    while True:
        if type(n) is str:
            try:
                n = float(n.replace(',','.').strip())
                break
            except:
                print('ERRO! Preço Inválido')
                n = input(frase)

        else:
            print('ERRO! Preço Inválido')
            n = input(frase)

    return n