class Habilidade():
    """
    Esta classe é utilizada para habilidades passivas e ativas.
    """

    def __init__(self, nome = "default", descricao = "default", tipo = "default", alvo = "default",
                passiva_ativa = "default", valor = 0, custo = [], recarga = 0, recarga_atual = 0, 
                modificadores = [], efeitos = [], singular_plural = "default", genero = "default",
                nao_causa_dano = False, chance_critico = 0.0, multiplicador_critico = 1.0):
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

        # Se o nome da habilidade é em singular ou plural
        self.singular_plural = singular_plural

        # Se o nome da habilidade é masculino ou feminino
        self.genero = genero

        # Se a habilidade causa dano ou não
        self.nao_causa_dano = nao_causa_dano

        # Chance da habilidade causar um crítico
        self.chance_critico = chance_critico

        # Multiplicador do crítico que irá afetar a habilidade
        self.multiplicador_critico = multiplicador_critico

    def ClonarHabilidade(self):
        """
        Cria e retorna uma nova habilidade que possui os atributos com os mesmos valores desta.
        """

        nome = self.nome
        descricao = self.descricao
        tipo = self.tipo
        alvo = self.alvo
        passiva_ativa = self.passiva_ativa
        valor = self.valor
        nao_causa_dano = self.nao_causa_dano

        recarga = self.recarga
        recarga_atual = self.recarga_atual

        singular_plural = self.singular_plural
        genero = self.genero

        chance_critico = self.chance_critico
        multiplicador_critico = self.multiplicador_critico
        
        custo = []
        for c in self.custo:
            custo.append(c)

        modificadores = []
        for m in self.modificadores:
            modificadores.append(m)
        
        efeitos = []
        for e in self.efeitos:
            efeitos.append(e)

        habilidade_2 = Habilidade(nome, descricao, tipo, alvo, passiva_ativa, valor, custo, recarga, recarga_atual, 
            modificadores, efeitos, singular_plural, genero, nao_causa_dano, chance_critico, multiplicador_critico)

        return habilidade_2
