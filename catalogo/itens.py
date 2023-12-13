import sys
from unidecode import unidecode

sys.path.append("..")
from itens import consumiveis, espolios, equipamentos

def RetornarItem(nome, quantidade=1, preco=0):
    """
    Retorna um item. Se o nome do item não for identificado, retorna None.

    Parâmetros:
    - nome: nome do item a ser retornado;
    - quantidade: quantidade do item que será retornado. Por padrão, a quantidade do item será 1;
    - preco: preço do item que será retornado. Por padrão, o preço do item será 0.
    """
    if not isinstance(nome, str):
        return None

    nome_normalizado = unidecode(nome.lower())

    # Consumíveis
    if nome_normalizado == "erva curativa":
        return consumiveis.ErvaCurativa(quantidade, preco)
    elif nome_normalizado == "mel de abelhoide":
        return consumiveis.MelAbelhoide(quantidade, preco)
    elif nome_normalizado == "pocao pequena de cura":
        return consumiveis.PocaoPequenaCura(quantidade, preco)
    elif nome_normalizado == "pocao pequena de mana":
        return consumiveis.PocaoPequenaMana(quantidade, preco)
    elif nome_normalizado == "pocao pequena de regeneracao":
        return consumiveis.PocaoPequenaRegeneracao(quantidade, preco)
    elif nome_normalizado == "elixir pequeno de ataque":
        return consumiveis.ElixirPequeno("Ataque", quantidade, preco)
    elif nome_normalizado == "elixir pequeno de defesa":
        return consumiveis.ElixirPequeno("Defesa", quantidade, preco)
    elif nome_normalizado == "elixir pequeno de magia":
        return consumiveis.ElixirPequeno("Magia", quantidade, preco)
    elif nome_normalizado == "elixir pequeno de velocidade":
        return consumiveis.ElixirPequeno("Velocidade", quantidade, preco)
    elif nome_normalizado == "antidoto":
        return consumiveis.Antidoto(quantidade, preco)
    elif nome_normalizado == "bomba inferior":
        return consumiveis.BombaInferior(quantidade, preco)
    elif nome_normalizado == "bomba grudenta inferior":
        return consumiveis.BombaGrudentaInferior(quantidade, preco)
    
    # Espólios
    elif nome_normalizado == "ouro":
        return espolios.Ouro(quantidade)
    elif nome_normalizado == "experiencia" or nome_normalizado == "exp":
        return espolios.Experiencia(quantidade)
    elif nome_normalizado == "fluido de slime":
        return espolios.FluidoSlime(quantidade, preco)
    elif nome_normalizado == "glandula venenosa":
        return espolios.GlandulaVenenosa(quantidade, preco)
    elif nome_normalizado == "carapaca de tortuga":
        return espolios.CarapacaTortuga(quantidade, preco)
    elif nome_normalizado == "rubi de fogo":
        return espolios.RubiFogo(quantidade, preco)

    # Equipamentos
    elif nome_normalizado == "item vazio" or nome_normalizado == "vazio":
        return equipamentos.Vazio()
    elif nome_normalizado == "espada enferrujada":
        return equipamentos.EspadaEnferrujada(quantidade, preco)
    elif nome_normalizado == "espada de ferro":
        return equipamentos.EspadaFerro(quantidade, preco)
    elif nome_normalizado == "cajado do iniciante":
        return equipamentos.CajadoIniciante(quantidade, preco)
    elif nome_normalizado == "cajado do aprendiz":
        return equipamentos.CajadoAprendiz(quantidade, preco)
    elif nome_normalizado == "broquel de madeira":
        return equipamentos.BroquelMadeira(quantidade, preco)
    elif nome_normalizado == "chapeu de couro":
        return equipamentos.ChapeuCouro(quantidade, preco)
    elif nome_normalizado == "peitoral de couro":
        return equipamentos.PeitoralCouro(quantidade, preco)
    elif nome_normalizado == "robe de algodao":
        return equipamentos.RobeAlgodao(quantidade, preco)
    elif nome_normalizado == "botas de couro":
        return equipamentos.BotasCouro(quantidade, preco)
    elif nome_normalizado == "amuleto de esmeralda":
        return equipamentos.AmuletoEsmeralda(quantidade, preco)

    return None
