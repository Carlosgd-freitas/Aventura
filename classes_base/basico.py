class Base():
    """
    Esta classe serve de base para outras classes.
    """

    def __init__(self, nome = "default", descricao = "default", tipo = "default", nivel = 0, experiencia = 0,
                maxHp = 0, hp = 0, maxMana = 0, mana = 0, ataque = 0, defesa = 0, magia = 0, velocidade = 0,
                singular_plural = "default", genero = "default", chance_critico = 0.0, multiplicador_critico = 1.0):
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
        self.chance_critico = chance_critico
        self.multiplicador_critico = multiplicador_critico

        self.singular_plural = singular_plural
        self.genero = genero

    def RetornarArtigo(self):
        """
        Retorna o artigo apropriado para o nome do componente em questão, com a primeira letra em maiúsculo.
        """

        if self.singular_plural == "singular":
            if self.genero == "M":
                return "O"
            elif self.genero == "F":
                return "A"

        elif self.singular_plural == "plural":
            if self.genero == "M":
                return "Os"
            elif self.genero == "F":
                return "As"
    
    def RetornarContracaoPor(self):
        """
        Retorna a contração da preposição 'por' + o artigo referente ao nome do componente em questão, com
        a primeira letra em maiúsculo.
        """

        if self.singular_plural == "singular":
            if self.genero == "M":
                return "Pelo"
            elif self.genero == "F":
                return "Pela"

        elif self.singular_plural == "plural":
            if self.genero == "M":
                return "Pelos"
            elif self.genero == "F":
                return "Pelas"
