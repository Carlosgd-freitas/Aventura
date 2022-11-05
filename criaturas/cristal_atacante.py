import random
import sys

sys.path.append("..")
from base import criatura
from habilidades import ativas_alvo_unico
from itens import espolios

class CristalAtacante(criatura.Criatura):
    """
    Classe para a criatura Cristal Atacante, que também é um chefão da primeira área.
    """

    def __init__(self, nivel, chefao = False):
        """
        Cria e retorna um Cristal Atacante de um determinado nível. Se chefao for verdadeiro, então será retornado
        o Cristal Atacante chefão da primeira área.
        """

        if chefao == True:

            # Atributos base da criatura considerando que o jogador esteja nível 5
            maxHp = 20
            maxMana = 20
            ataque = 3
            defesa = 2
            magia = 5
            velocidade = 2
            experiencia = 25
            ouro = 10
            chance_critico = 8.0
            multiplicador_critico = 1.7

            # Aumentado os atributos por nivel
            diferenca_nivel = nivel - 5
            i = 1
            while i <= diferenca_nivel:
                maxHp += 3
                maxMana += 3
                magia += 1
                experiencia += 4
                ouro += 2

                # A cada 2 níveis
                if i % 2 == 0:
                    ataque += 1

                # A cada 3 níveis
                if i % 3 == 0:
                    defesa += 1
                    velocidade += 1
                
                i += 1

            # Habilidades da Criatura
            habilidades = []
            atacar = ativas_alvo_unico.Atacar("Normal")
            habilidades.append(atacar)

            raio = ativas_alvo_unico.RaioFogo(magia, 5, 2)
            habilidades.append(raio)

            # Espolios da Criatura
            grana = espolios.Ouro(ouro)
            rubi = espolios.RubiFogo(1, 15)

            esp = [(100, grana), (100, rubi)]

        # Criando a Criatura
        super(CristalAtacante, self).__init__([], [], habilidades, esp, "Cristal Atacante", tipo = "Fogo",
            maxHp = maxHp, hp = maxHp, maxMana = maxMana, mana = maxMana, ataque = ataque, defesa = defesa,
            magia = magia, velocidade = velocidade, nivel = nivel, experiencia = experiencia,
            singular_plural = "singular", genero = "M", chance_critico = chance_critico,
            multiplicador_critico = multiplicador_critico,
            descricao = "Um cristal vermelho que flutua e possui várias inscrições rúnicas gravadas. Este tipo de " +
            "construto é especializado em utilizar magias ofensivas para atacar seus alvos, e necessita de um ótimo "+
            "conhecimento de magia para funcionar.")

    def EscolherAcao(self, aliados, inimigos, jogador):
        """
        Qual ação a criatura irá tomar.
        """
        alvo_inimigo = random.choice(inimigos)

        # Raio de Fogo -> 50% de chance de Cristal Atacante usar
        if self.mana >= 5 and super().ChecarRecarga(self.habilidades[1]):
            chance = random.randint(1, 100)
            if chance <= 50:
                return ("habilidade", self.habilidades[1], alvo_inimigo)

        # Atacar
        return ("atacar", self.habilidades[0], alvo_inimigo)
