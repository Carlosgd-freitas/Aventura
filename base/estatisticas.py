class Estatisticas():
    """
    Esta classe serve para armazenar estatísticas relacionadas ao jogador e ao jogo.
    """

    def __init__(self):
        """
        Inicializador da classe.
        """
        self.batalhas_ganhas = 0
    
    def Atualizar(self):
        """
        Se um objeto da classe Estatisticas não possui um dos atributos da classe, então um atributo é criado
        com o valor padrão.
        """
        if not hasattr(self, 'batalhas_ganhas'):
            self.batalhas_ganhas = 0
    