"""Funções utilitárias usadas por diversas partes do jogo."""

import math
import random

from unidecode import unidecode

def LerNumero(string, tipo = "int"):
    """
    Lê e retorna um número da entrada. Se a entrada não for um número, a função continuará em Loop.
    
    Parâmetros:
    - string: string que será impressa enquanto se espera a entrada do jogador.

    Parâmetros opcionais:
    - tipo: define o type cast que será realizado na entrada do jogador. O valor padrão é "int".
    """
    quebrar = 0
    while True:

        if quebrar == 1:
            break
        quebrar = 0

        try:
            if tipo == "int":
                value = int(input(string))
            elif tipo == "float":
                value = float(input(string))
            quebrar = 1
        except:
            quebrar = 0
    
    return value

def LerNumeroIntervalo(string, low, high, tipo = "int", permitido = []):
    """
    Lê e retorna um número da entrada que esteja dentro do intervalo [low, high]. Se a entrada não for
    um número válido, a função continuará em Loop.
    
    Parâmetros:
    - string: string que será impressa enquanto se espera a entrada do jogador;
    - low: menor número cuja entrada será considerada válida;
    - high: maior número cuja entrada será considerada válida.

    Parâmetros opcionais:
    - tipo: define o type cast que será realizado na entrada do jogador. O valor padrão é "int";
    - permitido: lista de números que não precisam estar no intervalo [low, high] para serem considerados
    válidos. Por padrão, a lista é vazia.
    """
    while True:

        value = LerNumero(string, tipo)
        if value >= low and value <= high:
            break
        elif value in permitido:
            break
    
    return value

def CalcularChance(chance):
    """
    Retorna verdadeiro se um número gerado aleatoriamente entre 0 e 1 for menor ou igual a <chance> e falso caso
    contrário.

    Parâmetros:
    - chance: um número real entre 0 e 1, que representariam 0% e 100%, respectivamente.
    """
    r = random.random()
    if r <= chance:
        return True
    else:
        return False

