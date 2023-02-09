import sys
from colorama import Fore, Back, Style

from . import jogador_acoes, mecanicas, usar_habilidade
sys.path.append("..")
from base import efeito, imprimir, utils
from menus import menu_equipamentos

def BatalhaPrincipal(aliados, inimigos, emboscada = 0, conf = None, correr = True, chefao = 0):
    """
    Recebe uma lista de aliados, onde a primeira posição da lista é o jogador, e uma lista de inimigos, e
    emula uma batalha. Retorna:
    * -1, se o jogador perdeu
    *  1, se o jogador venceu
    *  2, se o jogador escapou da batalha
    """
    
    # -1 -> o jogador perdeu
    #  0 -> a batalha continua
    #  1 -> o jogador venceu
    #  2 -> o jogador escapou da batalha
    acabou = 0

    turno = 1
    espolios = []
    jogador = aliados[0]

    # Garantindo nomes únicos
    nomes = {}
    nomes_zerados = {}
    nomes, nomes_zerados = utils.ContarNomes(nomes, nomes_zerados, aliados)
    nomes, nomes_zerados = utils.ContarNomes(nomes, nomes_zerados, inimigos)
    utils.NomesUnicos(nomes, nomes_zerados, aliados, inimigos)

    # Ativando certas habilidades no início da batalha
    for c in aliados:
        mecanicas.InicioBatalha(c)
    for c in inimigos:
        mecanicas.InicioBatalha(c)

    while acabou == 0:

        if jogador.hp <= 0:
            acabou = -1
            break

        elif len(inimigos) == 0:
            acabou = 1
            break

        else:
            ordem = []
            
            # A ordem dos turnos é atualizada normalmente
            if emboscada == 0:
                for c in aliados:
                    ordem.append(c)
                for c in inimigos:
                    ordem.append(c)
                ordem.sort(key = lambda x: x.velocidade, reverse = True)
            
            # Jogador sofreu uma emboscada e age por último no primeiro turno
            else:

                if jogador.genero == "M":
                    print('Você foi emboscado!')
                elif jogador.genero == "F":
                    print('Você foi emboscada!')

                for c in inimigos:
                    ordem.append(c)
                ordem.sort(key = lambda x: x.velocidade, reverse = True)

                aliados.sort(key = lambda x: x.velocidade, reverse = True)
                for c in aliados:
                    ordem.append(c)

                emboscada = 0
            
            # Imprimindo o índice do turno
            print('')
            print(Fore.BLACK + Back.WHITE + "> Turno " + str(turno) + " <" + Style.RESET_ALL)
            print('')

            # Caso o jogador não seja o primeiro a agir, imprime os inimigos em batalha
            if jogador != ordem[0]:
                print('\nInimigos em batalha:')
                imprimir.InimigosPresentes(inimigos)
            
            for c in ordem:

                if acabou == 0:
                    consciente = mecanicas.InicioTurno(c)
                    mecanicas.DecairBuffsDebuffs(c)
                    mecanicas.AcrescentarRecargas(c)
                    mecanicas.AbaterCriaturas(inimigos, espolios, nomes = nomes, nomes_zerados = nomes_zerados,
                        conf = conf, chefao = chefao)

                if jogador.hp <= 0:
                    acabou = -1
                    break

                # Vez do Jogador
                if c == jogador and jogador.hp > 0 and consciente == 1 and len(inimigos) > 0:
                    acabou = JogadorVez(jogador, inimigos, correr)

                    mecanicas.AbaterCriaturas(inimigos, espolios, nomes = nomes, nomes_zerados = nomes_zerados,
                        conf = conf, chefao = chefao)

                # Vez de um inimigo ou aliado
                elif c != jogador and c.hp > 0 and jogador.hp > 0 and acabou == 0 and consciente == 1:

                    morreu = 0

                    # Vez de um aliado
                    if c in aliados:
                        morreu = mecanicas.AbaterCriaturas(inimigos, espolios, c, gerar_espolios = False,
                            nomes = nomes, nomes_zerados = nomes_zerados, conf = conf, chefao = chefao)

                        if morreu == 0:
                            CriaturaVez(c, aliados, inimigos, jogador)
                    
                    # Vez de um inimigo
                    elif c in inimigos:
                        morreu = mecanicas.AbaterCriaturas(inimigos, espolios, c, nomes = nomes,
                            nomes_zerados = nomes_zerados, conf = conf, chefao = chefao)

                        if morreu == 0:
                            CriaturaVez(c, inimigos, aliados, jogador)

                # Jogador tentou escapar mas não conseguiu
                if acabou != 2:
                    acabou = 0
            
            turno += 1

    # Jogador recebe os espólios da batalha caso tenha vencido
    if acabou == 1:
        print('Você venceu!')

        # Abatendo criaturas aliadas no fim da batalha
        for c in aliados:
            if c != jogador:
                aliados.remove(c)

        print('\nEspólios:')

        if not espolios:
            print('Nenhum espólio foi ganho.')

        else:
            for e in espolios:
                if e.classificacao == "Ouro":
                    jogador.ouro += e.quantidade
                    print(f'Você ganhou {e.quantidade} de ' + Fore.YELLOW + 'ouro' + Style.RESET_ALL + '.')

                elif e.classificacao == "Experiência":
                    jogador.experiencia += e.quantidade
                    print(f'Você ganhou {e.quantidade} de experiência.')
                
                else:
                    jogador.AdicionarAoInventario(e)
                    print(f'Você ganhou {e.quantidade} {e.nome}.')
    
    if acabou == 1 or acabou == 2:
        mecanicas.TerminarBuffsDebuffs(jogador)
        mecanicas.AcrescentarRecargasMaximo(jogador)

    return acabou

