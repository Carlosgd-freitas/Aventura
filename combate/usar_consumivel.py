import sys
from tabulate import tabulate

sys.path.append("..")
from base import utils, imprimir

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

        if item.classe_batalha == "Consumível":

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
        print(f"Seu {imprimir.RetornarColorido('HP')} já está maximizado.\n")
        valido = False
    
    # Poções de Mana com a mana cheia
    elif jogador.mana == jogador.maxMana and item.nome == "Poção Pequena de Mana":
        print(f"Sua {imprimir.RetornarColorido('Mana')} já está maximizada.\n")
        valido = False
    
    # Antídoto sem estar envenenado
    elif jogador.EfeitoPresente("Veneno") is None and item.nome == "Antídoto":

        if jogador.genero == "M":
            print(f"Você não está {imprimir.RetornarColorido('envenenado')}.\n")
        elif jogador.genero == "F":
            print(f"Você não está {imprimir.RetornarColorido('envenenada')}.\n")

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

    if item.alvo == "Próprio":
        alvos = [jogador]
    elif item.alvo == "Inimigos":
        alvos = inimigos

    for alvo in alvos:

        # Processando os buffs que o item concede
        for buff in item.buffs:
            buff.Processar(jogador, alvo, item = item, fora_combate = fora_combate)
    
        # Processando dano e os debuffs que o item concede
        for debuff in item.debuffs:
            debuff.Processar(jogador, alvo, item = item, fora_combate = fora_combate)
                
    # Contabilizando a usagem do item
    item.quantidade -= 1
    if item.quantidade == 0:
        jogador.inventario.remove(jogador.inventario[indice])
