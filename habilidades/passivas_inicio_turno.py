import sys

sys.path.append("..")
from base import efeito, habilidade

def Regeneracao(valor):
    """
    Habilidade passiva que recupera parte do HP no início do turno.
    * Alvo: Próprio
    * Tipo: Normal
    """

    regen_efeito = efeito.Efeito("Regeneração HP", valor, 0, 999, 100)

    regeneracao = habilidade.Habilidade("Regeneração", "Recupera parte do HP no início do turno.", "Normal",
    "Próprio", "Passiva", valor, [], 0, 0, [], [regen_efeito], "singular", "F", False, 0.0, 1.0)
    
    return regeneracao
