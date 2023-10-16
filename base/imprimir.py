import sys
import time

from tabulate import tabulate
from unidecode import unidecode

sys.path.append("..")
from base.cor import colorir
from sistemas import receita

### Impressão de strings ###

def ImprimirComDelay(string, delay):
    """
    Imprime cada letra de uma string após um delay definido em segundos.
    """
    if delay > 0:
        for letra in string:
            print(letra, end = '')
            time.sleep(delay)
    else:
        print(string, end = '')

def ImprimirLocal(nome):
    """
    Imprime '== Local: X ==', onde X é o nome de um local a ser impresso em negrito.

    Parâmetros:
    - nome: nome do local a ser impresso.
    """
    print('\n== Local: ', end = '')

    if nome == "Planície de Slimes":
        print(colorir(nome, frente="lima", frente_claro=True), end = ' ')
    elif nome == "Vila Pwikutt":
        print(colorir(nome, frente="oliva", frente_claro=True), end = ' ')

    print('==')

def RetornarColorido(string):
    """
    Recebe uma string e a retorna colorida.
    """
    string_normalizada = unidecode(string).lower().strip()

    if string_normalizada == "hp":
        return colorir(string, frente="vermelho", frente_claro=True)
    elif string_normalizada == "mana":
        return colorir(string, frente="azul", frente_claro=True)
    
    elif string_normalizada == "ouro" or string_normalizada == "preco":
        return colorir(string, frente="dourado", frente_claro=True)
    
    elif string_normalizada == "+" or string_normalizada == ">>":
        return colorir(string, frente="verde", frente_claro=True)
    elif string_normalizada == "-" or string_normalizada == "<<":
        return colorir(string, frente="vermelho", frente_claro=True)
    
    elif string_normalizada == "normal":
        return colorir(string, frente="branco", frente_claro=True)
    elif string_normalizada == "fogo":
        return colorir(string, frente="vermelho", frente_claro=True)
    elif string_normalizada == "terrestre":
        return colorir(string, frente="verde", frente_claro=True)
    elif string_normalizada == "agua":
        return colorir(string, frente="azul", frente_claro=True)
    elif string_normalizada == "vento":
        return colorir(string, frente="azul claro", frente_claro=True)
    elif string_normalizada == "eletrico":
        return colorir(string, frente="amarelo", frente_claro=True)
    elif string_normalizada == "gelo":
        return colorir(string, frente="ciano", frente_claro=True)
    elif string_normalizada == "trevas":
        return colorir(string, frente="roxo", frente_claro=True)
    elif string_normalizada == "luz":
        return colorir(string, frente="rosa", frente_claro=True)
    
    elif string_normalizada in ["veneno", "envenenar", "envenenado", "envenenados", "envenenada", "envenenadas",
        "envenenamento", "envenenou"]:
        return colorir(string, frente="oliva", frente_claro=True)
    elif string_normalizada in ["lentidao"]:
        return colorir(string, frente="branco", frente_claro=True)
    elif string_normalizada in ["atordoamento", "atordoar", "atordoado", "atordoados", "atordoada", "atordoadas",
        "atordoou"]:
        return colorir(string, frente="branco", frente_claro=True)
    elif string_normalizada in ["defendendo", "defendeu"]:
        return colorir(string, frente="branco", frente_claro=True)
    
    elif string_normalizada in ["ataque", "atq", "defesa", "def", "magia", "mag", "velocidade", "vel",
        "chance de acerto critico", "crit%", "multiplicador de dano critico", "crit", "nivel"]:
        return colorir(string, frente="branco", frente_claro=True)

    elif string_normalizada in ["critico!"]:
        return colorir(string, frente='laranja queimado', frente_claro=True)

    return string

