import sys
from colorama import Fore, Back, Style

from . import jogador

sys.path.append("..")
from habilidades import ativas_alvo_unico
from itens import consumiveis, equipamentos

def CriarNovoGuerreiro(nome = "default", genero = "default"):
    """
    Cria um jogador de nível 1 da classe Guerreiro.
    """

    if genero == "M":
        classe = "Guerreiro"
    elif genero == "F":
        classe = "Guerreira"

    nivel = 1
    experiencia = 0
    ouro = 5

    maxHp = 40
    maxMana = 10
    ataque = 1
    defesa = 0
    magia = 0
    velocidade = 1
    chance_critico = 5.0
    multiplicador_critico = 1.5

    singular_plural = "singular"

    # Habilidade inicial
    habilidades = []
    atacar = ativas_alvo_unico.Atacar("Normal")
    habilidades.append(atacar)

    # Equipamentos iniciais
    equipados = []

    # Arma de Uma mão
    espada = equipamentos.EspadaEnferrujada(1, 1)
    equipados.append(espada)

    # Segunda mão
    vazio_1 = equipamentos.Vazio()
    equipados.append(vazio_1)

    # Cabeça
    vazio_2 = equipamentos.Vazio()
    equipados.append(vazio_2)

    # Peitoral
    vazio_3 = equipamentos.Vazio()
    equipados.append(vazio_3)

    # Pés
    vazio_4 = equipamentos.Vazio()
    equipados.append(vazio_4)

    # Acessório
    vazio_5 = equipamentos.Vazio()
    equipados.append(vazio_5)

    # Inventário inicial
    inventario = []
    pocao = consumiveis.PocaoPequenaCura(2, 2)
    inventario.append(pocao)

    j = jogador.Jogador(nome, classe, nivel, experiencia, ouro, maxHp, maxHp, maxMana, maxMana, ataque, defesa,
        magia, velocidade, habilidades, equipados, inventario, singular_plural, genero, chance_critico,
        multiplicador_critico)
    return j

def SubirNivelGuerreiro(jogador):
    """
    Concede aumento de atributos, novas habilidades e atualiza as habilidades existentes para um jogador da classe
    Guerreiro.
    """

    # Até o nível 5
    if jogador.nivel <= 5:

        # Aumento de atributos
        jogador.maxHp += 3
        jogador.hp = jogador.maxHp
        jogador.maxMana += 2
        jogador.mana = jogador.maxMana

        jogador.ataque += 1

        print('Seu ' + Fore.RED + 'HP' + Style.RESET_ALL + ' máximo aumentou em 3.')
        print('Sua ' + Fore.BLUE + 'Mana' + Style.RESET_ALL + ' máxima aumentou em 2.')
        print('Seu ataque aumentou em 1.')

        if jogador.nivel == 3:
            jogador.magia += 1
            jogador.defesa += 1

            print('Sua magia aumentou em 1.')
            print('Sua defesa aumentou em 1.')
        
        if jogador.nivel == 5:
            jogador.velocidade += 1
            print('Sua velocidade aumentou em 1.')
        
        # Habilidades

        if jogador.nivel == 2:
            impacto = ativas_alvo_unico.ImpactoAtordoante(1, 100, "Normal", 4, 3)
            jogador.habilidades.append(impacto)

            print('Você aprendeu uma nova habilidade: ' + Style.BRIGHT + 'Impacto Atordoante' + Style.RESET_ALL + '.')
        
        if jogador.nivel == 4:
            habilidade =  jogador.HabilidadePresente("Impacto Atordoante")
            custo = habilidade.RetornarCusto("Mana")
            habilidade.AlterarCusto("Mana", custo + 1)
    
    # Até o nível 10
    elif jogador.nivel <= 10:

        # Aumento de atributos
        jogador.maxHp += 5
        jogador.hp = jogador.maxHp
        jogador.maxMana += 3
        jogador.mana = jogador.maxMana

        jogador.ataque += 1

        print('Seu ' + Fore.RED + 'HP' + Style.RESET_ALL + ' máximo aumentou em 5.')
        print('Sua ' + Fore.BLUE + 'Mana' + Style.RESET_ALL + ' máxima aumentou em 3.')
        print('Seu ataque aumentou em 1.')

        # Níveis 6, 8 e 10
        if jogador.nivel % 2 == 0:
            jogador.magia += 1
            print('Sua magia aumentou em 1.')
        
        # Níveis 6 e 9
        if jogador.nivel % 3 == 0:
            jogador.defesa += 1
            print('Sua defesa aumentou em 1.')
        
        if jogador.nivel == 10:
            jogador.velocidade += 1
            print('Sua velocidade aumentou em 1.')
        
        # Habilidades

        # Níveis 6, 8 e 10
        if jogador.nivel % 2 == 0:
            habilidade =  jogador.HabilidadePresente("Impacto Atordoante")
            custo = habilidade.RetornarCusto("Mana")
            habilidade.AlterarCusto("Mana", custo + 1)
