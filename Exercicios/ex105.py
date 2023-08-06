def notas(lst=[], sit=False):
    """
    -> Função para mostrar a quantidade de notas, maior nota, menor nota e a média de uma turma.
    :param lst: Lista de notas
    :param sit: Printar a situação da turma
    """
    if lst == []:
        return "Você esqueceu de passar a lista de notas !"
    
    notas_dict = {
        'qnt_notas': len(lst),
        'maior': max(lst),
        'menor': min(lst),
        'media': sum(lst)/len(lst)
    }

    if sit is True:
        if notas_dict['media'] >= 9:
            notas_dict['situacao'] = "ÓTIMA"
        elif notas_dict['media'] >= 7:
            notas_dict['situacao'] = "BOA"
        elif notas_dict['media'] >= 5:
            notas_dict['situacao'] = "RUIM"
        else:
            notas_dict['situacao'] = "REPROVADOS"
    
    return notas_dict

print(notas([2,3,1,4,10], True))
    
