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

    def ClonarItem(self):
        """
        Cria e retorna um novo item que possui os atributos com os mesmos valores deste.
        """

        preco = self.preco
        quantidade = self.quantidade
        nome = self.nome
        descricao = self.descricao
        tipo = self.tipo
        nivel = self.nivel
        experiencia = self.experiencia
        maxHp = self.maxHp
        hp = self.hp
        maxMana = self.maxMana
        mana = self.mana
        ataque = self.ataque
        defesa = self.defesa
        magia = self.magia
        velocidade = self.velocidade
        
        buffs = []
        for b in self.buffs:
            b_2 = b.ClonarEfeito()
            buffs.append(b_2)

        debuffs = []
        for d in self.debuffs:
            d_2 = d.ClonarEfeito()
            debuffs.append(d_2)

        item_2 = Item(buffs, debuffs, preco, quantidade, nome, descricao, tipo, nivel, experiencia, maxHp, hp,
            maxMana, mana, ataque, defesa, magia, velocidade)

        return item_2