import random
import math
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

def QuantidadeEmSingularPlural(quantidade):
    """
    Retorna a string 'singular' se a quantidade passada por parâmetro for igual a 1 e 'plural' caso contrário.
    """
    if quantidade == 1:
        return "singular"
    else:
        return "plural"

def MenorAtributo(criaturas, atributo):
    """
    Recebe uma lista de criaturas e um atributo e retorna o índice da criatura com o menor valor referente ao
    atributo passado dentre todas as criaturas.

    Valores possíveis para o atributo: 'hp', 'mana', 'ataque', 'defesa', 'magia' e 'velocidade'.
    """
    menor_valor = 9999999
    menor_indice = -1

    i = 0
    for c in criaturas:
        if atributo == "hp" and c.hp < menor_valor:
            menor_valor = c.hp
            menor_indice = i
        elif atributo == "mana" and c.mana < menor_valor:
            menor_valor = c.mana
            menor_indice = i
        elif atributo == "ataque" and c.ataque < menor_valor:
            menor_valor = c.ataque
            menor_indice = i
        elif atributo == "defesa" and c.defesa < menor_valor:
            menor_valor = c.defesa
            menor_indice = i
        elif atributo == "magia" and c.magia < menor_valor:
            menor_valor = c.magia
            menor_indice = i
        elif atributo == "velocidade" and c.velocidade < menor_valor:
            menor_valor = c.velocidade
            menor_indice = i

        i += 1
    
    return menor_indice

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

