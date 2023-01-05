import sys

sys.path.append("..")
from base import efeito, item

# Materiais
def ErvaCurativa(quantidade, preco):
    """
    Cria <quantidade> de itens consumíveis, com preço igual à <preco>, que:
    * Curam 3 de hp
    """

    erva_efeito = efeito.Efeito("Cura HP", 3, 0, -1, 100)
    erva = item.Item([erva_efeito], [], preco, quantidade, "Erva Curativa",
        singular_plural = "singular", genero = "F",
        descricao = "Uma planta medicinal utilizada na fabricação de poções curativas. Quando crianças estão " + 
            "brincando e se machucam, pais cuidadosos as fazem mascarem essa erva, apesar de seu gosto amargo.")
    
    return ("Consumivel", erva)

def MelAbelhoide(quantidade, preco):
    """
    Cria <quantidade> de itens consumíveis, com preço igual à <preco>, que:
    * Regenera 2 de hp por 3 turnos
    """

    mel_efeito = efeito.Efeito("Regeneração HP", 2, 1, 3, 100)
    mel = item.Item([mel_efeito], [], preco, quantidade, "Mel de Abelhóide",
        singular_plural = "singular", genero = "M",
        descricao = "As abelhóides produzem esse mel após coletarem polén das plantas próximas a colméia em que " +
            "habitam.")
    
    return ("Consumivel", mel)

# Poções
def PocaoPequenaCura(quantidade, preco):
    """
    Cria <quantidade> de itens consumíveis, com preço igual à <preco>, que:
    * Curam 25% do hp máximo ou 5 de hp, o que for maior
    """

    pocao_efeito = efeito.Efeito("Cura HP % ou valor", [25, 5], 0, -1, 100)
    pocao = item.Item([pocao_efeito], [], preco, quantidade, "Poção Pequena de Cura",
        singular_plural = "singular", genero = "F",
        descricao = "A poção curativa de preparo mais básico - comumente utilizada como tutorial para botanistas " +
            "e alquimistas iniciantes.")
    
    return ("Consumivel", pocao)

def PocaoPequenaMana(quantidade, preco):
    """
    Cria <quantidade> de itens consumíveis, com preço igual à <preco>, que:
    * Curam 25% da mana máxima ou 5 de mana, o que for maior
    """

    pocao_efeito = efeito.Efeito("Cura Mana % ou valor", [25, 5], 0, -1, 100)
    pocao = item.Item([pocao_efeito], [], preco, quantidade, "Poção Pequena de Mana",
        singular_plural = "singular", genero = "F",
        descricao = "Uma pequena mudança no preparo de uma poção de cura fará com que o usuário recupere sua mana" +
            " em vez de fechar suas feridas. Este princípio básico\nda magia foi revolucionário na época, mas o que" +
            " tinha chamado atenção mesmo foi que a poção mudou de cor para azul.")

    return ("Consumivel", pocao)

def PocaoPequenaRegeneracao(quantidade, preco):
    """
    Cria <quantidade> de itens consumíveis, com preço igual à <preco>, que:
    * Regenera 10% do hp máximo por 3 turnos
    """

    pocao_efeito = efeito.Efeito("Regeneração HP %", 10, 1, 3, 100)
    pocao = item.Item([pocao_efeito], [], preco, quantidade, "Poção Pequena de Regeneração",
        singular_plural = "singular", genero = "F",
        descricao = "Ao retardar o efeito de cura, o usuário irá se sentir mais recuperado no fim das contas. Dê " +
            "tempo ao tempo ou algo do tipo.")
    
    return ("Consumivel", pocao)

# Elixires
def ElixirPequeno(atributo, quantidade, preco):
    """
    Cria <quantidade> de itens consumíveis, com preço igual à <preco>, que:
    * Aumenta <atributo> em 3 por 5 turnos
    """

    if atributo == "Ataque":
        descricao = "Usagem proibida em competições esportivas."
    
    elif atributo == "Defesa":
        descricao = "Tortugas com certeza foram feridas durante a realização deste elixir."

    elif atributo == "Magia":
        descricao =  "Alguns indivíduos com pouco talento mágico tendem a ficar viciados em elixires de magia."

    elif atributo == "Velocidade":
        descricao = "Praticamente cafeína concentrada."

    elixir_efeito = efeito.Efeito("Aumento " + atributo, 3, 1, 5, 100)
    elixir = item.Item([elixir_efeito], [], preco, quantidade, "Elixir Pequeno de " + atributo,
        singular_plural = "singular", genero = "M", descricao = descricao)
    
    return ("Consumivel", elixir)

# Miscelâneo
def Antidoto(quantidade, preco):
    """
    Cria <quantidade> de itens consumíveis, com preço igual à <preco>, que:
    * Curam debuff de Veneno
    """

    antidoto_efeito = efeito.Efeito("Cura Veneno", 0, 0, -1, 100)
    antidoto = item.Item([antidoto_efeito], [], preco, quantidade, "Antídoto",
        singular_plural = "singular", genero = "M",
        descricao = "Apesar de parecer simples, este andídoto é efetivo contra o envenenamento causado pelas mais" +
            " variadas espécies.")
    
    return ("Consumivel", antidoto)

# Bombas
def BombaInferior(quantidade, preco):
    """
    Cria <quantidade> de itens consumíveis, com preço igual à <preco>, que:
    * Dão 5 de dano em todos os inimigos
    """

    bomba_efeito = efeito.Efeito("Dano todos inimigos", 5, 0, -1, 100)
    bomba = item.Item([], [bomba_efeito], preco, quantidade, "Bomba Inferior",
        singular_plural = "singular", genero = "F",
        descricao = "Uma esfera metálica recheada de pólvora.")
    
    return ("Consumivel", bomba)

def BombaGrudentaInferior(quantidade, preco):
    """
    Cria <quantidade> de itens consumíveis, com preço igual à <preco>, que:
    * Dão 3 de dano em todos os inimigos
    * Dão 5 turnos de lentidão em todos os inimigos
    """

    bomba_dano = efeito.Efeito("Dano todos inimigos", 3, 0, -1, 100)
    bomba_lentidao = efeito.Efeito("Lentidão todos inimigos", 0, 1, 5, 100)

    bomba = item.Item([], [bomba_dano, bomba_lentidao], preco, quantidade, "Bomba Grudenta Inferior",
        singular_plural = "singular", genero = "F",
        descricao = "Apesar de causar menos dano que uma bomba comum, seu conteúdo pegajoso fará com que os " +
            "inimigos tenham dificuldade em tentar te matar rápido.")
    
    return ("Consumivel", bomba)
