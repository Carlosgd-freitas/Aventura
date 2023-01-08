import time
from tabulate import tabulate
from colorama import Fore, Back, Style

### Impressão de strings ###

def ImprimirComDelay(string, delay):
    """
    Imprime cada letra de uma string após um delay definido em segundos.
    """

    for letra in string:
        print(letra, end = '')
        time.sleep(delay)

def ImprimirLocal(nome):
    """
    Imprime '== Local: X ==', onde X é o nome de um local a ser impresso em negrito.

    Parâmetros:
    - nome: nome do local a ser impresso.
    """
    print('\n== Local: ', end = '')
    print(Style.BRIGHT, end = '')

    if nome == "Planície de Slimes":
        print(Fore.GREEN + Back.BLACK + 'Planície de Slimes', end = '')
    elif nome == "Vila Pwikutt":
        print(Fore.WHITE + Back.BLACK + 'Vila Pwikutt', end = '')

    print(Style.RESET_ALL, end = '')
    print(' ==')

def RetornarTipo(tipo):
    """
    Recebe um tipo como parâmetro e o retorna juntamente com as funções para aplicação de cor
    correspondentes:
    * Normal    -> Branco
    * Fogo      -> Vermelho
    * Terrestre -> Verde
    * Agua      -> Azul
    * Vento     -> Ciano
    * Trevas    -> Magenta
    * Luz       -> Amarelo
    """
    
    if tipo == 'Normal':
        return Back.BLACK + Fore.WHITE + 'Normal' + Style.RESET_ALL
    elif tipo == 'Fogo':
        return Back.BLACK + Fore.RED + 'Fogo' + Style.RESET_ALL
    elif tipo == 'Terrestre':
        return Back.BLACK + Fore.GREEN + 'Terrestre' + Style.RESET_ALL
    elif tipo == 'Água':
        return Back.BLACK + Fore.BLUE + 'Água' + Style.RESET_ALL
    elif tipo == 'Vento':
        return Back.BLACK + Fore.CYAN + 'Vento' + Style.RESET_ALL
    elif tipo == 'Trevas':
        return Back.BLACK + Fore.MAGENTA + 'Trevas' + Style.RESET_ALL
    elif tipo == 'Luz':
        return Back.BLACK + Fore.YELLOW + 'Luz' + Style.RESET_ALL

def RetornarStringColorida(string):
    """
    Recebe uma string e a retorna juntamente com as funções para aplicação de cor correspondentes.
    """
    
    if string.lower() == 'hp':
        return Back.BLACK + Fore.RED + string + Style.RESET_ALL
    elif string.lower() == 'mana':
        return Back.BLACK + Fore.BLUE + string + Style.RESET_ALL
    elif string.lower() == 'veneno' or 'envenenamento':
        return Back.BLACK + Fore.GREEN + string + Style.RESET_ALL
    elif string.lower() == 'lentidão':
        return Back.BLACK + Fore.WHITE + string + Style.RESET_ALL

