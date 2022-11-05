import time
from colorama import Fore, Back, Style

### Impressão de strings ###

def ImprimirComDelay(string, delay):
    """
    Imprime cada letra de uma string após um delay definido em segundos.
    """

    for letra in string:
        print(letra, end = '')
        time.sleep(delay)

### Impressão de classes ###

def ImprimirTipo(tipo):
    """
    Recebe um tipo como parâmetro e o imprime colorido, sem quebra de linha:
    * Normal    -> Branco
    * Fogo      -> Vermelho
    * Terrestre -> Verde
    * Agua      -> Azul
    * Vento     -> Ciano
    * Trevas    -> Magenta
    * Luz       -> Amarelo
    """

    if tipo == 'Normal':
        print('Normal', end = '')
    elif tipo == 'Fogo':
        print(Fore.RED + 'Fogo' + Style.RESET_ALL, end = '')
    elif tipo == 'Terrestre':
        print(Fore.GREEN + 'Terrestre' + Style.RESET_ALL, end = '')
    elif tipo == 'Agua':
        print(Fore.BLUE + 'Agua' + Style.RESET_ALL, end = '')
    elif tipo == 'Vento':
        print(Fore.CYAN + 'Vento' + Style.RESET_ALL, end = '')
    elif tipo == 'Trevas':
        print(Fore.MAGENTA + 'Trevas' + Style.RESET_ALL, end = '')
    elif tipo == 'Luz':
        print(Fore.YELLOW + 'Luz' + Style.RESET_ALL, end = '')

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

def ImprimirCriatura(indice, criatura):
    """
    Imprime uma criatura inimiga em batalha.
    """
    # Índice e nome da criatura
    mensagem = f'[{indice}] {criatura.nome} - '

    # Tipo da criatura
    mensagem += 'Tipo: '
    print(mensagem, end = '')
    ImprimirTipo(criatura.tipo)

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
