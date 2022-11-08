import random
import sys

sys.path.append("..")
from base import criatura, utils
from habilidades import ativas_alvo_unico, passivas_inicio_turno, ativas_alvo_proprio
from itens import espolios

class Larry(criatura.Criatura):
    """
    Classe para um chefão da primeira área Larry.
    """

    def __init__(self, nivel):
        """
        Cria e retorna Larry baseado no nível do jogador.
        """
        # Atributos base da criatura considerando que o jogador esteja nível 5
        maxHp = 20
        maxMana = 20
        ataque = 5
        defesa = 2
        magia = 3
        velocidade = 2
        experiencia = 25
        regen = 2
        ouro = 10
        chance_critico = 5.0
        multiplicador_critico = 1.5

        # Aumentado os atributos por nivel
        diferenca_nivel = nivel - 5
        i = 1
        while i <= diferenca_nivel:
            maxHp += 3
            maxMana += 3
            ataque += 1
            experiencia += 4
            ouro += 2

            # A cada 2 níveis
            if i % 2 == 0:
                magia += 1
                regen += 1
                multiplicador_critico += 0.1

            # A cada 3 níveis
            if i % 3 == 0:
                defesa += 1
                velocidade += 1
            
            i += 1

        # Habilidades da Criatura
        habilidades = []
        atacar = ativas_alvo_unico.Atacar("Normal")
        habilidades.append(atacar)

        regeneracao = passivas_inicio_turno.Regeneracao(regen)
        habilidades.append(regeneracao)

        cuspe = ativas_alvo_unico.CuspeAcido(ataque)
        habilidades.append(cuspe)

        focar = ativas_alvo_proprio.Focar(2, 20, 3, 5, 4)
        habilidades.append(focar)

        # Espolios da Criatura
        grana = espolios.Ouro(ouro)
        fluido = espolios.FluidoSlime(2, 1)

        esp = [(100, grana), (100, fluido)]

        # Criando a Criatura
        super(Larry, self).__init__([], [], habilidades, esp, "Larry", tipo = "Normal", maxHp = maxHp, hp = maxHp, 
            maxMana = maxMana, mana = maxMana, ataque = ataque, defesa = defesa, magia = magia,
            velocidade = velocidade, nivel = nivel, experiencia = experiencia, singular_plural = "singular",
            genero = "M", chance_critico = chance_critico, multiplicador_critico = multiplicador_critico,
            descricao = "Um slime muito mais perspicaz que o comum. Ele continha um óculos de ourives levemente " +
            "danificado em seu interior, e foi chamado de 'Anomalia' por um Cristal Atacante danificado que o " +
            "escoltava.")

    def EscolherAcao(self, aliados, inimigos, jogador):
        """
        Qual ação a criatura irá tomar.
        """
        alvo_inimigo = random.choice(inimigos)

        # Cuspe Ácido -> 75% de chance de Larry usar
        if self.mana >= 4 and super().ChecarRecarga(self.habilidades[2]):
            if utils.CalcularChance(0.75):
                return ("habilidade", self.habilidades[2], alvo_inimigo)

        # Focar -> 50% de chance de Larry usar se não estiver sob o efeito de Aumento de Velocidade
        elif super().EfeitoPresente("buff", "Aumento Velocidade") == -1 and self.mana >= 5 and super().ChecarRecarga(self.habilidades[3]):
            if utils.CalcularChance(0.5):
                return ("habilidade", self.habilidades[3], None)

        # Atacar
        return ("atacar", self.habilidades[0], alvo_inimigo)
