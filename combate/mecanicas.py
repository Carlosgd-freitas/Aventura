import math
import random
import sys
from colorama import Fore, Back, Style

from . import invocar_criaturas

sys.path.append("..")
from itens import espolios

def CalcularDano(atacante, alvo, habilidade):
    """
    Calcula e retorna o dano que um atacante irá infligir em um alvo ao utilizar uma habilidade.
    """
    # Se a habilidade não causa dano
    if habilidade.nao_causa_dano == True:
        return 0

    # Valor inicial
    dano = habilidade.valor

    # Acrescentando possíveis modificadores de dano
    for m in habilidade.modificadores:

        if m[0] == "ataque":
            dano += m[1]/100 * atacante.ataque

        elif m[0] == "magia":
            dano += m[1]/100 * atacante.magia
    
    # Em caso da habilidade ter a si mesmo como alvo
    if habilidade.alvo == "proprio":
        dano = math.floor(dano)
        if dano < 0:
            dano = 0

        return dano

    # Habilidade é efetiva contra o tipo do alvo
    if ((habilidade.tipo == "Fogo" and alvo.tipo == "Terrestre") or
        (habilidade.tipo == "Fogo" and alvo.tipo == "Trevas") or
        (habilidade.tipo == "Terrestre" and alvo.tipo == "Agua") or
        (habilidade.tipo == "Terrestre" and alvo.tipo == "Luz") or
        (habilidade.tipo == "Vento" and alvo.tipo == "Fogo") or
        (habilidade.tipo == "Vento" and alvo.tipo == "Terrestre") or
        (habilidade.tipo == "Agua" and alvo.tipo == "Fogo") or
        (habilidade.tipo == "Agua" and alvo.tipo == "Vento") or
        (habilidade.tipo == "Trevas" and alvo.tipo == "Agua") or
        (habilidade.tipo == "Trevas" and alvo.tipo == "Luz") or
        (habilidade.tipo == "Luz" and alvo.tipo == "Vento") or
        (habilidade.tipo == "Luz" and alvo.tipo == "Trevas")):

        dano *= 2
    
    # Alvo resiste o tipo da habilidade
    elif ((alvo.tipo == "Fogo" and habilidade.tipo == "Terrestre") or
        (alvo.tipo == "Fogo" and habilidade.tipo == "Trevas") or
        (alvo.tipo == "Terrestre" and habilidade.tipo == "Agua") or
        (alvo.tipo == "Terrestre" and habilidade.tipo == "Luz") or
        (alvo.tipo == "Vento" and habilidade.tipo == "Fogo") or
        (alvo.tipo == "Vento" and habilidade.tipo == "Terrestre") or
        (alvo.tipo == "Agua" and habilidade.tipo == "Fogo") or
        (alvo.tipo == "Agua" and habilidade.tipo == "Vento") or
        (alvo.tipo == "Trevas" and habilidade.tipo == "Agua") or
        (alvo.tipo == "Trevas" and habilidade.tipo == "Luz") or
        (alvo.tipo == "Luz" and habilidade.tipo == "Vento") or
        (alvo.tipo == "Luz" and habilidade.tipo == "Trevas")):

        dano /= 2
    
    # Checando se a habilidade é perfurante e diminuindo o dano pela defesa do alvo
    defesa = alvo.defesa

    for e in habilidade.efeitos:
        if e.nome == "Perfurante %":
            tentativa = random.randint(1, 100)
            if tentativa <= e.chance:
                defesa *= (e.valor / 100)
            break

    dano -= defesa

    # Checando se o alvo está defendendo
    if alvo.EfeitoPresente("buff", "Defendendo") != -1:
        indice = alvo.EfeitoPresente("buff", "Defendendo")
        valor = alvo.buffs[indice].valor
        dano *= (valor / 100)

    # Retornando o valor
    dano = math.floor(dano)
    if dano < 0:
        dano = 0

    return dano

