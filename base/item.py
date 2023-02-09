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

    def __str__(self):
        """
        Converte a classe em uma string.
        """
        string = f'Nome: {self.nome}, Tipo: {self.tipo}, Nível: {self.nivel}, Experiência: {self.experiencia}, HP Máximo: {self.maxHp}, HP: {self.hp}, ' + \
            f'Mana Máxima: {self.maxMana}, Mana: {self.mana}\n' + \
            f'Ataque: {self.ataque}, Defesa: {self.defesa}, Magia: {self.magia}, Velocidade: {self.velocidade}, Chance de Acerto Crítico: {self.chance_critico}, ' + \
            f'Multiplicador de Dano Crítico: {self.multiplicador_critico}\n' + \
            f'singular_plural: {self.singular_plural}, Gênero: {self.genero}\n' + \
            f'Descrição: {self.descricao}\n'
        string += 'Buffs:\n'
        for i, b in enumerate(self.buffs):
            string += '* ' + str(b)
            if i != len(self.buffs) - 1:
                string += '\n'
        string += 'Debuffs:\n'
        for i, d in enumerate(self.debuffs):
            string += '* ' + str(d)
            if i != len(self.debuffs) - 1:
                string += '\n'
        string += f'Preço: {self.preco}, Quantidade: {self.quantidade}, Classificação: {self.classificacao}, fora_batalha: {self.fora_batalha}'

        return string
