import time
from colorama import Fore, Back, Style

def LerNumero(string):
    """
    Lê e retorna um número da entrada. Se a entrada não for um número, a função continuará em Loop.
    """

    quebrar = 0
    while True:

        if quebrar == 1:
            break
        quebrar = 0

        try:
            value = int(input(string))
            quebrar = 1
        except:
            quebrar = 0
    
    return value

def LerNumeroIntervalo(string, low, high):
    """
    Lê e retorna um número da entrada que esteja dentro do intervalo [low, high]. Se a entrada não for um
    número, ou não estiver dentro do intervalo [low, high], a função continuará em Loop.
    """

    while True:

        value = LerNumero(string)
        if value >= low and value <= high:
            break
    
    return value

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

def ImprimirComDelay(string, delay = 0.04):
    """
    Imprime cada letra de uma string após um delay definido em milisegundos. O valor padrão do delay é de 0.04ms.
    """

    for letra in string:
        print(letra, end = '')
        time.sleep(delay)

def QuantidadeEmSingularPlural(quantidade):
    """
    Retorna a string 'singular' se a quantidade passada por parâmetro for igual a 1 e 'plural' caso contrário.
    """
    if quantidade == 1:
        return "singular"
    else:
        return "plural"

