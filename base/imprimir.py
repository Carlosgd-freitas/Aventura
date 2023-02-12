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
    elif  string.lower() == '+' or string.lower() == '>>':
        return Back.BLACK + Fore.GREEN + string + Style.RESET_ALL
    elif  string.lower() == '-' or string.lower() == '<<':
        return Back.BLACK + Fore.RED + string + Style.RESET_ALL
    elif string.lower() == 'defendendo':
        return Style.BRIGHT + Back.BLACK + Fore.WHITE + string + Style.RESET_ALL
    elif string.lower() == 'veneno' or string.lower() == 'envenenamento':
        return Back.BLACK + Fore.GREEN + string + Style.RESET_ALL
    elif string.lower() == 'lentidão' or string.lower() == 'atordoamento':
        return Style.BRIGHT + Back.BLACK + Fore.WHITE + string + Style.RESET_ALL
    elif string.lower() == 'ataque' or string.lower() == 'atq':
        return Style.BRIGHT + Back.BLACK + Fore.WHITE + string + Style.RESET_ALL
    elif string.lower() == 'defesa' or string.lower() == 'def':
        return Style.BRIGHT + Back.BLACK + Fore.WHITE + string + Style.RESET_ALL
    elif string.lower() == 'magia' or string.lower() == 'mag':
        return Style.BRIGHT + Back.BLACK + Fore.WHITE + string + Style.RESET_ALL
    elif string.lower() == 'velocidade' or string.lower() == 'vel':
        return Style.BRIGHT + Back.BLACK + Fore.WHITE + string + Style.RESET_ALL
    elif string.lower() == 'chance de acerto crítico' or string.lower() == 'crit%':
        return Style.BRIGHT + Back.BLACK + Fore.WHITE + string + Style.RESET_ALL
    elif string.lower() == 'multiplicador de dano crítico' or string.lower() == 'crit':
        return Style.BRIGHT + Back.BLACK + Fore.WHITE + string + Style.RESET_ALL
    elif string.lower() == 'nível':
        return Style.BRIGHT + Back.BLACK + Fore.WHITE + string + Style.RESET_ALL

### Impressão de classes ###