def FormatarTempo(tempo):
    """
    Retorna uma string no formato horas:minutos:segundos.milissegundos.

    Parâmetros:
    - tempo: um objeto datetime.timedelta.
    """
    tempo_separado = str(tempo).split('.')
    ms = tempo_separado[1]
    ms = ms[:2]
    tempo_separado = tempo_separado[0].split(':')
    h = tempo_separado[0]
    m = tempo_separado[1]
    s = tempo_separado[2]
    if int(h) < 10:
        h = '0' + h
    return f'{h}:{m}:{s}.{ms}'

### Impressões de Tabelas ###

def RetornarTabelaItens(itens, jogador, indice = -1):
    """
    Monta e retorna uma tabela a ser imprimida com cada item presente na lista de itens. Se <índice> for
    diferente de -1, [<indice>] será acrescentado antes do nome de cada item e incrementado em 1.
    """
    tabela = []
    cabecalho = ["Nome", "Quantidade", RetornarColorido("Preço"), "Classe", "Nível", "Tipo", "Alvo"]
    alinhamento = ("left", "center", "center", "center", "center", "center", "center")
        
    for item in itens:
        t = []

        if not isinstance(item, receita.Receita):
            # Índice + Nome
            if indice != -1:
                t.append(f'[{indice}] ' + item.nome)
            else:
                t.append(item.nome)
            t.append(item.quantidade)     # Quantidade
            t.append(item.preco)          # Preço
            t.append(item.classe_batalha) # Classe
            # Nível
            if item.nivel > 0:
                if item.nivel > jogador.nivel:
                    t.append(colorir(item.nivel, frente="vermelho"))
                else:
                    t.append(item.nivel)
            else:
                t.append("---")
            # Tipo
            if item.tipo != "default":
                t.append(RetornarColorido(item.tipo))
            else:
                t.append("---")
            # Alvo
            if item.alvo != "default":
                t.append(item.alvo)
            else:
                t.append("---")

        else:
            # Índice + Nome
            if indice != -1:
                t.append(f'[{indice}] Receita: ' + item.nome)
            else:
                t.append(item.nome)
            t.append(1)                   # Quantidade
            t.append(item.preco)          # Preço
            t.append("Receita")           # Classe
            # Nível
            if item.nivel > 0:
                if item.nivel > jogador.nivel:
                    t.append(colorir(item.nivel, frente="vermelho"))
                else:
                    t.append(item.nivel)
            else:
                t.append("---")
            # Tipo
            t.append("---")
            # Alvo
            t.append("---")

        tabela.append(t)
        indice += 1
    
    tabela = tabulate(tabela, headers = cabecalho, colalign = alinhamento, tablefmt="psql")
    return tabela

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
                custo += str(c[1]) + " " + RetornarColorido(c[0])
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
        t.append(RetornarColorido(habilidade.tipo)) # Tipo
        t.append(habilidade.passiva_ativa)          # Passiva/Ativa
        t.append(habilidade.alvo)                   # Alvo
        tabela.append(t)

        indice += 1
    
    tabela = tabulate(tabela, headers = cabecalho, colalign = alinhamento, tablefmt="psql")
    return tabela

def RetornarTabelaReceitas(receitas, jogador, incluir_preco = True, indice = -1):
    """
    Monta e retorna uma tabela a ser imprimida com cada receita de fabricação presente na lista de receitas. Se
    <índice> for diferente de -1, [<indice>] será acrescentado antes do nome de cada item e incrementado em 1.
    """
    tabela = []

    if incluir_preco:
        cabecalho = ["Nome", "Nível", RetornarColorido("Preço")]
        alinhamento = ("left", "center", "center")
    else:
        cabecalho = ["Nome", "Nível"]
        alinhamento = ("left", "center")
        
    for receita in receitas:
        t = []
        # Índice + Nome
        if indice != -1:
            t.append(f'[{indice}] ' + receita.nome)
        else:
            t.append(receita.nome)
        # Nível
        if receita.nivel > 0:
            if receita.nivel > jogador.nivel:
                t.append(colorir(receita.nivel, frente="vermelho"))
            else:
                t.append(receita.nivel)
        else:
            t.append("---")
        # Preço
        if incluir_preco:
            t.append(receita.preco)
        tabela.append(t)

        indice += 1
    
    tabela = tabulate(tabela, headers = cabecalho, colalign = alinhamento, tablefmt="psql")
    return tabela

