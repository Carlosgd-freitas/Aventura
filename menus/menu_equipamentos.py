import sys
from copy import deepcopy
from tabulate import tabulate
from colorama import Fore, Back, Style

sys.path.append("..")
from base import imprimir, utils
from itens import equipamentos

def LinhaEquipamento(item, linha):
    """
    Compõe uma linha de uma tabela com as colunas: nível, tipo, vida máxima, mana máxima, ataque, defesa, magia
    e velocidade de um item.

    Parâmetros:
    - item: o item que será usado para compor a linha da tabela;
    - linha: uma lista de atributos do item, representando a linha da tabela.
    """

    # Nível
    if item.classe_batalha != "Item Vazio":
        nivel = item.nivel
    else:
        nivel = '---'
    linha.append(nivel)

    # Tipo
    if item.classe_batalha != "Item Vazio":
        tipo = imprimir.RetornarTipo(item.tipo)
    else:
        tipo = '---'
    linha.append(tipo)

    # Vida Máxima
    if item.classe_batalha != "Item Vazio":
        maxHp = item.maxHp
    else:
        maxHp = '---'
    linha.append(maxHp)

    # Mana Máxima
    if item.classe_batalha != "Item Vazio":
        maxMana = item.maxMana
    else:
        maxMana = '---'
    linha.append(maxMana)

    # Ataque
    if item.classe_batalha != "Item Vazio":
        ataque = item.ataque
    else:
        ataque = '---'
    linha.append(ataque)

    # Defesa
    if item.classe_batalha != "Item Vazio":
        defesa = item.defesa
    else:
        defesa = '---'
    linha.append(defesa)

    # Magia
    if item.classe_batalha != "Item Vazio":
        magia = item.magia
    else:
        magia = '---'
    linha.append(magia)

    # Velocidade
    if item.classe_batalha != "Item Vazio":
        velocidade = item.velocidade
    else:
        velocidade = '---'
    linha.append(velocidade)

def ImprimirEquipados(jogador):
    """
    Imprime os equipamentos atualmente equipados no jogador.
    """

    print('|========================================> EQUIPAMENTOS <========================================|')

    tabela = []
    cabecalho = ["", "Nome", "Nível", "Tipo", Back.BLACK + Fore.RED + 'HP' + Style.RESET_ALL,
        Back.BLACK + Fore.BLUE + 'Mana' + Style.RESET_ALL, "ATQ", "DEF", "MAG", "VEL"]
    alinhamento = ("left", "left", "center", "center", "center", "center", "center", "center", "center", "center")
    
    for i, item in enumerate(jogador.equipados):
        t = []

        # Índice + Mão/Cabeça/Peitoral/Pés/Acessório
        if i == 0 or i == 1:
            parte = 'Mão'
        elif i == 2:
            parte = 'Cabeça'
        elif i == 3:
            parte = 'Peitoral'
        elif i == 4:
            parte = 'Pés'
        elif i == 5:
            parte = 'Acessório'
        t.append(f'[{i+1}] ' + parte)

        # Nome
        if item.classe_batalha != "Item Vazio":
            nome = item.nome
        else:
            nome = '---'
        t.append(nome)

        LinhaEquipamento(item, t)

        tabela.append(t)

    print(tabulate(tabela, headers = cabecalho, colalign = alinhamento, tablefmt="psql"))
    imprimir.ImprimirEfeitosEquipamentos(jogador)
    print('')

def EquipadosGanhos(jogador):
    """
    Aumenta os atributos do jogador e concede efeitos baseados nos itens equipados.
    """

    # Aumentando os atributos do jogador
    equipado_indice = 0
    for e in jogador.equipados:
        if equipado_indice == 1 and e.classe_batalha == "Duas Mãos":
            pass

        else:
            jogador.maxHp += e.maxHp
            jogador.maxMana += e.maxMana

            jogador.ataque += e.ataque
            jogador.defesa += e.defesa
            jogador.magia += e.magia
            jogador.velocidade += e.velocidade

            # Aplicando possíveis buffs/debuffs concedidos por equipamentos
            for b in e.buffs:
                jogador.buffs.append(b)
            for d in e.debuffs:
                jogador.debuffs.append(d)

        equipado_indice += 1
    
    # Mudando o tipo do Ataque Normal para o tipo da arma equipada na primeira mão
    atacar = jogador.HabilidadePresente("Atacar")

    if jogador.equipados[0].classe_batalha == "Item Vazio":
        atacar.tipo = "Normal"
    else:
        atacar.tipo = jogador.equipados[0].tipo

