import sys

sys.path.append("..")
from classes_base import efeito, item

def ErvaCurativa(quantidade, preco):
    """
    Cria <quantidade> de itens consumíveis, com preço igual à <preco>, que:
    * Curam 3 de hp
    """

    erva_efeito = [efeito.Efeito("Cura HP", 3, 0, -1, 100)]
    erva = item.Item(erva_efeito, [], preco, quantidade, "Erva Curativa",
        singular_plural = "singular", genero = "F",
        descricao = "Cura 3 de HP.")
    
    return ("Consumivel", erva)

def MelAbelhoide(quantidade, preco):
    """
    Cria <quantidade> de itens consumíveis, com preço igual à <preco>, que:
    * Regenera 2 de hp por 3 turnos
    """

    mel_efeito = [efeito.Efeito("Regeneração HP", 2, 1, 3, 100)]
    mel = item.Item(mel_efeito, [], preco, quantidade, "Mel de Abelhóide",
        singular_plural = "singular", genero = "M",
        descricao = "Regenera 2 de HP por 3 turnos.")
    
    return ("Consumivel", mel)

def PocaoCuraPequena(quantidade, preco):
    """
    Cria <quantidade> de itens consumíveis, com preço igual à <preco>, que:
    * Curam 25% do hp máximo ou 5 de hp, o que for maior
    """

    pocao_efeito = [efeito.Efeito("Cura HP % ou valor", [25, 5], 0, -1, 100)]
    pocao = item.Item(pocao_efeito, [], preco, quantidade, "Poção de Cura Pequena",
        singular_plural = "singular", genero = "F",
        descricao = "Cura 25% do HP máximo ou 5 de HP, o que for maior.")
    
    return ("Consumivel", pocao)

def PocaoManaPequena(quantidade, preco):
    """
    Cria <quantidade> de itens consumíveis, com preço igual à <preco>, que:
    * Curam 25% da mana máxima ou 5 de mana, o que for maior
    """

    pocao_efeito = [efeito.Efeito("Cura Mana % ou valor", [25, 5], 0, -1, 100)]
    pocao = item.Item(pocao_efeito, [], preco, quantidade, "Poção de Mana Pequena",
        singular_plural = "singular", genero = "F",
        descricao = "Cura 25% da Mana máxima ou 5 de Mana, o que for maior.")

    return ("Consumivel", pocao)

def Antidoto(quantidade, preco):
    """
    Cria <quantidade> de itens consumíveis, com preço igual à <preco>, que:
    * Curam debuff de Veneno
    """

    antidoto_efeito = [efeito.Efeito("Cura Veneno", 0, 0, -1, 100)]
    antidoto = item.Item(antidoto_efeito, [], preco, quantidade, "Antídoto",
        singular_plural = "singular", genero = "M",
        descricao = "Cura o debuff de envenenamento.")
    
    return ("Consumivel", antidoto)

def BombaInferior(quantidade, preco):
    """
    Cria <quantidade> de itens consumíveis, com preço igual à <preco>, que:
    * Dão 5 de dano em todos os inimigos
    """

    bomba_efeito = [efeito.Efeito("Dano todos inimigos", 5, 0, -1, 100)]
    bomba = item.Item(bomba_efeito, [], preco, quantidade, "Bomba Inferior",
        singular_plural = "singular", genero = "F",
        descricao = "Dá 5 de dano em todos os inimigos.")
    
    return ("Consumivel", bomba)
