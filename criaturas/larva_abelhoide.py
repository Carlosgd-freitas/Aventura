import random
import sys

sys.path.append("..")
from base import criatura
from habilidades import ativas_alvo_unico
from itens import espolios

class LarvaAbelhoide(criatura.Criatura):
    """
    Classe para a criatura Larva de Abelhóide.
    """

    def __init__(self, nivel):
        """
        Cria e retorna uma Larva de Abelhóide de um determinado nível.
        """
        # Atributos base da criatura
        maxHp = 1
        maxMana = 0
        ataque = 0
        defesa = 0
        magia = 0
        velocidade = 1
        experiencia = 1
        ouro = 1
        chance_critico = 0.0
        multiplicador_critico = 1.5

        # Aumentado os atributos por nivel
        i = 1
        while i <= nivel:
            maxHp += 1
            ataque += 1
            magia += 1

            # A cada 2 níveis
            if i % 2 == 0:
                experiencia += 1
                ouro += 1
            
            i += 1

        # Habilidades da Criatura
        habilidades = []
        atacar = ativas_alvo_unico.Atacar("Normal")
        habilidades.append(atacar)

        # Espolios da Criatura
        grana = espolios.Ouro(ouro)

        esp = [(100, grana)]

        # Criando a Criatura
        super(LarvaAbelhoide, self).__init__([], [], habilidades, esp, "Larva de Abelhóide", tipo = "Normal",
            maxHp = maxHp, hp = maxHp, maxMana = maxMana, mana = maxMana, ataque = ataque, defesa = defesa,
            magia = magia, velocidade = velocidade, nivel = nivel, experiencia = experiencia,
            singular_plural = "singular", genero = "F", chance_critico = chance_critico,
            multiplicador_critico = multiplicador_critico,
            descricao = "Ainda em seu estágio inicial, uma larva de abelhóide só busca se alimentar para se " +
            "desenvolver e posteriormente servir à colméia.")

    def EscolherAcao(self, aliados, inimigos, jogador):
        """
        Qual ação a criatura irá tomar.
        """
        alvo_inimigo = random.choice(inimigos)

        # Atacar
        return ("atacar", self.habilidades[0], alvo_inimigo)
        