def InicioTurno(criatura):
    """
    Esta função é chamada no início do turno da criatura e retorna 0 caso a criatura esteja atordoada.
    """

    consciente = 1

    # Acionando habilidades
    for h in criatura.habilidades:

        if h.nome == "Regeneração" and criatura.hp < criatura.maxHp and criatura.hp > 0:
            valor = CalcularDano(criatura, criatura, h)
            criatura.hp += valor
            mensagem = f'{criatura.nome} regenerou {valor} de ' + Fore.RED + 'HP' + Style.RESET_ALL +'.'

            if criatura.hp >= criatura.maxHp:
                criatura.hp = criatura.maxHp
                mensagem = f'{criatura.nome} regenerou seu ' + Fore.RED + 'HP' + Style.RESET_ALL + ' até o máximo.'

            print(mensagem)
            break
    
    # Aplicando efeitos de debuff
    criatura.CombinarEfeito("Veneno")
    criatura.CombinarEfeito("Atordoamento")

    if criatura.EfeitoPresente("debuff", "Veneno") != -1 and criatura.hp > 0:
        indice = criatura.EfeitoPresente("debuff", "Veneno")
        valor = criatura.debuffs[indice].valor
        criatura.hp -= valor
        print(f'{criatura.nome} sofreu {valor} de dano do ' + Fore.GREEN + 'envenenamento' + Style.RESET_ALL + '!')
    
    elif criatura.EfeitoPresente("debuff", "Atordoamento") != -1 and criatura.hp > 0:
        indice = criatura.EfeitoPresente("debuff", "Atordoamento")

        if criatura.debuffs[indice].duracao != 0:
            consciente = 0
            
            if criatura.singular_plural == "singular":
                if criatura.genero == "M":
                    print(f'{criatura.nome} está atordoado e não pode agir!')
                elif criatura.genero == "F":
                    print(f'{criatura.nome} está atordoada e não pode agir!')

            elif criatura.singular_plural == "plural":
                if criatura.genero == "M":
                    print(f'{criatura.nome} estão atordoados e não podem agir!')
                elif criatura.genero == "F":
                    print(f'{criatura.nome} estão atordoadas e não podem agir!')

    return consciente

def AcrescentarRecargas(criatura):
    """
    Acrescenta em 1 a recarga atual de todas as habilidades de uma criatura ou jogador caso ela não seja igual à
    recarga. Se alguma habilidade da criatura foi recarregada, a função retorna 1 e, caso contrário, retorna 0.
    """

    recarregou = 0

    for h in criatura.habilidades:
        if h.recarga_atual < h.recarga:
            h.recarga_atual += 1
            recarregou = 1
    
    return recarregou

def DecairBuffsDebuffs(criatura, verbose = 1):
    """
    Aplica o decaimento no valor de cada buff e debuff presente na criatura. Se houve algum decaimento de buff ou
    debuff na criatura, a função retorna 1 e, caso contrário, retorna 0. Se a verbose for igual à 0, a função
    não irá imprimir quaisquer mensagens.
    """

    decaiu = 0

    # Defendendo
    if criatura.EfeitoPresente("buff", "Defendendo") != -1:
        indice = criatura.EfeitoPresente("buff", "Defendendo")
        defendendo = criatura.buffs[indice]
        defendendo.duracao -= defendendo.decaimento

        if defendendo.duracao <= 0 and criatura.hp > 0:
            criatura.buffs.remove(defendendo)

            if verbose == 1:
                print(f'{criatura.nome} não está mais defendendo.')
        
        decaiu = 1
    
    # Veneno
    if criatura.EfeitoPresente("debuff", "Veneno") != -1:
        indice = criatura.EfeitoPresente("debuff", "Veneno")
        veneno = criatura.debuffs[indice]
        veneno.duracao -= veneno.decaimento

        if veneno.duracao <= 0 and criatura.hp > 0:
            criatura.debuffs.remove(veneno)

            if verbose == 1:
                if criatura.singular_plural == "singular":
                    if criatura.genero == "M":
                        print(f'{criatura.nome} não está mais ' + Fore.GREEN + 'envenenado' + Style.RESET_ALL + '.')
                    elif criatura.genero == "F":
                        print(f'{criatura.nome} não está mais ' + Fore.GREEN + 'envenenada' + Style.RESET_ALL + '.')

                elif criatura.singular_plural == "plural":
                    if criatura.genero == "M":
                        print(f'{criatura.nome} não estão mais ' + Fore.GREEN + 'envenenados' + Style.RESET_ALL + '.')
                    elif criatura.genero == "F":
                        print(f'{criatura.nome} não estão mais ' + Fore.GREEN + 'envenenadas' + Style.RESET_ALL + '.')
        
        decaiu = 1
    
    # Atordoamento
    if criatura.EfeitoPresente("debuff", "Atordoamento") != -1:
        indice = criatura.EfeitoPresente("debuff", "Atordoamento")
        atordoamento = criatura.debuffs[indice]
        atordoamento.duracao -= atordoamento.decaimento

        if atordoamento.duracao <= -1 and criatura.hp > 0:
            criatura.debuffs.remove(atordoamento)

            if verbose == 1:
                if criatura.singular_plural == "singular":
                    if criatura.genero == "M":
                        print(f'{criatura.nome} não está mais atordoado.')
                    elif criatura.genero == "F":
                        print(f'{criatura.nome} não está mais atordoada.')

                elif criatura.singular_plural == "plural":
                    if criatura.genero == "M":
                        print(f'{criatura.nome} não estão mais atordoados.')
                    elif criatura.genero == "F":
                        print(f'{criatura.nome} não estão mais atordoadas.')
        
        decaiu = 1
    
    # Aumento de Defesa
    if criatura.EfeitoPresente("buff", "Aumento Defesa") != -1:
        indice = criatura.EfeitoPresente("buff", "Aumento Defesa")
        aumento = criatura.buffs[indice]
        aumento.duracao -= aumento.decaimento

        if aumento.duracao <= 0 and criatura.hp > 0:
            criatura.defesa -= criatura.buffs[indice].valor
            criatura.buffs.remove(aumento)

            if verbose == 1:
                print(f'O aumento de defesa de {criatura.nome} terminou.')
        
        decaiu = 1
    
    # Diminuição de Defesa
    if criatura.EfeitoPresente("debuff", "Diminuição Defesa") != -1:
        indice = criatura.EfeitoPresente("debuff", "Diminuição Defesa")
        diminuicao = criatura.debuffs[indice]
        diminuicao.duracao -= diminuicao.decaimento

        if diminuicao.duracao <= 0 and criatura.hp > 0:
            criatura.defesa += criatura.debuffs[indice].valor
            criatura.debuffs.remove(diminuicao)

            if verbose == 1:
                print(f'A diminuição de defesa de {criatura.nome} terminou.')
        
        decaiu = 1

    return decaiu

