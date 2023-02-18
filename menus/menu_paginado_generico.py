import sys
from colorama import Fore, Back, Style

sys.path.append("..")
from base import utils

def ComporPagina(lista, indice_inicial, impressoes_por_pagina):
    """
    Retorna a parte da lista referente a página que será impressa.

    Parâmetros:
    - lista: lista cujos elementos serão impressos;
    - indice_inicial: índice do primeiro elemento de <lista> presente na página a ser impressa;
    - impressoes_por_pagina: número de elementos de <lista> que serão impressos por página.
    """

    if indice_inicial >= len(lista):
        return
    elif indice_inicial + impressoes_por_pagina >= len(lista):
        limite = len(lista)
    else:
        limite = impressoes_por_pagina

    return lista[indice_inicial:limite]

def ImprimirOpções(opcoes, pagina_atual, ultima_pagina):
    """
    Apresenta as opções que o jogador pode escolher ao navegar em um menu paginado. A última opção a ser
    impressa é relativa ao índice 0. Retorna a opção válida que o jogador escolheu. 

    Parâmetros:
    - opcoes: lista contendo os nomes das opções que serão impressas em ordem;
    - pagina_atual: índice da página atual;
    - ultima_pagina: índice da última página.
    """
    anterior = False
    anterior_indice = 0
    proximo = False
    proximo_indice = 0
    ultima_opcao = len(opcoes) - 1

    for indice, opcao in enumerate(opcoes):
        if indice != ultima_opcao:
            if opcao == "Anterior":
                anterior_indice = indice + 1
                if pagina_atual > 0:
                    anterior = True
                    print(f'[{indice+1}] {opcao}')
                else:
                    print(Fore.RED + f'[{indice+1}] {opcao}' + Style.RESET_ALL)
            elif opcao == "Próximo":
                proximo_indice = indice + 1
                if pagina_atual < ultima_pagina:
                    proximo = True
                    print(f'[{indice+1}] {opcao}')
                else:
                    print(Fore.RED + f'[{indice+1}] {opcao}' + Style.RESET_ALL)
            else:
                print(f'[{indice+1}] {opcao}')
    print(f'\n[0] {opcoes[-1]}')

    while True:
        op = utils.LerNumeroIntervalo('> ', 0, ultima_opcao)

        if (op == anterior_indice) and (not anterior) and (anterior_indice != 0):
            continue
        elif (op == proximo_indice) and (not proximo) and (proximo_indice != 0):
            continue
        else:
            break
    
    return op  
        