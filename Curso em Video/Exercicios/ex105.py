def notas(*notas, situacao=False):
    '''
    -> Função para análise de notas de uma classe.
    para n: Recebe uma ou mais nota dos alunos;
    para situação: valor opcional (padrão False), se adiciona ou não a situação da turma;
    return: Retorna um dicionario com as informações analisadas da turma;    
    '''
    notas_dict = {}
    notas_dict['QuantidadeNotas'] = len(notas)
    notas_dict['MaiorNota'] = max(notas)
    notas_dict['MenorNota'] = min(notas)
    notas_dict['MediaTurma'] = sum(notas) / len(notas)
    if situacao:
        notas_dict['Situação'] = "Boa" if notas_dict['MediaTurma'] > 6 else "Ruim"
        return notas_dict
    
    else:
        return notas_dict
    
resp = notas(10, 4, 6.5, 8, 7, 4, situacao=True)
print(resp)
help(notas)