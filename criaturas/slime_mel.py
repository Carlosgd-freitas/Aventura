import random
import sys

sys.path.append("..")
from classes_base import criatura, utils
from habilidades import ativas_alvo_unico, passivas_inicio_turno
from itens import espolios, consumiveis

class SlimeMel(criatura.Criatura):
    """
    Classe para a criatura Slime de Mel.
    """

    def __init__(self, nivel):
        """
        Cria e retorna um Slime de Mel de um determinado nível.
        """
        # Atributos base da criatura
        maxHp = 2
        maxMana = 2
        ataque = 1
        defesa = 0
        magia = 1
        velocidade = 1
        experiencia = 2
        regen = 0
        ouro = 2
        chance_critico = 0.0
        multiplicador_critico = 1.0

        # Aumentado os atributos por nivel
        i = 1
        while i <= nivel:
            maxHp += 2
            ataque += 1
            magia += 1
            experiencia += 2
            maxMana += 3
            ouro += 2

            # A cada 3 níveis
            if i % 3 == 0:
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

        cuspe = ativas_alvo_unico.CuspeDeMel()
        habilidades.append(cuspe)

        if nivel >= 3:
            regeneracao = passivas_inicio_turno.Regeneracao(regen)
            habilidades.append(regeneracao)
        
        if nivel >= 5:
            cura = ativas_alvo_unico.CuraInferior()
            habilidades.append(cura)
            
        # Espolios da Criatura
        grana = espolios.Ouro(ouro)
        mel = consumiveis.MelAbelhoide(1, 1)

        esp = [(100, grana), (100, mel)]

        # Criando a Criatura
        super(SlimeMel, self).__init__([], [], habilidades, esp, "Slime de Mel", tipo = "Normal", maxHp = maxHp,
            hp = maxHp, maxMana = maxMana, mana = maxMana, ataque = ataque, defesa = defesa, magia = magia,
            velocidade = velocidade, nivel = nivel, experiencia = experiencia, singular_plural = "singular",
            genero = "M", chance_critico = chance_critico, multiplicador_critico = multiplicador_critico,
            descricao = "Um slime que consumiu muito mel de abelhóide e viveu para contar a história. Com seu " +
            "interior modificado, essa variante mais robusta consegue cobrir suas vítimas de mel e deixá-las " +
            "lentas. Este cuspe de mel também a ajuda a roubar ainda mais mel das colméias que invade.")

    def EscolherAcao(self, aliados, inimigos, jogador):
        """
        Qual ação a criatura irá tomar.
        """
        alvo_inimigo = random.choice(inimigos)

        indice = utils.MenorAtributo(aliados, 'hp')
        alvo_aliado = aliados[indice]

        # Cuspe De Mel -> 75% de chance do Slime de Mel usar
        if self.mana >=  and super().ChecarRecarga(self.habilidades[1]):
            chance = random.randint(1, 100)
            if chance <= 75:
                return ("habilidade", self.habilidades[1], alvo_inimigo)

        # Cura Inferior -> 50% de chance do Slime de Mel usar no aliado ferido com menos HP atual
        if self.nivel >= 5 and self.mana >=  and super().ChecarRecarga(self.habilidades[3]) and \
            (alvo_aliado.hp < alvo_aliado.maxHp):
            chance = random.randint(1, 100)
            if chance <= 50:
                return ("habilidade", self.habilidades[3], alvo_aliado)

        # Atacar
        return ("atacar", self.habilidades[0], alvo_inimigo)
        