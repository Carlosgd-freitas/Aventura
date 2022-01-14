import os
import random
import sys
from colorama import Fore, Back, Style

from . import jogador_acoes, utils
sys.path.append("..")
from classes_base import efeito

def BatalhaPrinicipal(jogador, criaturas):
    """
    Recebe o jogador e uma lista de criatuas e emula uma batalha.
    """
    
    # -1 -> o jogador perdeu
    #  0 -> a batalha continua
    #  1 -> o jogador venceu
    #  2 -> o jogador escapou da batalha
    acabou = 0

    while acabou == 0:

        # A ordem dos turnos é atualizada no começo
        ordem = [jogador]
        for c in criaturas:
            ordem.append(c)
        ordem.sort(key = lambda x: x.velocidade)

        # Acrescenta a recarga das habilidades de todos em combate
        for c in ordem:
            utils.AcrescentarRecargas(c)
            utils.DecairBuffsDebuffs(c)

        if jogador.hp <= 0:
            acabou = -1

        elif len(criaturas) == 0:
            acabou = 1

        else:
            for c in ordem:
                # Vez do Jogador
                if c == jogador and jogador.hp > 0:
                    utils.InicioTurno(jogador)
                    acabou = JogadorVez(jogador, criaturas)
                    utils.AbaterCriaturas(criaturas)

                # Vez da Criatura
                elif c.hp > 0 and jogador.hp > 0 and acabou != 2:
                    utils.InicioTurno(c)
                    acao = c.EscolherAcao()

                    # Ataque normal
                    if acao[0] == "atacar":
                        dano = utils.CalcularDano(c, jogador, acao[1])
                        jogador.hp -= dano
                        print(f'{c.nome} te atacou e deu {dano} de dano!')
                    
                    # Usando uma Habilidade
                    elif acao[0] == "habilidade":

                        # Habilidade de alvo único
                        if acao[1].alvo == "inimigo":
                            dano = utils.UsarHabilidadeAlvoUnico(c, jogador, acao[1])
                            print(f'{c.nome} usou {acao[1].nome} e deu {dano} de dano!')

                # Jogador tentou escapar mas não conseguiu
                if acabou != 2:
                    acabou = 0

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
            print(f'\n{jogador.nome} - Classe: {jogador.classe} - ' + Fore.RED + 'HP' + Style.RESET_ALL +
            f' {jogador.hp}/{jogador.maxHp} - ' + Fore.BLUE + 'Mana' + Style.RESET_ALL +
            f' {jogador.mana}/{jogador.maxMana}')

            print('\nEscolha sua Ação:')
            print('[1] Atacar')
            print('[2] Defender')
            print('[3] Usar Consumível')
            print('[4] Habilidade')
            print('[5] Correr\n')

            retorno = 0
        
        # Jogador escapou da batalha
        elif retorno == 2:
            return retorno

        op = int(input('> '))

        ##################
        if op == 0:
            os._exit(0)
        ##################

        # Atacar
        if op == 1:
            atacar = jogador.habilidades[0]
            alvo = jogador_acoes.EscolherAlvo(criaturas)

            # Jogador não escolheu retornar 
            if alvo != -1:
                dano = utils.UsarHabilidadeAlvoUnico(jogador, criaturas[alvo], atacar)
                print(f'Você atacou e causou {dano} de dano à {criaturas[alvo].nome}.')
                break
            
            # Jogador escolheu retornar 
            else:
                retorno = 1

        # Defender
        elif op == 2:
            defendendo = efeito.Efeito("Defendendo", 50, 50, 1, 100)
            jogador.buffs.append(defendendo)
            print('Você está defendendo.')
            break

        # Usar um item consumível do inventário
        elif op == 3:

            if jogador_acoes.ContarConsumiveis(jogador.inventario) > 0:
            
                indice = jogador_acoes.EscolherConsumivel(jogador)

                # Jogador não escolheu retornar 
                if indice != -1:
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
                escolha = jogador.habilidades[indice]

                # Jogador não escolheu retornar 
                if indice != 0:

                    # Habilidade de alvo único
                    if escolha.alvo == "inimigo":
                        alvo = jogador_acoes.EscolherAlvo(criaturas)
                        dano = utils.UsarHabilidadeAlvoUnico(jogador, criaturas[alvo], escolha)
                        print(f'Você utilizou {escolha.nome} e causou {dano} de dano à {criaturas[alvo].nome}.')
                    
                    break
                
                # Jogador escolheu retornar 
                else:
                    retorno = 1

            else:
                print('Você não tem habilidades.')
        
        # Correr
        elif op == 5:

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
                escolha = int(input('> '))

                if escolha == 0 or escolha == 1:
                    break

            # Jogador decidiu não escapar
            if escolha == 0:
                retorno = 1
            
            # Jogador decidiu escapar
            elif escolha == 1:
                tentativa = random.randint(1, 100)

                if tentativa <= chance:
                    print('Você escapou da batalha com sucesso!')
                    retorno = 2
                
                else:
                    print('Você não conseguiu escapar.')
                    retorno = 3
                    break
