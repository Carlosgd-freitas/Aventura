import sys

sys.path.append("..")
from base import item

# Item Vazio
def Vazio():
    """
    Cria um item vazio, utilizado quando o jogador não possui nenhum item equipado em uma classificação
    (Cabeça, Peitoral, etc).
    """

    vazio = item.Item([], [], 0, 1, "Item Vazio", False, "Item Vazio",
        descricao = "Esse texto não é pra aparecer durante o jogo kkkkk")
    
    return vazio

# Espadas
def EspadaEnferrujada(quantidade, preco):
    """
    Cria <quantidade> de itens equipáveis, com preço igual à <preco>, que oferecem:
    * 1 de Ataque
    """

    espada = item.Item([], [], preco, quantidade, "Uma Mão", False, "Espada Enferrujada",
        nivel = 1, tipo = "Normal", ataque = 1, singular_plural = "singular", genero = "F",
        descricao = "Uma espada velha que se enferrujou com o tempo.")
    
    return espada

def EspadaAco(quantidade, preco):
    """
    Cria <quantidade> de itens equipáveis, com preço igual à <preco>, que oferecem:
    * 2 de Ataque
    * Requerimento: Nível 2
    """

    espada = item.Item([], [], preco, quantidade, "Uma Mão", False, "Espada de Aço", nivel = 2, tipo = "Normal",
        ataque = 2, singular_plural = "singular", genero = "F",
        descricao = "Uma espada de aço de fácil manuseio.")
    
    return espada

# Cajados
def CajadoIniciante(quantidade, preco):
    """
    Cria <quantidade> de itens equipáveis, com preço igual à <preco>, que oferecem:
    * 1 de Magia
    """

    cajado = item.Item([], [], preco, quantidade, "Duas Mãos", False, "Cajado de Iniciante", nivel = 1,
        tipo = "Normal", magia = 1, singular_plural = "singular", genero = "M",
        descricao = "Um cajado de madeira imbuído com uma pequena quantidade de mana. Este tipo de cajado " +
        "é normalmente utilizado por iniciantes da magia.")

    return cajado

def CajadoAprendiz(quantidade, preco):
    """
    Cria <quantidade> de itens equipáveis, com preço igual à <preco>, que oferecem:
    * 2 de Magia
    * Requerimento: Nível 2
    """

    cajado = item.Item([], [], preco, quantidade, "Duas Mãos", False, "Cajado de Aprendiz", nivel = 2,
        tipo = "Normal", magia = 2, singular_plural = "singular", genero = "M",
        descricao = "Um cajado de madeira que possui uma pequena pedra azul que funciona como um catalisador de "+
        "mana.")

    return cajado

# Escudos
def BroquelMadeira(quantidade, preco):
    """
    Cria <quantidade> de itens equipáveis, com preço igual à <preco>, que oferecem:
    * 1 de Defesa
    * Requerimento: Nível 2
    """

    broquel = item.Item([], [], preco, quantidade, "Uma Mão", False, "Broquel de Madeira", nivel = 2,
        tipo = "Normal", defesa = 1, singular_plural = "singular", genero = "M",
        descricao = "Um broquel de madeira que pode te ajudar a resistir alguns ataques.")
    
    return broquel

# Chapéus
def ChapeuCouro(quantidade, preco):
    """
    Cria <quantidade> de itens equipáveis, com preço igual à <preco>, que oferecem:
    * 2 de HP e HP Máximo
    * Requerimento: Nível 1
    """

    chapeu = item.Item([], [], preco, quantidade, "Cabeça", False, "Chapéu de Couro", nivel = 1, tipo = "Normal", hp = 2, maxHp = 2,
        singular_plural = "singular", genero = "M",
        descricao = "Um chapéu de couro bovino que oferece o mínimo de proteção.")
    
    return chapeu

# Peitorais de Guerreiro
def PeitoralCouro(quantidade, preco):
    """
    Cria <quantidade> de itens equipáveis, com preço igual à <preco>, que oferecem:
    * 5 de HP e HP Máximo
    * Requerimento: Nível 3
    """

    peitoral = item.Item([], [], preco, quantidade, "Peitoral", False, "Peitoral de Couro", nivel = 3,
        tipo = "Normal", hp = 5, maxHp = 5, singular_plural = "singular", genero = "M",
        descricao = "Um peitoral de couro bovino que protege contra ataques frontais.")
    
    return peitoral

# Robes de Mago
def RobeAlgodao(quantidade, preco):
    """
    Cria <quantidade> de itens equipáveis, com preço igual à <preco>, que oferecem:
    * 5 de Mana e Mana Máxima
    * 1 de Velocidade
    * Requerimento: Nível 3
    """

    robe = item.Item([], [], preco, quantidade, "Peitoral", False, "Robe de Algodão", nivel = 3, tipo = "Normal",
        mana = 5, maxMana = 5, velocidade = 1, singular_plural = "singular", genero = "M",
        descricao = "Um robe confortável feito de algodão para ajudar o fluxo de mana a correr pelo seu corpo.")
    
    return robe

# Botas
def BotasCouro(quantidade, preco):
    """
    Cria <quantidade> de itens equipáveis, com preço igual à <preco>, que oferecem:
    * 1 de Velocidade
    * Requerimento: Nível 3
    """

    botas = item.Item([], [], preco, quantidade, "Pés", False, "Botas de Couro", nivel = 3, tipo = "Normal",
        velocidade = 1, singular_plural = "plural", genero = "F",
        descricao = "Um par de botas de couro bovino para proteger seus pés de pequenas adversidades do terreno.")
    
    return botas