def ProcessarEfeito(usuario, efeito, alvo, item = None, habilidade = None, fora_combate = False):
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
    - fora_combate: se igual a True, o efeito sendo processado não foi causado em combate. O valor padrão é False.
    """

    chance = random.randint(1, 100)
    mensagem = None

    # Flags para efeitos de item
    sobrecura_hp = 0
    sobrecura_mana = 0
    regeneracao_hp = 0

    # Melhora das mensagens de uso de itens
    if item is not None:
        artigo = item.RetornarArtigo()
        contracao_por = item.RetornarContracaoPor().lower()

    # Item: Efeitos de Buff

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
        
        alvo.hp += valor

        # Buff foi causado através de um item
        if item is not None:
            mensagem = f'{artigo} {item.nome} recuperou {valor} de ' + Fore.RED + 'HP' + Style.RESET_ALL + f' de {alvo.nome}.'
        
        # Buff foi causado através de uma habilidade
        elif habilidade is not None:
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
        
        alvo.mana += valor

        # Buff foi causado através de um item
        if item is not None:
            mensagem = f'{artigo} {item.nome} recuperou {valor} de ' + Fore.BLUE + 'Mana' + Style.RESET_ALL + f' de {alvo.nome}.'
        
        # Buff foi causado através de uma habilidade
        elif habilidade is not None:
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
        
        # Buff foi causado através de uma habilidade
        elif habilidade is not None:
            mensagem = f'{alvo.nome} recuperou {valor} de ' + Fore.RED + 'HP' + Style.RESET_ALL + '.'

        if not fora_combate:
            regen = efeito.ClonarEfeito()
            regen.duracao -= regen.decaimento
            alvo.buffs.append(regen)

            regeneracao_hp = 1
        
        sobrecura_hp = 1
    
    # Cura debuff de envenenamento
    elif efeito.nome == "Cura Veneno":
        debuff_indice = alvo.EfeitoPresente("debuff", "Veneno")
        alvo.debuffs.remove(alvo.debuffs[debuff_indice])
        mensagem = f'{artigo} {item.nome} curou o ' + Fore.GREEN + 'envenenamento' + Style.RESET_ALL + f' de {alvo.nome}.'

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

    # Mensagem extra ao usar itens que concedem regeneração dentro de combate
    if regeneracao_hp == 1:
        mensagem = 'A regeneração de ' + Fore.RED + 'HP' + Style.RESET_ALL
        mensagem += f' concedida {contracao_por} {item.nome} irá durar mais {efeito.duracao - 1}'
        if efeito.duracao - 1 > 1:
            mensagem += ' turnos.'
        else:
            mensagem += ' turno.'

        if mensagem is not None:
            print(mensagem)

    # Item: Efeitos de Debuff

    # Dá dano em todos os inimigos
    if efeito.nome == "Dano todos inimigos":
        dano = efeito.valor - alvo.defesa

        # Checando se o alvo está defendendo
        if alvo.EfeitoPresente("buff", "Defendendo") != -1:
            indice = alvo.EfeitoPresente("buff", "Defendendo")
            valor = alvo.buffs[indice].valor
            dano *= (valor / 100)
        
        dano = math.floor(dano)
        if dano < 0:
            dano = 0

        alvo.hp -= dano
        mensagem = f'{artigo} {item.nome} infligiu {dano} de dano em {alvo.nome}.'

        if alvo.hp < 0:
            alvo.hp = 0
        
        if mensagem is not None:
            print(mensagem)

    # Habilidade: Efeitos de Buff
    if efeito.nome == "Defendendo" and chance <= efeito.chance:
        defendendo = efeito.ClonarEfeito()
        alvo.buffs.append(defendendo)
        print(f'{alvo.nome} está defendendo.')
    
    elif (efeito.nome == "Aumento Defesa" or efeito.nome == "Aumento Velocidade" or
        efeito.nome == "Aumento Chance Crítico") and chance <= efeito.chance:

        aumento = efeito.ClonarEfeito()

        valor_aumento = efeito.valor # Valor Base
        for m in habilidade.modificadores: # Modificadores
            if m[0] == "ataque":
                valor_aumento += usuario.ataque * (m[1] / 100)
            elif m[0] == "magia":
                valor_aumento += usuario.magia * (m[1] / 100)
        
        valor_aumento = math.floor(valor_aumento)
        aumento.valor = valor_aumento

        if efeito.nome == "Aumento Defesa":
            # Se a criatura já está sob o efeito de aumento de defesa
            if alvo.EfeitoPresente("buff", "Aumento Defesa") != -1:
                indice = alvo.EfeitoPresente("buff", "Aumento Defesa")
                alvo.defesa += math.floor(0.25 * alvo.buffs[indice].valor)
                alvo.buffs[indice].duracao += 1
                alvo.buffs[indice].valor += math.floor(0.25 * alvo.buffs[indice].valor)
                print(f'{alvo.nome} teve seu aumento de defesa melhorado em 25% e a duração do efeito extendida em 1 turno.')

            # Se a criatura não está sob o efeito de aumento de defesa
            else:
                alvo.buffs.append(aumento)
                alvo.defesa += valor_aumento
                print(f'{alvo.nome} aumentou sua defesa em {valor_aumento} por {efeito.duracao} turnos.')
        
        elif efeito.nome == "Aumento Velocidade":
            # Se a criatura já está sob o efeito de aumento de velocidade
            if alvo.EfeitoPresente("buff", "Aumento Velocidade") != -1:
                indice = alvo.EfeitoPresente("buff", "Aumento Velocidade")
                alvo.velocidade += math.floor(0.25 * alvo.buffs[indice].valor)
                alvo.buffs[indice].duracao += 1
                alvo.buffs[indice].valor += math.floor(0.25 * alvo.buffs[indice].valor)
                print(f'{alvo.nome} teve seu aumento de velocidade melhorado em 25% e a duração do efeito extendida em 1 turno.')

            # Se a criatura não está sob o efeito de aumento de velocidade
            else:
                alvo.buffs.append(aumento)
                alvo.velocidade += valor_aumento
                print(f'{alvo.nome} aumentou sua velocidade em {valor_aumento} por {efeito.duracao} turnos.')
        
        elif efeito.nome == "Aumento Chance Crítico":
            # Se a criatura já está sob o efeito de aumento de chance de crítico
            if alvo.EfeitoPresente("buff", "Aumento Chance Crítico") != -1:
                indice = alvo.EfeitoPresente("buff", "Aumento Chance Crítico")
                alvo.chance_critico += math.floor(0.25 * alvo.buffs[indice].valor)
                alvo.buffs[indice].duracao += 1
                alvo.buffs[indice].valor += math.floor(0.25 * alvo.buffs[indice].valor)
                print(f'{alvo.nome} teve seu aumento de chance de crítico melhorado em 25% e a duração do efeito extendida em 1 turno.')

            # Se a criatura não está sob o efeito de aumento de chance de crítico
            else:
                alvo.buffs.append(aumento)
                alvo.chance_critico += valor_aumento
                print(f'{alvo.nome} aumentou sua chance de crítico em {valor_aumento}% por {efeito.duracao} turnos.')

    # Habilidade: Efeitos de Debuff
    elif efeito.nome == "Veneno" and chance <= efeito.chance:
        veneno = efeito.ClonarEfeito()
        alvo.debuffs.append(veneno)
        print(f'{usuario.nome} ' + Fore.GREEN + 'envenenou' + Style.RESET_ALL + f' {alvo.nome}!')
        alvo.CombinarEfeito("Veneno")
    
    elif efeito.nome == "Atordoamento" and chance <= efeito.chance:
        atordoamento = efeito.ClonarEfeito()
        alvo.debuffs.append(atordoamento)
        print(f'{usuario.nome} atordoou {alvo.nome}!')
        alvo.CombinarEfeito("Atordoamento")
    
    elif (efeito.nome == "Lentidão" or efeito.nome == "Lentidão todos inimigos") and chance <= efeito.chance:
        debuff_ja_presente = alvo.EfeitoPresente("debuff", "Lentidão")

        lentidao = efeito.ClonarEfeito()
        lentidao.nome = "Lentidão"
        lentidao.valor = alvo.velocidade
        alvo.velocidade = 0
        alvo.debuffs.append(lentidao)

        # Debuff foi causado através de um item
        if item is not None:
            if debuff_ja_presente == -1:
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
            if debuff_ja_presente == -1:
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

    elif efeito.nome == "Diminuição Defesa" and chance <= efeito.chance:
        diminuicao = efeito.ClonarEfeito()

        valor_diminuicao = efeito.valor # Valor Base
        for m in habilidade.modificadores: # Modificadores
            if m[0] == "ataque":
                valor_diminuicao += usuario.ataque * (m[1] / 100)
            elif m[0] == "magia":
                valor_diminuicao += usuario.magia * (m[1] / 100)
        
        valor_diminuicao = math.floor(valor_diminuicao)
        diminuicao.valor = valor_diminuicao

        # Se a criatura alvo já está sob o efeito de diminuição de defesa
        if alvo.EfeitoPresente("debuff", "Diminuição Defesa") != -1:
            indice = alvo.EfeitoPresente("debuff", "Diminuição Defesa")
            alvo.defesa -= math.floor(0.25 * alvo.debuffs[indice].valor)
            alvo.debuffs[indice].duracao += 1
            alvo.debuffs[indice].valor += math.floor(0.25 * alvo.debuffs[indice].valor)
            print(f'{alvo.nome} teve sua dimimuição de defesa piorada em 25% e a duração do efeito extendida em 1 turno.')

        # Se a criatura não está sob o efeito de diminuição de defesa
        else:
            alvo.debuffs.append(diminuicao)
            alvo.defesa -= valor_diminuicao
            print(f'{alvo.nome} teve sua defesa diminuída em {valor_diminuicao} por {efeito.duracao} turnos.')
