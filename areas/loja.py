import sys
import math
from copy import deepcopy
from colorama import Fore, Back, Style

sys.path.append("..")
from base import imprimir, utils
from menus import menu_paginado_generico, menu_fabricacao
from sistemas import receita

### Métodos Auxiliares ###
    
def AdicionarAoEstoque(novo_item, loja_itens):
    """
    Caso o item <novo_item> já esteja presente na lista <loja_itens>, a quantidade do item presente é
    aumentada. Caso contrário o item <novo_item> é adicionado ao final da lista.

    Parâmetros:
    - novo_item: novo item a ser adicionado na loja;
    - loja_itens: lista de itens a venda na loja.
    """

    for item in loja_itens:
        if item.nome == novo_item.nome:
            item.quantidade += novo_item.quantidade
            return
    
    loja_itens.append(novo_item)

def Reestocar(area, est):
    """
    Irá retornar as lojas presentes na área so seu estado inicial com base no número de batalhas ganhas
    pelo jogador. Retorna True se houve um reestoque das lojas presentes na área e False caso contrário.
    """
    b = est.batalhas_ganhas - area.ultimo_batalhas_ganhas
    area.reestoque_atual += b
    area.ultimo_batalhas_ganhas = est.batalhas_ganhas

    if area.reestoque_atual >= area.reestoque:
        area.reestoque_atual = 0
        area.lojas_itens = area.EstoqueInicial()
        return True
        
    else:
        return False

def ItemPresente(loja_itens, item_nome):
    """
    Retorna o item com nome <item_nome> presente na loja, e retorna None caso a loja não possua aquele
    item.
    """

    for i in loja_itens:
        if i.nome == item_nome:
            return i
    return None
 
### Sistema de Loja ###

def LojaMenu(jogador, loja_itens, venda_compra):
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
                print('\n+-----> ITENS À VENDA <-----+')
            else:
                print('\n+-----> SEU INVENTÁRIO <-----+')

            # Ouro do jogador
            print(Fore.YELLOW + 'Ouro' + Style.RESET_ALL + f': {jogador.ouro}')

            # Listando os itens que o jogador pode comprar/vender
            disponivel = menu_paginado_generico.ComporPagina(vendedor, item_indice_atual, itens_por_pagina)
            tabela = imprimir.RetornarTabelaItens(disponivel, jogador, indice = item_indice_atual + 1)
            print(tabela)
            print('')

            # Opções disponíveis no menu da loja
            opcoes = []
            if anterior or proximo:
                if venda_compra == "Compra":
                    opcoes.append('Comprar Item')
                elif venda_compra == "Venda":
                    opcoes.append('Vender Item')
                opcoes.append('Anterior')
                opcoes.append('Próximo')
            opcoes.append('Retornar ao Menu Anterior')

            # O vendedor possui mais de <itens_por_pagina> itens a venda
            if len(opcoes) > 1:
                op = menu_paginado_generico.ImprimirOpções(opcoes, pagina, ultima_pagina)
                
                # Jogador quer sair do menu interno
                if op == 0:
                    break

                # Jogador quer comprar/vender um item
                elif op == 1:
                    print('')

                # Imprimir até <itens_por_pagina> itens anteriores
                elif op == 2 and anterior:
                    pagina -= 1
                
                # Imprimir até <itens_por_pagina> próximos itens
                elif op == 3 and proximo:
                    pagina += 1

            else:
                print('[0] Retornar ao Menu Anterior\n')

            # Comprar/Vender um item
            if (len(opcoes) == 1) or (len(opcoes) > 1 and op == 1):
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
                    is_receita = isinstance(item, receita.Receita)

                    if not is_receita:
                        imprimir.ImprimirItemDetalhado(item, jogador)
                    else:
                        imprimir.ImprimirReceitaDetalhada(item, jogador)

                    if not is_receita:
                        if venda_compra == "Compra":
                            print(f'Deseja comprar quanto de {item.nome}?')
                        else:
                            print(f'Deseja vender quanto de {item.nome}?')

                        # Jogador escolhendo a quantidade do item que quer vender
                        escolha_quantidade = utils.LerNumeroIntervalo('> ', 0, item.quantidade)
                    else:
                        escolha_quantidade = 1

                    # Jogador confirmou a compra/venda
                    if escolha_quantidade != 0:

                        if venda_compra == "Venda":
                            item_vendido = deepcopy(item)

                            item_vendido.preco = (item_vendido.preco * 2) + 1
                            item_vendido.quantidade = escolha_quantidade
                            jogador.ouro += escolha_quantidade * item.preco
                            AdicionarAoEstoque(item_vendido, loja_itens)
                            
                            item.quantidade -= escolha_quantidade
                            if item.quantidade == 0:
                                jogador.inventario.remove(item)

                            print(f'Você vendeu {escolha_quantidade} {item_vendido.nome}.')

                            operacao_realizada = True
                    
                        # Compra -> Jogador tem ouro suficiente
                        elif venda_compra == "Compra" and (jogador.ouro >= escolha_quantidade * item.preco):
                            item_comprado = deepcopy(item)
                            item_comprado.quantidade = escolha_quantidade
                            jogador.ouro -= escolha_quantidade * item.preco

                            # Compra de um item
                            if not is_receita:
                                item_comprado.preco = math.floor(item_comprado.preco / 2)
                                jogador.AdicionarAoInventario(item_comprado)

                                item.quantidade -= escolha_quantidade
                                if item.quantidade == 0:
                                    loja_itens.remove(item)

                            # Compra de uma receita
                            else:
                                item_comprado.preco = 0
                                jogador.AdicionarReceita(item_comprado)
                                loja_itens.remove(item)

                            if not is_receita:
                                print(f'Você comprou {escolha_quantidade} {item_comprado.nome}.')
                            else:
                                print(f'Você aprendeu uma nova receita de fabricação: {item_comprado.nome}.')

                            operacao_realizada = True
                        
                        # Compra -> Jogador não tem ouro suficiente
                        elif not is_receita:
                            print(f'Você não tem ouro suficiente para comprar {escolha_quantidade} {item.nome}.')
                        else:
                            print(f'Você não tem ouro suficiente para comprar Receita: {item.nome}.')

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