def JogadorVez(jogador, inimigos, correr = True):
    """
    Controla as ações que o jogador pode fazer. A função retornará o valor 2 se o jogador tiver escapado da
    batalha com sucesso.
    """

    retorno = 1
    
    while True:
        # Estas mensagens serão impressas no início do turno do jogador e toda vez que ele quiser retornar e 
        # escolher outra ação
        if retorno == 1:

            # Imprimindo os inimigos
            print('\nInimigos em batalha:')
            imprimir.InimigosPresentes(inimigos)

            # Imprimindo o jogador
            imprimir.ImprimirJogador(jogador)

            print('\nEscolha sua Ação:')
            print('[1] Atacar')
            print('[2] Defender')
            print('[3] Consumível')
            print('[4] Habilidades')
            print('[5] Equipamentos')

            if correr == True:
                print('[6] Correr')
            elif correr == False:
                print(Fore.RED + '[6] Correr' + Style.RESET_ALL)
            
            print('')

            retorno = 0
        
        # Jogador escapou da batalha
        elif retorno == 2:
            return retorno

        op = utils.LerNumero('> ')

        # Atacar
        if op == 1:

            atacar = jogador.HabilidadePresente("Atacar")
            alvo = jogador_acoes.EscolherAlvo(inimigos)

            # Jogador não escolheu retornar 
            if alvo > 0:
                alvo -= 1
                alvos = [inimigos[alvo]]
                print('')
                danos, acertos_criticos = usar_habilidade.UsarHabilidade(jogador, alvos, atacar, verbose = False)
                usar_habilidade.ImprimirDano(jogador, alvos, atacar, danos, acertos_criticos)
                break
            
            # Jogador escolheu retornar 
            else:
                retorno = 1

        # Defender
        elif op == 2:
            defendendo = efeito.Efeito("Defendendo", 50, 1, 1, 100)
            jogador.buffs.append(defendendo)
            print('\nVocê está defendendo.')
            break

        # Usar um item consumível do inventário
        elif op == 3:
            if jogador.ContarItens("Consumível") > 0:
            
                indice = jogador_acoes.EscolherConsumivel(jogador)

                # Jogador não escolheu retornar 
                if indice != -1:
                    print('')
                    jogador_acoes.UsarConsumivel(jogador, indice, inimigos)
                    break
                
                # Jogador escolheu retornar 
                else:
                    retorno = 1

            else:
                print('Você não tem itens consumíveis para usar em batalha.')

        # Usar uma Habilidade
        elif op == 4:
            if len(jogador.habilidades) > 1:
                indice = jogador_acoes.EscolherHabilidade(jogador)

                # Jogador não escolheu retornar 
                if indice != -1:
                    habilidade = jogador.habilidades[indice]

                    # Habilidade de alvo único
                    if habilidade.alvo == "Inimigo" or habilidade.alvo == "Aliado":
                        if habilidade.alvo == "Inimigo":
                            alvo = jogador_acoes.EscolherAlvo(inimigos)
                        # else:
                        #    alvo = jogador_acoes.EscolherAlvo([jogador, aliados])

                        # Jogador não escolheu retornar 
                        if alvo > 0:
                            alvo -= 1
                            alvos = [inimigos[alvo]]
                            print('')
                            danos, acertos_criticos = usar_habilidade.UsarHabilidade(jogador, alvos, habilidade)
                            usar_habilidade.ImprimirDano(jogador, alvos, habilidade, danos, acertos_criticos)
                            break
                        
                        # Jogador escolheu retornar 
                        else:
                            retorno = 1
                    
                    else:

                        # Habilidade que alveja a si próprio
                        if habilidade.alvo == "Próprio":
                            alvos = [jogador]

                        # Habilidade de alvos múltiplos
                        elif habilidade.alvo == "Inimigos" or habilidade.alvo == "Aliados":
                            if habilidade.alvo == "Inimigos":
                                alvos = inimigos
                            # else:
                            #    alvos = [jogador, aliados]

                        print('')
                        danos, acertos_criticos = usar_habilidade.UsarHabilidade(jogador, alvos, habilidade)
                        usar_habilidade.ImprimirDano(jogador, alvos, habilidade, danos, acertos_criticos)
                        break
                
                # Jogador escolheu retornar
                else:
                    retorno = 1

            else:
                print('Você não tem habilidades.')
        
        # Trocar Equipamentos
        elif op == 5:
            print('')
            troca = menu_equipamentos.MenuEquipamentos(jogador)

            # Nenhuma troca de equipamento realizada: jogador escolheu retornar
            if troca == 0:
                retorno = 1

            # Troca de equipamento realizada
            else:
                break

        # Correr
        elif op == 6:

            # Jogador não pode correr da batalha
            if correr == False:
                print('Você não pode correr desta batalha.')
                retorno = 1
            
            else:
                # Criatura de maior nível
                maior_nivel = 0
                for c in inimigos:
                    if c.nivel > maior_nivel:
                        maior_nivel = c.nivel
                
                # Calculando a chance de correr do combate
                chance_correr = 50
                if jogador.nivel > maior_nivel:
                    chance_correr += (jogador.nivel - maior_nivel) * 10
                
                else:
                    chance_correr -= (maior_nivel - jogador.nivel) * 10
                
                # Impedindo o extrapolamento da chance de correr
                if chance_correr > 100:
                    chance_correr = 100
                elif chance_correr < 0:
                    chance_correr = 0
                
                # Escolha do jogador
                print(f'Você tem {chance_correr}% de chance de correr dessa batalha. Prosseguir?')
                print('[0] Não, voltar ao combate.')
                print('[1] Sim, tentar escapar.\n')

                while True:
                    escolha = utils.LerNumero('> ')

                    if escolha == 0 or escolha == 1:
                        break

                # Jogador decidiu não escapar
                if escolha == 0:
                    retorno = 1
                
                # Jogador decidiu escapar
                elif escolha == 1:

                    if utils.CalcularChance(chance_correr / 100):
                        print('\nVocê conseguiu escapar da batalha.')
                        retorno = 2
                    
                    else:
                        print('\nVocê não conseguiu escapar da batalha.')
                        retorno = 3
                        break

