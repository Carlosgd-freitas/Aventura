import sys
from colorama import Fore, Back, Style

sys.path.append("..")
from classes_base import utils

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

def ImprimirCriatura(indice, criatura):
    """
    Imprime uma criatura inimiga em batalha.
    """
    # Índice e nome da criatura
    mensagem = f'[{indice}] {criatura.nome} - '

    # Tipo da criatura
    mensagem += 'Tipo: '
    print(mensagem, end = '')
    utils.ImprimirTipo(criatura.tipo)

    mensagem = ' - '

    # HP da criatura
    mensagem += Fore.RED + 'HP' + Style.RESET_ALL + f' {criatura.hp}/{criatura.maxHp} - '

    # Mana da criatura
    mensagem += Fore.BLUE + 'Mana' + Style.RESET_ALL + f' {criatura.mana}/{criatura.maxMana}'

    print(mensagem, end = '')
    ImprimirEfeitos(criatura)

def ImprimirEfeitos(criatura):
    """
    Imprime os efeitos que uma criatura está sob.
    """

    mensagem = ""

    # Buffs presentes na criatura
    if criatura.EfeitoPresente("buff", "Defendendo") != -1:
        mensagem += ' - DEFENDENDO'
    
    if criatura.EfeitoPresente("buff", "Aumento Ataque") != -1:
        mensagem += ' - ATQ' + Fore.GREEN + '+' + Style.RESET_ALL

    if criatura.EfeitoPresente("buff", "Aumento Defesa") != -1:
        mensagem += ' - DEF' + Fore.GREEN + '+' + Style.RESET_ALL
    
    if criatura.EfeitoPresente("buff", "Aumento Magia") != -1:
        mensagem += ' - MAG' + Fore.GREEN + '+' + Style.RESET_ALL

    if criatura.EfeitoPresente("buff", "Aumento Velocidade") != -1:
        mensagem += ' - VEL' + Fore.GREEN + '+' + Style.RESET_ALL
    
    if criatura.EfeitoPresente("buff", "Aumento Chance Crítico") != -1:
        mensagem += ' - CRIT%' + Fore.GREEN + '+' + Style.RESET_ALL
    
    if criatura.EfeitoPresente("buff", "Regeneração HP") != -1:
        mensagem += ' - REGEN ' + Fore.RED + 'HP' + Style.RESET_ALL

    # Debuffs presentes na criatura
    if criatura.EfeitoPresente("debuff", "Diminuição Ataque") != -1:
        mensagem += ' - ATQ' + Fore.RED + '-' + Style.RESET_ALL
    
    if criatura.EfeitoPresente("debuff", "Diminuição Defesa") != -1:
        mensagem += ' - DEF' + Fore.RED + '-' + Style.RESET_ALL
    
    if criatura.EfeitoPresente("debuff", "Diminuição Magia") != -1:
        mensagem += ' - MAG' + Fore.RED + '-' + Style.RESET_ALL
    
    if criatura.EfeitoPresente("debuff", "Diminuição Velocidade") != -1:
        mensagem += ' - VEL' + Fore.RED + '-' + Style.RESET_ALL
    
    if criatura.EfeitoPresente("debuff", "Diminuição Chance Crítico") != -1:
        mensagem += ' - CRIT%' + Fore.RED + '-' + Style.RESET_ALL

    if criatura.EfeitoPresente("debuff", "Veneno") != -1:

        if criatura.singular_plural == "singular":
            if criatura.genero == "M":
                mensagem += ' - ' + Fore.GREEN + 'ENVENENADO' + Style.RESET_ALL
            elif criatura.genero == "F":
                mensagem += ' - ' + Fore.GREEN + 'ENVENENADA' + Style.RESET_ALL

        elif criatura.singular_plural == "plural":
            if criatura.genero == "M":
                mensagem += ' - ' + Fore.GREEN + 'ENVENENADOS' + Style.RESET_ALL
            elif criatura.genero == "F":
                mensagem += ' - ' + Fore.GREEN + 'ENVENENADAS' + Style.RESET_ALL

    if criatura.EfeitoPresente("debuff", "Atordoamento") != -1:

        if criatura.singular_plural == "singular":
            if criatura.genero == "M":
                mensagem += ' - ATORDOADO'
            elif criatura.genero == "F":
                mensagem += ' - ATORDOADA'

        elif criatura.singular_plural == "plural":
            if criatura.genero == "M":
                mensagem += ' - ATORDOADOS'
            elif criatura.genero == "F":
                mensagem += ' - ATORDOADAS'
    
    if criatura.EfeitoPresente("debuff", "Lentidão") != -1:
        mensagem += ' - LENTIDÃO' + Style.RESET_ALL
    
    print(mensagem)