def GerarEspolios(criatura):
    """
    Retorna uma lista contendo os espólios de uma criatura derrotada.
    """

    lista_espolios = []

    # Ouro e Itens que o jogador irá ganhar por ter derrotado a criatura
    for e in criatura.espolios:
        chance = random.randint(1, 100)
        
        if chance <= e[0]:
            lista_espolios.append(e[1])
    
    # Experiência que o jogador irá ganhar por ter derrotado a criatura
    exp = espolios.Experiencia(criatura.experiencia)
    lista_espolios.append(exp)

    return lista_espolios

def AbaterCriaturas(lista_criaturas, lista_espolios, criatura = None, gerar_espolios = True):
    """
    Remove quaisquer criaturas que possuam 0 ou menos de HP da lista de criaturas. Retorna dois parâmetros:
    * 1 caso a criatura for removida da lista de criaturas, ou 0 caso contrário (criatura != None)
    * uma lista de espólios caso a criatura tenha sido derrotada, ou uma lista vazia caso contrário
    """

    morreu = 0

    for c in lista_criaturas:
        if c.hp <= 0:

            if c.singular_plural == "singular":
                if c.genero == "M":
                    print(f'{c.nome} foi derrotado!')
                elif c.genero == "F":
                    print(f'{c.nome} foi derrotada!')

            elif c.singular_plural == "plural":
                if c.genero == "M":
                    print(f'{c.nome} foram derrotados!')
                elif c.genero == "F":
                    print(f'{c.nome} foram derrotadas!')

            # Adicionando os espólios gerados à lista de espólios passada por parâmetro
            if gerar_espolios:
                espolios_gerados = GerarEspolios(c)
                for e in espolios_gerados:
                    lista_espolios.append(e)

            # Criatura passada por parâmetro foi derrotada
            if criatura is not None and c == criatura:
                morreu = 1
            
            # Habilidades que ativam quando a criatura é derrotada
            for h in c.habilidades:
                if h.nome == "Subdivisão":
                    lista_criaturas = invocar_criaturas.InvocarCriaturas(c, h, lista_criaturas)

            lista_criaturas.remove(c)
    
    # Compactando lista de espólios
    indice_1 = 0
    for espolio_1 in lista_espolios:

        indice_2 = 0
        for espolio_2 in lista_espolios:

            if espolio_1[1].nome == espolio_2[1].nome and indice_1 != indice_2:
                espolio_1[1].quantidade += espolio_2[1].quantidade
                lista_espolios.remove(espolio_2)
            
            indice_2 += 1
        
        indice_1 += 1

    return morreu

def TerminarBuffsDebuffs(criatura):
    """
    Remove todos os buffs e debuffs presentes na criatura de maneira apropriada.
    """

    while True:
        decaiu = DecairBuffsDebuffs(criatura, verbose = 0)

        if decaiu == 0:
            break

def AcrescentarRecargasMaximo(criatura):
    """
    Remove todos os buffs e debuffs presentes na criatura de maneira apropriada.
    """

    while True:
        recarregou = AcrescentarRecargas(criatura)

        if recarregou == 0:
            break
