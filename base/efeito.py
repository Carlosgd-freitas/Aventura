class Efeito():
    """
    Esta classe é utilizada para efeitos de buff e debuff.
    """

    def __init__(self, nome = "default", valor = 0, decaimento = 0, duracao = 0, chance = 100,
        singular_plural = "default", genero = "default"):
        """
        Inicializador da classe.
        """
        # Nome do Efeito
        self.nome = nome

        # Valor do Efeito
        self.valor = valor

        # Quanto o valor irá decair a cada turno
        self.decaimento = decaimento
        
        # Quantos turnos o efeito irá perdurar. Se igual a -1, o efeito é instantâneo.
        self.duracao = duracao

        # Qual é chance deste efeito acontecer, em %
        self.chance = chance

        # Se o nome do efeito é em singular ou plural
        self.singular_plural = singular_plural

        # Se o nome do efeito é masculino ou feminino
        self.genero = genero
    
    def __str__(self):
        """
        Converte a classe em uma string.
        """
        return f'Nome: {self.nome}, Valor: {self.valor}, Decaimento: {self.decaimento}, Duração: {self.duracao}, Chance: {self.chance}, ' + \
            f'singular_plural: {self.singular_plural}, Gênero: {self.genero}'

    def CombinarEfeito(self, efeito):
        """
        Combina os atributos de si mesmo com os de um outro efeito.
        """

        if self.nome == 'Veneno' and efeito.nome == 'Veneno':
            self.valor += efeito.valor
            self.duracao += efeito.duracao
            self.chance += efeito.chance
