import random
import sys

sys.path.append("..")
from classes_base import criatura
from habilidades import ativas_alvo_unico, passivas_inicio_turno
from itens import espolios

class Slime(criatura.Criatura):
    """
    Classe para a criatura Slime.
    """

    def __init__(self, nivel):
        """
        Cria e retorna um Slime de um determinado nível.
        """
        # Atributos base da criatura
        maxHp = 1
        maxMana = -1
        ataque = 0
        defesa = 0
        magia = 0
        velocidade = 1
        experiencia = 0
        regen = 0
        ouro = 0

        # Aumentado os atributos por nivel
        i = 1
        while i <= nivel:
            maxHp += 2
            ataque += 1
            experiencia += 1
            maxMana += 1
            ouro += 1

            # A cada 3 níveis
            if i % 3 == 0:
                magia += 1
                regen += 1

            # A cada 5 níveis
            if i % 5 == 0:
                defesa += 1
            
            # A cada 10 níveis
            if i % 10 == 0:
                velocidade += 1
            
            i += 1

        # Habilidades da Criatura
        habilidades = []
        atacar = ativas_alvo_unico.Atacar("Normal")
        habilidades.append(atacar)

        if nivel >= 3:
            regeneracao = passivas_inicio_turno.Regeneracao(regen)
            habilidades.append(regeneracao)

        if nivel >= 5:
            cuspe = ativas_alvo_unico.CuspeAcido(ataque)
            habilidades.append(cuspe)

        # Espolios da Criatura
        grana = espolios.Ouro(ouro)
        fluido = espolios.FluidoSlime(1, 1)

        esp = [(100, grana), (10, fluido)]

        # Criando a Criatura
        super(Slime, self).__init__([], [], habilidades, esp, "Slime", tipo = "Normal", maxHp = maxHp, hp = maxHp, 
            maxMana = maxMana, mana = maxMana, ataque = ataque, defesa = defesa, magia = magia,
            velocidade = velocidade, nivel = nivel, experiencia = experiencia, singular_plural = "singular",
            genero = "M",
            descricao = "Um monstro verde e gelatinoso que utiliza seu interior ácido para matar suas vítimas lentamente.")

    def EscolherAcao(self, aliados, inimigos, jogador):
        """
        Qual ação a criatura irá tomar.
        """
        alvo_inimigo = random.choice(inimigos)

        # Cuspe Ácido -> 75% de chance do Slime usar
        if self.nivel >= 5 and self.mana >= 4 and super().ChecarRecarga(self.habilidades[2]):
            chance = random.randint(1, 100)
            if chance <= 75:
                return ("habilidade", self.habilidades[2], alvo_inimigo)

        # Atacar
        return ("atacar", self.habilidades[0], alvo_inimigo)
