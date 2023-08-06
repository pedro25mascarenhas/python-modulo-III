from prettytable import PrettyTable
def formatar(n):
    n = f"R${round(n, 3):.2f}".replace('.', ',')
    return n
def metade(n, f=True):
    resultado = n/2
    if f:
        return formatar(resultado)
    return resultado
def dobro(n, f=True):
    resultado = n * 2
    if f:
        return formatar(resultado)
    return resultado

def aumentar(n, porcentagem, f=True):
    resultado = n * (1+porcentagem/100)
    if f:
        return formatar(resultado)
    return resultado

def diminuir(n, porcentagem, f=True):
    resultado = n * (1-porcentagem/100)
    if f:
        return formatar(resultado)
    return resultado

def resumo(n, aumento, reducao):
    titulo = "RESUMO DO VALOR"
    print(f"{titulo}")


    tabela = PrettyTable(header=False)
    tabela.add_row(['Preço analisado:', formatar(n)])
    tabela.add_row(['Dobro do preço:', dobro(n)])
    tabela.add_row(['Metade do preço:', metade(n)])
    tabela.add_row([f'{aumento}% de aumento:', aumentar(n, aumento)])
    tabela.add_row([f'{reducao}% de redução:', diminuir(n, reducao)])

    print(tabela)