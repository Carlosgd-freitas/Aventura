import time
import copy
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

        if nomes[nome] > 0:
            # Convertendo o valor numérico em uma letra
            sufixo = nomes_zerados[nome] + 1
            sufixo = NumeroEmSufixo(sufixo)
            nomes_zerados[nome] += 1

            nome += ' ' + sufixo
            c.nome = nome
