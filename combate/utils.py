import math
import random
import sys
from colorama import Fore, Back, Style

sys.path.append("..")
from classes_base.criatura import Criatura

def ImprimirCriatura(indice, criatura):
    """
    Imprime uma criatura inimiga em batalha.
    """
    # Índice e nome da criatura
    mensagem = f'[{indice}] {criatura.nome} - '

    # Tipo da criatura
    mensagem += 'Tipo: '
    if criatura.tipo == 'Normal':
        mensagem += 'Normal - '
    elif criatura.tipo == 'Fogo':
        mensagem += Fore.RED + 'Fogo' + Style.RESET_ALL + ' - '
    elif criatura.tipo == 'Terrestre':
        mensagem += Fore.GREEN + 'Terrestre' + Style.RESET_ALL + ' - '
    elif criatura.tipo == 'Agua':
        mensagem += Fore.BLUE + 'Agua' + Style.RESET_ALL + ' - '
    elif criatura.tipo == 'Vento':
        mensagem += Fore.CYAN + 'Vento' + Style.RESET_ALL + ' - '
    elif criatura.tipo == 'Trevas':
        mensagem += Fore.MAGENTA + 'Trevas' + Style.RESET_ALL + ' - '
    elif criatura.tipo == 'Luz':
        mensagem += Fore.YELLOW + 'Luz' + Style.RESET_ALL + ' - '

    # HP da criatura
    mensagem += Fore.RED + 'HP' + Style.RESET_ALL + f' {criatura.hp}/{criatura.maxHp} - '

    # Mana da criatura
    mensagem += Fore.BLUE + 'Mana' + Style.RESET_ALL + f' {criatura.mana}/{criatura.maxMana}'

    print(mensagem)

def CalcularDano(atacante, alvo, habilidade):
    """
    Calcula e retorna o dano que um atacante irá infligir em um alvo ao utilizar uma habilidade.
    """
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
    for b in alvo.buffs:
        if b.nome == "Defendendo":
            dano *= (b.valor / 100)
            break

    # Retornando o valor
    dano = math.floor(dano)
    if dano < 0:
        dano = 0

    return dano

def AcrescentarRecargas(criatura):
    """
    Acrescenta em 1 a recarga atual de todas as habilidades de uma criatura ou jogador caso ela não seja igual à
    recarga.
    """

    for h in criatura.habilidades:
        if h.recarga_atual != h.recarga:
            h.recarga_atual += 1

def DecairBuffsDebuffs(criatura):
    """
    Aplica o decaimento no valor de cada buff e debuff presente na criatura.
    """

    # Aplicando o decaimento nos Buffs
    for b in criatura.buffs:
        b.valor -= b.decaimento

        if b.valor <= 0:
            criatura.buffs.remove(b)
    
    # Aplicando o decaimento nos Debuffs
    for d in criatura.debuffs:
        d.valor -= d.decaimento

        if d.valor <= 0:
            criatura.debuffs.remove(d)

def UsarHabilidadeAlvoUnico(atacante, alvo, habilidade):
    """
    Utiliza uma habilidade em um único alvo e retorna o dano infligido.
    """

    dano = CalcularDano(atacante, alvo, habilidade)
    alvo.hp -= dano

    # Custos da habilidade
    for c in habilidade.custo:
        if c[0] == "Mana":
            atacante.mana -= c[1]

        elif c[0] == "HP":
            atacante.hp -= c[1]

    # Zerando a recarga atual da habilidade
    habilidade.recarga_atual = -1

    return dano

def AbaterCriaturas(criaturas):
    """
    Remove quaisquer criaturas que possuam 0 ou menos de HP da lista de criaturas.
    """

    for c in criaturas:
        if c.hp <= 0:
            print(f'{c.nome} foi derrotado!')
            criaturas.remove(c)

def InicioTurno(criatura):
    """
    Ativa certas habilidades ao início do turno da criatura.
    """
    for h in criatura.habilidades:

        if h.nome == "Regeneração" and criatura.hp < criatura.maxHp:
            valor = CalcularDano(criatura, criatura, h)
            criatura.hp += valor
            mensagem = f'{criatura.nome} regenerou {valor} de ' + Fore.RED + 'HP' + Style.RESET_ALL +'.'

            if criatura.hp >= criatura.maxHp:
                criatura.hp = criatura.maxHp
                mensagem = f'{criatura.nome} regenerou seu ' + Fore.RED + 'HP' + Style.RESET_ALL + ' até o máximo.'

            print(mensagem)
            break