def CalcularDano(atacante, alvo, item = None, habilidade = None):
    """
    Calcula e retorna o dano que um atacante irá infligir em um alvo ao utilizar uma habilidade e se o acerto
    foi crítico.
    """
    dano = 0
    acerto_critico = False
    fonte = None

    if habilidade is not None:
        # Se a habilidade não causa dano
        if habilidade.nao_causa_dano == True:
            return dano, acerto_critico

        # Valor inicial
        dano = habilidade.valor

        # Acrescentando possíveis modificadores de dano
        dano = habilidade.ContabilizarModificadores(dano, atacante)

        # Dano vem do uso de uma habilidade
        fonte = habilidade
    
    elif item is not None:
        # Se o item não causa dano
        if item.EfeitoPresente("Dano") is None:
            return dano, acerto_critico

        # Valor inicial
        efeito = item.EfeitoPresente("Dano")
        dano = efeito.valor

        # Dano vem do uso de um item
        fonte = item

    tipo_fonte = unidecode(fonte.tipo).lower()
    tipo_alvo = unidecode(alvo.tipo).lower()

    # Alvo recebe 200% do dano
    if ((tipo_fonte == "fogo" and tipo_alvo == "terrestre") or
        (tipo_fonte == "fogo" and tipo_alvo == "gelo") or
        (tipo_fonte == "terrestre" and tipo_alvo == "agua") or
        (tipo_fonte == "terrestre" and tipo_alvo == "eletrico") or
        (tipo_fonte == "agua" and tipo_alvo == "fogo") or
        (tipo_fonte == "agua" and tipo_alvo == "vento") or
        (tipo_fonte == "vento" and tipo_alvo == "fogo") or
        (tipo_fonte == "vento" and tipo_alvo == "gelo") or
        (tipo_fonte == "eletrico" and tipo_alvo == "agua") or
        (tipo_fonte == "eletrico" and tipo_alvo == "vento") or
        (tipo_fonte == "gelo" and tipo_alvo == "terrestre") or
        (tipo_fonte == "gelo" and tipo_alvo == "eletrico") or
        (tipo_fonte == "trevas" and tipo_alvo == "luz") or
        (tipo_fonte == "luz" and tipo_alvo == "trevas")):
        dano *= 2.0
    
    # Alvo recebe 75% do dano
    elif ((tipo_alvo == "trevas" and tipo_fonte == "fogo") or
        (tipo_alvo == "trevas" and tipo_fonte == "terrestre") or
        (tipo_alvo == "trevas" and tipo_fonte == "agua") or
        (tipo_alvo == "trevas" and tipo_fonte == "vento") or
        (tipo_alvo == "trevas" and tipo_fonte == "eletrico") or
        (tipo_alvo == "trevas" and tipo_fonte == "gelo") or
        (tipo_alvo == "luz" and tipo_fonte == "fogo") or
        (tipo_alvo == "luz" and tipo_fonte == "terrestre") or
        (tipo_alvo == "luz" and tipo_fonte == "agua") or
        (tipo_alvo == "luz" and tipo_fonte == "vento") or
        (tipo_alvo == "luz" and tipo_fonte == "eletrico") or
        (tipo_alvo == "luz" and tipo_fonte == "gelo")):
        dano *= 0.75
    
    # Alvo recebe 50% do dano
    elif ((tipo_alvo == "fogo" and tipo_fonte == "terrestre") or
        (tipo_alvo == "fogo" and tipo_fonte == "gelo") or
        (tipo_alvo == "terrestre" and tipo_fonte == "agua") or
        (tipo_alvo == "terrestre" and tipo_fonte == "eletrico") or
        (tipo_alvo == "agua" and tipo_fonte == "fogo") or
        (tipo_alvo == "agua" and tipo_fonte == "vento") or
        (tipo_alvo == "vento" and tipo_fonte == "fogo") or
        (tipo_alvo == "vento" and tipo_fonte == "gelo") or
        (tipo_alvo == "eletrico" and tipo_fonte == "agua") or
        (tipo_alvo == "eletrico" and tipo_fonte == "vento") or
        (tipo_alvo == "gelo" and tipo_fonte == "terrestre") or
        (tipo_alvo == "gelo" and tipo_fonte == "eletrico") or
        (tipo_alvo == "trevas" and tipo_fonte == "luz") or
        (tipo_alvo == "luz" and tipo_fonte == "trevas")):
        dano *= 0.5
    
    # Acerto Crítico
    chance_critico = atacante.chance_critico + fonte.chance_critico
    multiplicador_critico = atacante.multiplicador_critico * fonte.multiplicador_critico

    if CalcularChance(chance_critico / 100):
        dano = math.ceil(dano * multiplicador_critico)
        acerto_critico = True

    # Checando se a habilidade é perfurante e diminuindo o dano pela defesa do alvo
    defesa = alvo.defesa

    if habilidade is not None:
        for e in habilidade.efeitos:
            if e.nome == "Perfurante %" and CalcularChance(e.chance / 100):
                defesa *= (1 - (e.valor / 100))
            break
    elif item is not None:
        for e in item.buffs:
            if e.nome == "Perfurante %" and CalcularChance(e.chance / 100):
                defesa *= (1 - (e.valor / 100))
            break
    
    dano -= defesa

    # Checando se o alvo está defendendo
    if alvo.EfeitoPresente("Defendendo") is not None:
        buff = alvo.EfeitoPresente("Defendendo")
        dano *= (buff.valor / 100)

    # Impedindo valores negativos
    dano = math.floor(dano)
    if dano < 0:
        dano = 0

    return dano, acerto_critico

def ListaEmString(lista):
    """
    Converte uma lista de elementos quaisquer em uma string para métodos __str__.
    """
    if len(lista) == 0:
        string = '[]'
        return string

    string = '[\n'
    for indice, elemento in enumerate(lista):
        string += str(elemento)
        if indice != len(lista) - 1:
            string += ',\n'
    string += '\n]'
    return string

def AtributoDestaque(criaturas, menor_maior, atributo):
    """
    Recebe uma lista de criaturas e um atributo e retorna o índice da criatura com o maior ou menor valor
    referente ao atributo passado dentre todas as criaturas.

    Parâmetros:
    - criaturas: lista de criaturas cujos atributos serão checados;
    - menor_maior: se igual a 'menor', será retornado o índice da criatura com o menor valor referente ao
    atributo passado, e se igual a 'maior', será retornado o índice da criatura com o maior valor;
    - atributo: o atributo que será checado nas criaturas. Valores possíveis: 'hp', 'maxHp - hp', 'mana',
    'maxMana - mana', 'ataque', 'defesa', 'magia' e 'velocidade'.
    """

    if menor_maior == 'menor':
        valor = 9999999
    elif menor_maior == 'maior':
        valor = -9999999
    indice = -1

    for i, c in enumerate(criaturas):

        if atributo == "hp":
            if menor_maior == 'menor' and c.hp < valor:
                valor = c.hp
                indice = i
            if menor_maior == 'maior' and c.hp > valor:
                valor = c.hp
                indice = i

        elif atributo == "maxHp - hp":
            if menor_maior == 'menor' and (c.maxHp - c.hp) < valor:
                valor = (c.maxHp - c.hp)
                indice = i
            if menor_maior == 'maior' and (c.maxHp - c.hp) > valor:
                valor = (c.maxHp - c.hp)
                indice = i
        
        elif atributo == "mana":
            if menor_maior == 'menor' and c.mana < valor:
                valor = c.mana
                indice = i
            if menor_maior == 'maior' and c.mana > valor:
                valor = c.mana
                indice = i
            
        elif atributo == "maxMana - mana":
            if menor_maior == 'menor' and (c.maxMana - c.mana) < valor:
                valor = (c.maxMana - c.mana)
                indice = i
            if menor_maior == 'maior' and (c.maxMana - c.mana) > valor:
                valor = (c.maxMana - c.mana)
                indice = i
        
        elif atributo == "ataque":
            if menor_maior == 'menor' and c.ataque < valor:
                valor = c.ataque
                indice = i
            if menor_maior == 'maior' and c.ataque > valor:
                valor = c.ataque
                indice = i
        
        elif atributo == "defesa":
            if menor_maior == 'menor' and c.defesa < valor:
                valor = c.defesa
                indice = i
            if menor_maior == 'maior' and c.defesa > valor:
                valor = c.defesa
                indice = i
        
        elif atributo == "magia":
            if menor_maior == 'menor' and c.magia < valor:
                valor = c.magia
                indice = i
            if menor_maior == 'maior' and c.magia > valor:
                valor = c.magia
                indice = i
        
        elif atributo == "velocidade":
            if menor_maior == 'menor' and c.velocidade < valor:
                valor = c.velocidade
                indice = i
            if menor_maior == 'maior' and c.velocidade > valor:
                valor = c.velocidade
                indice = i
    
    return indice

