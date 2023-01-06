from . import basico

class Item(basico.Base):
    """
    Esta classe serve para itens consumíveis e equipamentos.
    """
    def __init__(self, buffs = [], debuffs = [], preco = 0, quantidade = 0, classificacao = "default",
        fora_batalha = False, nome = "default", descricao = "default", tipo = "default", nivel = 0,
        experiencia = 0, maxHp = 0, hp = 0,  maxMana = 0, mana = 0, ataque = 0, defesa = 0, magia = 0,
        velocidade = 0, singular_plural = "default", genero = "default", chance_critico = 0.0,
        multiplicador_critico = 1.0):
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

        # Classificação do Item (Consumível, Peitoral, Uma Mão...)
        self.classificacao = classificacao

        # Se o item pode ser usado fora de batalha
        self.fora_batalha = fora_batalha

        super(Item, self).__init__(nome, descricao, tipo, nivel, experiencia, maxHp, hp, maxMana, mana,
            ataque, defesa, magia, velocidade, singular_plural, genero, chance_critico, multiplicador_critico)

    def ClonarItem(self):
        """
        Cria e retorna um novo item que possui os atributos com os mesmos valores deste.
        """

        preco = self.preco
        quantidade = self.quantidade
        classificacao = self.classificacao
        fora_batalha = self.fora_batalha

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
        chance_critico = self.chance_critico
        multiplicador_critico = self.multiplicador_critico

        singular_plural = self.singular_plural
        genero = self.genero
        
        buffs = []
        for b in self.buffs:
            b_2 = b.ClonarEfeito()
            buffs.append(b_2)

        debuffs = []
        for d in self.debuffs:
            d_2 = d.ClonarEfeito()
            debuffs.append(d_2)

        item_2 = Item(buffs, debuffs, preco, quantidade, classificacao, fora_batalha, nome, descricao, tipo,
            nivel, experiencia, maxHp, hp, maxMana, mana, ataque, defesa, magia, velocidade, singular_plural,
            genero, chance_critico, multiplicador_critico)

        return item_2
