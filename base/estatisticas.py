from datetime import datetime, timedelta

class Estatisticas():
    """
    Esta classe serve para armazenar estatísticas relacionadas ao jogador e ao jogo.
    """

    def __init__(self):
        """
        Inicializador da classe.
        """
        self.batalhas_ganhas = 0

        self.data_jogo_salvo = None
        self.data_inicio = None
        self.tempo_total_jogado = timedelta(seconds = 0)
    
    def Atualizar(self):
        """
        Se um objeto da classe Estatisticas não possui um dos atributos da classe, então um atributo é criado
        com o valor padrão.
        """
        if not hasattr(self, 'batalhas_ganhas'):
            self.batalhas_ganhas = 0
        if not hasattr(self, 'data_jogo_salvo'):
            self.data_jogo_salvo = None
        if not hasattr(self, 'data_inicio'):
            self.data_inicio = None
        if not hasattr(self, 'tempo_total_jogado'):
            self.tempo_total_jogado = timedelta(seconds = 0)

    def ContabilizarTempoJogado(self):
        """
        Incrementa o tempo total jogado.
        """
        self.tempo_total_jogado += datetime.now() - self.data_inicio