def EquipadosPerdas(jogador):
    """
    Diminui os atributos do jogador e retira efeitos baseados nos itens equipados.
    """

    # Diminuindo os atributos do jogador
    equipado_indice = 0
    for e in jogador.equipados:
        if equipado_indice == 1 and e.classe_batalha == "Duas Mãos":
            pass

        else:
            jogador.maxHp -= e.maxHp
            jogador.maxMana -= e.maxMana

            jogador.ataque -= e.ataque
            jogador.defesa -= e.defesa
            jogador.magia -= e.magia
            jogador.velocidade -= e.velocidade

        equipado_indice += 1
    
    # Terminando possíveis buffs concedidos por equipamentos
    indices = []
    for i, b in enumerate(jogador.buffs):
        if b.nome.startswith("Equipamento:"):
            indices.append(i)
    for x, i in enumerate(indices):
        jogador.buffs.pop(i - x)

    # Terminando possíveis debuffs concedidos por equipamentos
    indices = []
    for i, d in enumerate(jogador.debuffs):
        if d.nome.startswith("Equipamento:"):
            indices.append(i)
    for x, i in enumerate(indices):
        jogador.debuffs.pop(i - x)
    
    # Voltando o tipo do Ataque Normal para "Normal"
    atacar = jogador.HabilidadePresente("Atacar")
    atacar.tipo = "Normal"

def MenuDesequipar(jogador, lugar, verbose = 1):
    """
    Menu que gerencia a ação de desequipar do jogador. Retorna:
    * 1 e o nome do equipamento desequipado, se foi possível desequipar um item;
    * 0 e "Item Vazio", caso contrário.

    <lugar> é um número inteiro que tem a seguinte equivalência:
    * 1 = Mão
    * 2 = Mão
    * 3 = Cabeça
    * 4 = Peitoral
    * 5 = Pés
    * 6 = Acessório

    Se verbose for igual à 0, a função não imprimirá nenhuma mensagem.
    """

    item = jogador.equipados[lugar - 1]

    if item.classe_batalha == "Item Vazio":
        return 0, "Item Vazio"

    # Mãos
    if lugar == 1 or lugar == 2:
        if item.classe_batalha == "Item Vazio" and verbose == 1:
            print('Não há nada equipado nesta mão para você desequipar.\n')

        # Desequipando Item
        else:
            vazio = equipamentos.Vazio()
            jogador.AdicionarAoInventario(item)

            if item.classe_batalha == "Uma Mão":
                jogador.equipados[lugar - 1] = vazio
            
            else:
                jogador.equipados[0] = vazio
                vazio_2 = equipamentos.Vazio()
                jogador.equipados[1] = vazio_2
            
            if item.singular_plural == "singular":
                if item.genero == "M":
                    print(f'{item.nome} foi desequipado.\n')
                elif item.genero == "F":
                    print(f'{item.nome} foi desequipada.\n')

            elif item.singular_plural == "plural":
                if item.genero == "M":
                    print(f'{item.nome} foram desequipados.\n')
                elif item.genero == "F":
                    print(f'{item.nome} foram desequipadas.\n')

            return 1, item.nome

    # Cabeça
    elif lugar == 3 and item.classe_batalha == "Item Vazio" and verbose == 1:
        print('Não há nada equipado na cabeça para você desequipar.\n')
    
    # Peitoral
    elif lugar == 4 and item.classe_batalha == "Item Vazio" and verbose == 1:
        print('Não há nada equipado no peitoral para você desequipar.\n')

    # Pés
    elif lugar == 5 and item.classe_batalha == "Item Vazio" and verbose == 1:
        print('Não há nada equipado nos pés para você desequipar.\n')

    # Acessório
    elif lugar == 6 and item.classe_batalha == "Item Vazio" and verbose == 1:
        print('Não há acessório equipado para você desequipar.\n')

    # Desequipando Item
    else:
        vazio = equipamentos.Vazio()
        jogador.AdicionarAoInventario(item)
        jogador.equipados[lugar - 1] = vazio

        if item.singular_plural == "singular":
            if item.genero == "M":
                print(f'{item.nome} foi desequipado.\n')
            elif item.genero == "F":
                print(f'{item.nome} foi desequipada.\n')

        elif item.singular_plural == "plural":
            if item.genero == "M":
                print(f'{item.nome} foram desequipados.\n')
            elif item.genero == "F":
                print(f'{item.nome} foram desequipadas.\n')

        return 1, item.nome
    
    return 0, "Item Vazio"