def ImprimirEfeitoDetalhado(efeito):
    """
    Imprime um efeito de uma habilidade ou efeito detalhadamente.

    Parâmetros:
    - efeito: efeito a ser impresso.
    """

    if efeito.duracao <= 1:
        mensagem_duracao = f'{efeito.duracao} turno'
    else:
        mensagem_duracao = f'{efeito.duracao} turnos'

    # Chance do efeito ocorrer
    if abs(efeito.chance - 100) < 0.0001:
        print('* ', end = '')
    else:
        print('* [{:.1f}%] '.format(efeito.chance), end = '')

    # Efeitos de Cura de HP
    if efeito.nome == "Cura HP":
        print(f'Cura {efeito.valor} de {RetornarStringColorida("HP")}.')
    elif efeito.nome == "Cura HP %":
        print(f'Cura {efeito.valor}% do {RetornarStringColorida("HP")} máximo.')
    elif efeito.nome == "Cura HP % ou valor":
        print(f'Cura {efeito.valor[0]}% do {RetornarStringColorida("HP")} máximo, ou ' +
            f'{efeito.valor[1]} de {RetornarStringColorida("HP")} o que for maior.')
    
    # Efeitos de Cura de Mana
    elif efeito.nome == "Cura Mana":
        print(f'Cura {efeito.valor} de {RetornarStringColorida("Mana")}.')
    elif efeito.nome == "Cura Mana %":
        print(f'Cura {efeito.valor}% + da {RetornarStringColorida("Mana")} máxima.')
    elif efeito.nome == "Cura Mana % ou valor":
        print(f'Cura {efeito.valor[0]}% da {RetornarStringColorida("Mana")} máxima, ou ' +
            f'{efeito.valor[1]} de {RetornarStringColorida("Mana")}, o que for maior.')
    
    # Efeitos de Regeneração de HP
    elif efeito.nome == "Regeneração HP":
        print(f'Cura {efeito.valor} de {RetornarStringColorida("HP")} ao longo de {mensagem_duracao}.')
    elif efeito.nome == "Regeneração HP %":
        print(f'Cura {efeito.valor}% do {RetornarStringColorida("HP")} máximo ao longo de {mensagem_duracao}.')
    
    # Efeitos de Aumento de Atributo
    elif efeito.nome == "Aumento Ataque":
        print(f'Aumenta o {RetornarStringColorida("ATAQUE")} em {efeito.valor} por {mensagem_duracao}.')
    elif efeito.nome == "Aumento Defesa":
        print(f'Aumenta a {RetornarStringColorida("DEFESA")} em {efeito.valor} por {mensagem_duracao}.')
    elif efeito.nome == "Aumento Magia":
        print(f'Aumenta a {RetornarStringColorida("MAGIA")} em {efeito.valor} por {mensagem_duracao}.')
    elif efeito.nome == "Aumento Velocidade":
        print(f'Aumenta a {RetornarStringColorida("VELOCIDADE")} em {efeito.valor} por {mensagem_duracao}.')
    elif efeito.nome == "Aumento Chance Crítico":
        print(f'Aumenta a {RetornarStringColorida("Chance de Acerto Crítico")} em {efeito.valor}% por {mensagem_duracao}.')

    # Efeitos de Buff
    elif efeito.nome == "Defendendo":
        print(f'Concede o buff {RetornarStringColorida("Defendendo")}, reduzindo todo o dano recebido ' +
            'em {:.1f}% por '.format(efeito.valor) + f'{mensagem_duracao}.')

    # Efeitos de Debuff
    elif efeito.nome == "Veneno":
        print(f'Causa o debuff {RetornarStringColorida("Veneno")}, causando {efeito.valor} de dano no ' +
            f'início de cada turno, por {mensagem_duracao}.')
    elif efeito.nome == "Atordoamento":
        print(f'Causa o debuff {RetornarStringColorida("Atordoamento")}, impedindo quaisquer ações de ' +
            f'serem realizadas por {mensagem_duracao}.')
    elif efeito.nome == "Lentidão":
        print(f'Causa o debuff {RetornarStringColorida("Lentidão")}, reduzindo a' +
            f'{RetornarStringColorida("VELOCIDADE")} para 1 por {mensagem_duracao}.')

    # Efeitos de Resistência a Debuffs
    if efeito.nome == "Resistência Veneno":
        print(f'{(efeito.valor * 100)}% de chance de não receber efeitos de {RetornarStringColorida("Veneno")}.')

    # Efeitos de Cura de Debuffs
    elif efeito.nome == "Cura Veneno":
        print(f'Cura o debuff de {RetornarStringColorida("Veneno")}.')

    # Efeitos Em área de Itens Consumíveis
    elif efeito.nome == "Dano todos inimigos":
        print(f'Causa {efeito.valor} de dano a todos os inimigos.')
    elif efeito.nome == "Lentidão todos inimigos":
        print(f'Causa o debuff {RetornarStringColorida("Lentidão")} a todos os inimigos, reduzindo a ' +
            f'{RetornarStringColorida("VELOCIDADE")} para 1 por {mensagem_duracao}.')

    # Efeitos de Diminuição de Atributo
    elif efeito.nome == "Diminuição Ataque":
        print(f'Diminui o {RetornarStringColorida("ATAQUE")} em {efeito.valor} por {mensagem_duracao}.')
    elif efeito.nome == "Diminuição Defesa":
        print(f'Diminui a {RetornarStringColorida("DEFESA")} em {efeito.valor} por {mensagem_duracao}.')
    elif efeito.nome == "Diminuição Magia":
        print(f'Diminui a {RetornarStringColorida("MAGIA")} em {efeito.valor} por {mensagem_duracao}.')
    elif efeito.nome == "Diminuição Velocidade":
        print(f'Diminui a {RetornarStringColorida("VELOCIDADE")} em {efeito.valor} por {mensagem_duracao}.')
    elif efeito.nome == "Diminuição Chance Crítico":
        print(f'Diminui a {RetornarStringColorida("Chance de Acerto Crítico")} em {efeito.valor}% por {mensagem_duracao}.')
    
    # Efeitos de Modificação de Ataque
    elif efeito.nome == "Perfurante %":
        print('Ignora {:.1f}% da '.format(efeito.valor) + f'{RetornarStringColorida("DEFESA")} no cálculo de dano.')

    # Efeitos Miscelâneos
    elif efeito.nome.startswith("Invocar:"):
        conteudo = efeito.nome.split(":") # ["Invocar", "2", "Slime", "1", "Derrotado", "M"]
        quantidade = conteudo[1]
        invocado = conteudo[2]
        nivel = conteudo[3]
        forma = conteudo[4]
        genero = conteudo[5]

        # Quantidade de criaturas a serem invocadas
        mensagem_invocacao = f'Invoca {quantidade} '
        if invocado == "Slime" and quantidade > 1:
            mensagem_invocacao += "Slimes"
        else:
            mensagem_invocacao += invocado

        # Forma com que as criaturas serão invocadas
        mensagem_invocacao += f' de nível {nivel}'
        if forma == "Derrotado":
            if genero == "M":
                mensagem_invocacao += ' ao ser derrotado.'
            if genero == "F":
                mensagem_invocacao += ' ao ser derrotada.'
        elif forma == "Usar":
            mensagem_invocacao += '.'

        print(mensagem_invocacao)
    
    elif efeito.nome.startswith("Vingança:"):
        conteudo = efeito.nome.split(":") # ["Vingança", "Larva de Abelhóide", "Aumento Ataque", "F"]
        derrotada = conteudo[1]
        efeito_acionado = conteudo[2]
        genero = conteudo[3]

        # Efeito a ser acionado quando uma criatura aliada é derrotada
        if efeito_acionado == "Aumento Ataque":
            mensagem_vinganca = f'Aumenta o {RetornarStringColorida("ATAQUE")} em {efeito.valor}'
        elif efeito_acionado == "Aumento Defesa":
            mensagem_vinganca = f'Aumenta a {RetornarStringColorida("DEFESA")} em {efeito.valor}'
        elif efeito_acionado == "Aumento Magia":
            mensagem_vinganca = f'Aumenta a {RetornarStringColorida("MAGIA")} em {efeito.valor}'
        elif efeito_acionado == "Aumento Velocidade":
            mensagem_vinganca = f'Aumenta a {RetornarStringColorida("VELOCIDADE")} em {efeito.valor}'
        elif efeito_acionado == "Aumento Chance Crítico":
            mensagem_vinganca = f'Aumenta a {RetornarStringColorida("Chance de Acerto Crítico")} em ' + \
                '{:.1f}%'.format(efeito.valor)
        elif efeito_acionado == "Diminuição Ataque":
            mensagem_vinganca = f'Diminui o {RetornarStringColorida("ATAQUE")} em {efeito.valor}'
        elif efeito_acionado == "Diminuição Defesa":
            mensagem_vinganca = f'Diminui a {RetornarStringColorida("DEFESA")} em {efeito.valor}'
        elif efeito_acionado == "Diminuição Magia":
            mensagem_vinganca = f'Diminui a {RetornarStringColorida("MAGIA")} em {efeito.valor}'
        elif efeito_acionado == "Diminuição Velocidade":
            mensagem_vinganca = f'Diminui a {RetornarStringColorida("VELOCIDADE")} em {efeito.valor}'
        elif efeito_acionado == "Diminuição Chance Crítico":
            mensagem_vinganca = f'Diminui a {RetornarStringColorida("Chance de Acerto Crítico")} em ' + \
                '{:.1f}%'.format(efeito.valor)

        # Criatura aliada a ser derrotada para ativar o efeito
        if genero == "M":
            mensagem_vinganca += f' quando um {derrotada} aliado é derrotado.'
        if genero == "F":
            mensagem_vinganca += f' quando uma {derrotada} aliada é derrotada.'

        print(mensagem_vinganca)

