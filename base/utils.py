import math
import random
from copy import deepcopy
from colorama import Fore, Back, Style

def LerNumero(string, tipo = "int"):
    """
    Lê e retorna um número da entrada. Se a entrada não for um número, a função continuará em Loop. O parâmetro
    'tipo' define que as operações serão realizadas com números inteiros por padrão, e para realizá-las com números
    reais, basta mudá-lo para 'float'.
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

def LerNumeroIntervalo(string, low, high, tipo = "int"):
    """
    Lê e retorna um número da entrada que esteja dentro do intervalo [low, high]. Se a entrada não for um
    número, ou não estiver dentro do intervalo [low, high], a função continuará em Loop. O parâmetro 'tipo'
    define que as operações serão realizadas com números inteiros por padrão, e para realizá-las com números
    reais, basta mudá-lo para 'float'.
    """

    while True:

        value = LerNumero(string, tipo)
        if value >= low and value <= high:
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

def NumeroEmSufixo(numero):
    """
    Recebe um número inteiro e retorna um sufixo para garantir o nome único das criaturas.
    """

    if numero == 1:
        return 'A'
    elif numero == 2:
        return 'B'
    elif numero == 3:
        return 'C'
    elif numero == 4:
        return 'D'
    elif numero == 5:
        return 'E'
    elif numero == 6:
        return 'F'
    elif numero == 7:
        return 'G'
    elif numero == 8:
        return 'H'
    elif numero == 9:
        return 'I'
    elif numero == 10:
        return 'J'

def CompararSufixos(nome):
    """
    Retorna verdadeiro se uma string for igual a um sufixo (letras maiúsculas de A até J), e falso caso contrário.

    Parâmetros:
    - nome: string a ser comparada.
    """
    if nome == 'A' or nome == 'B' or nome == 'C' or nome == 'D' or nome == 'E' or nome == 'F' or nome == 'G' or \
        nome == 'H' or nome == 'I' or nome == 'J':
        return True
    else:
        return False

def CompararNomesSufixos(nomeA, nomeB):
    """
    Retorna o valor de comparação de duas strings sem o possível sufixo existente nelas.

    Parâmetros:
    - nomeA: string a ser comparada;
    - nomeB: string a ser comparada.
    """
    a = nomeA.split(' ')
    b = nomeB.split(' ')

    novo_a = ''
    novo_b = ''

    if len(a) == 1:
        novo_a = a[0]
    else:
        for i, palavra in enumerate(a):
            if CompararSufixos(palavra):
                break
            if i > 0:
                novo_a += ' '
            novo_a += palavra

    if len(b) == 1:
        novo_b = b[0]
    else:
        for i, palavra in enumerate(b):
            if CompararSufixos(palavra):
                break
            if i > 0:
                novo_b += ' '
            novo_b += palavra

    return novo_a == novo_b

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
            sufixo = NumeroEmSufixo(sufixo)
            nomes_zerados[nome] += 1

            nome += ' ' + sufixo
            c.nome = nome

def ContabilizarModificadores(valor, usuario, habilidade):
    """
    Acrescenta os modificadores de uma habilidade em um valor, retornando o valor resultante.

    Parâmetros:
    - valor: valor base;
    - usuario: qual criatura (ou jogador) está usando a habilidade;
    - habilidade: habilidade que possui os modificadores.
    """
    saida = valor
    for m in habilidade.modificadores:
        if m[0] == "ataque":
            saida += usuario.ataque * (m[1] / 100)
        elif m[0] == "defesa":
            saida += usuario.defesa * (m[1] / 100) 
        elif m[0] == "magia":
            saida += usuario.magia * (m[1] / 100)
        elif m[0] == "velocidade":
            saida += usuario.velocidade * (m[1] / 100) 
    saida = math.floor(saida)
    return saida

def ProcessarEfeito(usuario, efeito, alvo, item = None, habilidade = None, fora_combate = False, append = True):
    """
    Processa um efeito de buff/debuff de um item ou habilidade, utilizado por um usuário em um alvo. Apenas um
    dos parâmetros 'item' ou 'habilidade' deve receber um argumento, enquanto o outro permanece com None.
    
    Parâmetros:
    - usuario: qual criatura (ou jogador) está causando o efeito;
    - efeito: efeito a ser processado;
    - alvo: alvo do efeito;
    - item: item que irá causar o efeito;
    - habilidade: habilidade que irá causar o efeito.

    Parâmetros opcionais:
    - fora_combate: se igual a True, o efeito sendo processado não foi causado em combate. O valor padrão é False;
    - append: se igual a False, o efeito sendo processado não será adicionado a lista de buffs/debuffs da
    criatura. O valor padrão é True.
    """

    # Alguns efeitos terão sua chance calculada posteriormente
    if efeito.nome == "Veneno":
        pass
    # Se o efeito veio de uma habilidade e possui uma % de acontecer
    elif (habilidade is not None) and (not CalcularChance(efeito.chance / 100)):
        return

    # Flags para efeitos de item
    sobrecura_hp = 0
    sobrecura_mana = 0

    # Melhora das mensagens de uso de itens
    mensagem = None
    if item is not None:
        artigo = item.RetornarArtigo()
        contracao_por = item.RetornarContracaoPor().lower()

    ## Efeitos de Buff ##

    # Cura o HP em um valor definido, com base no HP máximo ou o que for maior dentre estas opções
    if efeito.nome == "Cura HP" or efeito.nome == "Cura HP %" or efeito.nome == "Cura HP % ou valor":
        valor = 0

        if efeito.nome == "Cura HP":
            valor = efeito.valor
        elif efeito.nome == "Cura HP %":
            valor = math.floor(alvo.maxHp * (efeito.valor / 100))
        else:
            valor1 = math.floor(alvo.maxHp * (efeito.valor[0] / 100))
            valor2 = efeito.valor[1]
            if valor1 > valor2:
                valor = valor1
            else:
                valor = valor2
        
        if habilidade is not None:
            valor = ContabilizarModificadores(valor, usuario, habilidade)

            # Acerto Crítico
            chance_critico = usuario.chance_critico + habilidade.chance_critico
            multiplicador_critico = usuario.multiplicador_critico * habilidade.multiplicador_critico

            if CalcularChance(chance_critico / 100):
                valor = math.ceil(valor * multiplicador_critico)
                print(Fore.GREEN + 'CRÍTICO!' + Style.RESET_ALL + ' ', end = '')

        alvo.hp += valor

        # Buff foi causado através de um item
        if item is not None:
            mensagem = f'{artigo} {item.nome} recuperou {valor} de ' + Fore.RED + 'HP' + Style.RESET_ALL + f' de {alvo.nome}.'
        # Buff foi causado através de uma habilidade ou outra fonte
        else:
            mensagem = f'{alvo.nome} recuperou {valor} de ' + Fore.RED + 'HP' + Style.RESET_ALL + '.'

        sobrecura_hp = 1

    # Cura a Mana em um valor definido, com base na Mana máxima ou o que for maior dentre estas opções
    elif efeito.nome == "Cura Mana" or efeito.nome == "Cura Mana %" or efeito.nome == "Cura Mana % ou valor":
        valor = 0

        if efeito.nome == "Cura Mana":
            valor = efeito.valor
        elif efeito.nome == "Cura Mana %":
            valor = math.floor(alvo.maxMana * (efeito.valor / 100))
        else:
            valor1 = math.floor(alvo.maxMana * (efeito.valor[0] / 100))
            valor2 = efeito.valor[1]
            if valor1 > valor2:
                valor = valor1
            else:
                valor = valor2
        
        if habilidade is not None:
            valor = ContabilizarModificadores(valor, usuario, habilidade)

            # Acerto Crítico
            chance_critico = usuario.chance_critico + habilidade.chance_critico
            multiplicador_critico = usuario.multiplicador_critico * habilidade.multiplicador_critico

            if CalcularChance(chance_critico / 100):
                valor = math.ceil(valor * multiplicador_critico)
                print(Fore.GREEN + 'CRÍTICO!' + Style.RESET_ALL + ' ', end = '')

        alvo.mana += valor

        # Buff foi causado através de um item
        if item is not None:
            mensagem = f'{artigo} {item.nome} recuperou {valor} de ' + Fore.BLUE + 'Mana' + Style.RESET_ALL + f' de {alvo.nome}.'
        # Buff foi causado através de uma habilidade ou outra fonte
        else:
            mensagem = f'{alvo.nome} recuperou {valor} de ' + Fore.BLUE + 'Mana' + Style.RESET_ALL + '.'

        sobrecura_mana = 1

    # Regenera o HP em um valor definido ou com base no HP máximo durante vários turnos
    elif efeito.nome == "Regeneração HP" or efeito.nome == "Regeneração HP %":
        valor = 0

        if efeito.nome == "Regeneração HP":
            valor = efeito.valor
        elif efeito.nome == "Regeneração HP %":
            valor = math.floor(alvo.maxHp * (efeito.valor / 100))
        
        # Se o efeito de regeneração foi causado fora de combate: recuperar todo o HP de uma vez
        if fora_combate:
            valor *= efeito.duracao

        alvo.hp += valor

        # Buff foi causado através de um item
        if item is not None:
            mensagem = f'{artigo} {item.nome} recuperou {valor} de ' + Fore.RED + 'HP' + Style.RESET_ALL + f' de {alvo.nome}.'
        # Buff foi causado através de uma habilidade ou outra fonte
        else:
            mensagem = f'{alvo.nome} recuperou {valor} de ' + Fore.RED + 'HP' + Style.RESET_ALL + '.'

        if not fora_combate:
            regen = deepcopy(efeito)
            regen.duracao -= regen.decaimento
            if append:
                alvo.buffs.append(regen)
        
        sobrecura_hp = 1
    
    # Aumento de Atributo
    elif efeito.nome == "Aumento Ataque" or efeito.nome == "Aumento Defesa" or \
        efeito.nome == "Aumento Magia" or efeito.nome == "Aumento Velocidade" or \
        efeito.nome == "Aumento Chance Crítico":

        aumento = deepcopy(efeito)
        valor_aumento = efeito.valor
        if habilidade is not None:
            valor_aumento = ContabilizarModificadores(valor_aumento, usuario, habilidade)
        aumento.valor = valor_aumento

        # Se a criatura já está sob o efeito de aumento do atributo
        if alvo.EfeitoPresente(efeito.nome) is not None:
            efeito_presente = alvo.EfeitoPresente(efeito.nome)
            efeito_presente.duracao += 1
            efeito_presente.valor += math.floor(0.25 * efeito_presente.valor)

            if efeito.nome == "Aumento Ataque":
                alvo.ataque += math.floor(0.25 * efeito_presente.valor)
                print(f'{alvo.nome} teve seu aumento de ataque melhorado em 25% e a duração do efeito extendida em 1 turno.')
            elif efeito.nome == "Aumento Defesa":
                alvo.defesa += math.floor(0.25 * efeito_presente.valor)
                print(f'{alvo.nome} teve seu aumento de defesa melhorado em 25% e a duração do efeito extendida em 1 turno.')
            elif efeito.nome == "Aumento Magia":
                alvo.magia += math.floor(0.25 * efeito_presente.valor)
                print(f'{alvo.nome} teve seu aumento de magia melhorado em 25% e a duração do efeito extendida em 1 turno.')
            elif efeito.nome == "Aumento Velocidade":
                alvo.velocidade += math.floor(0.25 * efeito_presente.valor)
                print(f'{alvo.nome} teve seu aumento de velocidade melhorado em 25% e a duração do efeito extendida em 1 turno.')
            elif efeito.nome == "Aumento Chance Crítico":
                alvo.chance_critico += math.floor(0.25 * efeito_presente.valor)
                print(f'{alvo.nome} teve seu aumento de chance de crítico melhorado em 25% e a duração do efeito extendida em 1 turno.')

        # Se a criatura não está sob o efeito de aumento do atributo
        else:
            if append:
                alvo.buffs.append(aumento)
            
            if efeito.nome == "Aumento Ataque":
                alvo.ataque += valor_aumento
                if efeito.duracao >= 999:
                    print(f'{alvo.nome} teve seu ataque aumentado em {valor_aumento} até o fim da batalha.')
                else:
                    print(f'{alvo.nome} teve seu ataque aumentado em {valor_aumento} por {efeito.duracao} turnos.')

            elif efeito.nome == "Aumento Defesa":
                alvo.defesa += valor_aumento
                if efeito.duracao >= 999:
                    print(f'{alvo.nome} teve sua defesa aumentada em {valor_aumento} até o fim da batalha.')
                else:
                    print(f'{alvo.nome} teve sua defesa aumentada em {valor_aumento} por {efeito.duracao} turnos.')

            elif efeito.nome == "Aumento Magia":
                alvo.magia += valor_aumento
                if efeito.duracao >= 999:
                    print(f'{alvo.nome} teve sua magia aumentada em {valor_aumento} até o fim da batalha.')
                else:
                    print(f'{alvo.nome} teve sua magia aumentada em {valor_aumento} por {efeito.duracao} turnos.')

            elif efeito.nome == "Aumento Velocidade":
                alvo.velocidade += valor_aumento
                if efeito.duracao >= 999:
                    print(f'{alvo.nome} teve sua velocidade aumentada em {valor_aumento} até o fim da batalha.')
                else:
                    print(f'{alvo.nome} teve sua velocidade aumentada em {valor_aumento} por {efeito.duracao} turnos.')

            elif efeito.nome == "Aumento Chance Crítico":
                alvo.chance_critico += valor_aumento
                if efeito.duracao >= 999:
                    print(f'{alvo.nome} teve sua chance de crítico aumentada em {valor_aumento}% até o fim da batalha.')
                else:
                    print(f'{alvo.nome} teve sua chance de crítico aumentada em {valor_aumento}% por {efeito.duracao} turnos.')

    # Criatura está defendendo
    elif efeito.nome == "Defendendo":
        defendendo = deepcopy(efeito)
        if append:
            alvo.buffs.append(defendendo)
        print(f'{alvo.nome} está defendendo.')
    
    # Cura debuff de envenenamento
    elif efeito.nome == "Cura Veneno":
        debuff = alvo.EfeitoPresente("Veneno")
        if debuff is not None:
            alvo.debuffs.remove(debuff)

            # Buff foi causado através de um item
            if item is not None:
                mensagem = f'{artigo} {item.nome} curou o ' + Fore.GREEN + 'envenenamento' + Style.RESET_ALL + f' de {alvo.nome}.'
            # Buff foi causado através de uma habilidade ou outra fonte
            else:
                mensagem = f'O ' + Fore.GREEN + 'envenenamento' + Style.RESET_ALL + f' de {alvo.nome} foi curado.'

    # Caso o HP ou Mana estrapole o valor máximo
    if sobrecura_hp == 1 and alvo.hp >= alvo.maxHp:
        alvo.hp = alvo.maxHp

        if item is not None:
            mensagem = f'{artigo} {item.nome} maximizou o ' + Fore.RED + 'HP' + Style.RESET_ALL + f' de {alvo.nome}.'
        elif habilidade is not None:
            mensagem = f'O ' + Fore.RED + 'HP' + Style.RESET_ALL + f' de {alvo.nome} foi maximizado.'

    if sobrecura_mana == 1 and alvo.mana >= alvo.maxMana:
        alvo.mana = alvo.maxMana

        if item is not None:
            mensagem = f'{artigo} {item.nome} maximizou a ' + Fore.BLUE + 'Mana' + Style.RESET_ALL + f' de {alvo.nome}.'
        elif habilidade is not None:
            mensagem = f'A ' + Fore.BLUE + 'Mana' + Style.RESET_ALL + f' de {alvo.nome} foi maximizada.'

    if mensagem is not None:
        print(mensagem)

    ## Efeitos de Debuff ##

    # Dá dano em todos os inimigos
    if efeito.nome == "Dano todos inimigos":
        dano = efeito.valor - alvo.defesa

        # Checando se o alvo está defendendo
        if alvo.EfeitoPresente("Defendendo") is not None:
            buff = alvo.EfeitoPresente("Defendendo")
            dano *= (buff.valor / 100)
        
        dano = math.floor(dano)
        if dano < 0:
            dano = 0

        alvo.hp -= dano
        mensagem = f'{artigo} {item.nome} infligiu {dano} de dano em {alvo.nome}.'

        if alvo.hp < 0:
            alvo.hp = 0
        
        if mensagem is not None:
            print(mensagem)

    elif efeito.nome == "Veneno":

        chance_veneno = efeito.chance
        chance_resistencia = 0

        # Calculando a chance de resistir ao veneno
        buff = alvo.EfeitoPresente('Resistência Veneno')
        if buff is not None:
            chance_resistencia += buff.valor
        
        if chance_resistencia > 1:
            chance_resistencia = 1

        chance = chance_veneno * (1 - chance_resistencia)

        if CalcularChance(chance):
            veneno = deepcopy(efeito)
            if append:
                alvo.debuffs.append(veneno)
            print(f'{usuario.nome} ' + Fore.GREEN + 'envenenou' + Style.RESET_ALL + f' {alvo.nome}!')
            alvo.CombinarEfeito("Veneno")
    
    elif efeito.nome == "Atordoamento":
        atordoamento = deepcopy(efeito)
        if append:
            alvo.debuffs.append(atordoamento)
        print(f'{usuario.nome} atordoou {alvo.nome}!')
        alvo.CombinarEfeito("Atordoamento")
    
    elif efeito.nome == "Lentidão" or efeito.nome == "Lentidão todos inimigos":
        debuff_ja_presente = alvo.EfeitoPresente("Lentidão")

        lentidao = deepcopy(efeito)
        lentidao.nome = "Lentidão"
        lentidao.valor = alvo.velocidade
        alvo.velocidade = 0
        if append:
            alvo.debuffs.append(lentidao)

        # Debuff foi causado através de um item
        if item is not None:
            if debuff_ja_presente is None:
                if lentidao.duracao > 1:
                    print(f'{artigo} {item.nome} infligiu Lentidão em {alvo.nome} por {efeito.duracao} turnos.')
                else:
                    print(f'{artigo} {item.nome} infligiu Lentidão em {alvo.nome} por {efeito.duracao} turno.')
            else:
                if lentidao.duracao > 1:
                    print(f'{artigo} {item.nome} infligiu Lentidão em {alvo.nome} por mais {efeito.duracao} turnos.')
                else:
                    print(f'{artigo} {item.nome} infligiu Lentidão em {alvo.nome} por mais {efeito.duracao} turno.')
        
        # Debuff foi causado através de uma habilidade
        elif habilidade is not None:
            if debuff_ja_presente is None:
                if lentidao.duracao > 1:
                    print(f'{usuario.nome} infligiu Lentidão em {alvo.nome} por {lentidao.duracao} turnos.')
                else:
                    print(f'{usuario.nome} infligiu Lentidão em {alvo.nome} por {lentidao.duracao} turno.')
            else:
                if lentidao.duracao > 1:
                    print(f'{usuario.nome} infligiu Lentidão em {alvo.nome} por mais {lentidao.duracao} turnos.')
                else:
                    print(f'{usuario.nome} infligiu Lentidão em {alvo.nome} por mais {lentidao.duracao} turno.')

        alvo.CombinarEfeito("Lentidão")

    # Diminuição de Atributo
    elif efeito.nome == "Diminuição Ataque" or efeito.nome == "Diminuição Defesa" or \
        efeito.nome == "Diminuição Magia" or efeito.nome == "Diminuição Velocidade" or \
        efeito.nome == "Diminuição Chance Crítico":

        diminuicao = deepcopy(efeito)
        valor_diminuicao = efeito.valor
        if habilidade is not None:
            valor_diminuicao = ContabilizarModificadores(valor_diminuicao, usuario, habilidade)
        diminuicao.valor = valor_diminuicao

        # Se a criatura já está sob o efeito de diminuição do atributo
        if alvo.EfeitoPresente(efeito.nome) is not None:
            debuff = alvo.EfeitoPresente(efeito.nome)
            debuff.duracao += 1
            debuff.valor += math.floor(0.25 * debuff.valor)

            if efeito.nome == "Diminuição Ataque":
                alvo.ataque -= math.floor(0.25 * debuff.valor)
                print(f'{alvo.nome} teve sua diminuição de ataque piorada em 25% e a duração do efeito extendida em 1 turno.')
            elif efeito.nome == "Diminuição Defesa":
                alvo.defesa -= math.floor(0.25 * debuff.valor)
                print(f'{alvo.nome} teve sua diminuição de defesa piorada em 25% e a duração do efeito extendida em 1 turno.')
            elif efeito.nome == "Diminuição Magia":
                alvo.magia -= math.floor(0.25 * debuff.valor)
                print(f'{alvo.nome} teve sua diminuição de magia piorada em 25% e a duração do efeito extendida em 1 turno.')
            elif efeito.nome == "Diminuição Velocidade":
                alvo.velocidade -= math.floor(0.25 * debuff.valor)
                print(f'{alvo.nome} teve sua diminuição de velocidade piorada em 25% e a duração do efeito extendida em 1 turno.')
            elif efeito.nome == "Diminuição Chance Crítico":
                alvo.chance_critico -= math.floor(0.25 * debuff.valor)
                print(f'{alvo.nome} teve sua diminuição de chance de crítico piorada em 25% e a duração do efeito extendida em 1 turno.')

        # Se a criatura não está sob o efeito de diminuição do atributo
        else:
            if append:
                alvo.debuffs.append(diminuicao)
            
            if efeito.nome == "Diminuição Ataque":
                alvo.ataque -= valor_diminuicao
                if efeito.duracao >= 999:
                    print(f'{alvo.nome} teve seu ataque diminuído em {valor_diminuicao} até o fim da batalha.')
                else:
                    print(f'{alvo.nome} teve seu ataque diminuído em {valor_diminuicao} por {efeito.duracao} turnos.')
            
            elif efeito.nome == "Diminuição Defesa":
                alvo.defesa -= valor_diminuicao
                if efeito.duracao >= 999:
                    print(f'{alvo.nome} teve sua defesa diminuída em {valor_diminuicao} até o fim da batalha.')
                else:
                    print(f'{alvo.nome} teve sua defesa diminuída em {valor_diminuicao} por {efeito.duracao} turnos.')
            
            elif efeito.nome == "Diminuição Magia":
                alvo.magia -= valor_diminuicao
                if efeito.duracao >= 999:
                    print(f'{alvo.nome} teve sua magia diminuída em {valor_diminuicao} até o fim da batalha.')
                else:
                    print(f'{alvo.nome} teve sua magia diminuída em {valor_diminuicao} por {efeito.duracao} turnos.')
            
            elif efeito.nome == "Diminuição Velocidade":
                alvo.velocidade -= valor_diminuicao
                if efeito.duracao >= 999:
                    print(f'{alvo.nome} teve sua velocidade diminuída em {valor_diminuicao} até o fim da batalha.')
                else:
                    print(f'{alvo.nome} teve sua velocidade diminuída em {valor_diminuicao} por {efeito.duracao} turnos.')
            
            elif efeito.nome == "Diminuição Chance Crítico":
                alvo.chance_critico -= valor_diminuicao
                if efeito.duracao >= 999:
                    print(f'{alvo.nome} teve sua chance de crítico diminuída em {valor_diminuicao}% até o fim da batalha.')
                else:
                    print(f'{alvo.nome} teve sua chance de crítico diminuída em {valor_diminuicao}% por {efeito.duracao} turnos.')     
