import sys

sys.path.append("..")
from classes_base import item, utils

def Ouro(quantidade):
    """
    Cria <quantidade> de ouro.
    """

    ouro = item.Item(nome = "Ouro", quantidade = quantidade, singular_plural = "singular", genero = "M",
        descricao = "Peças de ouro aceitas como moeda por todo o mundo.")

    return ("Ouro", ouro)

def Experiencia(quantidade):
    """
    Cria <quantidade> de experiência.
    """

    exp = item.Item(nome = "Experiência", quantidade = quantidade, singular_plural = "singular", genero = "F", 
        descricao = "Pontos de experiência que se acumulam para subir o nível de uma criatura.")

    return ("Experiencia", exp)

def FluidoSlime(quantidade, preco):
    """
    Cria <quantidade> de Fluidos de Slime, com preço igual à <preco>.
    """

    fluido = item.Item(nome = "Fluido de Slime", quantidade = quantidade, preco = preco,
        singular_plural = "singular", genero = "M",
        descricao = "Uma parte viscosa e um pouco ácida do interior de um Slime derrotado.")

    return ("Material", fluido)

def GlandulaVenenosa(quantidade, preco):
    """
    Cria <quantidade> de Glândulas Venenosas, com preço igual à <preco>.
    """

    glandula = item.Item(nome = "Glândula Venenosa", quantidade = quantidade, preco = preco,
        singular_plural = "singular", genero = "F",
        descricao = "Uma glândula responsável por produzir veneno.")

    return ("Material", glandula)

def CarapacaTortuga(quantidade, preco):
    """
    Cria <quantidade> de Carapaças de Tortuga, com preço igual à <preco>.
    """

    casco = item.Item(nome = "Carapaça de Tortuga", quantidade = quantidade, preco = preco,
        singular_plural = "singular", genero = "F",
        descricao = "A parte resistente do casco de uma Tortuga.")

    return ("Material", casco)