def ClonarEquipar(jogador, lugar, item, lugar_adicional = None, verbose = 0):
    """
    Esta função é chamada ao:
    * Cancelar a operação de equipar um item;
    * Equipar um item.

    Se verbose for igual à 0, a função não imprimirá nenhuma mensagem.
    """

    # Criando um clone do item
    item_clone = deepcopy(item)
    item_clone.quantidade = 1

    # Equipando o clone
    jogador.equipados[lugar - 1] = item_clone
    
    if lugar_adicional is not None:
        jogador.equipados[lugar_adicional - 1] = item_clone

    # Imprimindo a mensagem se a verbose for igual à 1
    if verbose == 1:
        if item_clone.singular_plural == "singular":
            if item_clone.genero == "M":
                print(f'{item_clone.nome} foi equipado.\n')
            elif item_clone.genero == "F":
                print(f'{item_clone.nome} foi equipada.\n')

        elif item_clone.singular_plural == "plural":
            if item_clone.genero == "M":
                print(f'{item_clone.nome} foram equipados.\n')
            elif item_clone.genero == "F":
                print(f'{item_clone.nome} foram equipadas.\n')

    # Reduzindo a quantidade e possivelmente removendo o item do inventário
    item.quantidade -= 1
    if item.quantidade <= 0:
        jogador.inventario.remove(item)