def CriaturaVez(criatura, aliados, inimigos, jogador):
    """
    Controla as ações que uma criatura não-controlável pelo jogador pode fazer.

    Parâmetros:
    * criatura: criatura cuja ação será controlada;
    * aliados: aliados da criatura em questão;
    * inimigos: inimigos da criatura em questão;
    * jogador: objeto do jogador.
    """

    # acao será uma tupla: (tipo da ação, habilidade que será usada, alvo(s) da habilidade)
    acao = criatura.EscolherAcao(aliados, inimigos, jogador)
    habilidade = acao[1]

    # Ataque normal
    if acao[0] == "atacar":
        alvos = [acao[2]]
        danos, acertos_criticos = usar_habilidade.UsarHabilidade(criatura, alvos, habilidade, verbose = False)
        usar_habilidade.ImprimirDano(criatura, alvos, habilidade, danos, acertos_criticos)
    
    # Usando uma Habilidade
    elif acao[0] == "habilidade":

        # Habilidade de alvo único
        if acao[1].alvo == "Inimigo" or acao[1].alvo == "Aliado":
            alvos = [acao[2]]

        # Habilidade que alveja a si próprio
        elif acao[1].alvo == "Próprio":
            alvos = [criatura]

        # Habilidade de alvos múltiplos
        elif acao[1].alvo == "Inimigos" or acao[1].alvo == "Aliados":
            alvos = acao[2]

        danos, acertos_criticos = usar_habilidade.UsarHabilidade(criatura, alvos, habilidade)
        usar_habilidade.ImprimirDano(criatura, alvos, habilidade, danos, acertos_criticos)

    # Passou o turno
    elif acao[0] == "passar":
        print(acao[1])

    # Correu da batalha
    elif acao[0] == "correr":
        print(acao[1])
        aliados.remove(criatura)

def ProcessarResultado(resultado, jogador, est, chefao = False):
    """
    Tenta subir o jogador de nível caso ele tenha ganhado uma batalha e imprime a mensagem de Game Over caso ele
    tenha perdido.

    Parâmetros:
    - resultado: inteiro indicando o resultado de uma batalha;
    - jogador: objeto do jogador;
    - est: estatísticas relacionadas ao jogador e ao jogo.

    Parâmetros Opcionais:
    - chefao: Se igual a True, a mensagem padrão de vitória não será impressa. O valor padrão é False.
    """

    if resultado == 1:
        subiu = jogador.SubirNivel()
        est.batalhas_ganhas += 1
        if not chefao:
            print('\nVocê retoma seu fôlego e segue em sua Aventura.')

    elif resultado == -1:
        print('\nO último ataque foi grave demais. Sua consciência vai se esvaindo e você colapsa no chão.')
        print("     _____                                ____                         ")
        print("    / ____|                              / __ \                        ")
        print("   | |  __    __ _   _ __ ___     ___   | |  | | __   __  ___   _ __   ")
        print("   | | |_ |  / _` | | '_ ` _ \   / _ \  | |  | | \ \ / / / _ \ | '__|  ")
        print("   | |__| | | (_| | | | | | | | |  __/  | |__| |  \ V / |  __/ | |     ")
        print("    \_____|  \__,_| |_| |_| |_|  \___|   \____/    \_/   \___| |_|     ")                                                            
        input('\nPressione [ENTER] para retornar ao menu principal.')
        print('')
