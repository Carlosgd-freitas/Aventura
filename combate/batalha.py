import os
import random
import sys
from colorama import Fore, Back, Style

from . import jogador_acoes, mecanicas, imprimir, usar_habilidade
sys.path.append("..")
from classes_base import efeito, utils
from menus import menu_equipamentos

def BatalhaPrinicipal(jogador, criaturas, emboscada = 0):
    """
    Recebe o jogador e uma lista de criaturas inimigas e emula uma batalha.
    """
    
    # -1 -> o jogador perdeu
    #  0 -> a batalha continua
    #  1 -> o jogador venceu
    #  2 -> o jogador escapou da batalha
    acabou = 0
    turno = 1
    espolios = []

    while acabou == 0:

        if jogador.hp <= 0:
            acabou = -1

        elif len(criaturas) == 0:
            acabou = 1

        else:
            ordem = []
            
            # A ordem dos turnos é atualizada normalmente
            if emboscada == 0:
                ordem.append(jogador)
                for c in criaturas:
                    ordem.append(c)
                ordem.sort(key = lambda x: x.velocidade)
            
            # Jogador sofreu uma emboscada e age por último no primeiro turno
            else:

                if jogador.genero == "M":
                    print('Você foi emboscado!')
                elif jogador.genero == "F":
                    print('Você foi emboscada!')

                for c in criaturas:
                    ordem.append(c)
                ordem.sort(key = lambda x: x.velocidade)
                ordem.append(jogador)

                emboscada = 0
            
            # Imprimindo o índice do turno
            print(Fore.BLACK + Back.WHITE + "> Turno " + str(turno) + " <" + Style.RESET_ALL)
            print('')

            # Imprimindo os inimigos
            print('Inimigos em batalha:')
            indice_criatura = 1
            for c in criaturas:
                imprimir.ImprimirCriatura(indice_criatura, c)
                indice_criatura += 1

            for c in ordem:
                consciente = mecanicas.InicioTurno(c)
                mecanicas.DecairBuffsDebuffs(c)
                mecanicas.AcrescentarRecargas(c)
                mecanicas.AbaterCriaturas(criaturas, espolios)

                # Vez do Jogador
                if c == jogador and jogador.hp > 0 and consciente == 1:
                    acabou = JogadorVez(jogador, criaturas)

                    mecanicas.AbaterCriaturas(criaturas, espolios)

                # Vez da Criatura
                elif c.hp > 0 and jogador.hp > 0 and acabou != 2 and consciente == 1:
                   
                    morreu = mecanicas.AbaterCriaturas(criaturas, espolios, c)

                    if morreu == 0:
                        CriaturaInimigaVez(c, jogador, criaturas)

                # Jogador tentou escapar mas não conseguiu
                if acabou != 2:
                    acabou = 0
            
            turno += 1

    # Jogador recebe os espólios da batalha caso tenha vencido
    if acabou == 1:
        print('Você venceu!')
        print('\nEspólios:')

        for e in espolios:
            if e[0] == "Ouro":
                jogador.ouro += e[1].quantidade
                print(f'Você ganhou {e[1].quantidade} de ' + Fore.YELLOW + 'ouro' + Style.RESET_ALL + '.')

            elif e[0] == "Experiencia":
                jogador.experiencia += e[1].quantidade
                print(f'Você ganhou {e[1].quantidade} de experiência.')
            
            else:
                jogador.AdicionarAoInventario(e)
                print(f'Você ganhou {e[1].quantidade} {e[1].nome}.')
        
        print('')
    
    mecanicas.TerminarBuffsDebuffs(jogador)
    mecanicas.AcrescentarRecargasMaximo(jogador)

    return acabou

