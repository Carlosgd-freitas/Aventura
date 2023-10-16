import random
import sys

sys.path.append("..")
from base import criatura, utils
from habilidades import ativas_alvo_unico, invocacao, passivas_inicio_turno
from itens import espolios

class SlimeGigante(criatura.Criatura):
    """
    Classe para a criatura Slime Gigante.
    """

    def __init__(self, nivel):
        """
        Cria e retorna um Slime Gigante de um determinado nível.
        """
        # Atributos base da criatura
        maxHp = 2
        maxMana = 1
        ataque = 1
        defesa = 0
        magia = 1
        velocidade = 1
        experiencia = 1
        regen = 0
        ouro = 1
        chance_critico = 1.0
        multiplicador_critico = 1.1

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

        if nivel <= 1:
            subdivisao = invocacao.Subdivisao("Slime", 1, 2)
        else:
            subdivisao = invocacao.Subdivisao("Slime", nivel - 1, 2)
        habilidades.append(subdivisao)

        if nivel >= 3:
            regeneracao = passivas_inicio_turno.Regeneracao(regen)
            habilidades.append(regeneracao)

        if nivel >= 5:
            cuspe = ativas_alvo_unico.CuspeAcido(ataque)
            habilidades.append(cuspe)

        # Espolios da Criatura
        grana = espolios.Ouro(ouro)
        fluido = espolios.FluidoSlime(1, 1)

        esp = [(100, grana), (10, fluido), (10, fluido)]

        # Criando a Criatura
        super(SlimeGigante, self).__init__([], [], habilidades, esp, "Slime Gigante", tipo = "Normal", maxHp = maxHp,
            hp = maxHp, maxMana = maxMana, mana = maxMana, ataque = ataque, defesa = defesa, magia = magia,
            velocidade = velocidade, nivel = nivel, experiencia = experiencia, singular_plural = "singular",
            genero = "M", chance_critico = chance_critico, multiplicador_critico = multiplicador_critico,
            descricao = "A versão gigante de um Slime comum. Com um surpreso aumento em sua inteligência, em " +
            "situações de extremo perigo, esta criatura se divide em duas para aumentar suas chances de sobreviver.")

    def EscolherAcao(self, aliados, inimigos, jogador):
        """
        Qual ação a criatura irá tomar.
        """
        alvo_inimigo = random.choice(inimigos)

        # Cuspe Ácido -> 75% de chance do Slime Gigante usar
        if self.nivel >= 5 and self.mana >= 4 and super().ChecarRecarga(self.habilidades[2]):
            if utils.CalcularChance(0.75):
                return ("habilidade", self.habilidades[3], alvo_inimigo)

        # Atacar
        return ("atacar", self.habilidades[0], alvo_inimigo)
        