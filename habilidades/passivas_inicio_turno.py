import sys

sys.path.append("..")
from base import habilidade

def Regeneracao(valor):
    """
    Habilidade passiva que recupera parte do HP no início do turno.
    * Alvo: Próprio
    * Tipo: Normal
    """

    regeneracao = habilidade.Habilidade("Regeneração", "Recupera parte do HP no início do turno.", "Normal",
    "Próprio", "Passiva", valor, [], 0, 0, [], [], "singular", "F", False, 0.0, 1.0)
    
    return regeneracao
