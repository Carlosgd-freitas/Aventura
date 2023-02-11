import sys
from copy import deepcopy
from colorama import Fore, Back, Style

from . import mecanicas
sys.path.append("..")
from base import utils

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
        dano, acerto_critico = mecanicas.CalcularDano(usuario, alvo, habilidade)
        danos.append(dano)
        acertos_criticos.append(acerto_critico)

        if not habilidade.nao_causa_dano:
            alvo.hp -= dano

        # Aplicando efeitos da habilidade no alvo
        for e in habilidade.efeitos:
            utils.ProcessarEfeito(usuario, e, alvo, habilidade = habilidade)

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

