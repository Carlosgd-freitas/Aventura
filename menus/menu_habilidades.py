import math
import sys
from colorama import Fore, Back, Style

sys.path.append("..")
from base import imprimir, utils

def ImprimirHabilidades(criatura, habilidade_indice, impressoes_por_pagina):
    """
    Imprime até <impressoes_por_pagina> primeiras habilidades aprendidas pela criatura, incluindo e a partir
    do índice da habilidade passada como parâmetro.
    """

    # Imprimindo as habilidades aprendidas pela criatura
    print('|========================================> HABILIDADES <========================================|')

    if habilidade_indice >= len(criatura.habilidades):
        return
    elif habilidade_indice + impressoes_por_pagina >= len(criatura.habilidades):
        limite = len(criatura.habilidades)
    else:
        limite = impressoes_por_pagina

    habilidades = criatura.habilidades[habilidade_indice:limite]

    tabela = imprimir.RetornarTabelaHabilidades(habilidades, habilidade_indice)
    print(tabela)
    print('')

def MenuHabilidades(criatura):
    """
    Menu de gerenciamento das habilidades da criatura.
    """

    habilidades_por_pagina = 15
    ultima_pagina = len(criatura.habilidades) - 1 # Descontando o Ataque Normal
    ultima_pagina = math.ceil(ultima_pagina / habilidades_por_pagina)
    ultima_pagina -= 1
    habilidade_indice_atual = 1
    pagina = 0

    while True:

        # Imprimindo até 'habilidades_por_pagina' habilidades
        anterior = 0
        proximo = 0
        habilidade_indice_atual = (pagina * habilidades_por_pagina) + 1
        ImprimirHabilidades(criatura, habilidade_indice_atual, habilidades_por_pagina)

        print('[1] Analisar habilidade')

        # É possível imprimir até 'habilidades_por_pagina' Habilidades anteriores
        if pagina > 0:
            anterior = 1
            print('[2] Anterior')
        else:
            print(Fore.RED + '[2] Anterior' + Style.RESET_ALL)

        # É possível imprimir até 'habilidades_por_pagina' próximas Habilidades
        if pagina < ultima_pagina:
            proximo = 1
            print('[3] Próximo')
        else:
            print(Fore.RED + '[3] Próximo' + Style.RESET_ALL)

        print('\n[0] Retornar ao menu anterior')

        while True:
            op = utils.LerNumeroIntervalo('> ', 0, 3)

            if (op == 2 and anterior == 0) or (op == 3 and proximo == 0):
                continue
            else:
                break
        
        # Retornando ao menu anterior
        if op == 0:
            break
    
        # Imprimir até 'habilidades_por_pagina' habilidades anteriores
        elif op == 2 and anterior == 1:
            pagina -= 1
        
        # Imprimir até 'habilidades_por_pagina' próximas habilidades
        elif op == 3 and proximo == 1:
            pagina += 1
        
        # Analisar uma habilidade
        else:
            escolha = 1
            pergunta = 1

            menor_indice = (pagina * habilidades_por_pagina) + 1
            maior_indice = (pagina + 1) * habilidades_por_pagina
            if len(criatura.habilidades) - 1 < maior_indice:
                maior_indice = len(criatura.habilidades) - 1

            while escolha != 0:

                if pergunta == 1:
                    if op == 1:
                        print('\nQual habilidade deseja analisar?')
                    pergunta = 0

                escolha = utils.LerNumero('> ')
            
                # Saindo
                if escolha == 0:
                    break

                # Procedendo
                elif escolha >= menor_indice and escolha <= maior_indice:

                    habilidade_escolhida = criatura.habilidades[escolha]

                    # Analisar habilidade
                    if op == 1:
                        imprimir.ImprimirHabilidadeDetalhada(habilidade_escolhida)
                        break
