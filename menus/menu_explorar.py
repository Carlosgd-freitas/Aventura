import os
import sys

from . import creditos

sys.path.append("..")
from base.jogador import ReconhecerAcaoBasica
from base import configuracao, saver, imprimir, utils, cor
from combate import batalha
from areas import eventos

def MenuExplorar(jogador, area, est, conf, caminhos, pre_selecionado = None):
    """
    Emula a exploração de uma área pelo jogador. Retorna -1 quando o jogador perde o jogo.

    Parâmetros:
    - jogador: objeto do jogador;
    - area: area em que o jogador está;
    - est: estatísticas relacionadas ao jogador e ao jogo;
    - conf: configurações do usuário relativas ao jogo;
    - caminhos: caminho relativo a pasta que contém os saves;
    
    Parâmetros opcionais:
    - pre_selecionado: caso não seja None, a lista de ações não será impressa e ação que possuir o mesmo índice [X]
    será escolhida e executada. O Valor padrão é None.
    """

    chance_descanso = 0
    chance_vendedor_ambulante = 0
    explorar_flag = 0
    retorno = 1

    while True:

        # Opção pré-selecionada
        if pre_selecionado is not None:
            retorno = 0

        # Imprimindo as ações que o jogador pode tomar
        if retorno == 1:
            imprimir.ImprimirLocal(area.nome)
            print('Escolha sua Ação:')
            conf.ImprimirAcoes()

            print('\n[1] Explorar')

            if area.nome == "Planície de Slimes":
                if area.conhece_vila == False:
                    print('[2] Encontrar a vila mais próxima')
                elif area.conhece_vila == True:
                    print('[2] Ir até a Vila Pwikutt')
            
                print('[3] Ir em direção à Floresta\n')

            print('[0] Sair do Jogo\n')
            
            retorno = 0

        # Opção pré-selecionada
        if pre_selecionado is not None:
            op = pre_selecionado

        # Jogador digita sua ação
        else:
            op = input('> ')
            if op.isdecimal():
                op = int(op)

        # Status, Inventário, Habilidades, Equipamentos
        if ReconhecerAcaoBasica(op, jogador, conf, est):
            retorno = 1
        
        # Salvar o Jogo
        elif configuracao.CompararAcao(op, conf.tecla_salvar_jogo):
            print('')
            saver.Salvar(caminhos['saves'], jogador, est, area, area.nome)
            retorno = 1

        # Sair do Jogo
        elif op == 0:
            if conf.confirmacao_sair:
                print('\nDeseja sair do jogo?')
                print('[0] Não, retornar ao jogo.')
                print('[1] Sim, fechar o jogo.')

                sair = utils.LerNumeroIntervalo('> ', 0, 1)

                if sair == 0:
                    retorno = 1
                else:
                    if conf.salvar_sair == True:
                        saver.Salvar(caminhos['saves'], jogador, est, area, area.nome)
                    os._exit(0)
            
            else:
                if conf.salvar_sair == True:
                    saver.Salvar(caminhos['saves'], jogador, est, area, area.nome)
                os._exit(0)
        
        # Explorar a Área
        elif op == 1:

            explorar_flag = 0
            
            # Evento: Descanso
            if explorar_flag == 0 and utils.CalcularChance(chance_descanso / 100) and \
                (jogador.hp < jogador.maxHp or jogador.mana < jogador.maxMana):

                resultado = eventos.EventoDescanso(jogador, area)
                chance_descanso = 0
                explorar_flag = 1

                batalha.ProcessarResultado(resultado, jogador, est)
                if resultado == -1:
                    return -1

            elif explorar_flag == 0 and (jogador.hp < jogador.maxHp or jogador.mana < jogador.maxMana):
                chance_descanso += 5
            
            # Evento: Vendedor Ambulante
            if explorar_flag == 0 and utils.CalcularChance(chance_vendedor_ambulante / 100):
                operacao_realizada = area.EventoVendedorAmbulante(jogador, conf)
                chance_vendedor_ambulante = 0
                explorar_flag = 1

            elif explorar_flag == 0:
                chance_descanso += 5

            # Batalha
            if explorar_flag == 0:
                print('Uma batalha se iniciou!')

                inimigos = area.RetornarEncontro(jogador)
                aliados = [jogador]
                resultado = batalha.BatalhaPrincipal(aliados, inimigos)

                batalha.ProcessarResultado(resultado, jogador, est)
                if resultado == -1:
                    return -1

            retorno = 1
        
        # Ir até a Vila/Cidade
        elif op == 2:
            if pre_selecionado is None:
                print('')

                # Chance de 5% do jogador ser emboscado
                chance_emboscada = 5.00
                if utils.CalcularChance(chance_emboscada / 100):
                    inimigos = area.RetornarEncontro(jogador)
                    aliados = [jogador]
                    resultado = batalha.BatalhaPrincipal(aliados, inimigos, emboscada = 1)
                
                    batalha.ProcessarResultado(resultado, jogador, est)
                    if resultado == -1:
                        return -1

                area.MenuVila(jogador, est, conf, caminhos)

            else:
                area.MenuVila(jogador, est, conf, caminhos, True)

            retorno = 1

        # Ir em direção à Floresta
        elif op == 3:
            print('')
            resultado = area.EncontroChefe(jogador, est, conf)

            # Chefão derrotado
            if resultado == 1 and area.chefao_derrotado == True:
                est.ContabilizarTempoJogado()

                imprimir.ImprimirComDelay('\nVocê chegou ao final desta versão do jogo, parabéns! Você agora será '+
                'retornado ao menu de exploração, com sua vida e mana maximizadas,\ne pode continuar jogando. O ' +
                'chefão também estará vivo novamente, se quiser enfrentá-lo.\n\n', conf.npc_fala_delay)

                creditos.creditos()

                tempo_finalizado = imprimir.FormatarTempo(est.tempo_total_jogado)
                imprimir.ImprimirComDelay(f'\nJogo finalizado em: {cor.colorir(tempo_finalizado, frente_claro=True)}',
                    conf.npc_fala_delay)

                jogador.hp = jogador.maxHp
                jogador.mana = jogador.maxMana

                input('\n\nAperte [ENTER] para continuar.')
                print('')

                retorno = 1
            
            # Jogador decidiu não enfrentar o chefão
            elif area.chefao_derrotado == False and resultado == 1:
                retorno = 1
            
            # Jogador morreu para o chefão
            elif resultado == -1:
                return -1
        
        pre_selecionado = None
