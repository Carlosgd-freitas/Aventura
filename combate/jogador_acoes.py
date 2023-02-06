import sys
from tabulate import tabulate
from colorama import Fore, Back, Style

sys.path.append("..")
from base import imprimir, utils

def EscolherAlvo(criaturas):
    """
    Imprime as possíveis criaturas que o jogador pode atacar ou usar uma habilidade de alvo único e retorna
    o índice da lista de criaturas correspondente ao alvo escolhido.
    """

    print('\nEscolha quem deseja atacar:')
    for i, c in enumerate(criaturas):
        imprimir.ImprimirCriatura(i+1, c)
    
    print('\n[0] Retornar e escolher outra ação.\n')

    alvo = utils.LerNumeroIntervalo('> ', 0, len(criaturas))
    return alvo

def EscolherConsumivel(jogador):
    """
    Imprime os possíveis consumíveis que o jogador pode usar e retorna o índice do inventário correspondente
    ao item escolhido.
    """

    print('\nEscolha qual consumível deseja usar:')

    indice_print = 1
    indice_item = 0
    relacao = [(0, -1)]

    tabela = []
    cabecalho = ["Nome", "Quantidade"]
    alinhamento = ("left", "center")

    for item in jogador.inventario:

        if item.classificacao == "Consumível":

            t = []
            t.append(f'[{indice_print}] ' + item.nome) # Índice + Nome
            t.append(item.quantidade)                  # Quantidade
            tabela.append(t)

            relacao.append((indice_print, indice_item))
            indice_print += 1

        indice_item += 1
    
    print(tabulate(tabela, headers = cabecalho, colalign = alinhamento, tablefmt="psql"))
    print('\n[0] Retornar e escolher outra ação.\n')

    while True:
        escolha = utils.LerNumero('> ')

        if escolha >= 0 and escolha <= jogador.ContarItens("Consumível"):
            break
    
    # Mapeando a escolha para um índice do inventario
    for r in relacao:
        if r[0] == escolha:
            escolha = r[1]
            break
    
    # Impedindo alguns itens de serem utilizados em algumas situações
    if escolha != -1:
        valido = ValidaUsoConsumivel(jogador, jogador.inventario[escolha])

        if not valido:
            escolha = -1

    return escolha

def ValidaUsoConsumivel(jogador, item):
    """
    Retorna True se o item consumível pode ser utilizado normalmente ou False caso contrário.
    """
    valido = True

    # Usar itens com o hp cheio: Poções de Cura, Poções de Regeneração, Erva Curativa ou Mel de Abelhóide
    if jogador.hp == jogador.maxHp and (item.nome == "Poção Pequena de Cura" or \
        item.nome == "Poção Pequena de Regeneração" or item.nome == "Erva Curativa" or \
        item.nome == "Mel de Abelhóide"):
        print('Seu ' + Fore.RED + 'HP' + Style.RESET_ALL + ' já está maximizado.\n')
        valido = False
    
    # Poções de Mana com a mana cheia
    elif jogador.mana == jogador.maxMana and item.nome == "Poção Pequena de Mana":
        print('Sua ' + Fore.BLUE + 'Mana' + Style.RESET_ALL + ' já está maximizada.\n')
        valido = False
    
    # Antídoto sem estar envenenado
    elif jogador.EfeitoPresente("debuff", "Veneno") == -1 and item.nome == "Antídoto":

        if jogador.genero == "M":
            print('Você não está ' + Fore.GREEN + 'envenenado' + Style.RESET_ALL + '.\n')
        elif jogador.genero == "F":
            print('Você não está ' + Fore.GREEN + 'envenenada' + Style.RESET_ALL + '.\n')

        valido = False
    
    return valido