def RetirarSufixo(nome):
    """
    Retorna o nome de uma criatura sem o sufixo.

    Parâmetros:
    - nome: nome de uma criatura.
    """
    nome_separado = nome.split(' ')
    novo_nome = ''

    for palavra in nome_separado:
        if len(palavra) == 1 and palavra.isalpha() and palavra.isupper():
            break
        else:
            novo_nome += palavra
        novo_nome += ' '

    return novo_nome.strip()

def CompararNomes(nomes, ignorar_sufixos = True):
    """
    Retorna True se todos as strings presentes na lista <nomes> forem iguais e False caso contrário.

    Parâmetros:
    - nomes: lista de nomes das criaturas a serem comparados.
    
    Parâmetros Opcionais:
    - ignorar_sufixos: se igual a True, ignora possíveis sufixos nos nomes das criaturas. O valor padrão
    é True.
    """
    if ignorar_sufixos:
        novos_nomes = [RetirarSufixo(nome) for nome in nomes]
    else:
        novos_nomes = nomes
    
    comparacao = True
    if len(nomes) == 1:
        return comparacao
    else:
        for i, _ in enumerate(novos_nomes[1:]):
            comparacao = comparacao and (novos_nomes[i] == novos_nomes[i-1])
            if not comparacao:
                return comparacao
    return comparacao

def ContarNomes(nomes, nomes_zerados, criaturas, modifica_nomes_zerados = True):
    """
    Armazena no dicionário "nomes" quantas criaturas presentes na lista 'criaturas' possuem o mesmo nome, para
    cada nome único. No caso onde há apenas uma criatura com um determinado nome, sua entrada no dicionário terá
    o valor 0. O dicionário "nomes_zerados" possui o valor 0 para todos os nomes.
    """
    
    # Contando o número de criaturas com o mesmo nome
    for c in criaturas:
        nome = c.nome
        nomes[nome] = nomes.get(nome, 0) + 1

        if modifica_nomes_zerados:
            nomes_zerados[nome] = 0
    
    # Deixando apenas os número das criaturas com o mesmo nome
    for c in criaturas:
        nome = c.nome

        if nomes[nome] == 1:
            nomes[nome] = 0

    return nomes, nomes_zerados

def NomesUnicos(nomes, nomes_zerados, criaturas, criaturas2 = None):
    """
    Recebe dois dicionário "nomes", compostos pela função ContarNomes(), e duas listas de criaturas, uma para as
    aliadas e outra para as inimigas. Coloca um sufixo de uma letra ('A', 'B', 'C'...) após o nome das criaturas
    que possuam o mesmo nome.
    """

    todas_criaturas = []
    for c in criaturas:
        todas_criaturas.append(c)
    if criaturas2:
        for c in criaturas2:
            todas_criaturas.append(c)

    for c in todas_criaturas:
        nome = c.nome

        # Criatura não tinha seu nome no dicionário
        if (not (nome in nomes)) or (not (nome in nomes_zerados)):
            nomes[nome] = nomes.get(nome, 0) + 1
            nomes_zerados[nome] = 0

        if nomes[nome] > 0:
            # Convertendo o valor numérico em uma letra
            sufixo = nomes_zerados[nome] + 1
            sufixo = chr(sufixo + 64)
            nomes_zerados[nome] += 1

            nome += ' ' + sufixo
            c.nome = nome