def RetornarTabelaItens(itens, indice = -1):
    """
    Monta e retorna uma tabela a ser imprimida com cada item presente na lista de itens. Se <índice> for
    diferente de -1, [<indice>] será acrescentado antes do nome de cada item e incrementado em 1.
    """
    tabela = []
    cabecalho = ["Nome", "Quantidade", Fore.YELLOW + 'Preço' + Style.RESET_ALL, "Classe"]
    alinhamento = ("left", "center", "center", "center")
        
    for item in itens:
        t = []
        # Índice + Nome
        if indice != -1:
            t.append(f'[{indice}] ' + item.nome)
        else:
            t.append(item.nome)
        t.append(item.quantidade)     # Quantidade
        t.append(item.preco)          # Preço
        t.append(item.classe_batalha) # Classe
        tabela.append(t)

        indice += 1
    
    tabela = tabulate(tabela, headers = cabecalho, colalign = alinhamento, tablefmt="psql")
    return tabela

def ImprimirItemDetalhado(item):
    """
    Imprime um item do inventário detalhadamente.

    Parâmetros:
    - item: item a ser impresso.
    """

    # Informações "não-detalhadas" do item
    tabela = RetornarTabelaItens([item])
    print(tabela)

    # Descrição
    print(f'Descrição: {item.descricao}')

    if item.classe_batalha != "Consumível" and item.classe != "Material":
        # Nível e Tipo
        mensagem = 'Nível: {:2d} | Tipo: '.format(item.nivel)
        print(mensagem, end = '')
        print(RetornarTipo(item.tipo))

        # Atributos concedidos pelo item
        if item.maxHp > 0:
            print(f'* {RetornarStringColorida("+")}{item.maxHp} {RetornarStringColorida("HP")}')
        elif item.maxHp < 0:
            print(f'* {RetornarStringColorida("-")}{item.maxHp} {RetornarStringColorida("HP")}')

        if item.maxMana > 0:
            print(f'* {RetornarStringColorida("+")}{item.maxMana} {RetornarStringColorida("Mana")}')
        elif item.maxMana < 0:
            print(f'* {RetornarStringColorida("-")}{item.maxMana} {RetornarStringColorida("Mana")}')

        if item.ataque > 0:
            print(f'* {RetornarStringColorida("+")}{item.ataque} {RetornarStringColorida("ATAQUE")}')
        elif item.ataque < 0:
            print(f'* {RetornarStringColorida("-")}{item.ataque} {RetornarStringColorida("ATAQUE")}')

        if item.defesa > 0:
            print(f'* {RetornarStringColorida("+")}{item.defesa} {RetornarStringColorida("DEFESA")}')
        elif item.defesa < 0:
            print(f'* {RetornarStringColorida("-")}{item.defesa} {RetornarStringColorida("DEFESA")}')

        if item.magia > 0:
            print(f'* {RetornarStringColorida("+")}{item.magia} {RetornarStringColorida("MAGIA")}')
        elif item.magia < 0:
            print(f'* {RetornarStringColorida("-")}{item.magia} {RetornarStringColorida("MAGIA")}')

        if item.velocidade > 0:
            print(f'* {RetornarStringColorida("+")}{item.velocidade} {RetornarStringColorida("VELOCIDADE")}')
        elif item.velocidade < 0:
            print(f'* {RetornarStringColorida("-")}{item.velocidade} {RetornarStringColorida("VELOCIDADE")}')
        
    # Efeitos 'positivos' concedidos pelo item
    for buff in item.buffs:
        ImprimirEfeitoDetalhado(buff)
    
    # Efeitos 'negativos' concedidos pelo item  
    for debuff in item.debuffs:
        ImprimirEfeitoDetalhado(debuff)

    print('')

