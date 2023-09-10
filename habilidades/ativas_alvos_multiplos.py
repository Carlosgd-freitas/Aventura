import sys

sys.path.append("..")
from base import habilidade, efeito

def GritoEstremecedor(turnos, mana, recarga, modificador_magia):
    """
    Habilidade ativa onde o usuário grita e diminui a defesa de todos os inimigos por <turnos> turnos.
    * Alvo: Múltiplos inimigos
    * Tipo: Normal
    * Custo: <mana> de Mana
    * Recarga: <recarga> Turnos
    * Modificadores: <modificador_magia>% da magia
    * Efeitos: Diminui a defesa dos alvos
    """

    diminuicao = efeito.Efeito("Diminuição Defesa", 0, 1, turnos, 100)

    grito = habilidade.Habilidade("Grito Estremecedor", "O usuário grita tão forte que prejudica temporariamente a" +
        "audição de seus inimigos, diminuindo suas defesas.", "Normal", "Inimigos", "Ativa", 0, [("Mana", mana)], 
        recarga, recarga, [("magia", modificador_magia)], [diminuicao], "singular", "M", True, 0.0, 1.0)

    return grito

def DisparoEletrico(mana):
    """
    Habilidade ativa que atinge todos os inimigos com uma corrente elétrica, mas causa pouco dano.
    * Alvo: Múltiplos inimigos
    * Tipo: Elétrico
    * Custo: <mana> de Mana
    * Recarga: 3 Turnos
    * Modificadores: 50% da magia
    """

    disparo = habilidade.Habilidade("Disparo Elétrico", "Atinge todos os inimigos com uma corrente elétrica, " + 
    "mas causa pouco dano.", "Elétrico", "Inimigos", "Ativa", 0, [("Mana", mana)], 3, 3, [("magia", 50)], [],
    "singular", "M", False, 0.0, 1.0)

    return disparo
