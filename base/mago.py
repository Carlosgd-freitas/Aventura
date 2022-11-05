import sys
from colorama import Fore, Back, Style

from . import jogador

sys.path.append("..")
from habilidades import ativas_alvo_unico, ativas_alvo_proprio
from itens import consumiveis, equipamentos

def CriarNovoMago(nome = "default", genero = "default"):
    """
    Cria um jogador de nível 1 da classe Mago.
    """

    if genero == "M":
        classe = "Mago"
    elif genero == "F":
        classe = "Maga"

    nivel = 1
    experiencia = 0
    ouro = 5

    maxHp = 35
    maxMana = 20
    ataque = 1
    defesa = 0
    magia = 1
    velocidade = 1
    chance_critico = 5.0
    multiplicador_critico = 1.2

    singular_plural = "singular"

    # Habilidades iniciais
    habilidades = []
    atacar = ativas_alvo_unico.Atacar("Normal")
    habilidades.append(atacar)
    projetil = ativas_alvo_unico.ProjetilMana()
    habilidades.append(projetil)

    # Equipamentos iniciais
    equipados = []

    # Arma de Duas mãos
    cajado = equipamentos.CajadoIniciante(1, 1)
    equipados.append(cajado)
    equipados.append(cajado)

    # Cabeça
    vazio_1 = equipamentos.Vazio()
    equipados.append(vazio_1)

    # Peitoral
    vazio_2 = equipamentos.Vazio()
    equipados.append(vazio_2)

    # Pés
    vazio_3 = equipamentos.Vazio()
    equipados.append(vazio_3)

    # Acessório
    vazio_4 = equipamentos.Vazio()
    equipados.append(vazio_4)

    # Inventário inicial
    inventario = []
    pocao = consumiveis.PocaoCuraPequena(2, 2)
    inventario.append(pocao)
    pocao_mana = consumiveis.PocaoManaPequena(1, 2)
    inventario.append(pocao_mana)

    j = jogador.Jogador(nome, classe, nivel, experiencia, ouro, maxHp, maxHp, maxMana, maxMana, ataque, defesa,
        magia, velocidade, habilidades, equipados, inventario, singular_plural, genero, chance_critico,
        multiplicador_critico)
    return j

def SubirNivelMago(jogador):
    """
    Concede aumento de atributos, novas habilidades e atualiza as habilidades existentes para um jogador da classe
    Mago.
    """

    # Aumento de atributos até o nível 5
    if jogador.nivel <= 5:
        jogador.maxHp += 2
        jogador.hp = jogador.maxHp
        jogador.maxMana += 3
        jogador.mana = jogador.maxMana

        jogador.magia += 1

        # A cada 2 níveis: Aumentando o custo do Projétil de Mana
        if jogador.nivel % 2 == 0:
            indice =  jogador.HabilidadePresente("Projétil de Mana")
            custo = jogador.habilidades[indice].RetornarCusto("Mana")
            jogador.habilidades[indice].AlterarCusto("Mana", custo + 1)

        print('Seu ' + Fore.RED + 'HP' + Style.RESET_ALL + ' máximo aumentou em 2.')
        print('Sua ' + Fore.BLUE + 'Mana' + Style.RESET_ALL + ' máxima aumentou em 3.')
        print('Sua magia aumentou em 1.')

        # No nível 3
        if jogador.nivel == 3:
            jogador.ataque += 1

            escudo = ativas_alvo_proprio.EscudoMagico()
            jogador.habilidades.append(escudo)

            print('Seu ataque aumentou em 1.')
            print('Você aprendeu uma nova habilidade: ' + Style.BRIGHT + 'Escudo Mágico' + Style.RESET_ALL + '.')
        
        # Em níveis pares maiores que 3 (4, 6, 8...): Aumentando o custo do Escudo Mágico
        if jogador.nivel > 3 and jogador.nivel % 2 == 0:
            indice =  jogador.HabilidadePresente("Escudo Mágico")
            jogador.habilidades[indice].custo = [("Mana", jogador.nivel)]

        # No nível 5
        elif jogador.nivel == 5:
            jogador.defesa += 1
            jogador.velocidade += 1

            print('Sua defesa aumentou em 1.')
            print('Sua velocidade aumentou em 1.')
