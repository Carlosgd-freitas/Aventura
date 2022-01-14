class Habilidade():
    """
    Esta classe é utilizada para habilidades passivas e ativas.
    """

    def __init__(self, nome = "default", descricao = "default", tipo = "default", alvo = "default",
                passiva_ativa = "default", valor = 0, custo = [], recarga = 0, recarga_atual = 0, 
                modificadores = [], efeitos = []):
        """
        Inicializador da classe.
        """
        # Nome da Habilidade
        self.nome = nome

        # Descrição da Habilidade
        self.descricao = descricao

        # Tipo da Habilidade
        self.tipo = tipo

        # Alvo da Habilidade
        self.alvo = alvo

        # Se a Habilidade é passiva ou ativa
        self.passiva_ativa = passiva_ativa

        # Valor do efeito principal da Habilidade (Dano, Cura, etc.)
        self.valor = valor

        # Uma lista de tuplas (X, Y), onde X é o recurso que será gasto e Y é a quantidade
        self.custo = custo

        # Em quantos turnos a Habilidade poderá ser utilizada novamente
        self.recarga = recarga

        # A criatura ou jogador ainda deve esperar (recarga - recarga_atual) turnos para usar a habilidade novamente
        self.recarga_atual = recarga_atual

        # Uma lista de tuplas (X, Y), onde X é um atributo da Criatura ou Jogador em questão e Y é a % de quanto
        # este atributo irá contribuir para com o valor desta Habilidade
        self.modificadores = modificadores 

        # Efeitos secundários que a Habilidade irá causar
        self.efeitos = efeitos
