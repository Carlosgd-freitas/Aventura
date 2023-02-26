from . import basico, utils

class Item(basico.Base):
    """
    Esta classe serve para itens consumíveis e equipamentos.
    """
    def __init__(self, buffs = [], debuffs = [], preco = 0, quantidade = 0, classe = "default",
        classe_batalha = "default", fora_batalha = False, alvo = "default", nome = "default",
        descricao = "default", tipo = "default", nivel = 0, experiencia = 0, maxHp = 0, hp = 0,
        maxMana = 0, mana = 0, ataque = 0, defesa = 0, magia = 0, velocidade = 0, singular_plural = "default",
        genero = "default", chance_critico = 0.0, multiplicador_critico = 1.0):
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

        # Classe do Item (Poção, Espada, Cajado...)
        self.classe = classe

        # Classe do Item em Batalha (Consumível, Peitoral, Uma Mão...)
        self.classe_batalha = classe_batalha

        # Se o item pode ser usado fora de batalha
        self.fora_batalha = fora_batalha

        # Alvo do uso de um item consumível
        self.alvo = alvo

        super(Item, self).__init__(nome, descricao, tipo, nivel, experiencia, maxHp, hp, maxMana, mana,
            ataque, defesa, magia, velocidade, singular_plural, genero, chance_critico, multiplicador_critico)

    def __str__(self):
        """
        Converte a classe em uma string.
        """
        string = f'Nome: {self.nome}\n'
        string += f'Tipo: {self.tipo}\n'
        string += f'Nível: {self.nivel}\n'
        string += f'Experiência: {self.experiencia}\n'
        string += f'HP Máximo: {self.maxHp}\n'
        string += f'HP: {self.hp}\n'
        string += f'Mana Máxima: {self.maxMana}\n'
        string += f'Mana: {self.mana}\n'
        string += f'Ataque:{self.ataque}\n'
        string += f'Defesa: {self.defesa}\n'
        string += f'Magia: {self.magia}\n'
        string += f'Velocidade: {self.velocidade}\n'
        string += f'Chance de Acerto Crítico: {self.chance_critico}\n'
        string += f'Multiplicador de Dano Crítico: {self.multiplicador_critico}\n'
        string += f'singular_plural: {self.singular_plural}\n'
        string += f'Gênero: {self.genero}\n'
        string += f'Descrição: {self.descricao}\n'
        string += 'Buffs:\n'
        string += utils.ListaEmString(self.buffs) + '\n'
        string += 'Debuffs:\n'
        string += utils.ListaEmString(self.debuffs) + '\n'
        string += f'Preço: {self.preco}\n'
        string += f'Quantidade: {self.quantidade}\n'
        string += f'Classe: {self.classe}\n'
        string += f'classe_batalha: {self.classe_batalha}\n'
        string += f'fora_batalha: {self.fora_batalha}\n'
        string += f'Alvo: {self.alvo}'
        return string

    def EfeitoPresente(self, efeito_nome):
        """
        Retorna o primeiro efeito com nome <efeito_nome> presente no item, e retorna None caso o
        item não possua este efeito.
        """

        for e in self.buffs:
            if e.nome == efeito_nome:
                return e
        for e in self.debuffs:
            if e.nome == efeito_nome:
                return e
        return None
    