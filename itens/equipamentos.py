import sys

sys.path.append("..")
from base import efeito, item

# Item Vazio
def Vazio():
    """
    Cria um item vazio, utilizado quando o jogador não possui nenhum item equipado em uma classificação
    (Cabeça, Peitoral, etc).
    """

    vazio = item.Item([], [], 0, 1, "Item Vazio", "Item Vazio", False, "Item Vazio",
        descricao = "Esse texto não é pra aparecer durante o jogo kkkkk")
    
    return vazio

# Espadas
def EspadaEnferrujada(quantidade, preco):
    """
    Cria <quantidade> de itens equipáveis, com preço igual à <preco>, que oferecem:
    * 1 de Ataque
    """

    espada = item.Item([], [], preco, quantidade, "Espada", "Uma Mão", False, "Espada Enferrujada",
        nivel = 1, tipo = "Normal", ataque = 1, singular_plural = "singular", genero = "F",
        descricao = "Uma espada velha que se enferrujou com o tempo.")
    
    return espada

def EspadaFerro(quantidade, preco):
    """
    Cria <quantidade> de itens equipáveis, com preço igual à <preco>, que oferecem:
    * 2 de Ataque
    * Requerimento: Nível 2
    """

    espada = item.Item([], [], preco, quantidade, "Espada", "Uma Mão", False, "Espada de Ferro", nivel = 2,
        tipo = "Normal", ataque = 2, singular_plural = "singular", genero = "F",
        descricao = "Uma espada de ferro de fácil manuseio.")
    
    return espada

# Cajados
def CajadoIniciante(quantidade, preco):
    """
    Cria <quantidade> de itens equipáveis, com preço igual à <preco>, que oferecem:
    * 1 de Magia
    """

    cajado = item.Item([], [], preco, quantidade, "Cajado", "Duas Mãos", False, "Cajado de Iniciante", nivel = 1,
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

    cajado = item.Item([], [], preco, quantidade, "Cajado", "Duas Mãos", False, "Cajado de Aprendiz", nivel = 2,
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

    broquel = item.Item([], [], preco, quantidade, "Escudo", "Uma Mão", False, "Broquel de Madeira", nivel = 2,
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

    chapeu = item.Item([], [], preco, quantidade, "Chapéu", "Cabeça", False, "Chapéu de Couro", nivel = 1,
        tipo = "Normal", hp = 2, maxHp = 2, singular_plural = "singular", genero = "M",
        descricao = "Um chapéu de couro bovino que oferece o mínimo de proteção.")
    
    return chapeu

# Peitorais de Guerreiro
def PeitoralCouro(quantidade, preco):
    """
    Cria <quantidade> de itens equipáveis, com preço igual à <preco>, que oferecem:
    * 5 de HP e HP Máximo
    * Requerimento: Nível 3
    """

    peitoral = item.Item([], [], preco, quantidade, "Peitoral de Guerreiro", "Peitoral", False,
        "Peitoral de Couro", nivel = 3, tipo = "Normal", hp = 5, maxHp = 5, singular_plural = "singular",
        genero = "M",
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

    robe = item.Item([], [], preco, quantidade, "Robe de Mago", "Peitoral", False, "Robe de Algodão", nivel = 3,
        tipo = "Normal", mana = 5, maxMana = 5, velocidade = 1, singular_plural = "singular", genero = "M",
        descricao = "Um robe confortável feito de algodão para ajudar o fluxo de mana a correr pelo seu corpo.")
    
    return robe

# Botas
def BotasCouro(quantidade, preco):
    """
    Cria <quantidade> de itens equipáveis, com preço igual à <preco>, que oferecem:
    * 1 de Velocidade
    * Requerimento: Nível 3
    """

    botas = item.Item([], [], preco, quantidade, "Botas", "Pés", False, "Botas de Couro", nivel = 3,
        tipo = "Normal", velocidade = 1, singular_plural = "plural", genero = "F",
        descricao = "Um par de botas de couro bovino para proteger seus pés de pequenas adversidades do terreno.")
    
    return botas

# Acessórios
def AmuletoEsmeralda(quantidade, preco):
    """
    Cria <quantidade> de itens equipáveis, com preço igual à <preco>, que oferecem:
    * 50% de Resistência a Veneno
    * Requerimento: Nível 4
    """

    resistencia = efeito.Efeito("Resistência Veneno", 0.5, 0, 999, 100)
    amuleto = item.Item([resistencia], [], preco, quantidade, "Amuleto", "Acessório", False,
        "Amuleto de Esmeralda", nivel = 4, tipo = "Terrestre", singular_plural = "singular", genero = "M",
        descricao = "Este amuleto é adornado com Esmeraldas de Terra que foram imbuídas em magia reversa após a liberação de seus potenciais mágicos. O resultado é " +
            "que o\nportador do amuleto se torna resistente a efeitos de envenenamento.")
    
    return amuleto
