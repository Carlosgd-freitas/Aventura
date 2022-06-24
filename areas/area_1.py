import sys
import random
from colorama import Fore, Back, Style

sys.path.append("..")
from classes_base import area, utils
from itens import consumiveis, equipamentos
from criaturas import slime, cobra_venenosa, slime_gigante, tortuga, ervagora, slime_mel

class Area_1(area.Area):
    """
    Esta classe é utilizada para a primeira área presentes no jogo.
    """

    def __init__(self, estalagem_preco = 9999999):
        """
        Inicializador da classe.
        """

        # Flags relacionadas ao jogador e a vila
        self.conhece_vila = False

        # Flags para os diálogos entre o jogador e NPCs
        self.conhece_vendedor_pocoes = False
        self.conhece_vendedor_armamentos = False
        self.conhece_estalagem = False

        # Itens disponíveis para venda na loja do Vendedor de Poções da área 1
        loja_pocoes_itens = []

        # Consumíveis
        pocao_cura_pequena = consumiveis.PocaoCuraPequena(5, 5)
        loja_pocoes_itens.append(pocao_cura_pequena)

        pocao_mana_pequena = consumiveis.PocaoManaPequena(5, 5)
        loja_pocoes_itens.append(pocao_mana_pequena)

        antidoto = consumiveis.Antidoto(10, 3)
        loja_pocoes_itens.append(antidoto)

        mel = consumiveis.MelAbelhoide(3, 3)
        loja_pocoes_itens.append(mel)

        # Itens disponíveis para venda na loja do Vendedor de Armamentos da área 1
        loja_armamentos_itens = []

        # Armas e Escudos
        espada = equipamentos.Espada(3, 5)
        loja_armamentos_itens.append(espada)

        cajado_aprendiz = equipamentos.CajadoAprendiz(3, 5)
        loja_armamentos_itens.append(cajado_aprendiz)

        broquel_madeira = equipamentos.BroquelMadeira(3, 7)
        loja_armamentos_itens.append(broquel_madeira)

        # Armaduras
        chapeu_couro = equipamentos.ChapeuCouro(3, 4)
        loja_armamentos_itens.append(chapeu_couro)

        peitoral_couro = equipamentos.PeitoralCouro(3, 10)
        loja_armamentos_itens.append(peitoral_couro)

        robe_algodao = equipamentos.RobeAlgodao(3, 10)
        loja_armamentos_itens.append(robe_algodao)

        botas_couro = equipamentos.BotasCouro(3, 8)
        loja_armamentos_itens.append(botas_couro)

        # Consumíveis
        bomba_inferior = consumiveis.BombaInferior(2, 6)
        loja_armamentos_itens.append(bomba_inferior)

        bomba_grudenta_inferior = consumiveis.BombaGrudentaInferior(2, 8)
        loja_armamentos_itens.append(bomba_grudenta_inferior)

        # Armazenando os itens das lojas
        lojas_itens = [loja_pocoes_itens, loja_armamentos_itens]

        super(Area_1, self).__init__("Planície de Slimes", lojas_itens, estalagem_preco)

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
        # Slime de Mel

        # Slime de Mel no nível do jogador: 5% de chance de ser encontrado
        if random.randint(1, 100) <= 5:
            inimigo = slime_mel.SlimeMel(jogador.nivel)
            inimigos.append(inimigo)
            peso_restante -= 3

        while peso_restante > 0:
            indice = random.randint(1, 10)

            # 10 é o número máximo de inimigos que o jogador irá enfrentar de uma vez
            if len(inimigos) >= 10:
                break

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
            elif indice == 7 and peso_restante >= 3 and jogador.nivel > 1:
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

    def MenuVila(self, jogador, conf):
        """
        Menu referente ao que o jogador pode fazer quando está presente na vila/cidade da área.
        """

        # Jogador vai até a vila pela primeira vez
        if self.conhece_vila == False:
            utils.ImprimirComDelay('A procura pela vila mais próxima não demorou tanto, afinal de contas você está ' +
                'em uma planície. Você chutaria que esta vila tem umas poucas centenas de habitantes,\ne devido ao ' +
                'baixo perigo oferecido pelos monstros da região, os habitantes da vila estão seguros.', conf.npc_fala_delay)
            utils.ImprimirComDelay(" 'Bem-Vindo à Vila Pwikutt', diz uma placa de metal situada na\nentrada da vila. " +
                'Os habitantes são bem-educados e pareçem estar acostumados com a chegada de aventureiros. Dando uma ' +
                'pequena volta pela vila, uma loja de armamentos,\numa loja de poções e uma estalagem são os locais ' +
                'que lhe chamaram a atenção.\n', conf.npc_fala_delay)
            self.conhece_vila = True
        
        # Vezes subsequentes
        else:
            utils.ImprimirComDelay('Você chega na Vila Pwikutt.\n', conf.npc_fala_delay)

        retorno = 1
        
        while True:
            if retorno == 1:
                print('\n[1] Ir até a Loja de Poções')
                print('[2] Ir até a Loja de Armamentos')
                print('[3] Ir até a Estalagem')

                print('\n[0] Voltar a Explorar')

                retorno = 0
            
            op = utils.LerNumeroIntervalo('> ', 0, 3)

            if op == 0:
                print('Você retorna até a Planície para continuar explorando.')
                break

            if op == 1:

                if self.conhece_vendedor_pocoes == False:
                    if jogador.genero == 'M':
                        utils.ImprimirComDelay('???: Olá! Você deve ser novo por aqui.\n', conf.npc_fala_delay)
                    elif jogador.genero == 'F':
                        utils.ImprimirComDelay('???: Olá! Você deve ser nova por aqui.\n', conf.npc_fala_delay)

                    utils.ImprimirComDelay('???: Me chamo Maelia, sou a dona dessa loja de poções.\n', conf.npc_fala_delay)
                    utils.ImprimirComDelay('Maelia: É melhor dar uma estocada em algumas poções, elas podem salvar a ' +
                        'sua vida em situações perigosas!\n', conf.npc_fala_delay)
                    
                    self.conhece_vendedor_pocoes = True
                
                else:
                    utils.ImprimirComDelay(f'Maelia: Olá, {jogador.nome}! Veio se prevenir com algumas das minhas ' +
                        'poções?\n', conf.npc_fala_delay)

                self.Loja(jogador, self.lojas_itens[0])

                utils.ImprimirComDelay(f'Maelia: Até mais, {jogador.nome}! Volte sempre!\n', conf.npc_fala_delay)

                retorno = 1
            
            elif op == 2:

                if self.conhece_vendedor_armamentos == False:
                    if jogador.genero == 'M':
                        utils.ImprimirComDelay('???: Eaí rapaz, como vai essa vida de aventureiro novato?\n', conf.npc_fala_delay)
                        utils.ImprimirComDelay(f'{jogador.nome}: Como sabe que eu sou um aventureiro novato?\n', conf.npc_fala_delay)
                        utils.ImprimirComDelay('???: Só um novato se aventura com esse nível de equipamento que cê tá usando. Hahahaha!\n', conf.npc_fala_delay)
                        utils.ImprimirComDelay('???: Me chamo Scolf, rapaz! Prazer em conhecer ocê.\n', conf.npc_fala_delay)
                        
                    elif jogador.genero == 'F':
                        utils.ImprimirComDelay('???: Eaí moça, como vai essa vida de aventureira novata?\n', conf.npc_fala_delay)
                        utils.ImprimirComDelay(f'{jogador.nome}: Como sabe que eu sou uma aventureira novata?\n', conf.npc_fala_delay)
                        utils.ImprimirComDelay('???: Só uma novata se aventura com esse nível de equipamento que cê tá usando. Hahahaha!\n', conf.npc_fala_delay)
                        utils.ImprimirComDelay('???: Me chamo Scolf, moça! Prazer em conhecer ocê.\n', conf.npc_fala_delay)
                    
                    utils.ImprimirComDelay('Scolf: Fica a vontade aí na minha loja, se precisar é só me chamar.\n', conf.npc_fala_delay)
                    self.conhece_vendedor_armamentos = True
                
                else:
                    if jogador.genero == 'M':
                        utils.ImprimirComDelay(f'Scolf: Eaí rapaz! Vamo comprar uns equipamento novo?\n', conf.npc_fala_delay)
                    elif jogador.genero == 'F':
                        utils.ImprimirComDelay(f'Scolf: Eaí moça! Vamo comprar uns equipamento novo?\n', conf.npc_fala_delay)

                self.Loja(jogador, self.lojas_itens[1])

                utils.ImprimirComDelay(f'Scolf: Té mais, {jogador.nome}!\n', conf.npc_fala_delay)

                retorno = 1
            
            elif op == 3:

                if self.conhece_estalagem == False:
                    if jogador.genero == 'M':
                        utils.ImprimirComDelay('???: Olá aventureiro! Cansado da viagem né?\n', conf.npc_fala_delay)
                    elif jogador.genero == 'F':
                        utils.ImprimirComDelay('???: Olá aventureira! Cansada da viagem né?\n', conf.npc_fala_delay)

                    utils.ImprimirComDelay('???: Meu nome é Ruwick Pwikutt, bisneto do velho Pwikutt, fundador desta ' +
                        'vila. E claro, atual dono desta estalagem.\n', conf.npc_fala_delay)
                    utils.ImprimirComDelay('Ruwick: Descansar aqui vai recuperar suas energias por completo. E isso ' +
                        'inclui sua magia também! Seus fluxos de mana vão estar novinhos em folha!\n', conf.npc_fala_delay)
                    
                    self.conhece_estalagem = True
                
                else:
                    if jogador.genero == 'M':
                        utils.ImprimirComDelay(f'Ruwick: Cansado da viagem, {jogador.nome}? Faça uma pausa!\n', conf.npc_fala_delay)
                    elif jogador.genero == 'F':
                        utils.ImprimirComDelay(f'Ruwick: Cansada da viagem, {jogador.nome}? Faça uma pausa!\n', conf.npc_fala_delay)

                self.Estalagem(jogador, conf)

                utils.ImprimirComDelay(f'Ruwick: Boa sorte em sua aventura, {jogador.nome}!\n', conf.npc_fala_delay)

                retorno = 1

        utils.ImprimirComDelay('', conf.npc_fala_delay)

    def Estalagem(self, jogador, conf):
        """
        Menu principal de uma estalagem presente na área.
        """

        print('')

        if jogador.ouro >= self.estalagem_preco:
            print('[1] Descansar na estalagem: ' + Fore.YELLOW + 'Preço' + Style.RESET_ALL + f': {self.estalagem_preco}')
        else:
            print(Fore.RED + f'[1] Descansar na estalagem: Preço: {self.estalagem_preco}' + Style.RESET_ALL)
        print('[0] Sair da estalagem\n')
        
        op = utils.LerNumeroIntervalo('> ', 0, 1)

        # Jogador decide descansar na estalagem
        if op == 1:

            # Jogador está com vida e mana maximizados
            if jogador.hp == jogador.maxHp and jogador.mana == jogador.maxMana:
                utils.ImprimirComDelay(f'Ruwick: Pareçe que você já está descansado! Permitir sua estadia aqui ' + 
                    'seria um roubo do seu ', conf.npc_fala_delay)
                print(Fore.YELLOW, end = '')
                utils.ImprimirComDelay('ouro', conf.npc_fala_delay)
                print(Style.RESET_ALL, end = '')
                utils.ImprimirComDelay('!\n', conf.npc_fala_delay)

            # Jogador descansa na estalagem
            elif jogador.ouro >= self.estalagem_preco:
                jogador.ouro -= self.estalagem_preco
                jogador.hp = jogador.maxHp
                jogador.mana = jogador.maxMana

                print(f'Você gastou {self.estalagem_preco} de ' + Fore.YELLOW + 'ouro' + Style.RESET_ALL + ' e \
                    recuperou seu ' + Fore.RED + 'HP' + Style.RESET_ALL + ' e ' + Fore.BLUE + 'Mana' + Style.RESET_ALL
                    + ' completamente.')

            # Jogador não tem ouro suficiente pra descansar na estalagem
            elif op == 1:
                utils.ImprimirComDelay(f'Ruwick: Desculpe, mas pareçe que você não tem ', conf.npc_fala_delay)
                print(Fore.YELLOW, end = '')
                utils.ImprimirComDelay('ouro', conf.npc_fala_delay)
                print(Style.RESET_ALL, end = '')
                utils.ImprimirComDelay(f' o suficiente para descansar aqui.\n', conf.npc_fala_delay)