def RetornarTabelaHabilidades(habilidades, indice = -1):
    """
    Monta e retorna uma tabela a ser imprimida com cada habilidade presente na lista de habilidades. Se <índice>
    for diferente de -1, [<indice>] será acrescentado antes do nome de cada habilidade e incrementado em 1.
    """
    tabela = []
    cabecalho = ["Nome", "Custo", "Recarga", "Tipo", "Passiva/Ativa", "Alvo"]
    alinhamento = ("left", "center", "center", "center", "center", "center")

    for habilidade in habilidades:
        t = []
        # Índice + Nome
        if indice != -1:
            t.append(f'[{indice}] ' + habilidade.nome)
        else:
            t.append(habilidade.nome)
        # Custo
        custo = ""
        if len(habilidade.custo) > 0:
            for i, c in enumerate(habilidade.custo):
                if (i != 0) and (i < len(habilidade.custo) - 1):
                    custo += ', '
                if c[0] == "Mana":
                    custo += str(c[1]) + " " + RetornarStringColorida(c[0])
                elif c[0] == "HP":
                    custo += str(c[1]) + " " + RetornarStringColorida(c[0])
        else:
            custo += '---'
        t.append(custo)
        # Recarga
        recarga = ""
        if habilidade.recarga == 1:
            recarga += f'{habilidade.recarga} Turno'
        else:
            recarga += f'{habilidade.recarga} Turnos'
        t.append(recarga)
        t.append(RetornarTipo(habilidade.tipo)) # Tipo
        t.append(habilidade.passiva_ativa)      # Passiva/Ativa
        t.append(habilidade.alvo)               # Alvo
        tabela.append(t)

        indice += 1
    
    tabela = tabulate(tabela, headers = cabecalho, colalign = alinhamento, tablefmt="psql")
    return tabela