def RetornarTabelaSaves(saves):
    """
    Monta e retorna uma tabela a ser imprimida com cada jogo salvo presente na lista.
    """
    tabela = []

    alinhamento = ("left", "center", "center", "center", "center")
        
    for indice, save in enumerate(saves):
        t = []

        t.append(f'[{indice+1}] ' + save['jogador'].nome) # Índice + Nome do jogador
        t.append(save['jogador'].classe)                  # Classe do jogador
        t.append("Nível " + str(save['jogador'].nivel))   # Nível do jogador
        t.append(save['local'])                           # Local em que o jogo foi salvo
        # Data em que o jogo foi salvo
        t.append(save['estatisticas'].data_jogo_salvo.strftime("%d/%m/%Y - %H:%M:%S"))

        tabela.append(t)
    
    tabela = tabulate(tabela, colalign = alinhamento, tablefmt="grid")
    return tabela

### Impressões Detalhadas ###

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
        print(f'Cura {efeito.valor} de {RetornarColorido("HP")}.')
    elif efeito.nome == "Cura HP %":
        print(f'Cura {efeito.valor}% do {RetornarColorido("HP")} máximo.')
    elif efeito.nome == "Cura HP % ou valor":
        print(f'Cura {efeito.valor[0]}% do {RetornarColorido("HP")} máximo, ou ' +
            f'{efeito.valor[1]} de {RetornarColorido("HP")} o que for maior.')
    
    # Efeitos de Cura de Mana
    elif efeito.nome == "Cura Mana":
        print(f'Cura {efeito.valor} de {RetornarColorido("Mana")}.')
    elif efeito.nome == "Cura Mana %":
        print(f'Cura {efeito.valor}% + da {RetornarColorido("Mana")} máxima.')
    elif efeito.nome == "Cura Mana % ou valor":
        print(f'Cura {efeito.valor[0]}% da {RetornarColorido("Mana")} máxima, ou ' +
            f'{efeito.valor[1]} de {RetornarColorido("Mana")}, o que for maior.')
    
    # Efeitos de Regeneração de HP
    elif efeito.nome == "Regeneração HP":
        print(f'Cura {efeito.valor} de {RetornarColorido("HP")} ao longo de {mensagem_duracao}.')
    elif efeito.nome == "Regeneração HP %":
        print(f'Cura {efeito.valor}% do {RetornarColorido("HP")} máximo ao longo de {mensagem_duracao}.')
    
    # Efeitos de Aumento de Atributo
    elif efeito.nome == "Aumento Ataque":
        print(f'Aumenta o {RetornarColorido("ATAQUE")} em {efeito.valor} por {mensagem_duracao}.')
    elif efeito.nome == "Aumento Defesa":
        print(f'Aumenta a {RetornarColorido("DEFESA")} em {efeito.valor} por {mensagem_duracao}.')
    elif efeito.nome == "Aumento Magia":
        print(f'Aumenta a {RetornarColorido("MAGIA")} em {efeito.valor} por {mensagem_duracao}.')
    elif efeito.nome == "Aumento Velocidade":
        print(f'Aumenta a {RetornarColorido("VELOCIDADE")} em {efeito.valor} por {mensagem_duracao}.')
    elif efeito.nome == "Aumento Chance Crítico":
        print(f'Aumenta a {RetornarColorido("Chance de Acerto Crítico")} em {efeito.valor}% por {mensagem_duracao}.')

    # Efeitos de Buff
    elif efeito.nome == "Defendendo":
        print(f'Concede o buff {RetornarColorido("Defendendo")}, reduzindo todo o dano recebido ' +
            'em {:.1f}% por '.format(efeito.valor) + f'{mensagem_duracao}.')

    # Efeitos de Debuff
    elif efeito.nome == "Dano":
        print(f'Causa {efeito.valor} de dano.')
    elif efeito.nome == "Veneno":
        print(f'Causa o debuff {RetornarColorido("Veneno")}, causando {efeito.valor} de dano no ' +
            f'início de cada turno, por {mensagem_duracao}.')
    elif efeito.nome == "Atordoamento":
        print(f'Causa o debuff {RetornarColorido("Atordoamento")}, impedindo quaisquer ações de ' +
            f'serem realizadas por {mensagem_duracao}.')
    elif efeito.nome == "Lentidão":
        print(f'Causa o debuff {RetornarColorido("Lentidão")}, reduzindo a ' +
            f'{RetornarColorido("VELOCIDADE")} para 0 por {mensagem_duracao}.')

    # Efeitos de Resistência a Debuffs
    if efeito.nome == "Resistência Veneno":
        print(f'{(efeito.valor * 100)}% de chance de não receber efeitos de {RetornarColorido("Veneno")}.')

    # Efeitos de Cura de Debuffs
    elif efeito.nome == "Cura Veneno":
        print(f'Cura o debuff de {RetornarColorido("Veneno")}.')

    # Efeitos de Diminuição de Atributo
    elif efeito.nome == "Diminuição Ataque":
        print(f'Diminui o {RetornarColorido("ATAQUE")} em {efeito.valor} por {mensagem_duracao}.')
    elif efeito.nome == "Diminuição Defesa":
        print(f'Diminui a {RetornarColorido("DEFESA")} em {efeito.valor} por {mensagem_duracao}.')
    elif efeito.nome == "Diminuição Magia":
        print(f'Diminui a {RetornarColorido("MAGIA")} em {efeito.valor} por {mensagem_duracao}.')
    elif efeito.nome == "Diminuição Velocidade":
        print(f'Diminui a {RetornarColorido("VELOCIDADE")} em {efeito.valor} por {mensagem_duracao}.')
    elif efeito.nome == "Diminuição Chance Crítico":
        print(f'Diminui a {RetornarColorido("Chance de Acerto Crítico")} em {efeito.valor}% por {mensagem_duracao}.')
    
    # Efeitos de Modificação de Ataque
    elif efeito.nome == "Perfurante %":
        print('Ignora {:.1f}% da '.format(efeito.valor) + f'{RetornarColorido("DEFESA")} no cálculo de dano.')

    # Efeitos Miscelâneos
    elif efeito.nome == "Invocar":
        nome = efeito.invocacao["nome"]
        nivel = efeito.invocacao["nivel"]
        quantidade = efeito.invocacao["quantidade"]
        condicao = efeito.invocacao["condicao"]

        mensagem_invocacao = f"Invoca {quantidade} {nome} de nível {nivel}"
        if condicao.lower() == "derrota":
            mensagem_invocacao += " quando esta criatura é derrotada"
        mensagem_invocacao += "."

        print(mensagem_invocacao)
    
    elif efeito.nome.startswith("Vingança:"):
        conteudo = efeito.nome.split(":") # ["Vingança", "Larva de Abelhóide", "Aumento Ataque", "F"]
        derrotada = conteudo[1]
        efeito_acionado = conteudo[2]
        genero = conteudo[3]

        # Efeito a ser acionado quando uma criatura aliada é derrotada
        if efeito_acionado == "Aumento Ataque":
            mensagem_vinganca = f'Aumenta o {RetornarColorido("ATAQUE")} em {efeito.valor}'
        elif efeito_acionado == "Aumento Defesa":
            mensagem_vinganca = f'Aumenta a {RetornarColorido("DEFESA")} em {efeito.valor}'
        elif efeito_acionado == "Aumento Magia":
            mensagem_vinganca = f'Aumenta a {RetornarColorido("MAGIA")} em {efeito.valor}'
        elif efeito_acionado == "Aumento Velocidade":
            mensagem_vinganca = f'Aumenta a {RetornarColorido("VELOCIDADE")} em {efeito.valor}'
        elif efeito_acionado == "Aumento Chance Crítico":
            mensagem_vinganca = f'Aumenta a {RetornarColorido("Chance de Acerto Crítico")} em ' + \
                '{:.1f}%'.format(efeito.valor)
        elif efeito_acionado == "Diminuição Ataque":
            mensagem_vinganca = f'Diminui o {RetornarColorido("ATAQUE")} em {efeito.valor}'
        elif efeito_acionado == "Diminuição Defesa":
            mensagem_vinganca = f'Diminui a {RetornarColorido("DEFESA")} em {efeito.valor}'
        elif efeito_acionado == "Diminuição Magia":
            mensagem_vinganca = f'Diminui a {RetornarColorido("MAGIA")} em {efeito.valor}'
        elif efeito_acionado == "Diminuição Velocidade":
            mensagem_vinganca = f'Diminui a {RetornarColorido("VELOCIDADE")} em {efeito.valor}'
        elif efeito_acionado == "Diminuição Chance Crítico":
            mensagem_vinganca = f'Diminui a {RetornarColorido("Chance de Acerto Crítico")} em ' + \
                '{:.1f}%'.format(efeito.valor)

        # Criatura aliada a ser derrotada para ativar o efeito
        if genero == "M":
            mensagem_vinganca += f' quando um {derrotada} aliado é derrotado.'
        if genero == "F":
            mensagem_vinganca += f' quando uma {derrotada} aliada é derrotada.'

        print(mensagem_vinganca)

