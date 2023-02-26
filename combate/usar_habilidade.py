import sys
from copy import deepcopy
from tabulate import tabulate
from colorama import Fore, Back, Style

from . import batalha_mecanicas
sys.path.append("..")
from base import imprimir, utils

def EscolherHabilidade(jogador):
    """
    Imprime as possíveis habilidades que o jogador pode usar e retorna o índice da lista de habilidades
    correspondente à habilidade escolhida.
    """

    print('\nEscolha qual habilidade deseja usar:')

    indice_atacar = jogador.HabilidadeIndice("Atacar")
    indice_print = 1
    indice_item = 0
    relacao = [(0, -1)]

    tabela = []
    cabecalho = ["Nome", "Custo", "Recarga", "Tipo", "Passiva/Ativa", "Alvo"]
    alinhamento = ("left", "center", "center", "center", "center", "center")

    for habilidade in jogador.habilidades:

        # A habilidade de ataque normal, bem como habilidades passivas, não serão listadas
        if (indice_item != indice_atacar) and (habilidade.passiva_ativa == "Ativa"):

            t = []
            t.append(f'[{indice_print}] ' + habilidade.nome) # Índice + Nome
            # Custo
            custo = ""
            if len(habilidade.custo) > 0:
                for i, c in enumerate(habilidade.custo):
                    if (i != 0) and (i < len(habilidade.custo) - 1):
                        custo += ', '
                    if c[0] == "Mana":
                        custo += str(c[1]) + " " + imprimir.RetornarStringColorida(c[0])
                    elif c[0] == "HP":
                        custo += str(c[1]) + " " + imprimir.RetornarStringColorida(c[0])
            else:
                custo += '---'
            t.append(custo)
            # Recarga
            recarga = ""
            if habilidade.recarga_atual != habilidade.recarga:
                recarga += Back.BLACK + Fore.RED + str(habilidade.recarga_atual) + Style.RESET_ALL
            else:
                recarga += str(habilidade.recarga_atual)
            recarga += f' / {habilidade.recarga}'
            t.append(recarga)
            t.append(imprimir.RetornarTipo(habilidade.tipo))      # Tipo
            t.append(habilidade.passiva_ativa)                    # Passiva/Ativa
            t.append(habilidade.alvo)                             # Alvo
            tabela.append(t)

            relacao.append((indice_print, indice_item))
            indice_print += 1

        indice_item += 1
    
    print(tabulate(tabela, headers = cabecalho, colalign = alinhamento, tablefmt="psql"))
    print('\n[0] Retornar e escolher outra ação.\n')

    while True:
        valido = 1
        escolha = utils.LerNumero('> ')

        if escolha >= 0 and escolha <= relacao[-1][0]:

            # Mapeando a escolha para um índice da lista de habilidades
            for r in relacao:
                if r[0] == escolha:
                    escolha = r[1]
                    break
            
            if escolha != -1:

                # Checando o custo de usar a habilidade
                for c in jogador.habilidades[escolha].custo:
                    if c[0] == "Mana" and c[1] > jogador.mana:
                        print('Você não tem ' + Fore.BLUE + 'Mana' + Style.RESET_ALL +
                            ' o suficiente para usar esta habilidade.')
                        valido = 0

                    elif c[0] == "HP" and c[1] > jogador.hp:
                        print('Você não tem ' + Fore.RED + 'HP' + Style.RESET_ALL +
                            ' o suficiente para usar esta habilidade.')
                        valido = 0

                # Checando a recarga da habilidade
                if jogador.habilidades[escolha].recarga_atual < jogador.habilidades[escolha].recarga:
                    print('Esta habilidade ainda está em recarga.')
                    valido = 0

            if valido == 1:
                break
    
    return escolha

def ContabilizarCusto(usuario, habilidade):
    """
    Reduz alguns recursos do usuario da habilidade, como Mana ou HP, com base nos custos da habilidade usada.
    """
    for c in habilidade.custo:
        if c[0] == "Mana":
            usuario.mana -= c[1]

        elif c[0] == "HP":
            usuario.hp -= c[1]

def UsarHabilidade(usuario, alvos, habilidade, verbose = True):
    """
    Utiliza uma habilidade do usuário em alvos e retorna uma lista contendo o dano infligido em cada um
    e uma lista dizendo se cada acerto foi crítico.
    """
    if verbose:
        if habilidade.alvo == "Inimigo" or habilidade.alvo == "Aliado":
            print(f'{usuario.nome} utilizou {habilidade.nome} em {alvos[0].nome}.')
        else:
            print(f'{usuario.nome} utilizou {habilidade.nome}.')

    # Custos da habilidade
    ContabilizarCusto(usuario, habilidade)

    # Ativando o efeito de certas habilidades passivas
    efeitos_originais = None
    flag_veneno = 0

    if usuario.HabilidadePresente("Envenenamento") is not None:
        h = usuario.HabilidadePresente("Envenenamento")
        efeito_envenenamento = h.efeitos[0]

        # A habilidade usada já possui Veneno: aumenta a chance do efeito
        if habilidade.RetornarEfeito('Veneno') is not None:
            flag_veneno = 1

            efeito_habilidade = habilidade.RetornarEfeito('Veneno')
            efeito_habilidade.chance += efeito_envenenamento.chance

        #  A habilidade usada não possui Veneno: passa a ter o Veneno de 'Envenenamento'
        else:
            flag_veneno = 2

            efeitos_originais = []
            for e in habilidade.efeitos:
                efeitos_originais.append(deepcopy(e))

            habilidade.efeitos.append(efeito_envenenamento)

    # Calculando o dano que será aplicado aos Alvos
    danos = []
    acertos_criticos = []

    for alvo in alvos:
        dano, acerto_critico = utils.CalcularDano(usuario, alvo, habilidade = habilidade)
        danos.append(dano)
        acertos_criticos.append(acerto_critico)

        if not habilidade.nao_causa_dano:
            alvo.hp -= dano

        # Aplicando efeitos da habilidade no alvo
        for e in habilidade.efeitos:
            e.Processar(usuario, alvo, habilidade = habilidade)

    # Retornando possíveis alterações na habilidade
    if flag_veneno == 1:
        efeito_habilidade.chance -= efeito_envenenamento.chance

    elif flag_veneno == 2:
        habilidade.efeitos = efeitos_originais
        
    # Zerando a recarga atual da habilidade
    habilidade.recarga_atual = -1

    return danos, acertos_criticos

def ImprimirDano(atacante, alvos, habilidade, danos, acertos_criticos):
    """
    Imprime as mensagens de dano após o uso de uma habilidade.
    """

    for indice, alvo in enumerate(alvos):

        # Uso da habilidade básica: Atacar
        if habilidade.nome == "Atacar":
            if acertos_criticos[indice]:
                print(Fore.RED + 'CRÍTICO!' + Style.RESET_ALL + ' ', end = '')
            print(f'{atacante.nome} atacou {alvo.nome} e deu {danos[indice]} de dano!')

        # Uso de outras habilidades
        else:
            if acertos_criticos[indice]:
                print(Fore.RED + 'CRÍTICO!' + Style.RESET_ALL + ' ', end = '')
            
            if alvo.singular_plural == "singular":
                print(f'{alvo.nome} recebeu {danos[indice]} de dano.')
            elif alvo.singular_plural == "plural":
                print(f'{alvo.nome} receberam {danos[indice]} de dano.')

