class Base():
    """
    Esta classe serve de base para outras classes.
    """

    def __init__(self, nome = "default", descricao = "default", tipo = "default", nivel = 0, experiencia = 0,
                maxHp = 0, hp = 0, maxMana = 0, mana = 0, ataque = 0, defesa = 0, magia = 0, velocidade = 0,
                singular_plural = "default", genero = "default"):
        """
        Inicializador da classe.
        """
        self.nome = nome
        self.descricao = descricao
        self.tipo = tipo
        self.nivel = nivel
        self.experiencia = experiencia
        self.maxHp = maxHp
        self.hp = hp
        self.maxMana = maxMana
        self.mana = mana
        self.ataque = ataque
        self.defesa = defesa
        self.magia = magia
        self.velocidade = velocidade
        self.singular_plural = singular_plural
        self.genero = genero
