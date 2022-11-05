import sys
sys.path.append("..")
from base import imprimir

def DialogoChefaoDerrotado(chefao, lista_criaturas, criatura, conf):
    """
    Recebe:
    * chefao -> número inteiro que indica qual é a batalha de chefão em questão;
    * lista_criaturas -> lista de criaturas que o chefão faz parte;
    * criatura -> qual criatura acaba de ser derrotada;
    * conf -> configurações do jogo, que podem ser personalizadas pelo jogador.

    Imprime diálogos relacionados à derrota de uma criatura em uma batalha de chefão.
    """

    if chefao == 0:
        return

    # Larry e Cristal Atacante
    if chefao == 1:

        # Verificando quem ainda está vivo na batalha
        cristal_vivo = 0
        larry_vivo = 0
        for c in lista_criaturas:
            if c.nome == "Cristal Atacante" and c.hp > 0:
                cristal_vivo = 1
            
            elif c.nome == "Slime" or c.nome == "Larry" and c.hp > 0:
                larry_vivo = 1

        # Larry derrotado primeiro e Cristal ainda está vivo
        if (criatura.nome == "Slime" or criatura.nome == "Larry") and cristal_vivo == 1:
            imprimir.ImprimirComDelay('Cristal: Grave falha na missão de resgate...\n', conf.npc_fala_delay)
            imprimir.ImprimirComDelay('Cristal: Anomalia Larry...acaba de ser erradicada...\n', conf.npc_fala_delay)
            print('O slime anômalo, chamado de Larry pelo cristal, explode após sofrer o último ataque.')
        
        # Larry derrotado por último
        elif (criatura.nome == "Slime" or criatura.nome == "Larry") and cristal_vivo == 0:
            print('O slime anômalo, chamado de Larry pelo cristal, explode após sofrer o último ataque.')
        
        # Cristal Atacante derrotado primeiro e Larry ainda está vivo
        elif criatura.nome == "Cristal Atacante" and larry_vivo == 1:
            imprimir.ImprimirComDelay('Cristal: Falha na missão de resgate...\n', conf.npc_fala_delay)
            imprimir.ImprimirComDelay('Cristal: O Poder de fogo alocado para a missão...Não foi suficiente...\n', conf.npc_fala_delay)
            imprimir.ImprimirComDelay('Cristal: Alta chance da anomalia Larry ser erradicada...\n', conf.npc_fala_delay)
            print('Com suas inscrições rúnicas apagando lentamente, o Cristal Atacante cai no chão, derrotado.')
        
        # Cristal Atacante derrotado por último
        elif criatura.nome == "Cristal Atacante" and larry_vivo == 0:
            imprimir.ImprimirComDelay('Cristal: O responsável pela falha da missão e de futuros experimentos...segue vivo...\n', conf.npc_fala_delay)
            print('Com suas inscrições rúnicas apagando lentamente, o Cristal Atacante cai no chão, derrotado.')


def ChefaoDerrotado(chefao, lista_criaturas, criatura, conf):
    """
    Recebe:
    * chefao -> número inteiro que indica qual é a batalha de chefão em questão;
    * lista_criaturas -> lista de criaturas que o chefão faz parte;
    * criatura -> qual criatura acaba de ser derrotada;
    * conf -> configurações do jogo, que podem ser personalizadas pelo jogador.

    Altera o chefão em batalhas de múltiplas fases, concedendo efeitos, habilidades, etc.
    """

    if chefao == 0:
        return

    # Larry e Cristal Atacante
    if chefao == 1:

        # Cristal Atacante derrotado primeiro
        if criatura.nome == "Cristal Atacante":

            for c in lista_criaturas:
                if c.nome == "Slime" and c.hp > 0:
                    c.nome = "Larry"
