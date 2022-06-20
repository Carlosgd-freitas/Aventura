import sys

sys.path.append("..")
from classes_base import efeito, item

def PocaoCuraPequena(quantidade, preco):
    """
    Cria <quantidade> de itens consumíveis, com preço igual à <preco>, que:
    * Curam 25% do hp máximo ou 5 de hp, o que for maior
    """

    pocao_efeito = [efeito.Efeito("Cura HP % ou valor", [25, 5], 0, -1, 100)]
    pocao = item.Item(pocao_efeito, [], preco, quantidade, "Poção de Cura Pequena", genero = "F",
        descricao = "Cura 25% do HP máximo ou 5 de HP, o que for maior.")
    
    return ("Consumivel", pocao)

def PocaoManaPequena(quantidade, preco):
    """
    Cria <quantidade> de itens consumíveis, com preço igual à <preco>, que:
    * Curam 25% da mana máxima ou 5 de mana, o que for maior
    """

    pocao_efeito = [efeito.Efeito("Cura Mana % ou valor", [25, 5], 0, -1, 100)]
    pocao = item.Item(pocao_efeito, [], preco, quantidade, "Poção de Mana Pequena", genero = "F",
        descricao = "Cura 25% da Mana máxima ou 5 de Mana, o que for maior.")

    return ("Consumivel", pocao)

def Antidoto(quantidade, preco):
    """
    Cria <quantidade> de itens consumíveis, com preço igual à <preco>, que:
    * Curam debuff de Veneno
    """

    antidoto_efeito = [efeito.Efeito("Cura Veneno", 0, 0, -1, 100)]
    antidoto = item.Item(antidoto_efeito, [], preco, quantidade, "Antídoto", genero = "M",
        descricao = "Cura o debuff de envenenamento.")
    
    return ("Consumivel", antidoto)

def BombaInferior(quantidade, preco):
    """
    Cria <quantidade> de itens consumíveis, com preço igual à <preco>, que:
    * Dão 5 de dano em todos os inimigos
    """

    bomba_efeito = [efeito.Efeito("Dano todos inimigos", 5, 0, -1, 100)]
    bomba = item.Item(bomba_efeito, [], preco, quantidade, "Bomba Inferior", genero = "F",
        descricao = "Dá 5 de dano em todos os inimigos.")
    
    return ("Consumivel", bomba)
