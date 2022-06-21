import random
import sys

sys.path.append("..")
from classes_base import criatura
from habilidades import ativas_alvo_unico, ativas_alvo_proprio
from itens import espolios

class Tortuga(criatura.Criatura):
    """
    Classe para a criatura Tortuga.
    """

    def __init__(self, nivel):
        """
        Cria e retorna uma Tortuga de um determinado nível.
        """
        # Atributos base da criatura
        maxHp = 1
        maxMana = 0
        ataque = 1
        defesa = 1
        magia = 0
        velocidade = 1
        experiencia = 0
        ouro = 0

        # Aumentado os atributos por nivel
        i = 1
        while i <= nivel:
            maxHp += 2
            experiencia += 1
            ouro += 1

            # A cada 2 níveis
            if i % 2 == 0:
                maxHp += 1
                ataque += 1

            # A cada 3 níveis
            if i % 3 == 0:
                defesa += 1
            
            # A cada 10 níveis
            if i % 10 == 0:
                velocidade += 1
            
            i += 1

        # Habilidades da Criatura
        habilidades = []
        atacar = ativas_alvo_unico.Atacar("Terrestre")
        habilidades.append(atacar)

        entrar_casco = ativas_alvo_proprio.EsconderCasco()
        habilidades.append(entrar_casco)

        # Espolios da Criatura
        grana = espolios.Ouro(ouro)
        casco = espolios.CarapacaTortuga(1, 1)

        esp = [(100, grana), (10, casco)]

        # Criando a Criatura
        super(Tortuga, self).__init__([], [], habilidades, esp, "Tortuga", tipo = "Terrestre", maxHp = maxHp,
            hp = maxHp, maxMana = maxMana, mana = maxMana, ataque = ataque, defesa = defesa, magia = magia,
            velocidade = velocidade, nivel = nivel, experiencia = experiencia, singular_plural = "singular",
            genero = "F",
            descricao = "Um réptil grande que possui pouca capacidade ofensiva e que esconde em seu casco quando " +
            "se sente ameaçada.")

    def EscolherAcao(self, aliados, inimigos, jogador):
        """
        Qual ação a criatura irá tomar.
        """
        alvo_inimigo = random.choice(inimigos)

        # Entrar no Casco -> Se a Tortuga não estiver defendendo e estiver com HP <= 25%
        if super().EfeitoPresente("buff", "Defendendo") == -1 and self.hp <= (self.maxHp * 0.25) and super().ChecarRecarga(self.habilidades[1]):
            return ("habilidade", self.habilidades[1], None)

        # Passar o Turno -> Se a Tortuga estiver defendendo
        elif super().EfeitoPresente("buff", "Defendendo") != -1:
            return ("passar", "A Tortuga está dentro de seu casco.", None)

        # Atacar
        return ("atacar", self.habilidades[0], alvo_inimigo)
