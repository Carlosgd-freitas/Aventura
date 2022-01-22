import math
import sys
from colorama import Fore, Back, Style

sys.path.append("..")
from classes_base import utils

def ImprimirHabilidades(criatura, habilidade_indice, impressoes_por_pagina):
    """
    Imprime até <impressoes_por_pagina> primeiras habilidades aprendidas pela criatura, incluindo e a partir
    do índice da habilidade passada como parâmetro.
    """

    # Imprimindo as habilidades aprendidas pela criatura
    print('|========================================> HABILIDADES <========================================|')

    i = 0
    while i < impressoes_por_pagina:

        # Há menos que <impressoes_por_pagina> habilidades restantes
        if habilidade_indice == len(criatura.habilidades):
            break

        habilidade = criatura.habilidades[habilidade_indice]

        # Nome e tipo da Habilidade
        mensagem = f'{habilidade.nome} - Tipo: '
        print(mensagem, end = '')
        utils.ImprimirTipo(habilidade.tipo)

        mensagem = ''

        # Custos da Habilidade
        if len(habilidade.custo) > 0:
            mensagem += ' - Custo: '

            custo_indice = 0
            for c in habilidade.custo:
                if custo_indice != 0:
                    mensagem += ' e '

                mensagem += str(c[1]) + ' '

                if c[0] == "Mana":
                    mensagem += Fore.BLUE + 'Mana' + Style.RESET_ALL
                elif c[0] == "HP":
                    mensagem += Fore.RED + 'HP' + Style.RESET_ALL
                custo_indice += 1
        
        else:
            mensagem += ' - Sem Custo'
        
        # Recarga da Habilidade
        if habilidade.recarga > 0:
            mensagem += f' - Recarga: {habilidade.recarga} Turnos'
        else:
            mensagem += f' - Sem Recarga'

        # Se a Habilidade é passiva/ativa
        if habilidade.passiva_ativa == "passiva":
            mensagem += ' - Passiva'
        else:
            mensagem += ' - Ativa'

        print(mensagem)

        # Descrição da habilidade
        print(f'Descrição: {habilidade.descricao}\n')

        habilidade_indice += 1
        i += 1

def MenuHabilidades(criatura):
    """
    Menu de gerenciamento das habilidades da criatura.
    """

    ultima_pagina = len(criatura.habilidades) - 1 # Descontando o Ataque Normal
    ultima_pagina = math.ceil(ultima_pagina / 10)
    ultima_pagina -= 1
    habilidade_indice_atual = 1
    pagina = 0

    while True:

        # Imprimindo até 10 habilidades
        anterior = 0
        proximo = 0
        habilidade_indice_atual = (pagina * 10) + 1
        ImprimirHabilidades(criatura, habilidade_indice_atual, 10)

        # É possível imprimir até 10 Habilidades anteriores
        if pagina > 0:
            anterior = 1
            print('[1] Anterior')
        
        else:
            print(Fore.RED + '[1] Anterior' + Style.RESET_ALL + '')

        # É possível imprimir até 10 próximas Habilidades
        if pagina < ultima_pagina:
            proximo = 1
            print('[2] Próximo\n')
        
        else:
            print(Fore.RED + '[2] Próximo' + Style.RESET_ALL + '\n')

        print('[0] Retornar ao menu anterior')

        while True:
            op = utils.LerNumero('> ')

            if (op == 0) or (op == 1 and anterior == 1) or (op == 2 and proximo == 1):
                break
        
        # Retornando ao menu anterior
        if op == 0:
            break
    
        # Imprimir até 10 habilidades anteriores
        elif op == 1 and anterior == 1:
            pagina -= 1
        
        # Imprimir até 10 próximas habilidades
        elif op == 2 and proximo == 1:
            pagina += 1
