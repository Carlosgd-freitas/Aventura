"""Impressão colorida de textos."""

from enum import Enum
from unidecode import unidecode

class ANSI(Enum):
    """
    Enumeração para os códigos ANSI utilizados durante a impressão de textos coloridos.
    """

    FRENTE = "\033[38;2;"
    FUNDO = "\033[48;2;"

    NORMAL = "\033[2m"
    NEGRITO = "\033[1m"
    SUBLINHADO = "\033[4m"

    RESET = "\033[0m"
    
def retornar_rgb(r, g, b):
    """
    Retorna um código baseado em RGB para colorir um texto.
    
    Parâmetros:
    * r: quantidade de vermelho que a cor irá conter.
    * g: quantidade de verde que a cor irá conter.
    * b: quantidade de azul que a cor irá conter.
    """
    if (r is not None) and (r >= 0) and (r <= 255) and \
        (g is not None) and (g >= 0) and (g <= 255) and \
        (b is not None) and (b >= 0) and (b <= 255):
            return f"{r};{g};{b}m"
    else:
        return ""

def retornar_cor(cor, cor_padrao=(255, 255, 255)):
    """
    Retorna um código baseado no nome de uma cor para colorir um texto.

    Parâmetros:
    * cor: nome da cor. Este parâmetro não distingue letras maiúsculas e minúsculas. Os valores possíveis para este parâmetro
    são: "Bonina", "Vermelho", "Laranja Queimado", "Laranja", "Amarelo", "Dourado", "Bege", "Marrom Claro", "Marrom", "Oliva",
    "Verde", "Verde Gramado", "Lima", "Verde Primavera", "Ciano", "Azul Claro", "Azul Metálico", "Azul", "Lilás", "Roxo", "Magenta",
    "Salmão", "Rosa", "Branco", "Cinza", "Cinza Escuro" e "Preto".
    """

    if isinstance(cor, str):
        cor_normalizada = unidecode(cor).lower()

        # Cores primárias
        if cor_normalizada == "vermelho":
            return retornar_rgb(255, 0, 0)
        elif cor_normalizada == "verde":
            return retornar_rgb(0, 128, 0)
        elif cor_normalizada == "azul":
            return retornar_rgb(0, 0, 255)
        
        # Cores secundárias
        elif cor_normalizada == "amarelo":
            return retornar_rgb(255, 255, 0)
        elif cor_normalizada == "ciano":
            return retornar_rgb(0, 255, 255)
        elif cor_normalizada == "magenta":
            return retornar_rgb(255, 0, 255)
        
        # Demais cores
        elif cor_normalizada == "bonina":
            return retornar_rgb(128, 0, 0)
        elif cor_normalizada == "laranja queimado":
            return retornar_rgb(212, 81, 11)
        elif cor_normalizada == "laranja":
            return retornar_rgb(250, 143, 1)
        elif cor_normalizada == "dourado":
            return retornar_rgb(212, 175, 55)
        elif cor_normalizada == "bege":
            return retornar_rgb(208, 176, 132)
        elif cor_normalizada == "marrom claro":
            return retornar_rgb(159, 85, 41)
        elif cor_normalizada == "marrom":
            return retornar_rgb(87, 44, 2)
        elif cor_normalizada == "oliva":
            return retornar_rgb(107, 142, 35)
        elif cor_normalizada == "verde gramado":
            return retornar_rgb(124, 252, 0)
        elif cor_normalizada == "lima":
            return retornar_rgb(0, 255, 0)
        elif cor_normalizada == "verde primavera":
            return retornar_rgb(0, 255, 127)
        elif cor_normalizada == "azul claro":
            return retornar_rgb(96, 179, 247)
        elif cor_normalizada == "azul metalico":
            return retornar_rgb(72, 106, 131)
        elif cor_normalizada == "lilas":
            return retornar_rgb(204, 153, 255)
        elif cor_normalizada == "roxo":
            return retornar_rgb(147, 18, 172)
        elif cor_normalizada == "salmao":
            return retornar_rgb(250, 127, 114)
        elif cor_normalizada == "rosa":
            return retornar_rgb(255, 153, 204)
    
        # Cores monocromáticas
        elif cor_normalizada == "branco":
            return retornar_rgb(255, 255, 255)
        elif cor_normalizada == "cinza":
            return retornar_rgb(128, 128, 128)
        elif cor_normalizada == "cinza escuro":
            return retornar_rgb(64, 64, 64)
        elif cor_normalizada == "preto":
            return retornar_rgb(0, 0, 0)
        
        else:
            return retornar_rgb(cor_padrao[0], cor_padrao[1], cor_padrao[2])
        
    else:
        return retornar_rgb(cor_padrao[0], cor_padrao[1], cor_padrao[2])
    
