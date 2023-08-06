import datetime


def voto(a=2000):
    """
    Função para determinar se a pessoa tem o voto obrigatório ou não, baseando-se na idade.
    Se for menor de 16, não vota
    Se tiver 16 ou 17, é opcional
    Se for maior de 18, é obrigatório
    Se for maior de 65, é opcional
    
    :param ano_nascimento: ano de nascimento da pessoa
    """
    ano_atual = datetime.datetime.now().year
    idade = ano_atual - a
    if idade < 16:
        voto = 'Não vota'
    elif idade in [16,17] or idade >= 65:
        voto = 'Opcional'
    elif 18 <= idade < 65:
        voto = 'Obrigatório'

    return voto

print(voto(a=2007))