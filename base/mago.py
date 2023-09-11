import sys

from . import jogador, cor

sys.path.append("..")
from habilidades import ativas_alvo_unico, ativas_alvo_proprio, ativas_alvos_multiplos
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
    pocao_cura = consumiveis.PocaoPequenaCura(2, 2)
    inventario.append(pocao_cura)
    pocao_mana = consumiveis.PocaoPequenaMana(1, 2)
    inventario.append(pocao_mana)

    j = jogador.Jogador(nome = nome,
        classe = classe,
        nivel = nivel,
        experiencia = experiencia,
        ouro = ouro,
        maxHp = maxHp,
        hp = maxHp,
        maxMana = maxMana,
        mana = maxMana,
        ataque = ataque,
        defesa = defesa,
        magia = magia,
        velocidade = velocidade,
        habilidades = habilidades,
        equipados = equipados,
        inventario = inventario,
        receitas = [],
        singular_plural = singular_plural,
        genero = genero,
        chance_critico = chance_critico,
        multiplicador_critico = multiplicador_critico
    )

    return j

def SubirNivelMago(jogador):
    """
    Concede aumento de atributos, novas habilidades e atualiza as habilidades existentes para um jogador da classe
    Mago.
    """

    # Até o nível 5
    if jogador.nivel <= 5:

        # Aumento de atributos
        jogador.maxHp += 2
        jogador.hp = jogador.maxHp
        jogador.maxMana += 3
        jogador.mana = jogador.maxMana

        jogador.magia += 1

        if jogador.nivel == 3:
            jogador.ataque += 1

        if jogador.nivel == 5:
            jogador.defesa += 1
            jogador.velocidade += 1
        
        # Habilidades

        # Níveis 2 e 4
        if jogador.nivel % 2 == 0:
            habilidade =  jogador.HabilidadePresente("Projétil de Mana")
            custo = habilidade.RetornarCusto("Mana")
            habilidade.AlterarCusto("Mana", custo + 1)
        
        if jogador.nivel == 3:
            escudo = ativas_alvo_proprio.EscudoMagico()
            jogador.habilidades.append(escudo)

            print(f"Nova habilidade: {cor.colorir('Escudo Mágico', frente_claro=True)}.")
        
        if jogador.nivel == 4:
            habilidade =  jogador.HabilidadePresente("Escudo Mágico")
            habilidade.AlterarCusto("Mana", jogador.nivel)
        
        if jogador.nivel == 5:
            disparo = ativas_alvos_multiplos.DisparoEletrico(4)
            jogador.habilidades.append(disparo)

            print(f"Nova habilidade: {cor.colorir('Disparo Elétrico', frente_claro=True)}.")

    # Até o nível 10
    elif jogador.nivel <= 10:

        # Aumento de atributos
        jogador.maxHp += 3
        jogador.hp = jogador.maxHp
        jogador.maxMana += 5
        jogador.mana = jogador.maxMana

        jogador.magia += 1

        # Níveis 6, 8 e 10
        if jogador.nivel % 2 == 0:
            jogador.ataque += 1
        
        # Níveis 7
        if jogador.nivel == 7:
            jogador.velocidade += 1
        
        # Nível 10
        if jogador.nivel == 10:
            jogador.defesa += 1
    
        # Habilidades

        # Níveis 6, 8 e 10
        if jogador.nivel % 2 == 0:
            habilidade =  jogador.HabilidadePresente("Projétil de Mana")
            custo = habilidade.RetornarCusto("Mana")
            habilidade.AlterarCusto("Mana", custo + 1)
        
        # Níveis 7 e 9
        if jogador.nivel % 2 != 0:
            habilidade =  jogador.HabilidadePresente("Escudo Mágico")
            habilidade.AlterarCusto("Mana", jogador.nivel)