def ImprimirItemDetalhado(item):
    """
    Imprime um item do inventário detalhadamente.

    Parâmetros:
    - item: item a ser impresso.
    """

    # Informações "não-detalhadas" do item
    tabela = []
    cabecalho = ["Nome", "Quantidade", Fore.YELLOW + 'Preço' + Style.RESET_ALL, "Classificação"]
    alinhamento = ("left", "center", "center", "center")
    t = []
    t.append(item.nome)          # Índice + Nome
    t.append(item.quantidade)    # Quantidade
    t.append(item.preco)         # Preço
    t.append(item.classificacao) # Classificação
    tabela.append(t)
    print(tabulate(tabela, headers = cabecalho, colalign = alinhamento, tablefmt="psql"))

    # Descrição
    print(f'Descrição: {item.descricao}')

    if item.classificacao == "Consumível":

        # Efeitos 'positivos' concedidos pelo item
        for b in item.buffs:

            if b.nome == "Cura HP":
                print('* Cura ' + str(b.valor) + ' de ' + Fore.RED + 'HP' + Style.RESET_ALL + '.')
            elif b.nome == "Cura HP %":
                print('* Cura ' + str(b.valor) + '% do seu ' + Fore.RED + 'HP' + Style.RESET_ALL + ' máximo.')
            elif b.nome == "Cura HP % ou valor":
                print('* Cura ' + str(b.valor[0]) + '% do seu ' + Fore.RED + 'HP' + Style.RESET_ALL + ' máximo, ou ' +
                    str(b.valor[1]) + ' de ' + Fore.RED + 'HP' + Style.RESET_ALL + ', o que for maior.')
            
            elif b.nome == "Cura Mana":
                print('* Cura ' + str(b.valor) + ' de ' + Fore.BLUE + 'Mana' + Style.RESET_ALL + '.')
            elif b.nome == "Cura Mana %":
                print('* Cura ' + str(b.valor) + '% da sua ' + Fore.BLUE + 'Mana' + Style.RESET_ALL + ' máxima.')
            elif b.nome == "Cura Mana % ou valor":
                print('* Cura ' + str(b.valor[0]) + '% da sua ' + Fore.BLUE + 'Mana' + Style.RESET_ALL + ' máxima, ou ' +
                    str(b.valor[1]) + ' de ' + Fore.BLUE + 'Mana' + Style.RESET_ALL + ', o que for maior.')
            
            elif b.nome == "Regeneração HP":
                print('* Cura ' + str(b.valor) + ' de ' + Fore.RED + 'HP' + Style.RESET_ALL + ' ao longo de ' + 
                    str(b.duracao) + ' turnos.')
            elif b.nome == "Regeneração HP %":
                print('* Cura ' + str(b.valor) + '% do seu ' + Fore.RED + 'HP' + Style.RESET_ALL + ' máximo ao longo de ' +
                    str(b.duracao) + ' turnos.')
            
            elif b.nome == "Aumento Ataque":
                print('* Aumenta o ' + Style.BRIGHT + Back.BLACK + Fore.WHITE + 'ATAQUE' + Style.RESET_ALL + ' em ' +
                    str(b.valor) + ' por ' + str(b.duracao) + ' turnos.')
            elif b.nome == "Aumento Defesa":
                print('* Aumenta a ' + Style.BRIGHT + Back.BLACK + Fore.WHITE + 'DEFESA' + Style.RESET_ALL + ' em ' +
                    str(b.valor) + ' por ' + str(b.duracao) + ' turnos.')
            elif b.nome == "Aumento Magia":
                print('* Aumenta a ' + Style.BRIGHT + Back.BLACK + Fore.WHITE + 'MAGIA' + Style.RESET_ALL + ' em ' +
                    str(b.valor) + ' por ' + str(b.duracao) + ' turnos.')
            elif b.nome == "Aumento Velocidade":
                print('* Aumenta a ' + Style.BRIGHT + Back.BLACK + Fore.WHITE + 'VELOCIDADE' + Style.RESET_ALL + ' em ' +
                    str(b.valor) + ' por ' + str(b.duracao) + ' turnos.')

            elif b.nome == "Cura Veneno":
                print('* Cura o debuff de ' + Fore.GREEN + 'envenenamento' + Style.RESET_ALL + '.')

        # Efeitos 'negativos' concedidos pelo item  
        for d in item.debuffs:

            if d.nome == "Dano todos inimigos":
                print('* Causa ' + str(d.valor) + ' de dano a todos os inimigos.')
            elif d.nome == "Lentidão todos inimigos":
                print('* Causa ' + str(d.duracao) + ' turnos de ' + Style.BRIGHT + Back.BLACK + Fore.WHITE +
                    'Lentidão' + Style.RESET_ALL + ' a todos os inimigos.')

    else:
        # Nível e Tipo
        mensagem = 'Nível: {:2d} | Tipo: '.format(item.nivel)
        print(mensagem, end = '')
        print(RetornarTipo(item.tipo))

        # Atributos concedidos pelo item
        if item.maxHp > 0:
            print('* ' + Fore.GREEN + '+' + Style.RESET_ALL + f'{item.maxHp} ' +
                Fore.RED + 'HP' + Style.RESET_ALL)
        elif item.maxHp < 0:
            print('* ' + Fore.RED + '-' + Style.RESET_ALL + f'{item.maxHp} ' +
                Fore.RED + 'HP' + Style.RESET_ALL)

        if item.maxMana > 0:
            print('* ' + Fore.GREEN + '+' + Style.RESET_ALL + f'{item.maxMana} ' +
                Fore.BLUE + 'Mana' + Style.RESET_ALL)
        elif item.maxMana < 0:
            print('* ' + Fore.RED + '-' + Style.RESET_ALL + f'{item.maxMana} ' +
                Fore.BLUE + 'Mana' + Style.RESET_ALL)

        if item.ataque > 0:
            print('* ' + Fore.GREEN + '+' + Style.RESET_ALL + f'{item.ataque} ' +
                Style.BRIGHT + Back.BLACK + Fore.WHITE + 'ATAQUE' + Style.RESET_ALL)
        elif item.ataque < 0:
            print('* ' + Fore.RED + '-' + Style.RESET_ALL + f'{item.ataque} ' +
                Style.BRIGHT + Back.BLACK + Fore.WHITE + 'ATAQUE' + Style.RESET_ALL)

        if item.defesa > 0:
            print('* ' + Fore.GREEN + '+' + Style.RESET_ALL + f'{item.defesa} ' +
                Style.BRIGHT + Back.BLACK + Fore.WHITE + 'DEFESA' + Style.RESET_ALL)
        elif item.defesa < 0:
            print('* ' + Fore.RED + '-' + Style.RESET_ALL + f'{item.defesa} ' +
                Style.BRIGHT + Back.BLACK + Fore.WHITE + 'DEFESA' + Style.RESET_ALL)

        if item.magia > 0:
            print('* ' + Fore.GREEN + '+' + Style.RESET_ALL + f'{item.magia} ' +
                Style.BRIGHT + Back.BLACK + Fore.WHITE + 'MAGIA' + Style.RESET_ALL)
        elif item.magia < 0:
            print('* ' + Fore.RED + '-' + Style.RESET_ALL + f'{item.magia} ' +
                Style.BRIGHT + Back.BLACK + Fore.WHITE + 'MAGIA' + Style.RESET_ALL)

        if item.velocidade > 0:
            print('* ' + Fore.GREEN + '+' + Style.RESET_ALL + f'{item.velocidade} ' +
                Style.BRIGHT + Back.BLACK + Fore.WHITE + 'VELOCIDADE' + Style.RESET_ALL)
        elif item.velocidade < 0:
            print('* ' + Fore.RED + '-' + Style.RESET_ALL + f'{item.velocidade} ' +
                Style.BRIGHT + Back.BLACK + Fore.WHITE + 'VELOCIDADE' + Style.RESET_ALL)
        
        # Efeitos 'positivos' concedidos pelo item
        for b in item.buffs:
            if b.nome == "Resistência Veneno" or b.nome == "Equipamento:Resistência Veneno":
                print('* Resistência a ' + Fore.GREEN + 'Veneno' + Style.RESET_ALL + ': ' + str(b.valor * 100) + '%')

    print('')

