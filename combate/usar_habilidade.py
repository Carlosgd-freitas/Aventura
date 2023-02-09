import sys
from copy import deepcopy

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

def AlvoUnico(atacante, alvo, habilidade):
    """
    Utiliza uma habilidade em um único alvo e retorna o dano infligido e se o acerto foi crítico.
    """

    # Custos da habilidade
    ContabilizarCusto(atacante, habilidade)
    
    # Ativando o efeito de certas habilidades passivas
    efeitos_originais = None
    flag_veneno = 0

    if atacante.HabilidadePresente("Envenenamento") is not None:
        h = atacante.HabilidadePresente("Envenenamento")
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

    # Calculando o dano que será aplicado ao Alvo
    dano, acerto_critico = mecanicas.CalcularDano(atacante, alvo, habilidade)
    if not habilidade.nao_causa_dano:
        alvo.hp -= dano

    # Aplicando Debuffs no Alvo
    for e in habilidade.efeitos:
        utils.ProcessarEfeito(atacante, e, alvo, habilidade = habilidade)
    
    # Retornando possíveis alterações na habilidade
    if flag_veneno == 1:
        efeito_habilidade.chance -= efeito_envenenamento.chance

    elif flag_veneno == 2:
        habilidade.efeitos = efeitos_originais

    # Zerando a recarga atual da habilidade
    habilidade.recarga_atual = -1

    return dano, acerto_critico

def AlvoMultiplo(atacante, alvos, habilidade):
    """
    Utiliza uma habilidade em múltiplos alvos e retorna uma lista contendo o dano infligido em cada um
    e uma lista dizendo se cada acerto foi crítico.
    """

    # Custos da habilidade
    ContabilizarCusto(atacante, habilidade)

    # Ativando o efeito de certas habilidades passivas
    efeitos_originais = None
    flag_veneno = 0

    if atacante.HabilidadePresente("Envenenamento") != -1:
        h = atacante.HabilidadePresente("Envenenamento")
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
        dano, acerto_critico = mecanicas.CalcularDano(atacante, alvo, habilidade)
        danos.append(dano)
        acertos_criticos.append(acerto_critico)

        if not habilidade.nao_causa_dano:
            alvo.hp -= dano

        # Aplicando Debuffs no Alvo
        for e in habilidade.efeitos:
            utils.ProcessarEfeito(atacante, e, alvo, habilidade = habilidade)

    # Retornando possíveis alterações na habilidade
    if flag_veneno == 1:
        efeito_habilidade.chance -= efeito_envenenamento.chance

    elif flag_veneno == 2:
        habilidade.efeitos = efeitos_originais
        
    # Zerando a recarga atual da habilidade
    habilidade.recarga_atual = -1

    return danos, acertos_criticos

def AlvoProprio(criatura, habilidade):
    """
    Utiliza uma habilidade em si próprio.
    """

    # Custos da habilidade
    ContabilizarCusto(criatura, habilidade)

    # Aplicando efeitos em si próprio
    for e in habilidade.efeitos:
        utils.ProcessarEfeito(criatura, e, criatura, habilidade = habilidade)
                
    # Zerando a recarga atual da habilidade
    habilidade.recarga_atual = -1
