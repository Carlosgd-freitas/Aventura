import sys

sys.path.append("..")
from classes_base import habilidade, efeito

def GritoEstremecedor(mana, recarga, modificador_magia):
    """
    Habilidade ativa onde o usuário grita e diminui a defesa de todos os inimigos.
    * Alvo: Múltiplos inimigos
    * Tipo: Normal
    * Custo: <mana> de Mana
    * Recarga: <recarga> Turnos
    * Modificadores: <modificador_magia>% da magia
    * Efeitos: Diminui a defesa dos alvos
    """

    diminuicao = efeito.Efeito("Diminuição Defesa", 0, 1, 2, 100)

    grito = habilidade.Habilidade("Grito Estremecedor", "O usuário grita tão forte que prejudica temporariamente a" +
        "audição de seus inimigos, diminuindo suas defesas.", "Normal", "multiplos", "ativa", 0, [("Mana", mana)], 
        recarga, recarga, [("magia", modificador_magia)], [diminuicao], "singular", "M", True, 0.0, 1.0)

    return grito

