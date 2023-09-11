import sys
import math
from copy import deepcopy

sys.path.append("..")
from base import imprimir, utils
from menus import menu_paginado_generico

def MenuFabricacao(jogador, receitas, incluir_preco = True):
    """
    Menu de fabricação de itens na loja da área. Retorna True se o jogador fabricou algo e False caso contrário.
    """
    operacao_realizada = False

    # Variáveis do sistema de paginação
    receitas_por_pagina = 15
    ultima_pagina = len(receitas)
    ultima_pagina = math.ceil(ultima_pagina / receitas_por_pagina)
    ultima_pagina -= 1
    item_indice_atual = 0
    pagina = 0

    while True:

        if len(receitas) > 0:

            # Variáveis do sistema de paginação
            if pagina > 0:
                anterior = True
            else:
                anterior = False
            if pagina < ultima_pagina:
                proximo = True
            else:
                proximo = False
            item_indice_atual = (pagina * receitas_por_pagina)

            print('\n+-----> FABRICAÇÃO DE ITENS <-----+')

            # Ouro do jogador
            print(f"{imprimir.RetornarColorido('Ouro')}: {jogador.ouro}")

            # Listando os itens que o jogador pode fabricar
            disponivel = menu_paginado_generico.ComporPagina(receitas, item_indice_atual, receitas_por_pagina)
            tabela = imprimir.RetornarTabelaReceitas(disponivel, jogador, incluir_preco = incluir_preco, indice = item_indice_atual + 1)
            print(tabela)
            print('')

            # Opções disponíveis no menu da loja
            opcoes = []
            if anterior or proximo:
                opcoes.append('Fabricar Item')
                opcoes.append('Anterior')
                opcoes.append('Próximo')
            opcoes.append('Retornar ao Menu Anterior')

            # O vendedor possui mais de <receitas_por_pagina> itens a venda
            if len(opcoes) > 1:
                op = menu_paginado_generico.ImprimirOpções(opcoes, pagina, ultima_pagina)
                
                # Jogador quer sair do menu interno
                if op == 0:
                    break

                # Jogador quer fabricar um item
                elif op == 1:
                    print('')

                # Imprimir até <receitas_por_pagina> receitas anteriores
                elif op == 2 and anterior:
                    pagina -= 1
                
                # Imprimir até <receitas_por_pagina> próximas receitas
                elif op == 3 and proximo:
                    pagina += 1

            else:
                print('[0] Retornar ao Menu Anterior\n')

            # Comprar/Vender um item
            if (len(opcoes) == 1) or (len(opcoes) > 1 and op == 1):
                menor_indice = (pagina * receitas_por_pagina) + 1
                maior_indice = (pagina + 1) * receitas_por_pagina
                if len(receitas) < maior_indice:
                    maior_indice = len(receitas)

                print('Qual item deseja fabricar?')

                escolha = utils.LerNumeroIntervalo('> ', menor_indice, maior_indice, permitido = [0])

                # Saindo
                if escolha == 0:
                    break

                # Procedendo
                else:
                    receita = receitas[escolha - 1]
                    imprimir.ImprimirReceitaDetalhada(receita, jogador, incluir_preco = incluir_preco)

                    print(f'Deseja fabricar quanto de {receita.nome}?')

                    # Jogador escolhendo a quantidade do item que quer fabricar
                    escolha_quantidade = utils.LerNumeroIntervalo('> ', 0, 999)

                    # Jogador confirmou a fabricação de itens
                    if escolha_quantidade != 0:
                    
                        if receita.preco * escolha_quantidade > jogador.ouro:
                            print(f'Você não tem ouro suficiente para fabricar {escolha_quantidade} de {receita.nome}.')

                        elif receita.nivel > jogador.nivel:
                            print(f'Você não tem nível suficiente para fabricar {escolha_quantidade} de {receita.nome}.')

                        elif not receita.MateriaisNecessarios(jogador.inventario, escolha_quantidade):
                            print(f'Você não tem os materiais necessários para fabricar {escolha_quantidade} de {receita.nome}.')

                        else:
                            for item in receita.entrada:
                                item_inventario = jogador.ItemPresente(item.nome)
                                item_inventario.quantidade -= item.quantidade * escolha_quantidade

                                if item_inventario.quantidade == 0:
                                    jogador.inventario.remove(item_inventario)
                            
                            jogador.ouro -= receita.preco * escolha_quantidade

                            for item in receita.saida:
                                item_fabricado = deepcopy(item)
                                item_fabricado.quantidade *= escolha_quantidade
                                jogador.AdicionarAoInventario(item_fabricado)

                                if item.genero == "M":
                                    print(f'{escolha_quantidade} {item_fabricado.nome} foram fabricados.')
                                elif item.genero == "F":
                                    print(f'{escolha_quantidade} {item_fabricado.nome} foram fabricadas.')

                            operacao_realizada = True
    
    return operacao_realizada
