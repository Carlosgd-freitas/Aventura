import sys

sys.path.append("..")
from base import utils
from criaturas import slime

def InvocarCriaturas(invocador, habilidade, lista_criaturas, nomes, nomes_zerados):
    """
    Uma criatura invocadora adiciona criaturas à lista de criaturas ao utilizar uma habilidade. Então, a lista de
    criaturas é retornada.
    """

    lista_invocados = []

    efeito = habilidade.RetornarEfeito("Invocar", startswith = True)
    conteudo = efeito.nome.split(":") # ["Invocar", "2", "Slime", "1", "Derrotado", "M"]

    quantidade = int(conteudo[1])
    invocado = conteudo[2]
    nivel = int(conteudo[3])
    forma = conteudo[4]
    genero = conteudo[5]

    if nivel <= 0:
        nivel = 1

    # A criatura será invocada <quantidade> vezes
    for i in range(quantidade):
        if invocado == "Slime":
            invocacao = slime.Slime(nivel)

        lista_invocados.append(invocacao)

    # Mensagem a ser impressa
    if habilidade.nome == "Subdivisão":
        if invocado == "Slime" and quantidade > 1:
            print(f'{invocador.nome} se subdividiu em {quantidade} Slimes!')
        else:
            print(f'{invocador.nome} se subdividiu em {quantidade} {invocado}!')
    else:
        if invocado == "Slime" and quantidade > 1:
            print(f'{invocador.nome} invocou {quantidade} Slimes!')
        else:
            print(f'{invocador.nome} invocou {quantidade} {invocado}!')
    
    nomes, nomes_zerados = utils.ContarNomes(nomes, nomes_zerados, lista_invocados, modifica_nomes_zerados = False)
    utils.NomesUnicos(nomes, nomes_zerados, lista_invocados)

    for c in lista_invocados:
        lista_criaturas.append(c)

    return lista_criaturas
    