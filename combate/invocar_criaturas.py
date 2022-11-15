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

    efeito = habilidade.efeitos[0]
    efeito = efeito.nome.split(":") # ["Invocar", "2", "Slime"]

    quantidade = int(efeito[1])
    invocado = efeito[2]
    nivel = invocador.nivel - 1
    if nivel <= 0:
        nivel = 1

    if habilidade.nome == "Subdivisão":

        # A criatura será invocada <quantidade> vezes
        for i in range(0, quantidade):

            if invocado == "Slime":
                invocacao = slime.Slime(nivel)

            lista_invocados.append(invocacao)
        
        if invocado == "Slime":
            print(f'{invocador.nome} se subdividiu em {quantidade} Slimes!')
    
    nomes, nomes_zerados = utils.ContarNomes(nomes, nomes_zerados, lista_invocados, modifica_nomes_zerados = False)
    utils.NomesUnicos(nomes, nomes_zerados, lista_invocados)

    for c in lista_invocados:
        lista_criaturas.append(c)

    return lista_criaturas
    