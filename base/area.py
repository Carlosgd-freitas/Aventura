import math
import sys
from tabulate import tabulate
from abc import abstractmethod
from colorama import Fore, Back, Style

from . import imprimir, utils
sys.path.append("..")
from combate import batalha

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

    @abstractmethod
    def RetornarEncontro(self, jogador):
        """
        Retorna uma lista de criaturas inimigas.
        """

        pass

    @abstractmethod
    def EncontroChefe(self, jogador, conf):
        """
        Gerencia o encontro com o chefão da área.
        """

        pass

    @abstractmethod
    def MenuVila(self, jogador, caminhos):
        """
        Menu referente ao que o jogador pode fazer quando está presente na vila/cidade da área.
        """

        pass

    def PrecoItemMaisBarato(self, loja_itens):
        """
        Retorna o preço do item mais barato que se encontra na loja.
        """

        menor = 9999999

        for item in loja_itens:
            if item[1].preco < menor:
                menor = item[1].preco

        return menor

    def LojaMenu(self, jogador, loja_itens, venda_compra):
        """
        Menu de compra/venda de itens na loja da área. Retorna 1 se o jogador comoprou ou vendeu algo
        e 0 caso contrário.
        """

        operacao_realizada = 0

        if venda_compra == "Compra":
            vendedor = loja_itens

        elif venda_compra == "Venda":
            vendedor = jogador.inventario

        else:
            return operacao_realizada

        while True:

            if len(vendedor) > 0:

                if venda_compra == "Compra":
                    print('\n|=======================================> ITENS À VENDA <========================================|')
                else:
                    print('\n|=======================================> SEU INVENTÁRIO <=======================================|')

                # Ouro do jogador
                print(Fore.YELLOW + 'Ouro' + Style.RESET_ALL + f': {jogador.ouro}')

                # Listando os itens que o jogador pode comprar/vender
                tabela = []
                cabecalho = ["Nome", "Quantidade", Fore.YELLOW + 'Preço' + Style.RESET_ALL, "Classificação"]
                alinhamento = ("left", "center", "center", "center")
                for i, item in enumerate(vendedor):
                    t = []
                    t.append(f'[{i+1}] ' + item[1].nome) # Índice + Nome
                    t.append(item[1].quantidade)         # Quantidade
                    t.append(item[1].preco)              # Preço
                    t.append(item[0])                    # Classificação
                    tabela.append(t)
                print(tabulate(tabela, headers = cabecalho, colalign = alinhamento, tablefmt="psql"))
                print('\n[0] Voltar ao menu anterior')

                # Jogador escolhendo qual item quer comprar/vender
                while True:
                    escolha_item = utils.LerNumero('> ')

                    if escolha_item >= 0 and escolha_item <= len(vendedor):
                        break
                
                # Jogador quer sair do menu interno
                if escolha_item == 0:
                    break

                # Etapa final da compra/venda
                else:
                    item = vendedor[escolha_item - 1]

                    # Imprimindo o item escolhido
                    mensagem = f'\n{item[1].nome} | Qtd: {item[1].quantidade} | '              # Nome e Quantidade
                    mensagem += Fore.YELLOW + 'Preço' + Style.RESET_ALL + f': {item[1].preco}' # Preço
                    mensagem += f' | {item[0]}'                                                # Classificação
                    
                    if item[0] == "Consumivel":
                        print(mensagem)

                    else:
                        # Nível e Tipo
                        mensagem += ' | Nível: {:2d} | Tipo: '.format(item[1].nivel)
                        print(mensagem, end = '')
                        print(imprimir.RetornarTipo(item[1].tipo))

                        # Atributos concedidos pelo item
                        mensagem = ''
                        primeiro = 1

                        if item[1].maxHp > 0:
                            mensagem += Fore.GREEN + '+' + Style.RESET_ALL + f'{item[1].maxHp} '
                            mensagem += Fore.RED + 'HP' + Style.RESET_ALL
                            primeiro = 0
                        elif item[1].maxHp < 0:
                            mensagem += Fore.RED + '-' + Style.RESET_ALL + f'{item[1].maxHp} '
                            mensagem += Fore.RED + 'HP' + Style.RESET_ALL
                            primeiro = 0

                        if item[1].maxMana > 0:
                            if primeiro == 0:
                                mensagem += ', '
                            mensagem += Fore.GREEN + '+' + Style.RESET_ALL + f'{item[1].maxMana} '
                            mensagem += Fore.BLUE + 'Mana' + Style.RESET_ALL
                            primeiro = 0
                        elif item[1].maxMana < 0:
                            if primeiro == 0:
                                mensagem += ', '
                            mensagem += Fore.RED + '-' + Style.RESET_ALL + f'{item[1].maxMana} '
                            mensagem += Fore.BLUE + 'Mana' + Style.RESET_ALL 
                            primeiro = 0

                        if item[1].ataque > 0:
                            if primeiro == 0:
                                mensagem += ', '
                            mensagem += Fore.GREEN + '+' + Style.RESET_ALL + f'{item[1].ataque} '
                            mensagem += 'ATAQUE'
                            primeiro = 0
                        elif item[1].ataque < 0:
                            if primeiro == 0:
                                mensagem += ', '
                            mensagem += Fore.RED + '-' + Style.RESET_ALL + f'{item[1].ataque} '
                            mensagem += 'ATAQUE'
                            primeiro = 0

                        if item[1].defesa > 0:
                            if primeiro == 0:
                                mensagem += ', '
                            mensagem += Fore.GREEN + '+' + Style.RESET_ALL + f'{item[1].defesa} '
                            mensagem += 'DEFESA'
                            primeiro = 0
                        elif item[1].defesa < 0:
                            if primeiro == 0:
                                mensagem += ', '
                            mensagem += Fore.RED + '-' + Style.RESET_ALL + f'{item[1].defesa} '
                            mensagem +='DEFESA'
                            primeiro = 0

                        if item[1].magia > 0:
                            if primeiro == 0:
                                mensagem += ', '
                            mensagem += Fore.GREEN + '+' + Style.RESET_ALL + f'{item[1].magia} '
                            mensagem += 'MAGIA'
                            primeiro = 0
                        elif item[1].magia < 0:
                            if primeiro == 0:
                                mensagem += ', '
                            mensagem += Fore.RED + '-' + Style.RESET_ALL + f'{item[1].magia} '
                            mensagem +='MAGIA'
                            primeiro = 0

                        if item[1].velocidade > 0:
                            if primeiro == 0:
                                mensagem += ', '
                            mensagem += Fore.GREEN + '+' + Style.RESET_ALL + f'{item[1].velocidade} '
                            mensagem += 'VELOCIDADE'
                            primeiro = 0
                        elif item[1].velocidade < 0:
                            if primeiro == 0:
                                mensagem += ', '
                            mensagem += Fore.RED + '-' + Style.RESET_ALL + f'{item[1].velocidade} '
                            mensagem +='VELOCIDADE'
                            primeiro = 0

                        print(mensagem)

                    print(f'Descrição: {item[1].descricao}') # Descrição

                    if venda_compra == "Compra":
                        print(f'\nDeseja comprar quanto de {item[1].nome}?')
                    else:
                        print(f'\nDeseja vender quanto de {item[1].nome}?')

                    # Jogador escolhendo a quantidade do item que quer vender
                    while True:
                        escolha_quantidade = utils.LerNumero('> ')

                        if escolha_quantidade >= 0 and escolha_quantidade <= item[1].quantidade:
                            break

                    # Jogador confirmou a compra/venda
                    if escolha_quantidade != 0:

                        if venda_compra == "Venda":

                            item_vendido = item[1].ClonarItem()
                            item_vendido = (item[0], item_vendido)

                            item_vendido[1].preco = (item_vendido[1].preco * 2) + 1
                            item_vendido[1].quantidade = escolha_quantidade
                            self.AdicionarAoEstoque(item_vendido, loja_itens)

                            jogador.ouro += escolha_quantidade * item[1].preco
                            item[1].quantidade -= escolha_quantidade
                            if item[1].quantidade == 0:
                                jogador.inventario.remove(item)

                            print(f'Você vendeu {escolha_quantidade} {item_vendido[1].nome}.')

                            operacao_realizada = 1
                    
                        # Compra -> Jogador tem ouro suficiente
                        elif venda_compra == "Compra" and jogador.ouro >= escolha_quantidade * item[1].preco:

                            item_comprado = item[1].ClonarItem()
                            item_comprado = (item[0], item_comprado)

                            item_comprado[1].preco = math.floor(item_comprado[1].preco / 2)
                            item_comprado[1].quantidade = escolha_quantidade
                            jogador.ouro -= escolha_quantidade * item[1].preco
                            jogador.AdicionarAoInventario(item_comprado)

                            item[1].quantidade -= escolha_quantidade
                            if item[1].quantidade == 0:
                                loja_itens.remove(item)

                            print(f'Você comprou {escolha_quantidade} {item_comprado[1].nome}.')

                            operacao_realizada = 1
                        
                        # Compra -> Jogador não tem ouro suficiente
                        else:
                            print(f'Você não tem ouro suficiente para comprar {escolha_quantidade} {item[1].nome}.')
        
            elif venda_compra == "Compra":
                print('Não há mais itens à venda na loja.')
                break
            
            else:
                print('Não há mais itens que você possa vender.')
                break
        
        return operacao_realizada
    
    def AdicionarAoEstoque(self, novo_item, loja_itens):
        """
        Recebe uma tupla (X, Y), onde X é a classificação do item ("Consumível", "Material", etc.) e Y é o item em
        si e, caso o item já esteja presente no estoque da loja da área (loja_itens), sua quantidade é aumentada,
        e caso contrário, ele é adicionado normalmente ao estoque.
        """

        for item in loja_itens:
            if item[1].nome == novo_item[1].nome:
                item[1].quantidade += novo_item[1].quantidade
                return
        
        loja_itens.append(novo_item)

    def Loja(self, jogador, loja_itens):
        """
        Menu principal de uma loja presente na área. Retorna 1 se o jogador comprou ou vendeu algo
        e 0 caso contrário.
        """

        retorno = 1
        operacao_temporaria = 0
        operacao_realizada = 0

        while True:
            
            # Imprimindo o menu principal da loja
            if retorno == 1:
                print('\n|============================================> LOJA <============================================|')
                print(Fore.YELLOW + 'Ouro' + Style.RESET_ALL + f': {jogador.ouro}')
                print('[1] Comprar Itens')
                print('[2] Vender Itens\n')
                print('[0] Sair da Loja')
                retorno = 0

            escolha = utils.LerNumero('> ')

            # Saindo da loja
            if escolha == 0:
                break

            # Comprar itens
            elif escolha == 1:
                operacao_temporaria = self.LojaMenu(jogador, loja_itens, "Compra")
                if operacao_temporaria == 1:
                    operacao_realizada = 1
                retorno = 1
            
            # Vender itens
            elif escolha == 2:
                operacao_temporaria = self.LojaMenu(jogador, loja_itens, "Venda")
                if operacao_temporaria == 1:
                    operacao_realizada = 1
                retorno = 1
        
        return operacao_realizada

    @abstractmethod
    def Estalagem(self, jogador):
        """
        Menu principal de uma estalagem presente na área.
        """

        pass

    def EventoDescanso(self, jogador):
        """
        Ofereçe 2 opções ao jogador:
        * Ter chance de ser atacado e recuperar parte do HP e Mana;
        * Ignorar o evento.

        A função retorna:
        * -1, caso o jogador tenha escolhido a primeira opção, sofrido uma emboscada e perdido a batalha;
        * 2, caso o jogador tenha escolhido a primeira opção, sofrido uma emboscada e fugido da batalha.
        * 1, caso contrário.
        """

        print('\nApós alguns bons minutos sem ser atacado, você teve a idéia de descansar e recuperar suas' +
        ' energias. Você pode fazer uma clareira por onde você se encontra, \nse recuperando parcialmente mas' +
        ' com chance de ser emboscado por criaturas inimigas se ficar distraído. Também dá pra só ignorar esse' +
        ' pensamento e continuar\nbatalhando. O que você escolhe?\n')

        resultado = 1

        # Chance de sofrer emboscada ao escolher a clareira
        porcentagem_hp = (jogador.hp / jogador.maxHp) * 100
        porcentagem_mana = (jogador.mana / jogador.maxMana) * 100
        porcentagem_media = (porcentagem_hp + porcentagem_mana) / 2
        chance_emboscada = 100 - porcentagem_media

        # Impedindo valores absurdos e colocando uma chance mínima de emboscagem (25%)
        if chance_emboscada < 25.00:
            chance_emboscada = 25.00
        elif chance_emboscada > 100.00:
            chance_emboscada = 100.00

        # Imprimindo Opções
        print('[1] Fazer uma clareira - Chance de sofrer emboscada: {:.2f}'.format(chance_emboscada) + '%')
        print('[0] Continuar batalhando\n')

        # Escolha do jogador
        while True:
            op = utils.LerNumero('> ')

            if op == 0:
                break

            # Clareira
            elif op == 1:
                # Recuperar 5 de hp ou 25% do hp máximo, o que for maior
                valor = 5
                if math.floor(jogador.maxHp * 0.25) > valor:
                    valor = math.floor(jogador.maxHp * 0.25)
                jogador.hp += valor
                mensagem = f'Você recuperou {valor} de ' + Fore.RED + 'HP' + Style.RESET_ALL + '.'

                if jogador.hp >= jogador.maxHp:
                    jogador.hp = jogador.maxHp
                    mensagem = f'Você maximizou seu ' + Fore.RED + 'HP' + Style.RESET_ALL + '.'
                print(mensagem)

                # Recuperar 5 de mana ou 25% da mana máxima, o que for maior
                valor = 5
                if math.floor(jogador.maxMana) * 0.25 > valor:
                    valor = math.floor(jogador.maxMana * 0.25)
                jogador.mana += valor
                mensagem = f'Você recuperou {valor} de ' + Fore.BLUE + 'Mana' + Style.RESET_ALL + '.'

                if jogador.mana >= jogador.maxMana:
                    jogador.mana = jogador.maxMana
                    mensagem = f'Você maximizou sua ' + Fore.BLUE + 'Mana' + Style.RESET_ALL + '.'
                print(mensagem)

                # Emboscada
                if utils.CalcularChance(chance_emboscada / 100):
                    inimigos = self.RetornarEncontro(jogador)
                    aliados = [jogador]
                    resultado = batalha.BatalhaPrinicipal(aliados, inimigos, emboscada = 1)
                
                break

        return resultado

    @abstractmethod
    def EventoVendedorAmbulante(self, jogador, conf):
        """
        Uma loja que irá selecionar aleatoriamente alguns itens para serem vendidos ao jogador. Retorna 1 se o
        jogador comprou ou vendeu algo e 0 caso contrário.
        """

        pass
