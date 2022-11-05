import sys

sys.path.append("..")
from base import efeito, habilidade

def Envenenamento(veneno, turnos, chance):
    """
    Habilidade passiva que tem chance de envenenar um alvo sempre que um ataque normal é feito.
    * Alvo: Único inimigo
    * Tipo: Terrestre
    * Efeitos: <chance> % de chance de envenar o alvo por <turnos> turnos, dando <veneno> de dano no início de
    cada turno (Veneno)
    """

    veneno = efeito.Efeito("Veneno", veneno, 1, turnos, chance)
    envenenamento = habilidade.Habilidade("Envenenamento", "Sempre que um ataque normal é efetuado, há " +
    f"{chance}% de chance de envenenar o alvo.", "Terrestre", "inimigo", "passiva", 0, [], 0, 0, [], [veneno],
    "singular", "M", False, 0.0, 1.0)
    
    return envenenamento
    