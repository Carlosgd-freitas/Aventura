import sys
import random

sys.path.append("..")
from classes_base import area
from itens import consumiveis, equipamentos
from criaturas import slime, cobra_venenosa, slime_gigante, tortuga, ervagora

class Area_1(area.Area):
    """
    Esta classe é utilizada para a primeira área presentes no jogo.
    """

    def __init__(self, jogador, estalagem_preco = 9999999):
        """
        Inicializador da classe.
        """

        # Itens disponíveis para venda na loja da área 1
        loja_itens = []

        # Consumíveis
        pocao_cura_pequena = consumiveis.PocaoCuraPequena(5, 5)
        loja_itens.append(pocao_cura_pequena)

        pocao_mana_pequena = consumiveis.PocaoManaPequena(5, 5)
        loja_itens.append(pocao_mana_pequena)

        bomba_inferior = consumiveis.BombaInferior(2, 6)
        loja_itens.append(bomba_inferior)

        antidoto = consumiveis.Antidoto(10, 3)
        loja_itens.append(antidoto)

        # Armas e Escudos
        espada = equipamentos.Espada(3, 5)
        loja_itens.append(espada)

        cajado_aprendiz = equipamentos.CajadoAprendiz(3, 5)
        loja_itens.append(cajado_aprendiz)

        broquel_madeira = equipamentos.BroquelMadeira(3, 7)
        loja_itens.append(broquel_madeira)

        # Armaduras
        chapeu_couro = equipamentos.ChapeuCouro(3, 4)
        loja_itens.append(chapeu_couro)

        peitoral_couro = equipamentos.PeitoralCouro(3, 10)
        loja_itens.append(peitoral_couro)

        robe_algodao = equipamentos.RobeAlgodao(3, 10)
        loja_itens.append(robe_algodao)

        botas_couro = equipamentos.BotasCouro(3, 8)
        loja_itens.append(botas_couro)

        self.loja_itens = loja_itens

        super(Area_1, self).__init__("Planície de Slimes", loja_itens, estalagem_preco)

    def RetornarEncontro(self, jogador):
        """
        Retorna uma lista de criaturas inimigas.
        """

        inimigos = []
        peso_restante = jogador.nivel + 1

        # Possíveis inimigos a serem encontrados na área 1:
        # Slime
        # Slime Gigante
        # Cobra Venenosa
        # Tortuga
        # Ervágora

        # Possíveis inimigos raros a serem encontrados na área 1:
        # Slime Metálico

        # Inimigo Raro: 5% de chance de ser encontrado
        if random.randint(1, 100) <= 5:
            pass # adicionar um slime metálico

        while peso_restante > 0:
            indice = random.randint(1, 10)

            # 1/10 de chance: Slime no nível do jogador
            if indice == 1 and peso_restante >= 1:
                inimigo = slime.Slime(jogador.nivel)
                inimigos.append(inimigo)
                peso_restante -= 1
            
            # 1/10 de chance: Slime um nível abaixo do jogador
            elif indice == 2 and peso_restante >= 1 and jogador.nivel > 1:
                inimigo = slime.Slime(jogador.nivel - 1)
                inimigos.append(inimigo)
                peso_restante -= 1
            
            # 1/10 de chance: Cobra Venenosa no nível do jogador
            elif indice == 3 and peso_restante >= 2:
                inimigo = cobra_venenosa.CobraVenenosa(jogador.nivel)
                inimigos.append(inimigo)
                peso_restante -= 2
            
            # 1/10 de chance: Cobra Venenosa um nível abaixo do jogador
            elif indice == 4 and peso_restante >= 2 and jogador.nivel > 1:
                inimigo = cobra_venenosa.CobraVenenosa(jogador.nivel - 1)
                inimigos.append(inimigo)
                peso_restante -= 2
            
            # 1/10 de chance: Tortuga no nível do jogador
            elif indice == 5 and peso_restante >= 2:
                inimigo = tortuga.Tortuga(jogador.nivel)
                inimigos.append(inimigo)
                peso_restante -= 2
            
            # 1/10 de chance: Tortuga um nível abaixo do jogador
            elif indice == 6 and peso_restante >= 2 and jogador.nivel > 1:
                inimigo = tortuga.Tortuga(jogador.nivel - 1)
                inimigos.append(inimigo)
                peso_restante -= 2
            
            # 1/10 de chance: Slime Gigante no nível do jogador
            elif indice == 7 and peso_restante >= 3:
                inimigo = slime_gigante.SlimeGigante(jogador.nivel)
                inimigos.append(inimigo)
                peso_restante -= 3

            # 1/10 de chance: Slime Gigante um nível abaixo do jogador
            elif indice == 8 and peso_restante >= 3 and jogador.nivel > 1:
                inimigo = slime_gigante.SlimeGigante(jogador.nivel - 1)
                inimigos.append(inimigo)
                peso_restante -= 3
            
            # 1/10 de chance: Ervágora no nível do jogador
            elif indice == 9 and peso_restante >= 1:
                inimigo = ervagora.Ervagora(jogador.nivel)
                inimigos.append(inimigo)
                peso_restante -= 1

            # 1/10 de chance: Ervágora um nível abaixo do jogador
            elif indice == 10 and peso_restante >= 1 and jogador.nivel > 1:
                inimigo = ervagora.Ervagora(jogador.nivel - 1)
                inimigos.append(inimigo)
                peso_restante -= 1
        
        return inimigos
