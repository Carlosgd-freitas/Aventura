import sys

sys.path.append("..")
from base import habilidade, efeito

def EsconderCasco():
    """
    Habilidade ativa onde a criatura se esconde em seu casco resistente por 2 turnos.
    * Alvo: Próprio
    * Tipo: Normal
    * Recarga: 4 Turnos
    """

    defendendo = efeito.Efeito("Defendendo", 50, 1, 2, 100)

    esconder = habilidade.Habilidade("Esconder no Casco", "A criatura se esconde em seu casco resistente por " +
        "2 turnos.", "Normal", "Próprio", "Ativa", 0, [], 4, 4, [], [defendendo], "default", "default", True, 0.0,
        1.0)

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
        "concentrá-la em volta de seu corpo.", "Normal", "Próprio", "Ativa", 0, [("Mana", 2)], 4, 4,
        [("magia", 50)], [aumento], "singular", "M", True, 0.0, 1.0)

    return escudo

def Focar(valor_velocidade, valor_chance_critico, efeitos_turnos, mana, recarga):
    """
    Habilidade ativa onde a criatura aumenta sua velocidade em <valor_velocidade> e chance de acerto crítico em
    <valor_chance_critico> por <efeitos_turnos> turnos.
    * Alvo: Próprio
    * Tipo: Normal
    * Custo: <mana> de Mana
    * Recarga: <recarga> Turnos
    """

    aumento_velocidade = efeito.Efeito("Aumento Velocidade", valor_velocidade, 1, efeitos_turnos, 100)
    aumento_chance_critico = efeito.Efeito("Aumento Chance Crítico", valor_chance_critico, 1, efeitos_turnos, 100)

    focar = habilidade.Habilidade("Focar", "A criatura aumenta seu foco em combate, se tornando mais veloz e " +
    f"aumentando sua chance de acerto crítico por {str(efeitos_turnos)} turnos.", "Normal", "Próprio", "Ativa", 0,
    [("Mana", mana)], recarga, recarga, [], [aumento_velocidade, aumento_chance_critico], "default", "default",
    True, 0.0, 1.0)

    return focar
