import sys

sys.path.append("..")
from base import efeito, habilidade

def Vinganca(atributo, valor, criatura_nome, criatura_singular_plural, criatura_genero):
    """
    Habilidade passiva que aumenta <atributo> em <valor> quando uma criatura aliada de nome <criatura_nome>
    é derrotada. Os parâmetros criatura_singular_plural e criatura_genero são para melhora das mensagens impressas.
    * Alvo: Próprio
    * Tipo: Normal
    """

    # efeito.nome: "Vingança:Larva de Abelhóide:Aumento Ataque:F"]
    descricao = ''

    if atributo == 'Ataque':
        aumento = efeito.Efeito(f"Vingança:{criatura_nome}:Aumento Ataque:{criatura_genero}", valor, 0, 999, 100)
        descricao = 'Aumenta o ataque em ' + str(valor)
    elif atributo == 'Defesa':
        aumento = efeito.Efeito(f"Vingança:{criatura_nome}:Aumento Defesa:{criatura_genero}", valor, 0, 999, 100)
        descricao = 'Aumenta a defesa em ' + str(valor)
    elif atributo == 'Magia':
        aumento = efeito.Efeito(f"Vingança:{criatura_nome}:Aumento Magia:{criatura_genero}", valor, 0, 999, 100)
        descricao = 'Aumenta a magia em ' + str(valor)
    elif atributo == 'Velocidade':
        aumento = efeito.Efeito(f"Vingança:{criatura_nome}:Aumento Velocidade:{criatura_genero}", valor, 0, 999, 100)
        descricao = 'Aumenta a velocidade em ' + str(valor)
    elif atributo == 'Chance Crítico':
        aumento = efeito.Efeito(f"Vingança:{criatura_nome}:Aumento Chance Crítico:{criatura_genero}", valor, 0, 999, 100)
        descricao = 'Aumenta a velocidade em ' + str(valor)

    if criatura_singular_plural == 'singular':
        if criatura_genero == 'M':
            descricao += ' quando um ' + criatura_nome + ' aliado morre.'
        elif criatura_genero == 'F':
            descricao += ' quando uma ' + criatura_nome + ' aliada morre.'

    elif criatura_singular_plural == 'plural':
        if criatura_genero == 'M':
            descricao += ' quando ' + criatura_nome + ' aliados morrem.'
        elif criatura_genero == 'F':
            descricao += ' quando ' + criatura_nome + ' aliadas morrem.'

    vinganca = habilidade.Habilidade("Vingança", descricao, "Normal", "Próprio", "Passiva", valor, [], 0, 0,
        [], [aumento], "singular", "F", False, 0.0, 1.0)
    
    return vinganca