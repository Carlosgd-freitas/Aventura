import sys

sys.path.append("..")
from base import efeito, habilidade

def Vinganca(atributo, valor, criatura, criatura_singular_plural, criatura_genero):
    """
    Habilidade passiva que aumenta <atributo> em <valor> quando uma criatura aliada de nome <criatura> morre. Os
    parâmetros criatura_singular_plural e criatura_genero são para melhora das mensagens impressas.
    * Alvo: Próprio
    * Tipo: Normal
    """
    descricao = ''

    if atributo == 'Ataque':
        aumento = efeito.Efeito("Vingança:" + criatura + ":Aumento Ataque", valor, 0, 999, 100)
        descricao = 'Aumenta o ataque em ' + str(valor)
    elif atributo == 'Defesa':
        aumento = efeito.Efeito("Vingança:" + criatura + ":Aumento Defesa", valor, 0, 999, 100)
        descricao = 'Aumenta a defesa em ' + str(valor)
    elif atributo == 'Magia':
        aumento = efeito.Efeito("Vingança:" + criatura + ":Aumento Magia", valor, 0, 999, 100)
        descricao = 'Aumenta a magia em ' + str(valor)
    elif atributo == 'Velocidade':
        aumento = efeito.Efeito("Vingança:" + criatura + ":Aumento Velocidade", valor, 0, 999, 100)
        descricao = 'Aumenta a velocidade em ' + str(valor)

    if criatura_singular_plural == 'singular':
        if criatura_genero == 'M':
            descricao += ' quando um ' + criatura + ' aliado morre.'
        elif criatura_genero == 'F':
            descricao += ' quando uma ' + criatura + ' aliada morre.'

    elif criatura_singular_plural == 'plural':
        if criatura_genero == 'M':
            descricao += ' quando ' + criatura + ' aliados morrem.'
        elif criatura_genero == 'F':
            descricao += ' quando ' + criatura + ' aliadas morrem.'

    vinganca = habilidade.Habilidade("Vingança", descricao, "Normal", "proprio", "passiva", valor, [], 0, 0,
        [], [aumento], "singular", "F", False, 0.0, 1.0)
    
    return vinganca