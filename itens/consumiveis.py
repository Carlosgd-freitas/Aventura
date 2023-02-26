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
    erva = item.Item(buffs = [erva_efeito],
        debuffs = [],
        preco = preco,
        quantidade = quantidade,
        classe = "Poção",
        classe_batalha = "Consumível",
        fora_batalha = True,
        alvo = "Próprio",
        nome = "Erva Curativa",
        tipo = "Terrestre",
        singular_plural = "singular",
        genero = "F",
        descricao = "Uma planta medicinal utilizada na fabricação de poções curativas. Quando crianças estão " + 
            "brincando e se machucam, pais cuidadosos as\nfazem mascarem essa erva, apesar de seu gosto amargo.")
    return erva

def MelAbelhoide(quantidade, preco):
    """
    Cria <quantidade> de itens consumíveis, com preço igual à <preco>, que:
    * Regenera 2 de hp por 3 turnos
    """
    mel_efeito = efeito.Efeito("Regeneração HP", 2, 1, 3, 100)
    mel = item.Item(buffs = [mel_efeito],
        debuffs = [],
        preco = preco,
        quantidade = quantidade,
        classe = "Poção",
        classe_batalha = "Consumível",
        fora_batalha = True,
        alvo = "Próprio",
        nome = "Mel de Abelhóide",
        tipo = "Normal",
        singular_plural = "singular",
        genero = "M",
        descricao = "As abelhóides produzem esse mel após coletarem polén das plantas próximas a colméia em que " +
            "habitam.")
    return mel

# Poções
def PocaoPequenaCura(quantidade, preco):
    """
    Cria <quantidade> de itens consumíveis, com preço igual à <preco>, que:
    * Curam 25% do hp máximo ou 5 de hp, o que for maior
    """
    pocao_efeito = efeito.Efeito("Cura HP % ou valor", [25, 5], 0, -1, 100)
    pocao = item.Item(buffs = [pocao_efeito],
        debuffs = [],
        preco = preco,
        quantidade = quantidade,
        classe = "Poção",
        classe_batalha = "Consumível",
        fora_batalha = True,
        alvo = "Próprio",
        nome = "Poção Pequena de Cura",
        tipo = "Normal",
        singular_plural = "singular",
        genero = "F",
        descricao = "A poção curativa de preparo mais básico - comumente utilizada como tutorial para botanistas " +
            "e alquimistas iniciantes.")
    return pocao

def PocaoPequenaMana(quantidade, preco):
    """
    Cria <quantidade> de itens consumíveis, com preço igual à <preco>, que:
    * Curam 25% da mana máxima ou 5 de mana, o que for maior
    """
    pocao_efeito = efeito.Efeito("Cura Mana % ou valor", [25, 5], 0, -1, 100)
    pocao = item.Item(buffs = [pocao_efeito],
        debuffs = [],
        preco = preco,
        quantidade = quantidade,
        classe = "Poção",
        classe_batalha = "Consumível",
        fora_batalha = True,
        alvo = "Próprio",
        nome = "Poção Pequena de Mana",
        tipo = "Normal",
        singular_plural = "singular",
        genero = "F",
        descricao = "Uma pequena mudança no preparo de uma poção de cura fará com que o usuário recupere sua mana" +
            " em vez de fechar suas feridas. Este princípio básico\nda magia foi revolucionário na época, mas o que" +
            " tinha chamado atenção mesmo foi que a poção mudou de cor para azul.")
    return pocao

def PocaoPequenaRegeneracao(quantidade, preco):
    """
    Cria <quantidade> de itens consumíveis, com preço igual à <preco>, que:
    * Regenera 10% do hp máximo por 3 turnos
    """
    pocao_efeito = efeito.Efeito("Regeneração HP %", 10, 1, 3, 100)
    pocao = item.Item(buffs = [pocao_efeito],
        debuffs = [],
        preco = preco,
        quantidade = quantidade,
        classe = "Poção",
        classe_batalha = "Consumível",
        fora_batalha = True,
        alvo = "Próprio",
        nome = "Poção Pequena de Regeneração",
        tipo = "Normal",
        singular_plural = "singular",
        genero = "F",
        descricao = "Ao retardar o efeito de cura, o usuário irá se sentir mais recuperado no fim das contas. Dê " +
            "tempo ao tempo ou algo do tipo.")
    return pocao

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
    elixir = item.Item(buffs = [elixir_efeito],
        debuffs = [],
        preco = preco,
        quantidade = quantidade,
        classe = "Elixir",
        classe_batalha = "Consumível",
        fora_batalha = False,
        alvo = "Próprio",
        nome = "Elixir Pequeno de " + atributo,
        tipo = "Normal",
        singular_plural = "singular",
        genero = "M",
        descricao = descricao)
    return elixir

# Miscelâneo
def Antidoto(quantidade, preco):
    """
    Cria <quantidade> de itens consumíveis, com preço igual à <preco>, que:
    * Curam debuff de Veneno
    """
    antidoto_efeito = efeito.Efeito("Cura Veneno", 0, 0, -1, 100)
    antidoto = item.Item(buffs = [antidoto_efeito],
        debuffs = [],
        preco = preco,
        quantidade = quantidade,
        classe = "Antídoto",
        classe_batalha = "Consumível",
        fora_batalha = True,
        alvo = "Próprio",
        nome = "Antídoto",
        tipo = "Normal",
        singular_plural = "singular",
        genero = "M",
        descricao = "Apesar de parecer simples, este andídoto é efetivo contra o envenenamento causado pelas mais" +
            " variadas espécies.")
    return antidoto

# Bombas
def BombaInferior(quantidade, preco):
    """
    Cria <quantidade> de itens consumíveis, com preço igual à <preco>, que:
    * Dão 5 de dano em todos os inimigos
    """
    bomba_efeito = efeito.Efeito("Dano", 5, 0, -1, 100)
    bomba = item.Item(buffs = [],
        debuffs = [bomba_efeito],
        preco = preco,
        quantidade = quantidade,
        classe = "Bomba",
        classe_batalha = "Consumível",
        fora_batalha = False,
        alvo = "Inimigos",
        nome = "Bomba Inferior",
        tipo = "Normal",
        singular_plural = "singular",
        genero = "F",
        descricao = "Uma esfera metálica recheada de pólvora.")
    return bomba

def BombaGrudentaInferior(quantidade, preco):
    """
    Cria <quantidade> de itens consumíveis, com preço igual à <preco>, que:
    * Dão 3 de dano em todos os inimigos
    * Dão 5 turnos de lentidão em todos os inimigos
    """
    bomba_dano = efeito.Efeito("Dano", 5, 0, -1, 100)
    bomba_lentidao = efeito.Efeito("Lentidão", 0, 1, 5, 100)

    bomba = item.Item(buffs = [],
        debuffs = [bomba_dano, bomba_lentidao],
        preco = preco,
        quantidade = quantidade,
        classe = "Bomba",
        classe_batalha = "Consumível",
        fora_batalha = False,
        alvo = "Inimigos",
        nome = "Bomba Grudenta Inferior",
        tipo = "Normal",
        singular_plural = "singular",
        genero = "F",
        descricao = "Além de causar dano igual a uma bomba comum, seu conteúdo pegajoso fará com que os " +
            "inimigos tenham dificuldade em tentar te matar rápido.")
    return bomba