def ImprimirItemDetalhado(item, jogador):
    """
    Imprime um item detalhadamente.

    Parâmetros:
    - item: item a ser impresso;
    - jogador: objeto do jogador.
    """

    # Informações "não-detalhadas" do item
    tabela = RetornarTabelaItens([item], jogador)
    print(tabela)

    # Descrição
    print(f'Descrição: {item.descricao}')

    if item.classe_batalha != "Consumível" and item.classe != "Material":
        # Atributos concedidos pelo item
        if item.maxHp > 0:
            print(f'* {RetornarColorido("+")}{item.maxHp} {RetornarColorido("HP")}')
        elif item.maxHp < 0:
            print(f'* {RetornarColorido("-")}{item.maxHp} {RetornarColorido("HP")}')

        if item.maxMana > 0:
            print(f'* {RetornarColorido("+")}{item.maxMana} {RetornarColorido("Mana")}')
        elif item.maxMana < 0:
            print(f'* {RetornarColorido("-")}{item.maxMana} {RetornarColorido("Mana")}')

        if item.ataque > 0:
            print(f'* {RetornarColorido("+")}{item.ataque} {RetornarColorido("ATAQUE")}')
        elif item.ataque < 0:
            print(f'* {RetornarColorido("-")}{item.ataque} {RetornarColorido("ATAQUE")}')

        if item.defesa > 0:
            print(f'* {RetornarColorido("+")}{item.defesa} {RetornarColorido("DEFESA")}')
        elif item.defesa < 0:
            print(f'* {RetornarColorido("-")}{item.defesa} {RetornarColorido("DEFESA")}')

        if item.magia > 0:
            print(f'* {RetornarColorido("+")}{item.magia} {RetornarColorido("MAGIA")}')
        elif item.magia < 0:
            print(f'* {RetornarColorido("-")}{item.magia} {RetornarColorido("MAGIA")}')

        if item.velocidade > 0:
            print(f'* {RetornarColorido("+")}{item.velocidade} {RetornarColorido("VELOCIDADE")}')
        elif item.velocidade < 0:
            print(f'* {RetornarColorido("-")}{item.velocidade} {RetornarColorido("VELOCIDADE")}')
        
    # Efeitos 'positivos' concedidos pelo item
    for buff in item.buffs:
        ImprimirEfeitoDetalhado(buff)
    
    # Efeitos 'negativos' concedidos pelo item  
    for debuff in item.debuffs:
        ImprimirEfeitoDetalhado(debuff)

    print('')

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
        print(f'* {RetornarColorido("Chance de Acerto Crítico")}: ' + '{:.1f}%'.format(habilidade.chance_critico))
    if abs(habilidade.multiplicador_critico - 1) > 0.0001:
        print(f'* {RetornarColorido("Multiplicador de Dano Crítico")}: ' + '{:.1f}x'.format(habilidade.multiplicador_critico))

    # Efeitos causados pelo uso da habilidade
    for e in habilidade.efeitos:
        ImprimirEfeitoDetalhado(e)

    # Modificadores
    if habilidade.modificadores:
        print('\nModificadores:')
        for m in habilidade.modificadores:
            if m[0] == "ataque":
                print(f'* {RetornarColorido("ATAQUE")}: ' + '{:.1f}%'.format(m[1]))
            elif m[0] == "defesa":
                print(f'* {RetornarColorido("DEFESA")}: ' + '{:.1f}%'.format(m[1]))
            elif m[0] == "magia":
                print(f'* {RetornarColorido("MAGIA")}: ' + '{:.1f}%'.format(m[1]))
            elif m[0] == "velocidade":
                print(f'* {RetornarColorido("VELOCIDADE")}: ' + '{:.1f}%'.format(m[1])) 

    print('')