def UsarConsumivel(jogador, indice, inimigos = None, fora_combate = False):
    """
    Utiliza um item consumível do inventário do jogador.

    Parâmetros:
        - jogador: jogador que irá utilizar o item consumível;
        - indice: índice do item no inventário;
        - inimigos: lista de criaturas inimigas atualmente em combate.
    
    Parâmetros opcionais:
    - fora_combate: se igual a True, o item cosumível não foi usado em combate. O valor padrão é False.
    """

    item = jogador.inventario[indice]

    # Processando os buffs que o item concede
    for buff in item.buffs:
        utils.ProcessarEfeito(jogador, buff, jogador, item = item, fora_combate = fora_combate)
    
    # Processando dano e os debuffs que o item concede
    for debuff in item.debuffs:

        # Debuffs que afetam todos os inimigos
        if debuff.nome == "Dano todos inimigos" or debuff.nome == "Lentidão todos inimigos":
            for c in inimigos:
                utils.ProcessarEfeito(jogador, debuff, c, item = item, fora_combate = fora_combate)
                
    # Contabilizando a usagem do item
    item.quantidade -= 1
    if item.quantidade == 0:
        jogador.inventario.remove(jogador.inventario[indice])

def EscolherHabilidade(jogador):
    """
    Imprime as possíveis habilidades que o jogador pode usar e retorna o índice da lista de habilidades
    correspondente à habilidade escolhida.
    """

    print('\nEscolha qual habilidade deseja usar:')

    indice_atacar = jogador.HabilidadePresente("Atacar")
    indice_print = 1
    indice_item = 0
    relacao = [(0, -1)]

    tabela = []
    cabecalho = ["Nome", "Custo", "Recarga", "Tipo", "Passiva/Ativa", "Alvo"]
    alinhamento = ("left", "center", "center", "center", "center", "center")

    for habilidade in jogador.habilidades:

        # A habilidade de ataque normal, bem como habilidades passivas, não serão listadas
        if (indice_item != indice_atacar) and (habilidade.passiva_ativa == "Ativa"):

            t = []
            t.append(f'[{indice_print}] ' + habilidade.nome) # Índice + Nome
            # Custo
            custo = ""
            if len(habilidade.custo) > 0:
                for i, c in enumerate(habilidade.custo):
                    if (i != 0) and (i < len(habilidade.custo) - 1):
                        custo += ', '
                    if c[0] == "Mana":
                        custo += str(c[1]) + " " + imprimir.RetornarStringColorida(c[0])
                    elif c[0] == "HP":
                        custo += str(c[1]) + " " + imprimir.RetornarStringColorida(c[0])
            else:
                custo += '---'
            t.append(custo)
            # Recarga
            recarga = ""
            if habilidade.recarga_atual != habilidade.recarga:
                recarga += Back.BLACK + Fore.RED + str(habilidade.recarga_atual) + Style.RESET_ALL
            else:
                recarga += str(habilidade.recarga_atual)
            recarga += f' / {habilidade.recarga}'
            t.append(recarga)
            t.append(imprimir.RetornarTipo(habilidade.tipo))      # Tipo
            t.append(habilidade.passiva_ativa)                    # Passiva/Ativa
            t.append(habilidade.alvo)                             # Alvo
            tabela.append(t)

            relacao.append((indice_print, indice_item))
            indice_print += 1

        indice_item += 1
    
    print(tabulate(tabela, headers = cabecalho, colalign = alinhamento, tablefmt="psql"))
    print('\n[0] Retornar e escolher outra ação.\n')

    while True:
        valido = 1
        escolha = utils.LerNumero('> ')

        if escolha >= 0 and escolha <= relacao[-1][0]:

            # Mapeando a escolha para um índice da lista de habilidades
            for r in relacao:
                if r[0] == escolha:
                    escolha = r[1]
                    break
            
            if escolha != -1:

                # Checando o custo de usar a habilidade
                for c in jogador.habilidades[escolha].custo:
                    if c[0] == "Mana" and c[1] > jogador.mana:
                        print('Você não tem ' + Fore.BLUE + 'Mana' + Style.RESET_ALL +
                            ' o suficiente para usar esta habilidade.')
                        valido = 0

                    elif c[0] == "HP" and c[1] > jogador.hp:
                        print('Você não tem ' + Fore.RED + 'HP' + Style.RESET_ALL +
                            ' o suficiente para usar esta habilidade.')
                        valido = 0

                # Checando a recarga da habilidade
                if jogador.habilidades[escolha].recarga_atual < jogador.habilidades[escolha].recarga:
                    print('Esta habilidade ainda está em recarga.')
                    valido = 0

            if valido == 1:
                break
    
    return escolha
