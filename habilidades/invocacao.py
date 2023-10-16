import sys

sys.path.append("..")
from base import habilidade, efeito

def Subdivisao(nome, nivel, quantidade):
    """
    Habilidade passiva que invoca <quantidade> <nome> de nível <nivel> quando a criatura é derrotada.
    * Alvo: Invocação
    * Tipo: Normal
    """

    invocacao = {
        "nome": nome,
        "nivel": nivel,
        "quantidade": quantidade,
        "condicao": "derrota",
    }
    invocar = efeito.Efeito("Invocar", -1, 0, -1, 100, invocacao=invocacao)
    
    subdivisao = habilidade.Habilidade("Subdivisão", "Ao ser derrotada, essa criatura invoca duas versões menores " +
    "de si mesma.", "Normal", "Invocação", "Passiva", 0, [], 0, 0, [], [invocar], "singular", "F", False, 0.0, 1.0)

    return subdivisao
