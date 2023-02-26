from . import utils
from abc import abstractmethod

class Area():
    """
    Esta classe é utilizada para áreas presentes no jogo.
    """

    def __init__(self, nome = "default", lojas_itens = [], estalagem_preco = 9999999):
        """
        Inicializador da classe.
        """
        # Nome da Área
        self.nome = nome

        # Cada elemento da lista 'lojas_itens' é uma lista que contém os itens disponíveis para a venda
        # nas respectivas lojas da área
        self.lojas_itens = lojas_itens
        
        # Preço da estalagem na primeira opção do evento de descanso
        self.estalagem_preco = estalagem_preco

    def __str__(self):
        """
        Converte a classe em uma string.
        """
        string = f'Nome: {self.nome}\n'
        string += 'Itens das Lojas:\n'
        if len(self.lojas_itens) == 0:
            string += '[]\n'
        else:
            string += '[\n'
            for loja_itens in self.lojas_itens:
                string += utils.ListaEmString(loja_itens) + '\n'
            string += ']\n'
        string += f'Preço da Estalagem: {self.estalagem_preco}'
        return string
    
    # Métodos Abstratos

    @abstractmethod
    def RetornarEncontro(self, jogador):
        """
        Retorna uma lista de criaturas inimigas.
        """

        pass

    @abstractmethod
    def EncontroChefe(self, jogador, est, conf):
        """
        Gerencia o encontro com o chefão da área.
        """

        pass

    @abstractmethod
    def MenuVila(self, jogador, est, conf, caminhos, save_carregado = False):
        """
        Menu referente ao que o jogador pode fazer quando está presente na vila/cidade da área.
        """

        pass

    @abstractmethod
    def EstoqueInicial(self):
        """
        Retorna uma lista de listas, onde cada lista é o conjunto inicial de itens disponíveis para venda em
        uma loja presente na área. Este método também será chamado quando a loja for reestocada.
        """

        pass

    @abstractmethod
    def Estalagem(self, jogador):
        """
        Menu principal de uma estalagem presente na área.
        """

        pass
    
    @abstractmethod
    def EventoVendedorAmbulante(self, jogador, conf):
        """
        Uma loja que irá selecionar aleatoriamente alguns itens para serem vendidos ao jogador. Retorna True
        se o jogador comprou ou vendeu algo e False caso contrário.
        """

        pass

