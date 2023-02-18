import sys

sys.path.append("..")
from base import item

def Ouro(quantidade):
    """
    Cria <quantidade> de ouro.
    """

    ouro = item.Item(nome = "Ouro", quantidade = quantidade, classe = "Ouro", classe_batalha = "Ouro",
        fora_batalha = False, singular_plural = "singular", genero = "M",
        descricao = "Peças de ouro aceitas como moeda por todo o mundo.")

    return ouro

def Experiencia(quantidade):
    """
    Cria <quantidade> de experiência.
    """

    exp = item.Item(nome = "Experiência", quantidade = quantidade, classe = "Experiência",
        classe_batalha = "Experiência", fora_batalha = False, singular_plural = "singular", genero = "F", 
        descricao = "Pontos de experiência acumulados após uma batalha.")

    return exp

def FluidoSlime(quantidade, preco):
    """
    Cria <quantidade> de Fluidos de Slime, com preço igual à <preco>.
    """

    fluido = item.Item(nome = "Fluido de Slime", quantidade = quantidade, preco = preco,
        classe = "Material", classe_batalha = "Material", fora_batalha = False, singular_plural = "singular",
        genero = "M",
        descricao = "Uma parte viscosa e um pouco ácida do interior de um Slime derrotado.")

    return fluido

def GlandulaVenenosa(quantidade, preco):
    """
    Cria <quantidade> de Glândulas Venenosas, com preço igual à <preco>.
    """

    glandula = item.Item(nome = "Glândula Venenosa", quantidade = quantidade, preco = preco,
        classe = "Material", classe_batalha = "Material", fora_batalha = False, singular_plural = "singular",
        genero = "F",
        descricao = "Uma glândula responsável por produzir veneno.")

    return glandula

def CarapacaTortuga(quantidade, preco):
    """
    Cria <quantidade> de Carapaças de Tortuga, com preço igual à <preco>.
    """

    casco = item.Item(nome = "Carapaça de Tortuga", quantidade = quantidade, preco = preco,
        classe = "Material", classe_batalha = "Material", fora_batalha = False, singular_plural = "singular",
        genero = "F",
        descricao = "A parte resistente do casco de uma Tortuga.")

    return casco

def RubiFogo(quantidade, preco):
    """
    Cria <quantidade> de Rubis de Fogo, com preço igual à <preco>.
    """

    rubi = item.Item(nome = "Rubi de Fogo", quantidade = quantidade, preco = preco,
        classe = "Material", classe_batalha = "Material", fora_batalha = False, singular_plural = "singular",
        genero = "M",
        descricao = "Uma pedra preciosa vermelha, útil para ferreiros, que emana magia do tipo Fogo.")

    return rubi
