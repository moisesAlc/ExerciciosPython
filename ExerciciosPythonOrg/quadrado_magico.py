"""
    Solução do exercício 14 da lista de exercícios de funções da python.org
"""

def exibe_quadrado_formatado(quadrado):
    """Exibe o quadrado dado em formato amigável"""
    for i in range(0,len(quadrado)):
        for j in range(0,len(quadrado[0])):
            print(f'{quadrado[i][j]} ', end='')
        print()

def linhas_sao_magicas(quadrado):
    """Dado um quadrado, retorna se ele é mágico e tbm retorna a soma.
    Se não for mágico, retornará False e None"""

    eh_magico = True
    somas_linhas = []

    for linha in quadrado:
        somas_linhas.append(sum(linha))
    for i in range(0, len(somas_linhas) - 1):
        if somas_linhas[i] != somas_linhas[i + 1]:
            eh_magico = False

    if eh_magico:
        soma_ret = somas_linhas[0]
        return eh_magico, soma_ret

    return eh_magico, None

def diagonais_sao_magicas(quadrado, soma_arg):
    """Dado um quadrado e uma determinada soma, verifica
    as somas das elementos nas diagonais do quadrão são as mesmas e
    se são iguais à soma passada."""

    eh_magico = True

    diagonal_no_se = []
    diagonal_so_ne = []

    for i in range(0,len(quadrado)):
        diagonal_no_se.append(quadrado[i][i])

    for i in range(len(quadrado)-1,-1,-1):
        diagonal_so_ne.append(quadrado[i][i])

    if sum(diagonal_so_ne) == sum(diagonal_no_se) == soma_arg:
        return eh_magico

    return False

def colunas_sao_magicas(quadrado, soma_arg):
    eh_magico = True
    soma_colunas = []
    for i in range(0,len(quadrado)):
        colunas = []
        for linha in quadrado:
            colunas.append(linha[i])
        if sum(colunas) != soma_arg:
            return False
        soma_colunas.append(sum(colunas))

if __name__ == "__main__":

    quadrado_2l = ((3, 2), (1, 4))

    quadrado_3l = ((1, 2, 5), (1, 2, 5), (1, 2, 5))

    quadrado_3l_b = ((8, 5, 4), (1, 5, 9), (6, 7, 2))

    exibe_quadrado_formatado(quadrado_3l)
    magico, soma = linhas_sao_magicas(quadrado_3l)
    if magico:
        print(diagonais_sao_magicas(quadrado_3l, soma))