### Impressão de classes ###

def ImprimirEfeitos(criatura, espaco = True):
    """
    Imprime os efeitos que uma criatura está sob. Retorna o número de efeitos que foram impressos.

    Parâmetros:
    - criatura: criatura cujos efeitos serão impressos.

    Parâmetros Opcionais:
    - espaco: se igual a False, o espaço antes do primeiro grupo de efeitos não será impresso. O valor padrão é
    True.
    """

    c_buffs = criatura.ContarEfeitos("buff")
    c_debuffs = criatura.ContarEfeitos("debuff")

    res_veneno = 0

    # Buffs presentes na criatura
    if len(c_buffs) > 0:

        if espaco:
            print(' ', end = '')
        print('[', end = '')

        for i, b in enumerate(c_buffs):
            if criatura.buffs[b].nome == "Defendendo":
                print(Style.BRIGHT + Fore.WHITE + 'DEFENDENDO'+ Style.RESET_ALL, end = '')
            
            elif criatura.buffs[b].nome == "Aumento Ataque":
                print('ATQ' + Fore.GREEN + '+' + Style.RESET_ALL, end = '')

            elif criatura.buffs[b].nome == "Aumento Defesa":
                print('DEF' + Fore.GREEN + '+' + Style.RESET_ALL, end = '')
            
            elif criatura.buffs[b].nome == "Aumento Magia":
                print('MAG' + Fore.GREEN + '+' + Style.RESET_ALL, end = '')

            elif criatura.buffs[b].nome == "Aumento Velocidade":
                print('VEL' + Fore.GREEN + '+' + Style.RESET_ALL, end = '')
            
            elif criatura.buffs[b].nome == "Aumento Chance Crítico":
                print('CRIT%' + Fore.GREEN + '+' + Style.RESET_ALL, end = '')
            
            elif criatura.buffs[b].nome == "Regeneração HP" or criatura.buffs[b].nome == "Regeneração HP %":
                print('REGEN ' + Fore.RED + 'HP' + Style.RESET_ALL, end = '')
            
            elif (criatura.buffs[b].nome == "Resistência Veneno" or criatura.buffs[b].nome == "Equipamento:Resistência Veneno") and (res_veneno == 0):
                print(Fore.RED + '-' + Fore.GREEN + 'VENENO' + Style.RESET_ALL + '%', end = '')
                res_veneno = 1

            if i != len(c_buffs) - 1:
                print(' | ', end = '')
        
        print(']', end = '')

    # Debuffs presentes na criatura
    if len(c_debuffs) > 0:

        if espaco and len(c_buffs) == 0:
            print(' ', end = '')
        elif len(c_buffs) > 0:
            print(' ', end = '')
        print('[', end = '')

        for i, d in enumerate(c_debuffs):
            if criatura.debuffs[d].nome == "Defendendo":
                print(Style.BRIGHT + Fore.WHITE + 'DEFENDENDO'+ Style.RESET_ALL, end = '')
            
            elif criatura.debuffs[d].nome == "Diminuição Ataque":
                print('ATQ' + Fore.RED + '-' + Style.RESET_ALL, end = '')

            elif criatura.debuffs[d].nome == "Diminuição Defesa":
                print('DEF' + Fore.RED + '-' + Style.RESET_ALL, end = '')
            
            elif criatura.debuffs[d].nome == "Diminuição Magia":
                print('MAG' + Fore.RED + '-' + Style.RESET_ALL, end = '')

            elif criatura.debuffs[d].nome == "Diminuição Velocidade":
                print('VEL' + Fore.RED + '-' + Style.RESET_ALL, end = '')
            
            elif criatura.debuffs[d].nome == "Diminuição Chance Crítico":
                print('CRIT%' + Fore.RED + '-' + Style.RESET_ALL, end = '')
            
            elif criatura.debuffs[d].nome == "Veneno":
                print(Fore.GREEN + 'VENENO' + Style.RESET_ALL, end = '')
            
            elif criatura.debuffs[d].nome == "Atordoamento":
                print(Style.BRIGHT + Fore.WHITE + 'ATORDOAMENTO' + Style.RESET_ALL, end = '')
            
            elif criatura.debuffs[d].nome == "Lentidão":
                print(Style.BRIGHT + Fore.WHITE + 'LENTIDÃO' + Style.RESET_ALL, end = '')

            if i != len(c_debuffs) - 1:
                print(' | ', end = '')
        
        print(']', end = '')
    
    print('')

    return len(c_buffs) + len(c_debuffs)

