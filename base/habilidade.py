import math
from . import utils

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

    def __str__(self):
        """
        Converte a classe em uma string.
        """
        string = f'Nome: {self.nome}\n'
        string += f'Tipo: {self.tipo}\n'
        string += f'Alvo: {self.alvo}\n'
        string += f'passiva_ativa: {self.passiva_ativa}\n'
        string += f'Valor: {self.valor}\n'
        string += f'Custo: {self.custo}\n'
        string += f'Recarga: {self.recarga}\n'
        string += f'Recarga Atual: {self.recarga_atual}\n'
        string += f'Modificadores:{self.modificadores}\n'
        string += f'singular_plural: {self.singular_plural}\n'
        string += f'Gênero: {self.genero}\n'
        string += f'Não causa dano: {self.nao_causa_dano}\n'
        string += f'Chance de Acerto Crítico: {self.chance_critico}\n'
        string += f'Multiplicador de Dano Crítico: {self.multiplicador_critico}\n'
        string += f'Descrição: {self.descricao}\n'
        string += 'Efeitos:\n'
        string += utils.ListaEmString(self.efeitos)
        return string

    def RetornarCusto(self, recurso):
        """
        Retorna o custo de algum recurso ao usar a habilidade.

        Parâmetros:
        - recurso: um recurso gasto ao usar uma habilidade, como 'Mana' ou 'Vida'.
        """

        for c in self.custo:
            if c[0] == recurso:
                return c[1]
        
        return 0

    def AlterarCusto(self, recurso, valor):
        """
        Altera o custo de algum recurso já presente ao usar a habilidade. Não adiciona recursos novos no custo
        da habilidade.

        Parâmetros:
        - recurso: um recurso gasto ao usar uma habilidade, como 'Mana' ou 'HP';
        - valor: o novo custo do recurso.
        """

        novo = (recurso, valor)
        indice = 0
        existe = 0
        
        for c in self.custo:
            if c[0] == recurso:
                self.custo.pop(indice)
                existe = 1
                break
            indice += 1
        
        if existe == 1:
            self.custo.insert(indice, novo)
    
    def RetornarEfeito(self, nome, startswith = False):
        """
        Retorna um efeito causado pelo uso da habilidade, e None caso a habilidade não cause esse efeito.

        Parâmetros:
        - nome: nome de um efeito que a habilidade pode causar.
        """

        for e in self.efeitos:
            if (not startswith) and (e.nome == nome):
                return e
            elif e.nome.startswith(nome):
                return e
        
        return None
    
    def ContabilizarModificadores(self, valor, usuario):
        """
        Acrescenta os modificadores de uma habilidade em um valor, retornando o valor resultante.

        Parâmetros:
        - valor: valor base;
        - usuario: qual criatura (ou jogador) está usando a habilidade;
        - habilidade: habilidade que possui os modificadores.
        """
        saida = valor
        for m in self.modificadores:
            if m[0] == "ataque":
                saida += usuario.ataque * (m[1] / 100)
            elif m[0] == "defesa":
                saida += usuario.defesa * (m[1] / 100) 
            elif m[0] == "magia":
                saida += usuario.magia * (m[1] / 100)
            elif m[0] == "velocidade":
                saida += usuario.velocidade * (m[1] / 100) 
        saida = math.floor(saida)
        return saida
