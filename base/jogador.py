import sys
from colorama import Fore, Back, Style

from . import criatura, guerreiro, mago

sys.path.append("..")
from base import imprimir, configuracao
from menus import menu_inventario, menu_habilidades, menu_equipamentos

class Jogador(criatura.Criatura):
    """
    Esta classe serve para o jogador.
    """
    def __init__(self, nome = "default", classe = "default", nivel = 0, experiencia = 0, ouro = 0, maxHp = 0,
        hp = 0, maxMana = 0, mana  = 0, ataque  = 0, defesa  = 0, magia  = 0, velocidade  = 0, habilidades = [],
        equipados = [], inventario  = [], singular_plural = "default", genero = "default", chance_critico = 0.0,
        multiplicador_critico = 1.0):
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
            maxHp, hp, maxMana, mana, ataque, defesa, magia, velocidade, singular_plural, genero, chance_critico,
            multiplicador_critico)

    def __str__(self):
        """
        Converte a classe em uma string.
        """
        string = f'Nome: {self.nome}, Tipo: {self.tipo}, Nível: {self.nivel}, Experiência: {self.experiencia}, HP Máximo: {self.maxHp}, HP: {self.hp}, ' + \
            f'Mana Máxima: {self.maxMana}, Mana: {self.mana}\n' + \
            f'Ataque: {self.ataque}, Defesa: {self.defesa}, Magia: {self.magia}, Velocidade: {self.velocidade}, Chance de Acerto Crítico: {self.chance_critico}, ' + \
            f'Multiplicador de Dano Crítico: {self.multiplicador_critico}\n' + \
            f'singular_plural: {self.singular_plural}, Gênero: {self.genero}\n' + \
            f'Descrição: {self.descricao}\n'
        string += 'Buffs:\n'
        for i, b in enumerate(self.buffs):
            string += '* ' + str(b)
            if i != len(self.buffs) - 1:
                string += '\n'
        string += 'Debuffs:\n'
        for i, d in enumerate(self.debuffs):
            string += '* ' + str(d)
            if i != len(self.debuffs) - 1:
                string += '\n'
        string += 'Habilidades:\n'
        for i, h in enumerate(self.habilidades):
            string += '* ' + str(h)
            if i != len(self.habilidades) - 1:
                string += '\n'
        string += 'Espólios:\n'
        for i, (e0, e1) in enumerate(self.espolios):
            string += f'* {e0}% de chance: {e1}'
            if i != len(self.espolios) - 1:
                string += '\n'
        string += f'Classe: {self.classe}, Ouro: {self.ouro}\n'
        string += 'Inventário:\n'
        for i, it in enumerate(self.inventario):
            string += '* ' + str(it)
            if i != len(self.inventario) - 1:
                string += '\n'
        string += 'Equipados:\n'
        for i, eq in enumerate(self.equipados):
            string += '* ' + str(eq)
            if i != len(self.equipados) - 1:
                string += '\n'

        return string

    def AdicionarAoInventario(self, novo_item):
        """
        Recebe uma tupla (X, Y), onde X é a classificação do item ("Consumível", "Material", etc.) e Y é o item em
        si e, caso o item já esteja presente no inventário, sua quantidade é aumentada, e caso contrário, ele é
        adicionado normalmente ao inventário.
        """

        for item in self.inventario:
            if item.nome == novo_item.nome:
                item.quantidade += novo_item.quantidade
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
        elif nivel == 6:
            return 80
        elif nivel == 7:
            return 135
        elif nivel == 8:
            return 210
        elif nivel == 9:
            return 300
        elif nivel == 10:
            return 400
        else:
            return 999999

    def ImprimirStatus(self):
        """
        Imprime o jogador fora de batalha.
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
        print(mensagem)

        # Possíveis Buffs/Debuffs
        n_efeitos = imprimir.ImprimirEfeitos(self, espaco = False)
        if n_efeitos > 0:
            print('')

        # Atributos do jogador
        print('    ATAQUE: {:2d}'.format(self.ataque), end = '')
        print(' |      CHANCE DE ACERTO CRÍTICO: {:.2f}'.format(self.chance_critico) + '%')

        print('    DEFESA: {:2d}'.format(self.defesa), end = '')
        print(' | MULTIPLICADOR DE DANO CRÍTICO: {:.2f}'.format(self.multiplicador_critico) + 'x')

        print('     MAGIA: {:2d}'.format(self.magia))
        print('VELOCIDADE: {:2d}'.format(self.velocidade))

        # Imprime os efeitos concedidos pelos equipamentos do jogador
        imprimir.ImprimirEfeitosEquipamentos(self)

    def SubirNivel(self):
        """
        Confere se o jogador tem a experiência necessária para subir de nível. Se tiver, a função de subir de nível
        da classe do jogador é chamada, e a condição para subir para o próximo nível é checada. Retorna a quantidade
        de níveis que o jogador subiu.
        """

        subiu = 0

        while True:
            exp_necessaria = self.ExperienciaSubirNivel(self.nivel)

            if self.experiencia >= exp_necessaria:
                self.experiencia -= exp_necessaria
                self.nivel += 1

                print('\nVocê subiu para o ', end = '')
                print(Style.BRIGHT + 'Nível ' + f'{self.nivel}' + Style.RESET_ALL, end = '')
                print('!')

                if self.classe == "Guerreiro" or self.classe == "Guerreira":
                    guerreiro.SubirNivelGuerreiro(self)
                elif self.classe == "Mago" or self.classe == "Maga":
                    mago.SubirNivelMago(self)
                
                subiu += 1
            
            else:
                break
        
        return subiu

    def ItemPresente(self, item_nome):
        """
        Retorna o índice do inventário correspondente ao nome do item passado por parâmetro se o jogador possui
        aquele item e -1 caso contrário.
        """

        valor = -1
        indice = 0

        for i in self.inventario:
            if i.nome == item_nome:
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

            if (condicao_1) or (condicao_2 and item.classificacao == classificacao) or (condicao_3 and item.nivel <= nivel) or (condicao_4 and item.classificacao == classificacao and item.nivel <= nivel):
                cont += 1
        
        return cont

    def ClonarLista(self, lista):
        """
        Cria e retorna uma novo lista de itens que possui os mesmos itens da passada por parâmetro, com
        os mesmos valores.
        """

        nova_lista = []

        for item in lista:
            item_clonado = item.ClonarItem()
            nova_lista.append(item_clonado)

        return nova_lista

def ReconhecerAcaoBasica(acao, jogador, conf):
    """
    Compara uma ação tomada pelo jogador fora de combate e a executa caso ela seja uma das ações básicas:
    status, inventário, habilidades ou equipamentos. Caso uma das ações básicas seja executada, retorna True,
    e caso contrário, retorna False.

    Parâmetros:
    - acao: ação do jogador a ser comparada;
    - jogador: objeto do jogador;
    - conf: configurações do usuário relativas ao jogo;
    """

    # Status do Jogador
    if configuracao.CompararAcao(acao, conf.tecla_status):
        jogador.ImprimirStatus()
        return True
    
    # Inventário do Jogador
    elif configuracao.CompararAcao(acao, conf.tecla_inventario):
        print('')

        if not jogador.inventario:
            print('Você não tem itens em seu inventário.')
        else:
            menu_inventario.MenuInventario(jogador)

        return True
    
    # Habilidades do Jogador
    elif configuracao.CompararAcao(acao, conf.tecla_habilidades):
        print('')

        if len(jogador.habilidades) == 1: # Jogador só possui a habilidade "Atacar"
            print('Você não tem habilidades.')
        else:
            menu_habilidades.MenuHabilidades(jogador)

        return True

    # Equipamentos do Jogador
    elif configuracao.CompararAcao(acao, conf.tecla_equipamentos):
        print('')
        menu_equipamentos.MenuEquipamentos(jogador)
        return True
    
    return False