def ImprimirHabilidadeDetalhada(habilidade):
    """
    Imprime uma habilidade de uma criatura detalhadamente.

    Parâmetros:
    - habilidade: habilidade a ser impressa.
    """

    # Informações "não-detalhadas" da habilidade
    tabela = RetornarTabelaHabilidades([habilidade])
    print(tabela)

    # Descrição
    print(f'Descrição: {habilidade.descricao}')

    # Chance de Acerto Crítico e Multiplicador de Dano Crítico
    if abs(habilidade.chance_critico - 0) > 0.0001:
        print(f'* {RetornarStringColorida("Chance de Acerto Crítico")}: ' + '{:.1f}%'.format(habilidade.chance_critico))
    if abs(habilidade.multiplicador_critico - 1) > 0.0001:
        print(f'* {RetornarStringColorida("Multiplicador de Dano Crítico")}: ' + '{:.1f}x'.format(habilidade.multiplicador_critico))

    # Efeitos causados pelo uso da habilidade
    for e in habilidade.efeitos:
        ImprimirEfeitoDetalhado(e)

    # Modificadores
    if habilidade.modificadores:
        print('\nModificadores:')
        for m in habilidade.modificadores:
            if m[0] == "ataque":
                print(f'* {RetornarStringColorida("ATAQUE")}: ' + '{:.1f}%'.format(m[1]))
            elif m[0] == "defesa":
                print(f'* {RetornarStringColorida("DEFESA")}: ' + '{:.1f}%'.format(m[1]))
            elif m[0] == "magia":
                print(f'* {RetornarStringColorida("MAGIA")}: ' + '{:.1f}%'.format(m[1]))
            elif m[0] == "velocidade":
                print(f'* {RetornarStringColorida("VELOCIDADE")}: ' + '{:.1f}%'.format(m[1])) 

    print('')

