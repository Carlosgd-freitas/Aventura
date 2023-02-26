import sys
from colorama import Fore, Back, Style
from tabulate import tabulate

from . import criatura, guerreiro, mago, utils

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
        string = f'Nome: {self.nome}\n'
        string += f'Tipo: {self.tipo}\n'
        string += f'Nível: {self.nivel}\n'
        string += f'Experiência: {self.experiencia}\n'
        string += f'HP Máximo: {self.maxHp}\n'
        string += f'HP: {self.hp}\n'
        string += f'Mana Máxima: {self.maxMana}\n'
        string += f'Mana: {self.mana}\n'
        string += f'Ataque:{self.ataque}\n'
        string += f'Defesa: {self.defesa}\n'
        string += f'Magia: {self.magia}\n'
        string += f'Velocidade: {self.velocidade}\n'
        string += f'Chance de Acerto Crítico: {self.chance_critico}\n'
        string += f'Multiplicador de Dano Crítico: {self.multiplicador_critico}\n'
        string += f'singular_plural: {self.singular_plural}\n'
        string += f'Gênero: {self.genero}\n'
        string += f'Descrição: {self.descricao}\n'
        string += 'Buffs:\n'
        string += utils.ListaEmString(self.buffs) + '\n'
        string += 'Debuffs:\n'
        string += utils.ListaEmString(self.debuffs) + '\n'
        string += 'Habilidades:\n'
        string += utils.ListaEmString(self.habilidades) + '\n'
        string += 'Espólios:\n'
        if len(self.espolios) == 0:
            string += '[]\n'
        else:
            string += '[\n'
            for indice, espolio in enumerate(self.espolios):
                string += f'Chance de Drop: {espolio[0]}%\n'
                string += f'Drop: {espolio[1]}'
                if indice != len(self.espolios) - 1:
                    string += f',\n'
                string += "\n"
            string += ']\n'
        string += f'Classe: {self.classe}\n'
        string += f'Ouro: {self.ouro}\n'
        string += 'Inventário:\n'
        string += utils.ListaEmString(self.inventario) + '\n'
        string += 'Equipados:\n'
        string += utils.ListaEmString(self.equipados)
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

        # Nome do jogador + Possíveis Buffs/Debuffs
        tabela = []
        efeitos, n_efeitos = imprimir.RetornarEfeitos(self, espaco = False)

        l1 = []
        l1.append(self.nome)
        if n_efeitos > 0:
            alinhamento = ("center", "center")
            l1.append(efeitos)
        else:
            alinhamento = ("center",)
        tabela.append(l1)
        
        tabela = tabulate(tabela, colalign = alinhamento, tablefmt="grid")
        print(tabela)

        # Classe, Nível, Experiência, HP, Mana e Ouro do jogador
        tabela = []
        alinhamento = ("right", "right", "right", "right", "right", "right")

        # Linha 1: Classe + Nível + Experiência
        l1 = []
        l1.append("Classe")
        l1.append(self.classe)
        l1.append("Nível")
        l1.append(self.nivel)
        l1.append("Experiência")
        exp = self.ExperienciaSubirNivel(self.nivel)
        l1.append(f'{self.experiencia}/{exp}')
        tabela.append(l1)

        # Linha 2: HP + Mana + Ouro
        l2 = []
        l2.append(imprimir.RetornarStringColorida("HP"))
        l2.append(f'{self.hp}/{self.maxHp}')
        l2.append(imprimir.RetornarStringColorida("Mana"))
        l2.append(f'{self.mana}/{self.maxMana}')
        l2.append(imprimir.RetornarStringColorida("Ouro"))
        l2.append(self.ouro)
        tabela.append(l2)
        
        tabela = tabulate(tabela, colalign = alinhamento, tablefmt="grid")
        print(tabela)

        # Atributos do jogador
        tabela = []
        alinhamento = ("right", "right", "right", "right")

        # Linha 1: Ataque + Defesa
        l1 = []
        l1.append("ATAQUE")
        l1.append(self.ataque)
        l1.append("DEFESA")
        l1.append(self.defesa)
        tabela.append(l1)

        # Linha 2: Magia + Velocidade
        l2 = []
        l2.append("MAGIA")
        l2.append(self.magia)
        l2.append("VELOCIDADE")
        l2.append(self.velocidade)
        tabela.append(l2)

        # Linha 3: Chance de Acerto Crítico + Multiplicador de Dano Crítico
        l3 = []
        l3.append("CHANCE DE ACERTO CRÍTICO")
        l3.append('{:.2f}'.format(self.chance_critico) + '%')
        l3.append("MULTIPLICADOR DE DANO CRÍTICO")
        l3.append('{:.2f}'.format(self.multiplicador_critico) + 'x')
        tabela.append(l3)
        
        tabela = tabulate(tabela, colalign = alinhamento, tablefmt="grid")
        print(tabela)

        # Imprime os efeitos concedidos pelos equipamentos do jogador
        imprimir.ImprimirEfeitosEquipamentos(self)

    def AtributosBasicos(self):
        """
        Retorna um dicionário contendo os atributos maxHp, hp, maxMana, mana, ataque, defesa, magia, e 
        velocidade.
        """
        menu_equipamentos.EquipadosPerdas(self)
        atributos = {}
        atributos["maxHp"] = self.maxHp
        atributos["hp"] = self.hp
        atributos["maxMana"] = self.maxMana
        atributos["mana"] = self.mana
        atributos["ataque"] = self.ataque
        atributos["defesa"] = self.defesa
        atributos["magia"] = self.magia
        atributos["velocidade"] = self.velocidade
        menu_equipamentos.EquipadosGanhos(self)
        return atributos

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
                atributos_antes = self.AtributosBasicos()

                if self.classe == "Guerreiro" or self.classe == "Guerreira":
                    guerreiro.SubirNivelGuerreiro(self)
                elif self.classe == "Mago" or self.classe == "Maga":
                    mago.SubirNivelMago(self)
                
                atributos_depois = self.AtributosBasicos()
                imprimir.MensagemSubirNivel(atributos_antes, atributos_depois)
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

    def ContarItens(self, classe_batalha = None, nivel = None):
        """
        * Se nenhuma classe de batalha de item e nível de item forem passados por parâmetro, retorna o número
        de itens únicos presentes no inventário do jogador.
        * Se uma classe de batalha de item for passada por parâmetro, mas não um nível de item, retorna o número
        de itens únicos presentes no inventário do jogador que sejam daquela classe de batalha.
        * Se uma nível de item for passado por parâmetro, mas não uma classe de batalha de item, retorna o número
        de itens únicos presentes no inventário do jogador que possuam um nível igual ou inferior àquele nível.
        * Se uma classe de batalha de item e um nível de item forem passados por parâmetro, retorna o número de
        itens únicos presentes no inventário do jogador que sejam daquela classe de batalha e que possuam um nível
        igual ou inferior àquele nível.
        """

        cont = 0
        
        condicao_1 = classe_batalha is None and nivel is None
        condicao_2 = classe_batalha is not None and nivel is None
        condicao_3 = classe_batalha is None and nivel is not None
        condicao_4 = classe_batalha is not None and nivel is not None

        for item in self.inventario:

            if (condicao_1) or (condicao_2 and item.classe_batalha == classe_batalha) or (condicao_3 and item.nivel <= nivel) or (condicao_4 and item.classe_batalha == classe_batalha and item.nivel <= nivel):
                cont += 1
        
        return cont

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