def ImprimirCriatura(indice, criatura):
    """
    Imprime uma criatura inimiga em batalha.
    """
    # Índice e nome da criatura
    mensagem = f'[{indice}] {criatura.nome} - '

    # Tipo da criatura
    mensagem += 'Tipo: '
    print(mensagem, end = '')
    print(RetornarTipo(criatura.tipo), end = '')

    mensagem = ' - '

    # HP da criatura
    mensagem += Fore.RED + 'HP' + Style.RESET_ALL + f' {criatura.hp}/{criatura.maxHp} - '

    # Mana da criatura
    mensagem += Fore.BLUE + 'Mana' + Style.RESET_ALL + f' {criatura.mana}/{criatura.maxMana}'

    print(mensagem, end = '')
    ImprimirEfeitos(criatura)

def ImprimirJogador(jogador):
    """
    Imprime o jogador em batalha.
    """
    # Nome e classe do jogador
    mensagem = f'{jogador.nome} - Classe: {jogador.classe} - Nível: {jogador.nivel} - '

    # HP do jogador
    mensagem += Fore.RED + 'HP' + Style.RESET_ALL + f' {jogador.hp}/{jogador.maxHp} - '

    # Mana do jogador
    mensagem += Fore.BLUE + 'Mana' + Style.RESET_ALL + f' {jogador.mana}/{jogador.maxMana}'

    print(mensagem, end = '')
    ImprimirEfeitos(jogador)

