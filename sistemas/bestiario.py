import sys

sys.path.append("..")
from criaturas import slime, slime_gigante, cobra_venenosa, tortuga, ervagora, slime_mel, \
    larva_abelhoide, abelhoide, larry, cristal_atacante

def CriaturasPagina(pagina, criaturas_por_pagina):
    """
    Retorna uma lista contendo os nomes de cada criatura presente em uma página do bestiário.

    Parâmetros:
    - pagina: índice da página do bestiário;
    - criaturas_por_pagina: quantidade de criaturas por página do bestiário.
    """
    criaturas = ['Slime', 'Slime Gigante', 'Cobra Venenosa', 'Tortuga', 'Ervágora', 'Slime de Mel',
        'Larva de Abelhóide', 'Abelhóide', 'Larry', 'Cristal Atacante']
    
    indice_inicio = pagina * criaturas_por_pagina
    indice_fim = indice_inicio + criaturas_por_pagina
    if indice_fim > len(criaturas):
        indice_fim = len(criaturas)

    return criaturas[indice_inicio:indice_fim]

def RetornarCriatura(nome, nivel):
    """
    Retorna uma criatura com o nome e nível especificados.

    Parâmetros:
    - nome: nome da criatura a ser retornada;
    - nivel: nível da criatura a ser retornada.
    """
    if nome == 'Slime':
        return slime.Slime(nivel)
    elif nome == 'Slime Gigante':
        return slime_gigante.SlimeGigante(nivel)
    elif nome == 'Cobra Venenosa':
        return cobra_venenosa.CobraVenenosa(nivel)
    elif nome == 'Tortuga':
        return tortuga.Tortuga(nivel)
    elif nome == 'Ervágora':
        return ervagora.Ervagora(nivel)
    elif nome == 'Slime de Mel':
        return slime_mel.SlimeMel(nivel)
    elif nome == 'Larva de Abelhóide':
        return larva_abelhoide.LarvaAbelhoide(nivel)
    elif nome == 'Abelhóide':
        return abelhoide.Abelhoide(nivel)
    elif nome == 'Larry':
        return larry.Larry(nivel)
    elif nome == 'Cristal Atacante':
        return cristal_atacante.CristalAtacante(nivel)
    