def colorir(texto, frente=None, fundo=None, frente_claro=False, fundo_claro=False, sublinhado=False):
    """
    Colore e retorna um texto.

    Parâmetros:
    * texto: texto que será colorido. Se este parâmetro não for uma string, a função tentará converter a variável recebida para
    string e aplicar a coloração se for possível.

    Parâmetros opcionais:
    * frente: cor que será utilizada no texto. Este parâmetro pode ser:
        * Uma tupla de três valores (r, g, b), que contém os valores RGB que serão aplicados no texto.
        * Uma string, sem distinção entre letras maiúsculas e minúsculas, equivalente ao nome da cor que será utilizada no texto.
        Os valores possíveis para este parâmetro são: "Bonina", "Vermelho", "Laranja Queimado", "Laranja", "Amarelo", "Dourado",
        "Bege", "Marrom Claro", "Marrom", "Oliva", "Verde", "Verde Gramado", "Lima", "Verde Primavera", "Ciano", "Azul Claro",
        "Azul Metálico", "Azul", "Lilás", "Roxo", "Magenta", "Salmão", "Rosa", "Branco", "Cinza", "Cinza Escuro" e "Preto".
    * fundo: cor que será utilizada no fundo do texto. Este parâmetro pode ser:
        * Uma tupla de três valores (r, g, b), que contém os valores RGB que serão aplicados no fundo do texto.
        * Uma string, sem distinção entre letras maiúsculas e minúsculas, equivalente ao nome da cor que será utilizada no fundo
        do texto. Os valores possíveis para este parâmetro são: "Bonina", "Vermelho", "Laranja Queimado", "Laranja", "Amarelo",
        "Dourado", "Bege", "Marrom Claro", "Marrom", "Oliva", "Verde", "Verde Gramado", "Lima", "Verde Primavera", "Ciano",
        "Azul Claro", "Azul Metálico", "Azul", "Lilás", "Roxo", "Magenta", "Salmão", "Rosa", "Branco", "Cinza", "Cinza Escuro" e
        "Preto".
    * frente_claro: Se igual a True, o texto retornado terá uma cor mais clara, semelhante a negrito. Por padrão, este parâmetro
    é igual a False.
    * fundo_claro: Se igual a True, o fundo do texto retornado terá uma cor mais clara, semelhante a negrito. Por padrão, este
    parâmetro é igual a False.
    * sublinhado: Se igual a True, o texto retornado será sublinhado. Por padrão, este parâmetro é igual a False.
    """
    try:
        texto_str = str(texto)
    except:
        return texto

    texto_colorido = ""

    if frente is not None:
        # Estilo
        if not frente_claro:
            texto_colorido = ANSI.NORMAL.value
        else:
            texto_colorido = ANSI.NEGRITO.value
        if sublinhado:
            texto_colorido = ANSI.SUBLINHADO.value + texto_colorido
        texto_colorido += ANSI.FRENTE.value

        # Cor
        frente_padrao = (200, 200, 200)
        if isinstance(frente, str):
            texto_colorido += retornar_cor(frente, cor_padrao=frente_padrao)
        elif isinstance(frente, tuple) and len(frente) == 3:
            texto_colorido += retornar_rgb(frente[0], frente[1], frente[2], cor_padrao=frente_padrao)
    
    if fundo is not None:
        # Estilo
        if not fundo_claro:
            texto_colorido += ANSI.NORMAL.value
        else:
            texto_colorido += ANSI.NEGRITO.value
        texto_colorido += ANSI.FUNDO.value

        # Cor
        fundo_padrao = (12, 12, 12)
        if isinstance(fundo, str):
            texto_colorido += retornar_cor(fundo, cor_padrao=fundo_padrao)
        elif isinstance(fundo, tuple) and len(fundo) == 3:
            texto_colorido += retornar_rgb(fundo[0], fundo[1], fundo[2], cor_padrao=fundo_padrao)

    texto_colorido += texto_str + ANSI.RESET.value

    return texto_colorido

def teste_cor(texto):
    """
    Imprime um texto utilizando todas as cores possíveis, em suas opções normais (escuras) e claras. A cor de fundo não será
    mudada.

    Parâmetros:
    * texto: texto que será impresso durante o teste.
    """

    cores = ["bonina", "vermelho", "laranja queimado", "laranja", "amarelo", "dourado", "bege", "marrom claro", "marrom", "oliva",
        "verde", "verde gramado", "lima", "verde primavera", "ciano", "azul claro", "azul metalico", "azul", "lilas", "roxo",
        "magenta", "salmao", "rosa", "branco", "cinza", "cinza escuro", "preto"]
    
    print("=== Escuro ===")
    for cor in cores:
        print(colorir(texto, frente=cor))

    print("\n=== Claro ===")
    for cor in cores:
        print(colorir(texto, frente=cor, frente_claro=True))
    