def ImprimirEfeitosEquipamentos(jogador):
    """
    Imprime os efeitos concedidos pelos equipamentos do jogador. Retorna True se algum efeito foi impresso e False caso contrário.
    """

    efeitos = {}
    imprimiu = False

    # Contabilizando efeitos
    for e in jogador.equipados:
        for b in e.buffs:
            if (b.nome == "Resistência Veneno" or b.nome == "Equipamento:Resistência Veneno") and ("Resistência Veneno" not in efeitos):
                efeitos["Resistência Veneno"] = b.valor
            elif (b.nome == "Resistência Veneno" or b.nome == "Equipamento:Resistência Veneno"):
                efeitos["Resistência Veneno"] += b.valor
    
    # Imprimindo efeitos
    if "Resistência Veneno" in efeitos:
        print('* Resistência a ' + Fore.GREEN + 'Veneno' + Style.RESET_ALL + ': ' + str(b.valor * 100) + '%')
        imprimiu = True
    
    return imprimiu

### Mensagens do Sistema ###

def MensagemErro(string, modo = 'input'):
    """
    Imprime '[ERRO]' em vermelho, negrito e fundo preto, seguido de um espaço e uma string na cor padrão.
    
    Parâmetros:
    - string: a string que será impressa.

    Parâmetros opcionais:
    - modo: caso seja 'input', o jogo irá esperar o usuário apertar [ENTER] antes de prosseguir, e caso seja
    'print', esta espera não ocorrerá. O valor padrão é 'input'.
    """
    print(Style.BRIGHT + Back.BLACK + Fore.RED + '[ERRO]' + Style.RESET_ALL, end = '')

    if modo == 'input':
        input(' ' + string)
    else:
        print(' ' + string)

def MensagemSistema(string, modo = 'input'):
    """
    Imprime '[SISTEMA]' em branco, negrito e fundo preto, seguido de um espaço e uma string na cor padrão.

    Parâmetros:
    - string: a string que será impressa.

    Parâmetros opcionais:
    - modo: caso seja 'input', o jogo irá esperar o usuário apertar [ENTER] antes de prosseguir, e caso seja
    'print', esta espera não ocorrerá. O valor padrão é 'input'.
    """
    print(Style.BRIGHT + Back.BLACK + Fore.WHITE + '[SISTEMA]' + Style.RESET_ALL, end = '')

    if modo == 'input':
        input(' ' + string)
    else:
        print(' ' + string)
