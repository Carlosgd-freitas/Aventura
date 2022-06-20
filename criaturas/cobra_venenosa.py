import random
import math
import sys

sys.path.append("..")
from classes_base import criatura
from habilidades import ativas_alvo_unico, passivas_ao_atacar
from itens import espolios

class CobraVenenosa(criatura.Criatura):
    """
    Classe para a criatura Cobra Venenosa.
    """

    def __init__(self, nivel):
        """
        Cria e retorna uma Cobra Venenosa de um determinado nível.
        """
        # Atributos base da criatura
        maxHp = 2
        maxMana = 2
        ataque = 0
        defesa = 0
        magia = 1
        velocidade = 1
        experiencia = 1
        ouro = 1
        envenenamento_chance = 10

        # Aumentado os atributos por nivel
        i = 1
        while i <= nivel:
            maxHp += 1
            ataque += 1
            experiencia += 1
            maxMana += 1   
            ouro += 1

            # A cada 3 níveis
            if i % 3 == 0:
                magia += 1
                velocidade += 1

            # A cada 5 níveis
            if i % 5 == 0:
                envenenamento_chance += 10
            
            i += 1
        
        if envenenamento_chance > 100:
            envenenamento_chance = 100

        # Habilidades da Criatura
        habilidades = []
        atacar = ativas_alvo_unico.Atacar("Terrestre")
        habilidades.append(atacar)

        picada = ativas_alvo_unico.AtaqueVenenoso(magia, 3, 3, 3)
        picada.nome = "Picada Venenosa"
        picada.descricao = "Ao utilizar suas presas, a Cobra Venenosa injeta veneno no alvo."
        habilidades.append(picada)

        envenenamento = passivas_ao_atacar.Envenenamento(math.ceil(magia/2), 2, envenenamento_chance)
        habilidades.append(envenenamento)

        # Espolios da Criatura
        grana = espolios.Ouro(ouro)
        glandula = espolios.GlandulaVenenosa(1, 1)

        esp = [(100, grana), (10, glandula)]

        # Criando a Criatura
        super(CobraVenenosa, self).__init__([], [], habilidades, esp, "Cobra Venenosa", tipo = "Terrestre",
            maxHp = maxHp, hp = maxHp, maxMana = maxMana, mana = maxMana, ataque = ataque, defesa = defesa,
            magia = magia, velocidade = velocidade, nivel = nivel, experiencia = experiencia,
            singular_plural = "singular", genero = "F",
            descricao = "Uma cobra com grandes presas e um padrão de manchas típico de uma espécie venenosa.")

    def EscolherAcao(self, jogador = None):
        """
        Qual ação a criatura irá tomar.
        """
        # Picada Venenosa -> 80% de chance da Cobra Venenosa usar em um alvo não-envenenado
        if jogador.EfeitoPresente("debuff", "Veneno") == -1 and self.mana >= 3 and super().ChecarRecarga(self.habilidades[1]):
            chance = random.randint(1, 100)
            if chance <= 80:
                return ("habilidade", self.habilidades[1])

        # Atacar
        return ("atacar", self.habilidades[0])
