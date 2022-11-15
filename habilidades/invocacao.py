import sys

sys.path.append("..")
from base import habilidade, efeito

def Subdivisao(criatura_nome, quantidade):
    """
    Habilidade passiva que invoca <quantidade> <criatura_nome>(s) quando a criatura é derrotada.
    * Alvo: Invocação
    * Tipo: Normal
    """

    invocar = efeito.Efeito("Invocar:" + str(quantidade) + ":" + criatura_nome, -1, 0, -1, 100)
    subdivisao = habilidade.Habilidade("Subdivisão", "Ao ser derrotado, essa criatura invoca duas versões menores " +
    "de si mesma.", "Normal", "invocacao", "passiva", 0, [], 0, 0, [], [invocar], "singular", "F", False, 0.0, 1.0)

    return subdivisao
