import random
import sys

sys.path.append("..")
from classes_base import criatura
from habilidades import ativas_alvo_unico, passivas_inicio_turno, invocar_criaturas
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

        subdivisao = invocar_criaturas.Subdivisao("Slime", 2)
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
            genero = "M",
            descricao = "A versão gigante de um Slime comum. Com um surpreso aumento em sua inteligência, em " +
            "situações de extremo perigo, esta criatura se divide em duas para aumentar suas chances de sobreviver.")

    def EscolherAcao(self, jogador = None):
        """
        Qual ação a criatura irá tomar.
        """
        # Cuspe Ácido -> 75% de chance do Slime Gigante usar
        if self.nivel >= 5 and self.mana >= 4 and super().ChecarRecarga(self.habilidades[2]):
            chance = random.randint(1, 100)
            if chance <= 75:
                return ("habilidade", self.habilidades[2])

        # Atacar
        return ("atacar", self.habilidades[0])
        