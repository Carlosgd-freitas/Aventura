import sys

sys.path.append("..")
from base import habilidade, efeito

def Atacar(tipo):
    """
    Habilidade ativa que ataca o inimigo normalmente.
    * Alvo: Único inimigo
    * Tipo: Deve ser passado por parâmetro
    * Modificadores: 100% do ataque
    """

    atacar = habilidade.Habilidade("Atacar", "Um ataque normal.", tipo, "inimigo", "ativa", 0, [], 0, 0,
        [("ataque", 100)], [], "default", "default", False, 0.0, 1.0)

    return atacar

def ProjetilMana():
    """
    Habilidade ativa que concentra e dispara uma pequena quantidade de mana.
    * Alvo: Único inimigo
    * Tipo: Normal
    * Custo: 2 de Mana
    * Recarga: 1 Turno
    * Modificadores: 100% da magia
    """

    projetil = habilidade.Habilidade("Projétil de Mana", "Concentra e dispara uma pequena quantidade de " + 
    "mana, causando dano igual à sua magia.", "Normal", "inimigo", "ativa", 0,
    [("Mana", 2)], 1, 1, [("magia", 100)], [], "singular", "M", False, 0.0, 1.0)

    return projetil

def CuspeAcido(ataque):
    """
    Habilidade ativa que cospe ácido e ignora a defesa do alvo.
    * Alvo: Único inimigo
    * Tipo: Normal
    * Custo: 4 de Mana
    * Recarga: 2 Turnos
    * Modificadores: 50% da magia
    * Efeitos: Ignora 50% da defesa do alvo (Perfurante)
    """

    perfurante = efeito.Efeito("Perfurante %", 50, 0, -1, 100)
    cuspe = habilidade.Habilidade("Cuspe Ácido", "Um cuspe ácido que ignora 50% da defesa do alvo.", "Normal",
    "inimigo", "ativa", ataque, [("Mana", 4)], 2, 2, [("magia", 50)], [perfurante], "singular", "M", False, 0.0,
    1.0)
    
    return cuspe

def AtaqueVenenoso(veneno, turnos, mana, recarga):
    """
    Habilidade ativa que envenena o alvo além de atacar normalmente.
    * Alvo: Único inimigo
    * Tipo: Terrestre
    * Custo: <mana>
    * Recarga: <recarga> Turnos
    * Modificadores: 100% do ataque
    * Efeitos: Envena o alvo por <turnos> turnos, dando <veneno> de dano no início de cada turno (Veneno)
    """

    veneno = efeito.Efeito("Veneno", veneno, 1, turnos, 100)
    ataque = habilidade.Habilidade("Ataque Venenoso", "Um ataque que tem 100% de chance de envenenar o alvo.",
    "Terrestre", "inimigo", "ativa", 0, [("Mana", mana)], recarga, recarga, [("ataque", 100)], [veneno],
    "singular", "M", False, 0.0, 1.0)
    
    return ataque

def ImpactoAtordoante(atordoamento_turnos, chance, tipo, mana, recarga):
    """
    Habilidade ativa que realiza um ataque concussivo no alvo.
    * Alvo: Único inimigo
    * Tipo: <tipo>
    * Custo: <mana>
    * Recarga: <recarga> Turnos
    * Modificadores: 120% do ataque
    * Efeitos: <chance>% de atordoar o alvo por <atordoamento_turnos> turnos (Atordoamento)
    """

    atordoamento = efeito.Efeito("Atordoamento", 0, 1, atordoamento_turnos, chance)
    impacto = habilidade.Habilidade("Impacto Atordoante", f"Um ataque concussivo que tem {chance}% de chance de " +
        f"deixar o alvo atordoado por {atordoamento_turnos} turnos.", tipo, "inimigo", "ativa", 0, [("Mana", mana)],
        recarga, recarga, [("ataque", 120)], [atordoamento], "singular", "M", False, 0.0, 1.0)

    return impacto

def CuspeMel(mana, recarga, efeitos_turnos):
    """
    Habilidade ativa que cospe mel e reduz a defesa do alvo e aplica lentidão, mas não causa dano.
    * Alvo: Único inimigo
    * Tipo: Normal
    * Custo: <mana>
    * Recarga: <recarga> Turnos
    * Modificadores: 50% da magia
    * Efeitos: Diminui a defesa do alvo e aplica lentidão por <efeitos_turnos> Turnos
    """

    diminuicao = efeito.Efeito("Diminuição Defesa", 0, 1, efeitos_turnos, 100)
    lentidao = efeito.Efeito("Lentidão", 0, 1, efeitos_turnos, 100)

    cuspe = habilidade.Habilidade("Cuspe de Mel", "Um cuspe de Mel que reduz a defesa do alvo e aplica lentidão.",
    "Normal", "inimigo", "ativa", 0, [("Mana", mana)], recarga, recarga, [("magia", 50)], [diminuicao, lentidao],
    "singular", "M", True, 0.0, 1.0)
    
    return cuspe

def CuraInferior(mana, recarga):
    """
    Habilidade ativa que cura o hp do alvo.
    * Alvo: Único aliado
    * Tipo: Normal
    * Custo: <mana>
    * Recarga: <recarga> Turnos
    * Efeitos: Cura o hp do alvo em 20% de seu hp máximo.
    """

    cura_efeito = efeito.Efeito("Cura HP %", 20, 0, -1, 100)

    cura = habilidade.Habilidade("Cura Inferior", "Utiliza magia para curar o alvo em 20% de sua vida máxima.",
    "Normal", "aliado", "ativa", 0, [("Mana", mana)], recarga, recarga, [], [cura_efeito], "singular", "F", True,
    0.0, 1.0)
    
    return cura

def RaioFogo(magia, mana, recarga):
    """
    Habilidade ativa que atira um raio de fogo e ignora completamente a defesa do alvo.
    * Alvo: Único inimigo
    * Tipo: Fogo
    * Custo: <mana> de Mana
    * Recarga: <recarga> Turnos
    * Efeitos: Ignora 100% da defesa do alvo (Perfurante)
    """

    perfurante = efeito.Efeito("Perfurante %", 100, 0, -1, 100)
    raio = habilidade.Habilidade("Raio de Fogo", "Um raio de fogo que ignora completamente a defesa do alvo.",
    "Fogo", "inimigo", "ativa", magia, [("Mana", mana)], recarga, recarga, [], [perfurante], "singular", "M",
    False, 0.0, 1.0)
    
    return raio