def JogadorVez(jogador, criaturas):
    """
    Controla as ações que o jogador pode fazer. A função retornará o valor 2 se o jogador tiver escapado da
    batalha com sucesso.
    """

    retorno = 1
    
    while True:
        # Estas mensagens serão impressas no início do turno do jogador e toda vez que ele quiser retornar e 
        # escolher outra ação
        if retorno == 1:
            print('')
            imprimir.ImprimirJogador(jogador)

            print('\nEscolha sua Ação:')
            print('[1] Atacar')
            print('[2] Defender')
            print('[3] Consumível')
            print('[4] Habilidades')
            print('[5] Equipamentos')
            print('[6] Correr\n')

            retorno = 0
        
        # Jogador escapou da batalha
        elif retorno == 2:
            return retorno

        op = utils.LerNumero('> ')

        # Atacar
        if op == 1:
            atacar = jogador.habilidades[0]
            alvo = jogador_acoes.EscolherAlvo(criaturas)

            # Jogador não escolheu retornar 
            if alvo != -1:
                print('')
                dano = usar_habilidade.AlvoUnico(jogador, criaturas[alvo], atacar)

                if criaturas[alvo].singular_plural == "singular":
                    if criaturas[alvo].genero == "M":
                        print(f'Você atacou e causou {dano} de dano ao {criaturas[alvo].nome}.')
                    elif criaturas[alvo].genero == "F":
                        print(f'Você atacou e causou {dano} de dano à {criaturas[alvo].nome}.')

                elif criaturas[alvo].singular_plural == "plural":
                    if criaturas[alvo].genero == "M":
                        print(f'Você atacou e causou {dano} de dano aos {criaturas[alvo].nome}.')
                    elif criaturas[alvo].genero == "F":
                        print(f'Você atacou e causou {dano} de dano às {criaturas[alvo].nome}.')

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
            if jogador.ContarItens("Consumivel") > 0:
            
                indice = jogador_acoes.EscolherConsumivel(jogador)

                # Jogador não escolheu retornar 
                if indice != -1:
                    print('')
                    jogador_acoes.UsarConsumivel(jogador, indice, criaturas)
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

                    escolha = jogador.habilidades[indice]

                    # Habilidade de alvo único
                    if escolha.alvo == "inimigo":
                        alvo = jogador_acoes.EscolherAlvo(criaturas)
                        print(f'\nVocê utilizou {escolha.nome}.')
                        dano = usar_habilidade.AlvoUnico(jogador, criaturas[alvo], escolha)

                        if criaturas[alvo].singular_plural == "singular":
                            if criaturas[alvo].genero == "M":
                                print(f'Você causou {dano} de dano ao {criaturas[alvo].nome}.')
                            elif criaturas[alvo].genero == "F":
                                print(f'Você causou {dano} de dano à {criaturas[alvo].nome}.')

                        elif criaturas[alvo].singular_plural == "plural":
                            if criaturas[alvo].genero == "M":
                                print(f'Você causou {dano} de dano aos {criaturas[alvo].nome}.')
                            elif criaturas[alvo].genero == "F":
                                print(f'Você causou {dano} de dano às {criaturas[alvo].nome}.')
                    
                    # Habilidade que alveja a si próprio
                    elif escolha.alvo == "proprio":
                        print(f'\nVocê utilizou {escolha.nome}.')
                        usar_habilidade.AlvoProprio(jogador, escolha)
                    
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
            print('')

            # Nenhuma troca de equipamento realizada: jogador escolheu retornar
            if troca == 0:
                retorno = 1

            # Troca de equipamento realizada
            else:
                break

        # Correr
        elif op == 6:
            # Criatura de maior nível
            maior_nivel = 0
            for c in criaturas:
                if c.nivel > maior_nivel:
                    maior_nivel = c.nivel
            
            # Calculando a chance de escapar do combate
            chance = 50
            if jogador.nivel > maior_nivel:
                chance += (jogador.nivel - maior_nivel) * 10
            
            else:
                chance -= (maior_nivel - jogador.nivel) * 10
            
            # Impedindo o extrapolamento da chance de correr
            if chance > 100:
                chance = 100
            elif chance < 0:
                chance = 0
            
            # Escolha do jogador
            print(f'Você tem {chance}% de chance de correr dessa batalha. Prosseguir?')
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
                tentativa = random.randint(1, 100)

                if tentativa <= chance:
                    print('\nVocê conseguiu escapar da batalha.')
                    retorno = 2
                
                else:
                    print('\nVocê não conseguiu escapar da batalha.')
                    retorno = 3
                    break

def CriaturaInimigaVez(criatura, jogador, criaturas):
    """
    Controla as ações que a criatura pode fazer.
    """
    acao = criatura.EscolherAcao(jogador)

    # Ataque normal
    if acao[0] == "atacar":
        dano = usar_habilidade.AlvoUnico(criatura, jogador, acao[1])
        print(f'{criatura.nome} te atacou e deu {dano} de dano!')
    
    # Usando uma Habilidade
    elif acao[0] == "habilidade":

        # Habilidade de alvo único
        if acao[1].alvo == "inimigo":
            print(f'{criatura.nome} usou {acao[1].nome}!')
            dano = usar_habilidade.AlvoUnico(criatura, jogador, acao[1])
            print(f'Você recebeu {dano} de dano.')
        
        # Habilidade que alveja a si próprio
        if acao[1].alvo == "proprio":
            print(f'{criatura.nome} usou {acao[1].nome}!')
            usar_habilidade.AlvoProprio(criatura, acao[1])

    # Passou o turno
    elif acao[0] == "passar":
        print(acao[1])
        