import sys
import math
from colorama import Fore, Back, Style

sys.path.append("..")
from base import utils
from combate import batalha

def EventoDescanso(jogador, area):
    """
    Ofereçe 2 opções ao jogador:
    * Ter chance de ser atacado e recuperar parte do HP e Mana;
    * Ignorar o evento.

    A função retorna:
    * -1, caso o jogador tenha escolhido a primeira opção, sofrido uma emboscada e perdido a batalha;
    * 2, caso o jogador tenha escolhido a primeira opção, sofrido uma emboscada e fugido da batalha.
    * 1, caso contrário.
    """

    print('\nApós alguns bons minutos sem ser atacado, você teve a idéia de descansar e recuperar suas' +
    ' energias. Você pode fazer uma clareira por onde você se encontra, \nse recuperando parcialmente mas' +
    ' com chance de ser emboscado por criaturas inimigas se ficar distraído. Também dá pra só ignorar esse' +
    ' pensamento e continuar\nbatalhando. O que você escolhe?\n')

    resultado = 1

    # Chance de sofrer emboscada ao escolher a clareira
    porcentagem_hp = (jogador.hp / jogador.maxHp) * 100
    porcentagem_mana = (jogador.mana / jogador.maxMana) * 100
    porcentagem_media = (porcentagem_hp + porcentagem_mana) / 2
    chance_emboscada = 100 - porcentagem_media

    # Impedindo valores absurdos e colocando uma chance mínima de emboscagem (25%)
    if chance_emboscada < 25.00:
        chance_emboscada = 25.00
    elif chance_emboscada > 100.00:
        chance_emboscada = 100.00

    # Imprimindo Opções
    print('[1] Fazer uma clareira - Chance de sofrer emboscada: {:.2f}'.format(chance_emboscada) + '%')
    print('[0] Continuar batalhando\n')

    # Escolha do jogador
    while True:
        op = utils.LerNumero('> ')

        if op == 0:
            break

        # Clareira
        elif op == 1:
            # Recuperar 5 de hp ou 25% do hp máximo, o que for maior
            valor = 5
            if math.floor(jogador.maxHp * 0.25) > valor:
                valor = math.floor(jogador.maxHp * 0.25)
            jogador.hp += valor
            mensagem = f'Você recuperou {valor} de ' + Fore.RED + 'HP' + Style.RESET_ALL + '.'

            if jogador.hp >= jogador.maxHp:
                jogador.hp = jogador.maxHp
                mensagem = f'Você maximizou seu ' + Fore.RED + 'HP' + Style.RESET_ALL + '.'
            print(mensagem)

            # Recuperar 5 de mana ou 25% da mana máxima, o que for maior
            valor = 5
            if math.floor(jogador.maxMana) * 0.25 > valor:
                valor = math.floor(jogador.maxMana * 0.25)
            jogador.mana += valor
            mensagem = f'Você recuperou {valor} de ' + Fore.BLUE + 'Mana' + Style.RESET_ALL + '.'

            if jogador.mana >= jogador.maxMana:
                jogador.mana = jogador.maxMana
                mensagem = f'Você maximizou sua ' + Fore.BLUE + 'Mana' + Style.RESET_ALL + '.'
            print(mensagem)

            # Emboscada
            if utils.CalcularChance(chance_emboscada / 100):
                inimigos = area.RetornarEncontro(jogador)
                aliados = [jogador]
                resultado = batalha.BatalhaPrincipal(aliados, inimigos, emboscada = 1)
            
            break

    return resultado
