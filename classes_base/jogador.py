from colorama import Fore, Back, Style

from . import criatura, guerreiro, mago

class Jogador(criatura.Criatura):
    """
    Esta classe serve para o jogador.
    """
    def __init__(self, nome = "default", classe = "default", nivel = 0, experiencia = 0, ouro = 0, maxHp = 0,
        hp = 0, maxMana = 0, mana  = 0, ataque  = 0, defesa  = 0, magia  = 0, velocidade  = 0, habilidades = [],
        equipados = [], inventario  = []):
        """
        Cria um jogador novo.
        """
        # Classe do Jogador (Guerreiro, Mago, etc.)
        self.classe = classe

        # Quantidade inicial de ouro do Jogador
        self.ouro = ouro

        # Inventário do Jogador
        self.inventario = inventario

        # Equipamentos atualmente equipados do Jogador
        self.equipados = equipados

        super(Jogador, self).__init__([], [], habilidades, [], nome, "default", "Normal", nivel, experiencia,
            maxHp, hp, maxMana, mana, ataque, defesa, magia, velocidade)

    def AdicionarAoInventario(self, novo_item):
        """
        Recebe uma tupla (X, Y), onde X é a classificação do item ("Consumível", "Material", etc.) e Y é o item em
        si e, caso o item já esteja presente no inventário, sua quantidade é aumentada, e caso contrário, ele é
        adicionado normalmente ao inventário.
        """

        for item in self.inventario:
            if item[1].nome == novo_item[1].nome:
                item[1].quantidade += novo_item[1].quantidade
                return
        
        self.inventario.append(novo_item)

    def ExperienciaSubirNivel(self, nivel):
        """
        Retorna a quantidade de experiência necessária para o jogador subir do nível passado por parâmetro para o
        próximo.
        """

        if nivel == 1:
            return 5
        elif nivel == 2:
            return 10
        elif nivel == 3:
            return 20
        elif nivel == 4:
            return 35
        elif nivel == 5:
            return 50

    def ImprimirStatus(self):
        """
        Imprime os atributos do jogador na situação atual.
        """

        # Nome, classe e nível do jogador
        print(f'\n{self.nome} - Classe: {self.classe} - Nível: {self.nivel} - ', end = '')

        # Experiência do jogador
        exp = self.ExperienciaSubirNivel(self.nivel)
        print(f'Experiência: {self.experiencia}/{exp}')

        # HP do jogador
        mensagem = Fore.RED + 'HP' + Style.RESET_ALL + f' {self.hp}/{self.maxHp} - '

        # Mana do jogador
        mensagem += Fore.BLUE + 'Mana' + Style.RESET_ALL + f' {self.mana}/{self.maxMana} - '

        # Ouro do jogador
        mensagem += Fore.YELLOW + 'Ouro' + Style.RESET_ALL + f': {self.ouro}'
        print(mensagem + '\n')

        # Atributos do jogador
        print(f'ATAQUE: {self.ataque}')
        print(f'DEFESA: {self.defesa}')
        print(f'MAGIA: {self.magia}')
        print(f'VELOCIDADE: {self.velocidade}')

    def SubirNivel(self):
        """
        Confere se o jogador pode tem a experiência necessária para subir de nível. Se tiver, também chama a função
        de subir de nível da classe do jogador. Retorna 1 caso o jogador tenha subido de nível e retorna 1 caso
        contrário.
        """

        subiu = 0
        exp_necessaria = self.ExperienciaSubirNivel(self.nivel)

        # Jogador tem a experiencia necessária
        if self.experiencia >= exp_necessaria:
            self.experiencia -= exp_necessaria
            self.nivel += 1

            print(f'\nVocê subiu para o nível {self.nivel}!')

            if self.classe == "Guerreiro":
                subiu = guerreiro.SubirNivelGuerreiro(self)
            elif self.classe == "Mago":
                subiu = mago.SubirNivelMago(self)
            
            subiu = 1
        
        return subiu

    def ItemPresente(self, item_nome):
        """
        Retorna o índice do inventário correspondente ao nome do item passado por parâmetro se o jogador possui
        aquele item e -1 caso contrário.
        """

        valor = -1
        indice = 0

        for i in self.inventario:
            if i[1].nome == item_nome:
                valor = indice
                break
            indice += 1

        return valor

    def ContarItens(self, classificacao = None, nivel = None):
        """
        * Se nenhuma classificação de item e nível de item forem passados por parâmetro, retorna o número de itens
        únicos presentes no inventário do jogador.
        * Se uma classificação de item for passada por parâmetro, mas não um nível de item, retorna o número de
        itens únicos presentes no inventário do jogador que sejam daquela classificação.
        * Se uma nível de item for passado por parâmetro, mas não uma classificação de item, retorna o número de
        itens únicos presentes no inventário do jogador que possuam um nível igual ou inferior àquele nível.
        * Se uma classificação de item e um nível de item forem passados por parâmetro, retorna o número de
        itens únicos presentes no inventário do jogador que sejam daquela classificação e que possuam um nível igual
        ou inferior àquele nível.
        """

        cont = 0
        
        condicao_1 = classificacao is None and nivel is None
        condicao_2 = classificacao is not None and nivel is None
        condicao_3 = classificacao is None and nivel is not None
        condicao_4 = classificacao is not None and nivel is not None

        for item in self.inventario:

            if (condicao_1) or (condicao_2 and item[0] == classificacao) or (condicao_3 and item[1].nivel <= nivel) or (condicao_4 and item[0] == classificacao and item[1].nivel <= nivel):
                cont += 1
        
        return cont

    def ClonarLista(self, lista):
        """
        Cria e retorna uma novo lista de itens que possui os mesmos itens da passada por parâmetro, com
        os mesmos valores.
        """

        nova_lista = []

        for item in lista:
            item_clonado = (item[0], item[1].ClonarItem())
            nova_lista.append(item_clonado)

        return nova_lista