def RetornarEfeitos(criatura, espaco = True):
    """
    Retorna uma string referente aos efeitos que uma criatura está sob e o número de efeitos contidos
    nessa string.

    Parâmetros:
    - criatura: criatura cujos efeitos serão impressos.

    Parâmetros Opcionais:
    - espaco: se igual a False, o espaço antes do primeiro grupo de efeitos não será impresso. O valor padrão é
    True.
    """

    c_buffs = criatura.ContarEfeitos("buff")
    c_debuffs = criatura.ContarEfeitos("debuff")

    n_buffs = criatura.ContarEfeitosImprimiveis("buff")
    n_debuffs = criatura.ContarEfeitosImprimiveis("debuff")

    mensagem = ''

    # Buffs presentes na criatura
    if n_buffs > 0:

        if espaco:
            mensagem += ' '
        mensagem += '['

        for i, b in enumerate(c_buffs):
            if criatura.buffs[b].nome == "Defendendo":
                mensagem += RetornarStringColorida("DEFENDENDO")
            
            elif criatura.buffs[b].nome == "Aumento Ataque":
                mensagem +=  RetornarStringColorida("ATQ") + RetornarStringColorida("+")

            elif criatura.buffs[b].nome == "Aumento Defesa":
                mensagem += RetornarStringColorida("DEF") + RetornarStringColorida("+")
            
            elif criatura.buffs[b].nome == "Aumento Magia":
                mensagem += RetornarStringColorida("MAG") + RetornarStringColorida("+")

            elif criatura.buffs[b].nome == "Aumento Velocidade":
                mensagem += RetornarStringColorida("VEL") + RetornarStringColorida("+")
            
            elif criatura.buffs[b].nome == "Aumento Chance Crítico":
                mensagem += RetornarStringColorida("CRIT%") + RetornarStringColorida("+")
            
            elif criatura.buffs[b].nome == "Regeneração HP" or criatura.buffs[b].nome == "Regeneração HP %":
                mensagem += 'REGEN ' + RetornarStringColorida("HP")

            if i != n_buffs - 1:
                mensagem += ' | '
        
        mensagem += ']'

    # Debuffs presentes na criatura
    if n_debuffs > 0:

        if espaco and n_buffs == 0:
            mensagem += ' '
        elif n_buffs > 0:
            mensagem += ' '
        mensagem += '['

        for i, d in enumerate(c_debuffs):
            
            if criatura.debuffs[d].nome == "Veneno":
                mensagem += RetornarStringColorida('VENENO')
            
            elif criatura.debuffs[d].nome == "Atordoamento":
                mensagem += RetornarStringColorida('ATORDOAMENTO')
            
            elif criatura.debuffs[d].nome == "Lentidão":
                mensagem += RetornarStringColorida("LENTIDÃO")
            
            elif criatura.debuffs[d].nome == "Diminuição Ataque":
                mensagem += RetornarStringColorida("ATQ") + RetornarStringColorida("-")

            elif criatura.debuffs[d].nome == "Diminuição Defesa":
                mensagem += RetornarStringColorida("DEF") + RetornarStringColorida("-")
            
            elif criatura.debuffs[d].nome == "Diminuição Magia":
                mensagem += RetornarStringColorida("MAG") + RetornarStringColorida("-")

            elif criatura.debuffs[d].nome == "Diminuição Velocidade":
                mensagem += RetornarStringColorida("VEL") + RetornarStringColorida("-")
            
            elif criatura.debuffs[d].nome == "Diminuição Chance Crítico":
                mensagem += RetornarStringColorida("CRIT%") + RetornarStringColorida("-")

            if i != n_debuffs - 1:
                mensagem += ' | '
        
        mensagem += ']'

    return mensagem, n_buffs + n_debuffs

