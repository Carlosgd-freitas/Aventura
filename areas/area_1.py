import sys

sys.path.append("..")
from classes_base import area
from itens import consumiveis, equipamentos
from criaturas import slime, cobra_venenosa, slime_gigante, tortuga

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

        # Definindo os encontros de criaturas inimigas possíveis
        self.DefinirEncontros(jogador)

        super(Area_1, self).__init__("Planície de Slimes", loja_itens, estalagem_preco)
    
    def DefinirEncontros(self, jogador):
        """
        Retorna uma lista de números inteiros inimigas baseada no nível do jogador, onde cada um corresponde à um
        grupo de criaturas que pode ser encontrado pela área.
        """

        encontros = []

        if jogador.nivel == 1:
            encontros = [1, 2, 4, 6, 8, 10]

        elif jogador.nivel == 2:
            encontros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

        elif jogador.nivel == 3:
            encontros = [2, 3, 5, 6, 7, 9, 10, 11, 12, 13, 14]
            
        elif jogador.nivel == 4:
            encontros = [3, 7, 11, 13, 15, 16, 17, 18]
            
        elif jogador.nivel == 5:
            encontros = [19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]
        
        else:
            encontros = [27, 29]

        self.encontros = encontros

    def RetornarEncontro(self, jogador, numero):
        """
        Retorna uma lista de criaturas inimigas baseada no número passado como parâmetro.
        """

        inimigos = []

        # Um Slime no nível do jogador
        if numero == 1:
            slime_1 = slime.Slime(jogador.nivel)
            inimigos.append(slime_1)

        # Dois Slimes no nível do jogador
        elif numero == 2:
            slime_1 = slime.Slime(jogador.nivel)
            slime_2 = slime.Slime(jogador.nivel)
            inimigos.append(slime_1)
            inimigos.append(slime_2)

        # Três Slimes um nível abaixo do nível do jogador
        elif numero == 3:
            slime_1 = slime.Slime(jogador.nivel - 1)
            slime_2 = slime.Slime(jogador.nivel - 1)
            slime_3 = slime.Slime(jogador.nivel - 1)
            inimigos.append(slime_1)
            inimigos.append(slime_2)
            inimigos.append(slime_3)

        # Uma Cobra Venenosa no nível do jogador
        elif numero == 4:
            cobra_1 = cobra_venenosa.CobraVenenosa(jogador.nivel)
            inimigos.append(cobra_1)

        # Duas Cobras Venenosas no nível do jogador
        elif numero == 5:
            cobra_1 = cobra_venenosa.CobraVenenosa(jogador.nivel)
            cobra_2 = cobra_venenosa.CobraVenenosa(jogador.nivel)
            inimigos.append(cobra_1)
            inimigos.append(cobra_2)
        
        # Um Slime e uma Cobra Venenosa no nível do jogador
        elif numero == 6:
            slime_1 = slime.Slime(jogador.nivel)
            cobra_1 = cobra_venenosa.CobraVenenosa(jogador.nivel)
            inimigos.append(slime_1)
            inimigos.append(cobra_1)
        
        # Dois Slimes e uma Cobra Venenosa um nível abaixo do nível do jogador
        elif numero == 7:
            slime_1 = slime.Slime(jogador.nivel - 1)
            slime_2 = slime.Slime(jogador.nivel - 1)
            cobra_1 = cobra_venenosa.CobraVenenosa(jogador.nivel - 1)
            inimigos.append(slime_1)
            inimigos.append(slime_2)
            inimigos.append(cobra_1)

        # Uma Tortuga no nível do jogador
        elif numero == 8:
            tortuga_1 = tortuga.Tortuga(jogador.nivel)
            inimigos.append(tortuga_1)
        
        # Duas Tortugas no nível do jogador
        elif numero == 9:
            tortuga_1 = tortuga.Tortuga(jogador.nivel)
            tortuga_2 = tortuga.Tortuga(jogador.nivel)
            inimigos.append(tortuga_1)
            inimigos.append(tortuga_2)
        
        # Um Slime e uma Tortuga no nível do jogador
        elif numero == 10:
            slime_1 = slime.Slime(jogador.nivel)
            tortuga_1 = tortuga.Tortuga(jogador.nivel)
            inimigos.append(slime_1)
            inimigos.append(tortuga_1)
        
        # Dois Slimes e uma Tortuga um nível abaixo do nível do jogador
        elif numero == 11:
            slime_1 = slime.Slime(jogador.nivel - 1)
            slime_2 = slime.Slime(jogador.nivel - 1)
            tortuga_1 = tortuga.Tortuga(jogador.nivel - 1)
            inimigos.append(slime_1)
            inimigos.append(slime_2)
            inimigos.append(tortuga_1)

        # Uma Cobra Venenosa e uma Tortuga no nível do jogador
        elif numero == 12:
            cobra_1 = cobra_venenosa.CobraVenenosa(jogador.nivel)
            tortuga_1 = tortuga.Tortuga(jogador.nivel)
            inimigos.append(cobra_1)
            inimigos.append(tortuga_1)
        
        # Um Slime, uma Cobra Venenosa e uma Tortuga no nível do jogador
        elif numero == 13:
            slime_1 = slime.Slime(jogador.nivel)
            cobra_1 = cobra_venenosa.CobraVenenosa(jogador.nivel)
            tortuga_1 = tortuga.Tortuga(jogador.nivel)
            inimigos.append(slime_1)
            inimigos.append(cobra_1)
            inimigos.append(tortuga_1)

        # Um Slime Gigante um nível abaixo do nível do jogador
        elif numero == 14:
            slime_gigante_1 = slime_gigante.SlimeGigante(jogador.nivel - 1)
            inimigos.append(slime_gigante_1)
        
        # Um Slime no nível do jogador e um Slime Gigante um nível abaixo do nível do jogador
        elif numero == 15:
            slime_1 = slime.Slime(jogador.nivel)
            slime_gigante_1 = slime_gigante.SlimeGigante(jogador.nivel - 1)
            inimigos.append(slime_1)
            inimigos.append(slime_gigante_1)
        
        # Uma Cobra Venenosa no nível do jogador e um Slime Gigante um nível abaixo do nível do jogador
        elif numero == 16:
            cobra_1 = cobra_venenosa.CobraVenenosa(jogador.nivel)
            slime_gigante_1 = slime_gigante.SlimeGigante(jogador.nivel - 1)
            inimigos.append(cobra_1)
            inimigos.append(slime_gigante_1)
        
        # Uma Tortuga no nível do jogador e um Slime Gigante um nível abaixo do nível do jogador
        elif numero == 17:
            tortuga_1 = tortuga.Tortuga(jogador.nivel)
            slime_gigante_1 = slime_gigante.SlimeGigante(jogador.nivel - 1)
            inimigos.append(tortuga_1)
            inimigos.append(slime_gigante_1)
        
        # Um Slime Gigante no nível do jogador
        elif numero == 18:
            slime_gigante_1 = slime_gigante.SlimeGigante(jogador.nivel)
            inimigos.append(slime_gigante_1)

        # Um Slime Gigante no nível do jogador e um Slime um nível abaixo do nível do jogador
        elif numero == 19:
            slime_gigante_1 = slime_gigante.SlimeGigante(jogador.nivel)
            slime_1 = slime.Slime(jogador.nivel - 1)
            inimigos.append(slime_gigante_1)
            inimigos.append(slime_1)
        
        # Um Slime Gigante no nível do jogador e dois Slimes um nível abaixo do nível do jogador
        elif numero == 20:
            slime_gigante_1 = slime_gigante.SlimeGigante(jogador.nivel)
            slime_1 = slime.Slime(jogador.nivel - 1)
            slime_2 = slime.Slime(jogador.nivel - 1)
            inimigos.append(slime_gigante_1)
            inimigos.append(slime_1)
            inimigos.append(slime_2)
        
        # Um Slime Gigante no nível do jogador e uma Cobra Venenosa um nível abaixo do nível do jogador
        elif numero == 21:
            slime_gigante_1 = slime_gigante.SlimeGigante(jogador.nivel)
            cobra_1 = cobra_venenosa.CobraVenenosa(jogador.nivel - 1)
            inimigos.append(slime_gigante_1)
            inimigos.append(cobra_1)
        
        # Um Slime Gigante no nível do jogador e duas Cobras Venenosas um nível abaixo do nível do jogador
        elif numero == 22:
            slime_gigante_1 = slime_gigante.SlimeGigante(jogador.nivel)
            cobra_1 = cobra_venenosa.CobraVenenosa(jogador.nivel - 1)
            cobra_2 = cobra_venenosa.CobraVenenosa(jogador.nivel - 1)
            inimigos.append(slime_gigante_1)
            inimigos.append(cobra_1)
            inimigos.append(cobra_2)
        
        # Um Slime Gigante no nível do jogador e uma Tortuga um nível abaixo do nível do jogador
        elif numero == 23:
            slime_gigante_1 = slime_gigante.SlimeGigante(jogador.nivel)
            tortuga_1 = tortuga.Tortuga(jogador.nivel - 1)
            inimigos.append(slime_gigante_1)
            inimigos.append(tortuga_1)
        
        # Um Slime Gigante no nível do jogador e duas Tortugas um nível abaixo do nível do jogador
        elif numero == 24:
            slime_gigante_1 = slime_gigante.SlimeGigante(jogador.nivel)
            tortuga_1 = tortuga.Tortuga(jogador.nivel - 1)
            tortuga_2 = tortuga.Tortuga(jogador.nivel - 1)
            inimigos.append(slime_gigante_1)
            inimigos.append(tortuga_1)
            inimigos.append(tortuga_2)
        
        # Um Slime Gigante no nível do jogador; um Slime e uma Cobra Venenosa um nível abaixo do nível do jogador
        elif numero == 25:
            slime_gigante_1 = slime_gigante.SlimeGigante(jogador.nivel)
            slime_1 = slime.Slime(jogador.nivel - 1)
            cobra_1 = cobra_venenosa.CobraVenenosa(jogador.nivel - 1)
            inimigos.append(slime_gigante_1)
            inimigos.append(slime_1)
            inimigos.append(cobra_1)
        
        # Um Slime Gigante no nível do jogador; um Slime e uma Tortuga um nível abaixo do nível do jogador
        elif numero == 26:
            slime_gigante_1 = slime_gigante.SlimeGigante(jogador.nivel)
            slime_1 = slime.Slime(jogador.nivel - 1)
            tortuga_1 = tortuga.Tortuga(jogador.nivel - 1)
            inimigos.append(slime_gigante_1)
            inimigos.append(slime_1)
            inimigos.append(tortuga_1)

        # Um Slime Gigante no nível do jogador; uma Cobra Venenosa e uma Tortuga um nível abaixo do nível do jogador
        elif numero == 27:
            slime_gigante_1 = slime_gigante.SlimeGigante(jogador.nivel)
            cobra_1 = cobra_venenosa.CobraVenenosa(jogador.nivel - 1)
            tortuga_1 = tortuga.Tortuga(jogador.nivel - 1)
            inimigos.append(slime_gigante_1)
            inimigos.append(cobra_1)
            inimigos.append(tortuga_1)

        # Dois Slimes Gigantes um nível abaixo do nível do jogador
        elif numero == 28:
            slime_gigante_1 = slime_gigante.SlimeGigante(jogador.nivel - 1)
            slime_gigante_2 = slime_gigante.SlimeGigante(jogador.nivel - 1)
            inimigos.append(slime_gigante_1)
            inimigos.append(slime_gigante_2)

        # Dois Slimes Gigantes no nível do jogador
        elif numero == 29:
            slime_gigante_1 = slime_gigante.SlimeGigante(jogador.nivel)
            slime_gigante_2 = slime_gigante.SlimeGigante(jogador.nivel)
            inimigos.append(slime_gigante_1)
            inimigos.append(slime_gigante_2)

        return inimigos
