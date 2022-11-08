import sys

from . import mecanicas
sys.path.append("..")
from base import utils

def CopiarEfeitos(efeitos):
    """
    Cria e retorna uma lista de novos efeitos que possuem os atributos com os mesmos valores dos contidos na
    lista passada por parâmetro.
    """
    efeitos_2 = []
    for e in efeitos:
        efeitos_2.append(e.ClonarEfeito())
    return efeitos_2

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
    Utiliza uma habilidade em um único alvo e retorna o dano infligido.
    """

    dano = mecanicas.CalcularDano(atacante, alvo, habilidade)

    if not habilidade.nao_causa_dano:
        alvo.hp -= dano

    # Custos da habilidade
    ContabilizarCusto(atacante, habilidade)
    
    # Adicionando efeitos ao ataque normal temporariamente
    for h in atacante.habilidades:
        if h.nome == "Envenenamento":
            efeito = h.efeitos[0]
            atacante.habilidades[0].efeitos.append(efeito)
    
    # Aplicando Debuffs no Alvo
    for e in habilidade.efeitos:
        utils.ProcessarEfeito(atacante, e, alvo, habilidade = habilidade)
    
    # Removendo os efeitos temporários do ataque normal
    atacante.habilidades[0].efeitos = []

    # Zerando a recarga atual da habilidade
    habilidade.recarga_atual = -1

    return dano

def AlvoMultiplo(atacante, alvos, habilidade):
    """
    Utiliza uma habilidade em múltiplos alvos e retorna uma lista contendo o dano infligido em cada um.
    """

    # Custos da habilidade
    ContabilizarCusto(atacante, habilidade)
    
    # Adicionando efeitos ao ataque normal temporariamente
    for h in atacante.habilidades:
        if h.nome == "Envenenamento":
            efeito = h.efeitos[0]
            atacante.habilidades[0].efeitos.append(efeito)

    danos = []

    for alvo in alvos:
        dano = mecanicas.CalcularDano(atacante, alvo, habilidade)
        danos.append(dano)

        if not habilidade.nao_causa_dano:
            alvo.hp -= dano

        # Aplicando Debuffs no Alvo
        for e in habilidade.efeitos:
            utils.ProcessarEfeito(atacante, e, alvo, habilidade = habilidade)
        
    # Removendo os efeitos temporários do ataque normal
    atacante.habilidades[0].efeitos = []

    # Zerando a recarga atual da habilidade
    habilidade.recarga_atual = -1

    return danos

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