def ImprimirReceitaDetalhada(receita, jogador, incluir_preco = True):
    """
    Imprime uma receita de fabricação detalhadamente.

    Parâmetros:
    - receita: receita de fabricação a ser impressa;
    - jogador: objeto do jogador.

    Parâmetros Opcionais:
    - incluir_preco: se igual a True, o preço da receita será impresso. O valor padrão é True.
    """

    # Receita
    print('\nReceita:')
    print(RetornarTabelaReceitas([receita], jogador, incluir_preco = incluir_preco))

    # Materiais
    tabela = []
    cabecalho = ["Nome", "Quantidade"]
    alinhamento = ("left", "center")

    for item in receita.entrada:
        item_inventario = jogador.ItemPresente(item.nome)
        t = []

        # Nome
        t.append(item.nome)

        # Quantidade
        if not item_inventario:
            quantidade = colorir(f'[0 / {item.quantidade}]', frente="vermelho")
        elif item_inventario.quantidade < item.quantidade:
            quantidade = colorir(f'[{item_inventario.quantidade} / {item.quantidade}]', frente="vermelho")
        else:
            quantidade = colorir(f'[{item_inventario.quantidade} / {item.quantidade}]', frente="verde")
        t.append(quantidade)

        tabela.append(t)

    print('\nMateriais:')
    print(tabulate(tabela, headers = cabecalho, colalign = alinhamento, tablefmt="psql"))

    print('\nResultado:')
    for indice, item in enumerate(receita.saida):
        ImprimirItemDetalhado(item, jogador)

        if indice != len(receita.saida) - 1:
            print('')

