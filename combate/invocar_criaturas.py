import sys
from colorama import Fore, Back, Style

sys.path.append("..")
from criaturas import slime

def InvocarCriaturas(invocador, habilidade, lista_criaturas):
    """
    Uma criatura invocadora adiciona criaturas à lista de criaturas ao utilizar uma habilidade. Então, a lista de
    criaturas é retornada.
    """

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

            lista_criaturas.append(invocacao)
        
        if quantidade > 1:
            print(f'{invocador.nome} se subdividiu em {quantidade} {invocado}s!')
        else:
            print(f'{invocador.nome} se subdividiu em {quantidade} {invocado}!')

    return lista_criaturas
    