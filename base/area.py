import sys
import math
from copy import deepcopy
from tabulate import tabulate
from abc import abstractmethod
from colorama import Fore, Back, Style

from . import imprimir, utils
sys.path.append("..")
from combate import batalha
from menus import menu_paginado_generico

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

    # Métodos

    def LojaMenu(self, jogador, loja_itens, venda_compra):
        """
        Menu de compra/venda de itens na loja da área. Retorna True se o jogador comprou ou vendeu algo
        e False caso contrário.
        """
        operacao_realizada = False

        if venda_compra == "Compra":
            vendedor = loja_itens
        elif venda_compra == "Venda":
            vendedor = jogador.inventario
        else:
            return operacao_realizada

        # Variáveis do sistema de paginação
        itens_por_pagina = 15
        ultima_pagina = len(vendedor)
        ultima_pagina = math.ceil(ultima_pagina / itens_por_pagina)
        ultima_pagina -= 1
        item_indice_atual = 0
        pagina = 0

        while True:

            if len(vendedor) > 0:

                # Variáveis do sistema de paginação
                if pagina > 0:
                    anterior = True
                else:
                    anterior = False
                if pagina < ultima_pagina:
                    proximo = True
                else:
                    proximo = False
                item_indice_atual = (pagina * itens_por_pagina)

                if venda_compra == "Compra":
                    print('\n|=======================================> ITENS À VENDA <========================================|')
                else:
                    print('\n|=======================================> SEU INVENTÁRIO <=======================================|')

                # Ouro do jogador
                print(Fore.YELLOW + 'Ouro' + Style.RESET_ALL + f': {jogador.ouro}')

                # Listando os itens que o jogador pode comprar/vender
                disponivel = menu_paginado_generico.ComporPagina(vendedor, item_indice_atual, itens_por_pagina)
                tabela = imprimir.RetornarTabelaItens(disponivel, jogador, indice = item_indice_atual + 1)
                print(tabela)
                print('')

                # Opções disponíveis no menu da loja
                opcoes = []
                if venda_compra == "Compra":
                    opcoes.append('Comprar Item')
                elif venda_compra == "Venda":
                    opcoes.append('Vender Item')
                if anterior or proximo:
                    opcoes.append('Anterior')
                    opcoes.append('Próximo')
                opcoes.append('Retornar ao Menu Anterior')  
                op = menu_paginado_generico.ImprimirOpções(opcoes, pagina, ultima_pagina)
                if op == 1:
                    print('')
                
                # Jogador quer sair do menu interno
                if op == 0:
                    break

                # Imprimir até 'itens_por_pagina' itens anteriores
                elif op == 2 and anterior:
                    pagina -= 1
                
                # Imprimir até 'itens_por_pagina' próximos itens
                elif op == 3 and proximo:
                    pagina += 1

                # Comprar/Vender um item
                else:
                    menor_indice = (pagina * itens_por_pagina) + 1
                    maior_indice = (pagina + 1) * itens_por_pagina
                    if len(vendedor) < maior_indice:
                        maior_indice = len(vendedor)

                    if venda_compra == "Compra":
                        print('Qual item deseja comprar?')
                    elif venda_compra == "Venda":
                        print('Qual item deseja vender?')

                    escolha = utils.LerNumeroIntervalo('> ', menor_indice, maior_indice, permitido = [0])

                    # Saindo
                    if escolha == 0:
                        break

                    # Procedendo
                    else:
                        item = vendedor[escolha - 1]
                        imprimir.ImprimirItemDetalhado(item, jogador)

                        if venda_compra == "Compra":
                            print(f'Deseja comprar quanto de {item.nome}?')
                        else:
                            print(f'Deseja vender quanto de {item.nome}?')

                        # Jogador escolhendo a quantidade do item que quer vender
                        escolha_quantidade = utils.LerNumeroIntervalo('> ', 0, item.quantidade)

                        # Jogador confirmou a compra/venda
                        if escolha_quantidade != 0:

                            if venda_compra == "Venda":
                                item_vendido = deepcopy(item)

                                item_vendido.preco = (item_vendido.preco * 2) + 1
                                item_vendido.quantidade = escolha_quantidade
                                jogador.ouro += escolha_quantidade * item.preco
                                self.AdicionarAoEstoque(item_vendido, loja_itens)
                                
                                item.quantidade -= escolha_quantidade
                                if item.quantidade == 0:
                                    jogador.inventario.remove(item)

                                print(f'Você vendeu {escolha_quantidade} {item_vendido.nome}.')

                                operacao_realizada = True
                        
                            # Compra -> Jogador tem ouro suficiente
                            elif venda_compra == "Compra" and (jogador.ouro >= escolha_quantidade * item.preco):
                                item_comprado = deepcopy(item)

                                item_comprado.preco = math.floor(item_comprado.preco / 2)
                                item_comprado.quantidade = escolha_quantidade
                                jogador.ouro -= escolha_quantidade * item.preco
                                jogador.AdicionarAoInventario(item_comprado)

                                item.quantidade -= escolha_quantidade
                                if item.quantidade == 0:
                                    loja_itens.remove(item)

                                print(f'Você comprou {escolha_quantidade} {item_comprado.nome}.')

                                operacao_realizada = True
                            
                            # Compra -> Jogador não tem ouro suficiente
                            else:
                                print(f'Você não tem ouro suficiente para comprar {escolha_quantidade} {item.nome}.')

                            # Checando se a página tinha 1 item sobrando, e ele foi removido
                            tentativa_ultima_pagina = len(vendedor)
                            tentativa_ultima_pagina = math.ceil(tentativa_ultima_pagina / itens_por_pagina)
                            tentativa_ultima_pagina -= 1

                            if ultima_pagina != tentativa_ultima_pagina:
                                ultima_pagina -= 1
                                if pagina > 0:
                                    pagina -= 1

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
            if item.nome == novo_item.nome:
                item.quantidade += novo_item.quantidade
                return
        
        loja_itens.append(novo_item)

    def Loja(self, jogador, loja_itens):
        """
        Menu principal de uma loja presente na área. Retorna True se o jogador comprou ou vendeu algo
        e False caso contrário.
        """

        retorno = 1
        operacao_temporaria = False
        operacao_realizada = False

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
                if operacao_temporaria:
                    operacao_realizada = True
                retorno = 1
            
            # Vender itens
            elif escolha == 2:
                operacao_temporaria = self.LojaMenu(jogador, loja_itens, "Venda")
                if operacao_temporaria:
                    operacao_realizada = True
                retorno = 1
        
        return operacao_realizada

    def Reestocar(self, est):
        """
        Irá retornar as lojas presentes na área so seu estado inicial com base no número de batalhas ganhas
        pelo jogador. Retorna True se houve um reestoque das lojas presentes na área e False caso contrário.
        """

        b = est.batalhas_ganhas - self.ultimo_batalhas_ganhas
        self.reestoque_atual += b
        self.ultimo_batalhas_ganhas = est.batalhas_ganhas

        if self.reestoque_atual >= self.reestoque:
            self.reestoque_atual = 0
            self.lojas_itens = self.EstoqueInicial()
            return True
            
        else:
            return False

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
                    resultado = batalha.BatalhaPrincipal(aliados, inimigos, emboscada = 1)
                
                break

        return resultado
