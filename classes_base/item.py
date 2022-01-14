from . import basico

class Item(basico.Base):
    """
    Esta classe serve para itens consumíveis e equipamentos.
    """
    def __init__(self, buffs = [], debuffs = [], preco = 0, quantidade = 0, nome = "default", descricao = "default",
                tipo = "default", nivel = 0, experiencia = 0, maxHp = 0, hp = 0,  maxMana = 0, mana = 0, ataque = 0,
                defesa = 0, magia = 0, velocidade = 0):
        """
        Inicializador da classe.
        """
        # Uma lista de efeitos positivos que o Item concede
        self.buffs = buffs

        # Uma lista de efeitos negativos que o Item concede
        self.debuffs = debuffs

        # A quantidade de ouro que será ganha ou perdida quando o Item é vendido ou comprado, respectivamente
        self.preco = preco

        # Quantidade do Item
        self.quantidade = quantidade

        super(Item, self).__init__(nome, descricao, tipo, nivel, experiencia, maxHp, hp, maxMana, mana,
                                        ataque, defesa, magia, velocidade)