### Impressões de Classes ###

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
                mensagem += RetornarColorido("DEFENDENDO")
            
            elif criatura.buffs[b].nome == "Aumento Ataque":
                mensagem +=  RetornarColorido("ATQ") + RetornarColorido("+")

            elif criatura.buffs[b].nome == "Aumento Defesa":
                mensagem += RetornarColorido("DEF") + RetornarColorido("+")
            
            elif criatura.buffs[b].nome == "Aumento Magia":
                mensagem += RetornarColorido("MAG") + RetornarColorido("+")

            elif criatura.buffs[b].nome == "Aumento Velocidade":
                mensagem += RetornarColorido("VEL") + RetornarColorido("+")
            
            elif criatura.buffs[b].nome == "Aumento Chance Crítico":
                mensagem += RetornarColorido("CRIT%") + RetornarColorido("+")
            
            elif criatura.buffs[b].nome == "Regeneração HP" or criatura.buffs[b].nome == "Regeneração HP %":
                mensagem += 'REGEN ' + RetornarColorido("HP")

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
                mensagem += RetornarColorido('VENENO')
            
            elif criatura.debuffs[d].nome == "Atordoamento":
                mensagem += RetornarColorido('ATORDOAMENTO')
            
            elif criatura.debuffs[d].nome == "Lentidão":
                mensagem += RetornarColorido("LENTIDÃO")
            
            elif criatura.debuffs[d].nome == "Diminuição Ataque":
                mensagem += RetornarColorido("ATQ") + RetornarColorido("-")

            elif criatura.debuffs[d].nome == "Diminuição Defesa":
                mensagem += RetornarColorido("DEF") + RetornarColorido("-")
            
            elif criatura.debuffs[d].nome == "Diminuição Magia":
                mensagem += RetornarColorido("MAG") + RetornarColorido("-")

            elif criatura.debuffs[d].nome == "Diminuição Velocidade":
                mensagem += RetornarColorido("VEL") + RetornarColorido("-")
            
            elif criatura.debuffs[d].nome == "Diminuição Chance Crítico":
                mensagem += RetornarColorido("CRIT%") + RetornarColorido("-")

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
        hp = f'- {RetornarColorido("HP")} {inimigo.hp}/{inimigo.maxHp}'
        t.append(hp)
        # Mana / MaxMana
        mana = f'- {RetornarColorido("Mana")} {inimigo.mana}/{inimigo.maxMana}'
        t.append(mana)
        # Tipo
        t.append(f'- Tipo: {RetornarColorido(inimigo.tipo)}')
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
    mensagem += f'{RetornarColorido("HP")} {jogador.hp}/{jogador.maxHp} - '

    # Mana do jogador
    mensagem += f'{RetornarColorido("Mana")} {jogador.mana}/{jogador.maxMana}'

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
        print(f'* Resistência a {RetornarColorido("Veneno")}: {b.valor * 100}%')
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
        print(f'{RetornarColorido("HP")}: {atributos_antes["maxHp"]} {RetornarColorido(">>")} {atributos_depois["maxHp"]}')
    if mana > 0:
        print(f'{RetornarColorido("Mana")}: {atributos_antes["maxMana"]} {RetornarColorido(">>")} {atributos_depois["maxMana"]}')
    if ataque > 0:
        print(f'{RetornarColorido("ATAQUE")}: {atributos_antes["ataque"]} {RetornarColorido(">>")} {atributos_depois["ataque"]}')
    if defesa > 0:
        print(f'{RetornarColorido("DEFESA")}: {atributos_antes["defesa"]} {RetornarColorido(">>")} {atributos_depois["defesa"]}')
    if magia > 0:
        print(f'{RetornarColorido("MAGIA")}: {atributos_antes["magia"]} {RetornarColorido(">>")} {atributos_depois["magia"]}')
    if velocidade > 0:
        print(f'{RetornarColorido("VELOCIDADE")}: {atributos_antes["velocidade"]} {RetornarColorido(">>")} {atributos_depois["velocidade"]}')

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
    print(colorir("[ERRO]", frente="vermelho", frente_claro=True), end = ' ')

    if modo == 'input':
        input(string)
    else:
        print(string)

def MensagemSistema(string, modo = 'input'):
    """
    Imprime '[SISTEMA]' em branco, negrito e fundo preto, seguido de um espaço e uma string na cor padrão.

    Parâmetros:
    - string: a string que será impressa.

    Parâmetros opcionais:
    - modo: caso seja 'input', o jogo irá esperar o usuário apertar [ENTER] antes de prosseguir, e caso seja
    'print', esta espera não ocorrerá. O valor padrão é 'input'.
    """
    print(colorir("[SISTEMA]", frente="branco", frente_claro=True), end = ' ')

    if modo == 'input':
        input(string)
    else:
        print(string)
