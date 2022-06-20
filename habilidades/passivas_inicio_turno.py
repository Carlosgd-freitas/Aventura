import sys

sys.path.append("..")
from classes_base import habilidade

def Regeneracao(valor):
    """
    Habilidade passiva que recupera parte do HP no início do turno.
    * Alvo: Próprio
    * Tipo: Normal
    * Modificadores: 50% da magia
    """

    regeneracao = habilidade.Habilidade("Regeneração", "Recupera parte do HP no início do turno.", "Normal",
    "proprio", "passiva", valor, [], 0, 0, [("magia", 50)], [], "singular", "F")
    
    return regeneracao
