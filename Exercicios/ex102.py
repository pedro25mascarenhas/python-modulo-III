def fatorial(num=1, show=False):
    """
    -> Função para calcular o fatorial de algum número
    :param num: Número para calcular o fatorial
    :param show: Mostrar a multiplicação do fatorial
    :return: Sem retorno
    """
    f = 1
    for c in range(num, 0, -1):
        f *= c
        if show is True:
            print(c, 'x ' if c != 1 else '' f'= {f}' if c == 1 else '', end='' if c != 1 else '\n')
    if show is False:
        print(f)

fatorial(5, show=True)
