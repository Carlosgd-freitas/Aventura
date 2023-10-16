import sys
from unidecode import unidecode

sys.path.append("..")
from criaturas import abelhoide, cobra_venenosa, cristal_atacante, ervagora, larry, larva_abelhoide, slime, slime_mel, \
    slime_gigante, tortuga

def RetornarCriatura(nome, nivel=1, chefao=False):
    """
    Retorna uma criatura. Se o nome da criatura não for identificado, retorna None.

    Parâmetros:
    - nome: nome da criatura a ser retornada;
    - nivel: nível da criatura a ser retornada. Por padrão, o nível da criatura será 1;
    - chefao: se igual a verdadeiro, a criatura retornada será ajustada para sua forma de chefão, se possível. Por padrão,
    este parâmetro é igual a falso.
    """
    if not isinstance(nome, str):
        return None

    nome_normalizado = unidecode(nome.lower())

    if nome_normalizado == "abelhoide":
        return abelhoide.Abelhoide(nivel)
    elif nome_normalizado == "cobra venenosa":
        return cobra_venenosa.CobraVenenosa(nivel)
    elif nome_normalizado == "cristal atacante":
        return cristal_atacante.CristalAtacante(nivel, chefao=chefao)
    elif nome_normalizado == "ervagora":
        return ervagora.Ervagora(nivel)
    elif nome_normalizado == "larry":
        return larry.Larry(nivel)
    elif nome_normalizado == "larva de abelhoide" or nome_normalizado == "larva abelhoide":
        return larva_abelhoide.LarvaAbelhoide(nivel)
    elif nome_normalizado == "slime":
        return slime.Slime(nivel)
    elif nome_normalizado == "slime de mel" or nome_normalizado == "slime mel":
        return slime_mel.SlimeMel(nivel)
    elif nome_normalizado == "slime gigante":
        return slime_gigante.SlimeGigante(nivel)
    elif nome_normalizado == "tortuga":
        return tortuga.Tortuga(nivel)
    
    return None
