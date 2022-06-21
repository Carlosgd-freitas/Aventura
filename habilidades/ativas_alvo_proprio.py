import sys

sys.path.append("..")
from classes_base import habilidade, efeito

def EsconderCasco():
    """
    Habilidade ativa onde a criatura se esconde em seu casco resistente por 2 turnos.
    * Alvo: Próprio
    * Tipo: Normal
    * Recarga: 4 Turnos
    """

    defendendo = efeito.Efeito("Defendendo", 50, 1, 2, 100)

    esconder = habilidade.Habilidade("Esconder no Casco", "A criatura se esconde em seu casco resistente por " +
        "2 turnos.", "Normal", "proprio", "ativa", 0, [], 4, 4, [], [defendendo], nao_causa_dano = True)

    return esconder

def EscudoMagico():
    """
    Habilidade ativa onde a criatura se esconde em seu casco resistente por 2 turnos.
    * Alvo: Próprio
    * Tipo: Normal
    * Custo: 2 de Mana
    * Recarga: 4 Turnos
    * Modificadores: 50% da magia
    """

    aumento = efeito.Efeito("Aumento Defesa", 0, 1, 2, 100)

    escudo = habilidade.Habilidade("Escudo Mágico", "O usuário utiliza a mana de uma maneira defensiva ao " +
        "concentrá-la em volta de seu corpo.", "Normal", "proprio", "ativa", 0, [("Mana", 2)], 4, 4,
        [("magia", 50)], [aumento], "singular", "M", nao_causa_dano = True)

    return escudo
