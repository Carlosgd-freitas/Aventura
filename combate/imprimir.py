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
    
    if criatura.EfeitoPresente("buff", "Aumento Defesa") != -1:
        mensagem += ' - DEFESA' + Fore.GREEN + '+' + Style.RESET_ALL

    # Debuffs presentes na criatura
    if criatura.EfeitoPresente("debuff", "Veneno") != -1:
        mensagem += ' - ' + Fore.GREEN + 'ENVENENADO' + Style.RESET_ALL

    if criatura.EfeitoPresente("debuff", "Atordoamento") != -1:
        mensagem += ' - ATORDOADO'
    
    print(mensagem)
