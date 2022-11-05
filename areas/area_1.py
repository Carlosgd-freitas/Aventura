import sys
import random
from colorama import Fore, Back, Style

sys.path.append("..")
from base import area, saver, configuracao, imprimir, utils
from itens import consumiveis, equipamentos
from criaturas import slime, cobra_venenosa, slime_gigante, tortuga, ervagora, slime_mel, larry, cristal_atacante
from combate import batalha
from menus import menu_equipamentos, menu_habilidades, menu_inventario

class Area_1(area.Area):
    """
    Esta classe é utilizada para a primeira área presentes no jogo.
    """

    def __init__(self, estalagem_preco = 9999999):
        """
        Inicializador da classe.
        """

        # Flags relacionadas ao jogador e a área
        self.conhece_vila = False
        self.chefao_encontrado = False
        self.chefao_derrotado = False

        # Flags para os diálogos entre o jogador e NPCs
        self.conhece_vendedor_pocoes = False
        self.conhece_vendedor_armamentos = False
        self.conhece_estalagem = False
        self.primeira_compra_pocoes = False
        self.primeira_compra_armamentos = False

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
        bomba_inferior = consumiveis.BombaInferior(3, 6)
        loja_armamentos_itens.append(bomba_inferior)

        bomba_grudenta_inferior = consumiveis.BombaGrudentaInferior(5, 6)
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

            # 4 é o número máximo de inimigos que o jogador irá enfrentar de uma vez
            if len(inimigos) >= 4:
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
            elif indice == 8 and peso_restante >= 3 and jogador.nivel > 2:
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

    def EncontroChefe(self, jogador, conf):
        """
        Gerencia o encontro com o chefão da área.
        """

        if self.chefao_encontrado == False:
            imprimir.ImprimirComDelay('Caminhando em direção à floresta, você percebe uma coisa incomum. Um cristal ' +
            'de médio porte, vermelho, e que flutua a mais ou menos um metro do chão, está\neliminando todas as ' +
            'criaturas que chegam perto dele com um Raio de Fogo, enquanto também se move lentamente em direção a ' +
            'floresta. O cristal possui várias\ninscrições rúnicas encravadas em si, e aparenta estar danificado.\n\n', conf.npc_fala_delay)
            imprimir.ImprimirComDelay('Observando melhor, o cristal está atacando criaturas que chegam próximas à um '+
            'slime que o acompanha. Este slime possui um óculos de ourives em seu interior,\ndaqueles com várias ' +
            'lentes, que utilizam para examinar pedras preciosas, praticamente intacto. O slime percebe sua presença, ' +
            'e rapidamente se move até uma\ndistância de mais ou menos cinco metros de você. Ele aparenta saber que se ' +
            'você tentar atacá-lo, o cristal irá tentar te vaporizar, e caso não consiga, será\numa batalha 2 contra 1, ' +
            'o favorecendo de qualquer jeito.\n\n', conf.npc_fala_delay)

            self.chefao_encontrado = True

        print('Enfrentar o Slime perspicaz e o Cristal Vermelho? (Nível Recomendado: 5)')
        print('[1] Sim, enfrentá-los.')
        print('[0] Não, retornar a exploração na planície.')
        op = utils.LerNumeroIntervalo('> ', 0, 1)

        if op == 0:
            return 1
        
        elif op == 1:
            inimigos = []
            inimigo = larry.Larry(jogador.nivel)
            inimigo.nome = "Slime"
            inimigos.append(inimigo)
            inimigo = cristal_atacante.CristalAtacante(jogador.nivel, chefao = True)
            inimigos.append(inimigo)
            aliados = [jogador]
            resultado = batalha.BatalhaPrinicipal(aliados, inimigos, conf = conf, correr = False, chefao = 1)

            if resultado == 1:
                subiu = jogador.SubirNivel() # Tentativa de subir de nível
                self.chefao_derrotado = True
            
            elif resultado == -1:
                print('\nO último ataque foi grave demais. Sua consciência vai se esvaindo e você colapsa no chão.')
                print("     _____                                ____                         ")
                print("    / ____|                              / __ \                        ")
                print("   | |  __    __ _   _ __ ___     ___   | |  | | __   __  ___   _ __   ")
                print("   | | |_ |  / _` | | '_ ` _ \   / _ \  | |  | | \ \ / / / _ \ | '__|  ")
                print("   | |__| | | (_| | | | | | | | |  __/  | |__| |  \ V / |  __/ | |     ")
                print("    \_____|  \__,_| |_| |_| |_|  \___|   \____/    \_/   \___| |_|     ")                                                            
                input('\nPressione [ENTER] para retornar ao menu principal.\n')
            
            return resultado

    def MenuVila(self, jogador, conf, caminhos, save_carregado = False):
        """
        Menu referente ao que o jogador pode fazer quando está presente na vila/cidade da área.

        Parâmetros:
        - jogador: objeto do jogador;
        - conf: configurações do usuário relativas ao jogo;
        - caminhos: caminho relativo a pasta que contém os saves;

        Parâmetros opcionais:
        - save_carregado: True se um jogo que foi salvo dentro desta vila está sendo carregado e False caso
        contrário. O Valor padrão é False.;
        """

        if save_carregado == True:
            pass

        else:
            # Jogador vai até a vila pela primeira vez
            if self.conhece_vila == False:
                imprimir.ImprimirComDelay('A procura pela vila mais próxima não demorou tanto, afinal de contas você está ' +
                    'em uma planície. Você chutaria que esta vila tem umas poucas centenas de habitantes,\ne devido ao ' +
                    'baixo perigo oferecido pelos monstros da região, os habitantes da vila estão seguros.', conf.npc_fala_delay)
                imprimir.ImprimirComDelay(" 'Bem-Vindo à Vila Pwikutt', diz uma placa de metal situada na\nentrada da vila. " +
                    'Os habitantes são bem-educados e pareçem estar acostumados com a chegada de aventureiros. Dando uma ' +
                    'pequena volta pela vila, uma loja de armamentos,\numa loja de poções e uma estalagem são os locais ' +
                    'que lhe chamaram a atenção.\n', conf.npc_fala_delay)
                self.conhece_vila = True
            
            # Vezes subsequentes
            else:
                imprimir.ImprimirComDelay('Você chega na Vila Pwikutt.\n', conf.npc_fala_delay)

        save_carregado = False
        retorno = 1
        
        while True:
            if retorno == 1:
                print('\nEscolha sua Ação:')
                conf.ImprimirAcoes()

                print('\n[1] Ir até a Loja de Poções')
                print('[2] Ir até a Loja de Armamentos')
                print('[3] Ir até a Estalagem\n')

                print('[0] Voltar a Explorar\n')

                retorno = 0
            
            op = input('> ')
            if op.isdecimal():
                op = int(op)
            
            # Status do Jogador
            if configuracao.CompararAcao(op, conf.tecla_status):
                jogador.ImprimirStatus()
                retorno = 1
            
            # Inventário do Jogador
            elif configuracao.CompararAcao(op, conf.tecla_inventario):
                print('')

                if not jogador.inventario:
                    print('Você não tem itens em seu inventário.')
                else:
                    menu_inventario.MenuInventario(jogador)

                retorno = 1
            
            # Habilidades do Jogador
            elif configuracao.CompararAcao(op, conf.tecla_habilidades):
                print('')

                if len(jogador.habilidades) == 1: # Jogador só possui a habilidade "Atacar"
                    print('Você não tem habilidades.')
                else:
                    menu_habilidades.MenuHabilidades(jogador)

                retorno = 1

            # Equipamentos do Jogador
            elif configuracao.CompararAcao(op, conf.tecla_equipamentos):
                print('')
                menu_equipamentos.MenuEquipamentos(jogador)
                retorno = 1

            # Salvar o Jogo
            elif configuracao.CompararAcao(op, conf.tecla_salvar_jogo):
                print('')
                saver.Salvar(caminhos['saves'], jogador, self, "Vila Pwikutt")
                retorno = 1

            # Voltar a Explorar
            if op == 0:
                print('Você retorna até a Planície para continuar explorando.')
                break

            # Loja de Poções
            if op == 1:

                if self.conhece_vendedor_pocoes == False:
                    if jogador.genero == 'M':
                        imprimir.ImprimirComDelay('???: Olá! Você deve ser novo por aqui.\n', conf.npc_fala_delay)
                    elif jogador.genero == 'F':
                        imprimir.ImprimirComDelay('???: Olá! Você deve ser nova por aqui.\n', conf.npc_fala_delay)

                    imprimir.ImprimirComDelay('???: Me chamo Maelia, sou a dona dessa loja de poções.\n', conf.npc_fala_delay)
                    imprimir.ImprimirComDelay('Maelia: É melhor dar uma estocada em algumas poções, elas podem salvar a ' +
                        'sua vida em situações perigosas!\n', conf.npc_fala_delay)
                    
                    self.conhece_vendedor_pocoes = True
                
                else:
                    imprimir.ImprimirComDelay(f'Maelia: Olá, {jogador.nome}! Veio se prevenir com algumas das minhas ' +
                        'poções?\n', conf.npc_fala_delay)

                operacao_realizada = self.Loja(jogador, self.lojas_itens[0])

                # Primeira compra de poções realizada nesta loja
                if operacao_realizada == 1 and self.primeira_compra_pocoes == False:

                    imprimir.ImprimirComDelay('Maelia: Minhas poções vão ajudar na sua aventura, pode ter certeza!\n', conf.npc_fala_delay)
                    imprimir.ImprimirComDelay('Maelia: No entanto, você não vai conseguir agir enquanto bebe uma delas, ' +
                        'então faça isso quando tiver certeza que não vai morrer pros ataques dos seus inimigos.\n', conf.npc_fala_delay)
                    imprimir.ImprimirComDelay('Maelia: Ou quando não estiver lutando, isso também serve.\n', conf.npc_fala_delay)

                    self.primeira_compra_pocoes = True

                imprimir.ImprimirComDelay(f'Maelia: Até mais, {jogador.nome}! Volte sempre!\n', conf.npc_fala_delay)

                retorno = 1
            
            # Loja de Armamentos
            elif op == 2:

                if self.conhece_vendedor_armamentos == False:
                    if jogador.genero == 'M':
                        imprimir.ImprimirComDelay('???: Eaí rapaz, como vai essa vida de aventureiro novato?\n', conf.npc_fala_delay)
                        imprimir.ImprimirComDelay(f'{jogador.nome}: Como sabe que eu sou um aventureiro novato?\n', conf.npc_fala_delay)
                        imprimir.ImprimirComDelay('???: Só um novato se aventura com esse nível de equipamento que cê tá usando. Hahahaha!\n', conf.npc_fala_delay)
                        imprimir.ImprimirComDelay('???: Me chamo Scolf, rapaz! Prazer em conhecer ocê.\n', conf.npc_fala_delay)
                        
                    elif jogador.genero == 'F':
                        imprimir.ImprimirComDelay('???: Eaí moça, como vai essa vida de aventureira novata?\n', conf.npc_fala_delay)
                        imprimir.ImprimirComDelay(f'{jogador.nome}: Como sabe que eu sou uma aventureira novata?\n', conf.npc_fala_delay)
                        imprimir.ImprimirComDelay('???: Só uma novata se aventura com esse nível de equipamento que cê tá usando. Hahahaha!\n', conf.npc_fala_delay)
                        imprimir.ImprimirComDelay('???: Me chamo Scolf, moça! Prazer em conhecer ocê.\n', conf.npc_fala_delay)
                    
                    imprimir.ImprimirComDelay('Scolf: Fica a vontade aí na minha loja, se precisar é só me chamar.\n', conf.npc_fala_delay)
                    self.conhece_vendedor_armamentos = True
                
                else:
                    if jogador.genero == 'M':
                        imprimir.ImprimirComDelay(f'Scolf: Eaí rapaz! Vamo comprar uns equipamento novo?\n', conf.npc_fala_delay)
                    elif jogador.genero == 'F':
                        imprimir.ImprimirComDelay(f'Scolf: Eaí moça! Vamo comprar uns equipamento novo?\n', conf.npc_fala_delay)

                operacao_realizada = self.Loja(jogador, self.lojas_itens[1])

                # Primeira compra de armamentos realizada nesta loja
                if operacao_realizada == 1 and self.primeira_compra_armamentos == False:

                    if jogador.genero == 'M':
                        imprimir.ImprimirComDelay(f'Scolf: Boa escolha, rapaz.\n', conf.npc_fala_delay)
                    elif jogador.genero == 'F':
                        imprimir.ImprimirComDelay(f'Scolf: Boa escolha, moça.\n', conf.npc_fala_delay)
                    
                    imprimir.ImprimirComDelay(f'Scolf: Mas presta atenção nos níveis dos equipamento que cê comprar. ' +
                        'Cê não vai conseguir equipar se ocê tiver um nível menor que o do equipamento, ein?\n', conf.npc_fala_delay)

                    self.primeira_compra_armamentos = True

                imprimir.ImprimirComDelay(f'Scolf: Té mais, {jogador.nome}!\n', conf.npc_fala_delay)

                retorno = 1
            
            # Estalagem
            elif op == 3:

                if self.conhece_estalagem == False:
                    if jogador.genero == 'M':
                        imprimir.ImprimirComDelay('???: Olá aventureiro! Cansado da viagem né?\n', conf.npc_fala_delay)
                    elif jogador.genero == 'F':
                        imprimir.ImprimirComDelay('???: Olá aventureira! Cansada da viagem né?\n', conf.npc_fala_delay)

                    imprimir.ImprimirComDelay('???: Meu nome é Ruwick Pwikutt, bisneto do velho Pwikutt, fundador desta ' +
                        'vila. E claro, atual dono desta estalagem.\n', conf.npc_fala_delay)
                    imprimir.ImprimirComDelay('Ruwick: Descansar aqui vai recuperar suas energias por completo. E isso ' +
                        'inclui sua magia também! Seus fluxos de mana vão estar novinhos em folha!\n', conf.npc_fala_delay)
                    
                    self.conhece_estalagem = True
                
                else:
                    if jogador.genero == 'M':
                        imprimir.ImprimirComDelay(f'Ruwick: Cansado da viagem, {jogador.nome}? Faça uma pausa!\n', conf.npc_fala_delay)
                    elif jogador.genero == 'F':
                        imprimir.ImprimirComDelay(f'Ruwick: Cansada da viagem, {jogador.nome}? Faça uma pausa!\n', conf.npc_fala_delay)

                self.Estalagem(jogador, conf)

                imprimir.ImprimirComDelay(f'Ruwick: Boa sorte em sua aventura, {jogador.nome}!\n', conf.npc_fala_delay)

                retorno = 1

        imprimir.ImprimirComDelay('', conf.npc_fala_delay)

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
                imprimir.ImprimirComDelay(f'Ruwick: Pareçe que você já está descansado! Permitir sua estadia aqui ' + 
                    'seria um roubo do seu ', conf.npc_fala_delay)
                print(Fore.YELLOW, end = '')
                imprimir.ImprimirComDelay('ouro', conf.npc_fala_delay)
                print(Style.RESET_ALL, end = '')
                imprimir.ImprimirComDelay('!\n', conf.npc_fala_delay)

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
                imprimir.ImprimirComDelay(f'Ruwick: Desculpe, mas pareçe que você não tem ', conf.npc_fala_delay)
                print(Fore.YELLOW, end = '')
                imprimir.ImprimirComDelay('ouro', conf.npc_fala_delay)
                print(Style.RESET_ALL, end = '')
                imprimir.ImprimirComDelay(f' o suficiente para descansar aqui.\n', conf.npc_fala_delay)