def InimigosPresentes(inimigos):
    """
    Imprime uma lista de criaturas inimigas atualmente presentes em batalha.
    """
    
    tabela = []
    alinhamento = ("left", "left", "left", "left", "left")
        
    for indice, inimigo in enumerate(inimigos):
        t = []
        # Índice + Nome
        t.append(f'[{indice+1}] ' + inimigo.nome)
        # HP / MaxHP
        hp = f'- {RetornarStringColorida("HP")} {inimigo.hp}/{inimigo.maxHp}'
        t.append(hp)
        # Mana / MaxMana
        mana = f'- {RetornarStringColorida("Mana")} {inimigo.mana}/{inimigo.maxMana}'
        t.append(mana)
        # Tipo
        t.append(f'- Tipo: {RetornarTipo(inimigo.tipo)}')
        # Efeitos de buff/debuff
        efeitos, n_efeitos = RetornarEfeitos(inimigo)
        if n_efeitos > 0:
            t.append('- ' + efeitos)
        else:
            t.append('')
        tabela.append(t)
    
    print(tabulate(tabela, colalign = alinhamento, tablefmt="plain", numalign="right"))
    print('')

def ImprimirJogador(jogador):
    """
    Imprime o jogador em batalha.
    """
    # Nome e classe do jogador
    mensagem = f'{jogador.nome} - Classe: {jogador.classe} - Nível: {jogador.nivel} - '

    # HP do jogador
    mensagem += f'{RetornarStringColorida("HP")} {jogador.hp}/{jogador.maxHp} - '

    # Mana do jogador
    mensagem += f'{RetornarStringColorida("Mana")} {jogador.mana}/{jogador.maxMana}'

    print(mensagem, end = '')
    mensagem, n_efeitos = RetornarEfeitos(jogador)
    print(mensagem)

def ImprimirEfeitosEquipamentos(jogador):
    """
    Imprime os efeitos concedidos pelos equipamentos do jogador. Retorna True se algum efeito foi impresso e False caso contrário.
    """

    efeitos = {}
    imprimiu = False

    # Contabilizando efeitos
    for e in jogador.equipados:
        for b in e.buffs:
            if b.nome == "Resistência Veneno" and "Resistência Veneno" not in efeitos:
                efeitos["Resistência Veneno"] = b.valor
            elif b.nome == "Resistência Veneno":
                efeitos["Resistência Veneno"] += b.valor
    
    # Imprimindo efeitos
    if "Resistência Veneno" in efeitos:
        print(f'* Resistência a {RetornarStringColorida("Veneno")}: {b.valor * 100}%')
        imprimiu = True
    
    return imprimiu

def MensagemSubirNivel(atributos_antes, atributos_depois):
    """
    Imprime a mudança nos atributos do jogador após ele subir de nível.
    """
    hp = atributos_depois["maxHp"] -  atributos_antes["maxHp"]
    mana = atributos_depois["maxMana"] -  atributos_antes["maxMana"]
    ataque = atributos_depois["ataque"] -  atributos_antes["ataque"]
    defesa = atributos_depois["defesa"] -  atributos_antes["defesa"]
    magia = atributos_depois["magia"] -  atributos_antes["magia"]
    velocidade = atributos_depois["velocidade"] -  atributos_antes["velocidade"]

    if hp > 0:
        print(f'{RetornarStringColorida("HP")}: {atributos_antes["maxHp"]} {RetornarStringColorida(">>")} {atributos_depois["maxHp"]}')
    if mana > 0:
        print(f'{RetornarStringColorida("Mana")}: {atributos_antes["maxMana"]} {RetornarStringColorida(">>")} {atributos_depois["maxMana"]}')
    if ataque > 0:
        print(f'{RetornarStringColorida("ATAQUE")}: {atributos_antes["ataque"]} {RetornarStringColorida(">>")} {atributos_depois["ataque"]}')
    if defesa > 0:
        print(f'{RetornarStringColorida("DEFESA")}: {atributos_antes["defesa"]} {RetornarStringColorida(">>")} {atributos_depois["defesa"]}')
    if magia > 0:
        print(f'{RetornarStringColorida("MAGIA")}: {atributos_antes["magia"]} {RetornarStringColorida(">>")} {atributos_depois["magia"]}')
    if velocidade > 0:
        print(f'{RetornarStringColorida("VELOCIDADE")}: {atributos_antes["velocidade"]} {RetornarStringColorida(">>")} {atributos_depois["velocidade"]}')

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
