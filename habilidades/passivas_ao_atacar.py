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
    descricao = f'Atacar ou utilizar uma habilidade em um inimigo possui {chance}% de chance de envenená-lo. Ataques e habilidades que possuem\nchance de ' + \
        f'envenenar um alvo inimigo têm essa chance aumentada em {chance}%.'

    envenenamento = habilidade.Habilidade("Envenenamento", descricao, "Terrestre", "Inimigo", "Passiva", 0, [], 0, 0, [], [veneno],
        "singular", "M", False, 0.0, 1.0)
    
    return envenenamento
    