def MenuEquipar(jogador, lugar):
    """
    Menu que gerencia a ação de equipar do jogador. Retorna:
    * 1 e o nome do equipamento equipado, se foi possível equipar um item;
    * 0 e "Item Vazio", caso contrário.
    
    <lugar> é um número inteiro que tem a seguinte equivalência:
    * 1 = Mão
    * 2 = Mão
    * 3 = Cabeça
    * 4 = Peitoral
    * 5 = Pés
    * 6 = Acessório
    """

    # Estados do inventário e equipados antes de qualquer modificação
    inventario_antigo = deepcopy(jogador.inventario)
    equipados_antigo = deepcopy(jogador.equipados)

    # Classificação do item
    if lugar == 1 or lugar == 2:
        classe_batalha = "Uma Mão"
    elif lugar == 3:
        classe_batalha = "Cabeça"
    elif lugar == 4:
        classe_batalha = "Peitoral"
    elif lugar == 5:
        classe_batalha = "Pés"
    elif lugar == 6:
        classe_batalha = "Acessório"
        
    print('Qual item você deseja equipar?')

    # Imprimindo os itens que podem ser equipados
    print_indice = 1
    item_indice = 0
    relacao = [(0, -1)]
    
    tabela = []
    cabecalho = ["Nome", "Classificação", "Nível", "Tipo", Back.BLACK + Fore.RED + 'HP' + Style.RESET_ALL,
        Back.BLACK + Fore.BLUE + 'Mana' + Style.RESET_ALL, "ATQ", "DEF", "MAG", "VEL"]
    alinhamento = ("left", "center", "center", "center", "center", "center", "center", "center", "center", "center")

    for item in jogador.inventario:
        t = []

        if ((classe_batalha == "Uma Mão") and (item.classe_batalha == "Uma Mão" or item.classe_batalha == "Duas Mãos") and \
            (item.nivel <= jogador.nivel)) or \
            ((item.classe_batalha == classe_batalha) and (item.nivel <= jogador.nivel)):

            t.append(f'[{print_indice}] ' + item.nome)
            t.append(item.classe_batalha)
            LinhaEquipamento(item, t)
            tabela.append(t)

            relacao.append((print_indice, item_indice))
            print_indice += 1

        item_indice += 1

    # Nenhum item pode ser equipado
    if len(tabela) == 0:
        print('Não há itens deste tipo que possam ser equipados.\n')
        return 0, "Item Vazio"
    
    print(tabulate(tabela, headers = cabecalho, colalign = alinhamento, tablefmt="psql"))
    
    print('\n[0] Cancelar e retornar ao menu anterior.\n')

    # Jogador escolhe qual item quer equipar ou se quer cancelar a operação
    while True:
        escolha = utils.LerNumero('> ')

        if escolha >= 0 and escolha <= relacao[-1][0]:
            break
    
    # Mapeando a escolha para um índice do inventario
    for r in relacao:
        if r[0] == escolha:
            escolha = r[1]
            break
    
    # Jogador procedeu com a operação
    if escolha != -1:

        item_equipado = jogador.inventario[escolha]

        if ((lugar == 1 or lugar == 2) and item_equipado.classe_batalha == "Uma Mão") or (lugar >= 3 and lugar <= 6):
            MenuDesequipar(jogador, lugar, verbose = 0)
            ClonarEquipar(jogador, lugar, item_equipado, verbose = 1)

        elif (lugar == 1 or lugar == 2) and item_equipado.classe_batalha == "Duas Mãos":
            MenuDesequipar(jogador, 1, verbose = 0)
            MenuDesequipar(jogador, 2, verbose = 0)
            ClonarEquipar(jogador, 1, item_equipado, 2, verbose = 1)

        return 1, item_equipado.nome

    # Jogador cancelou a operação
    else:
        
        # Retornando aos estados do inventário e equipados antes de qualquer modificação
        jogador.inventario = inventario_antigo
        jogador.equipados = equipados_antigo

        return 0, "Item Vazio"

def MenuEquipamentos(jogador):
    """
    Menu de gerenciamento dos equipamentos do jogador. Retorna 1 se o jogador realizou alguma troca de equipamentos
    e retorna 0 caso contrário.
    """

    EquipadosPerdas(jogador)

    flag = 0
    troca_realizada = 0
    retorno = 1

    while True:

        # Jogador realizou alguma troca de equipamentos
        if flag == 1:
            troca_realizada = 1

        if retorno == 1:
            ImprimirEquipados(jogador)
            print('[1] Equipar')
            print('[2] Desequipar\n')
            print('[0] Retornar ao menu anterior')
            retorno = 0

        op = utils.LerNumero('> ')

        # Voltar ao Menu Anterior
        if op == 0:
            break

        # Equipar
        elif op == 1:
            print("\nEm qual lugar deseja equipar?")

            # Jogador escolhe um lugar para equipar (Mão, Peitoral, etc.)
            while True:
                lugar = utils.LerNumero('> ')

                if lugar >= 0 and lugar <= 6:
                    print('')
                    break
            
            # Jogador procede em equipar
            if lugar > 0:
                flag, inutilizado = MenuEquipar(jogador, lugar)

            retorno = 1

        # Desequipar
        elif op == 2:
            print("\nEm qual lugar deseja desequipar?")

            # Jogador escolhe um lugar para desequipar (Mão, Peitoral, etc.)
            while True:
                lugar = utils.LerNumero('> ')

                if lugar >= 0 and lugar <= 6:
                    print('')
                    break
            
            # Jogador procede em desequipar
            if lugar > 0:
                flag, inutilizado = MenuDesequipar(jogador, lugar)

            retorno = 1
    
    EquipadosGanhos(jogador)
    
    return troca_realizada
    