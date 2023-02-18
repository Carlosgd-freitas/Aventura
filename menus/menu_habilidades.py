import math
import sys

from . import menu_paginado_generico

sys.path.append("..")
from base import imprimir, utils

def MenuHabilidades(criatura, atacar_incluso = False):
    """
    Menu de gerenciamento das habilidades da criatura.
    """

    habilidades_por_pagina = 15
    pagina = 0
    # Descontando o Ataque Normal
    if not atacar_incluso:
        ultima_pagina = len(criatura.habilidades) - 1
        habilidade_indice_atual = 1
    # Contabilizando o Ataque Normal
    else:
        ultima_pagina = len(criatura.habilidades)
        habilidade_indice_atual = 0
    ultima_pagina = math.ceil(ultima_pagina / habilidades_por_pagina)
    ultima_pagina -= 1

    while True:
        if pagina > 0:
            anterior = True
        else:
            anterior = False
        if pagina < ultima_pagina:
            proximo = True
        else:
            proximo = False
        habilidade_indice_atual = (pagina * habilidades_por_pagina) + 1

        # Imprimindo uma página de itens presentes no inventário do jogador
        print('|========================================> HABILIDADES <========================================|')
        habilidades = menu_paginado_generico.ComporPagina(criatura.habilidades, habilidade_indice_atual, habilidades_por_pagina)
        tabela = imprimir.RetornarTabelaHabilidades(habilidades, habilidade_indice_atual)
        print(tabela)
        print('')

        # Opções disponíveis no menu de habilidades
        opcoes = ['Analisar Habilidade']
        if anterior or proximo:
            opcoes.append('Anterior')
            opcoes.append('Próximo')
        opcoes.append('Retornar ao Menu Anterior')
        op = menu_paginado_generico.ImprimirOpções(opcoes, pagina, ultima_pagina)
        if op != 0:
            print('')

        # Retornando ao menu anterior
        if op == 0:
            break
    
        # Imprimir até 'habilidades_por_pagina' habilidades anteriores
        elif op == 2 and anterior:
            pagina -= 1
        
        # Imprimir até 'habilidades_por_pagina' próximas habilidades
        elif op == 3 and proximo:
            pagina += 1
        
        # Analisar uma habilidade
        else:
            escolha = 1
            pergunta = 1

            menor_indice = (pagina * habilidades_por_pagina) + 1
            maior_indice = (pagina + 1) * habilidades_por_pagina
            if (not atacar_incluso) and (len(criatura.habilidades) - 1 < maior_indice):
                maior_indice = len(criatura.habilidades) - 1
            elif (atacar_incluso) and (len(criatura.habilidades) < maior_indice):
                maior_indice = len(criatura.habilidades)

            while escolha != 0:

                if pergunta == 1:
                    if op == 1:
                        print('Qual habilidade deseja analisar?')
                    pergunta = 0

                escolha = utils.LerNumeroIntervalo('> ', menor_indice, maior_indice, permitido = [0])
                print('')
            
                # Saindo
                if escolha == 0:
                    break

                # Procedendo
                else:
                    if atacar_incluso:
                        escolha -= 1
                    habilidade_escolhida = criatura.habilidades[escolha]

                    # Analisar habilidade
                    if op == 1:
                        imprimir.ImprimirHabilidadeDetalhada(habilidade_escolhida)
                        break