def Loja(loja_nome, jogador, loja_itens, receitas_fabricacao = []):
    """
    Menu principal de uma loja presente na área. Retorna True se o jogador comprou ou vendeu algo
    e False caso contrário.

    Parâmetros:
    - jogador: objeto da classe Jogador;
    - loja_itens: lista de itens a venda na loja;
    - loja_nome: nome da loja.

    Parâmetros Opcionais:
    - receitas_fabricacao: lista de receitas de fabricação disponíveis na loja.
    """
    retorno = 1
    operacao_temporaria = False
    operacao_realizada = False

    while True:
        
        # Imprimindo o menu principal da loja
        if retorno == 1:
            print(f'\n+-----> {loja_nome} <-----+')
            print(Fore.YELLOW + 'Ouro' + Style.RESET_ALL + f': {jogador.ouro}')
            print('[1] Comprar Itens')
            print('[2] Vender Itens')

            if receitas_fabricacao:
                print('[3] Fabricação')

            print('\n[0] Sair da Loja')
            retorno = 0

        escolha = utils.LerNumero('> ')

        # Saindo da loja
        if escolha == 0:
            break

        # Comprar itens
        elif escolha == 1:
            operacao_temporaria = LojaMenu(jogador, loja_itens, "Compra")
            if operacao_temporaria:
                operacao_realizada = True
            retorno = 1
        
        # Vender itens
        elif escolha == 2:
            operacao_temporaria = LojaMenu(jogador, loja_itens, "Venda")
            if operacao_temporaria:
                operacao_realizada = True
            retorno = 1
        
        # Fabricação
        elif receitas_fabricacao and escolha == 3:
            operacao_temporaria = menu_fabricacao.FabricacaoMenu(jogador, receitas_fabricacao)
            if operacao_temporaria:
                operacao_realizada = True
            retorno = 1
    
    return operacao_realizada
    