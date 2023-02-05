import sys

sys.path.append("..")
from base import habilidade, efeito

def Subdivisao(quantidade, criatura_nome, criatura_nivel, criatura_genero):
    """
    Habilidade passiva que invoca <quantidade> <criatura_nome>(s), de nível <criatura_nivel> e gênero
    <criatura_genero>, quando a criatura é derrotada.
    * Alvo: Invocação
    * Tipo: Normal
    """

    # "Invocar:2:Slime:1:Derrotado:M"
    efeito_nome = f"Invocar:{quantidade}:{criatura_nome}:{criatura_nivel}:Derrotado:{criatura_genero}"

    invocar = efeito.Efeito(efeito_nome, -1, 0, -1, 100)
    subdivisao = habilidade.Habilidade("Subdivisão", "Ao ser derrotado, essa criatura invoca duas versões menores " +
    "de si mesma.", "Normal", "Invocação", "Passiva", 0, [], 0, 0, [], [invocar], "singular", "F", False, 0.0, 1.0)

    return subdivisao
