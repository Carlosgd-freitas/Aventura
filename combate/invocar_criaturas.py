import sys

sys.path.append("..")
from base import utils
from catalogo.criaturas import RetornarCriatura

def InvocarCriaturas(invocador, habilidade, lista_criaturas, nomes, nomes_zerados):
    """
    Uma criatura invocadora adiciona criaturas à lista de criaturas ao utilizar uma habilidade. Então, a lista de
    criaturas é retornada.
    """

    lista_invocados = []

    efeito = habilidade.RetornarEfeito("Invocar")
    nome = efeito.invocacao["nome"]
    nivel = efeito.invocacao["nivel"]
    quantidade = int(efeito.invocacao["quantidade"])
    condicao = efeito.invocacao["condicao"]

    if nivel <= 0:
        nivel = 1

    # A criatura será invocada <quantidade> vezes
    for i in range(quantidade):
        invocacao = RetornarCriatura(nome, nivel)
        lista_invocados.append(invocacao)

    # Mensagem a ser impressa
    if habilidade.nome == "Subdivisão":
        print(f'{invocador.nome} se subdividiu em {quantidade} {nome}!')
    else:
        print(f'{invocador.nome} invocou {quantidade} {nome}!')
    
    nomes, nomes_zerados = utils.ContarNomes(nomes, nomes_zerados, lista_invocados, modifica_nomes_zerados = False)
    utils.NomesUnicos(nomes, nomes_zerados, lista_invocados)

    for c in lista_invocados:
        lista_criaturas.append(c)

    return lista_criaturas
    