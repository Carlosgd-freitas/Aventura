class Efeito():
    """
    Esta classe é utilizada para efeitos de buff e debuff.
    """

    def __init__(self, nome = "default", valor = 0, decaimento = 0, duracao = 0, chance = 100):
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
        
    def ClonarEfeito(self):
        """
        Cria e retorna um novo efeito que possui os atributos com os mesmos valores deste.
        """

        nome = self.nome
        decaimento = self.decaimento
        duracao = self.duracao
        chance = self.chance

        valor = 0
        if isinstance(self.valor, (list)):
            valor = []
            for v in self.valor:
                valor.append(v)
        else:
            valor = self.valor

        efeito_2 = Efeito(nome, valor, decaimento, duracao, chance)

        return efeito_2
