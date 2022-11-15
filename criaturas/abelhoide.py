import random
import sys

sys.path.append("..")
from base import criatura
from habilidades import ativas_alvo_unico, passivas_abater_criaturas
from itens import espolios, consumiveis

class Abelhoide(criatura.Criatura):
    """
    Classe para a criatura Abelhóide.
    """

    def __init__(self, nivel):
        """
        Cria e retorna uma Abelhóide de um determinado nível.
        """
        # Atributos base da criatura
        maxHp = 2
        maxMana = 2
        ataque = 1
        defesa = 0
        magia = 1
        velocidade = 1
        experiencia = 0
        ouro = 0
        chance_critico = 5.0
        multiplicador_critico = 1.5

        # Aumentado os atributos por nivel
        i = 1
        while i <= nivel:
            maxHp += 1
            maxMana += 1
            ataque += 1
            magia += 1
            experiencia += 1
            ouro += 1

            # A cada 3 níveis
            if i % 3 == 0:
                maxHp += 1
                maxMana += 1
                velocidade += 1
            
            i += 1

        # Habilidades da Criatura
        habilidades = []
        atacar = ativas_alvo_unico.Atacar("Vento")
        habilidades.append(atacar)

        vinganca = passivas_abater_criaturas.Vinganca('Ataque', 1, 'Larva de Abelhóide', 'singular', 'F')
        habilidades.append(vinganca)

        # Espolios da Criatura
        grana = espolios.Ouro(ouro)
        mel = consumiveis.MelAbelhoide(1, 1)

        esp = [(100, grana), (50, mel)]

        # Criando a Criatura
        super(Abelhoide, self).__init__([], [], habilidades, esp, "Abelhóide", tipo = "Vento",
            maxHp = maxHp, hp = maxHp, maxMana = maxMana, mana = maxMana, ataque = ataque, defesa = defesa,
            magia = magia, velocidade = velocidade, nivel = nivel, experiencia = experiencia,
            singular_plural = "singular", genero = "F", chance_critico = chance_critico,
            multiplicador_critico = multiplicador_critico,
            descricao = "As abelhóides comuns são responsáveis pela maioria das tarefas na colméia. Como as " +
            "outras de sua espécie, uma abelhóide irá apresentar um comportamento muito mais agressivo se uma " +
            "das jovens larvas da colméia for morta.")

    def EscolherAcao(self, aliados, inimigos, jogador):
        """
        Qual ação a criatura irá tomar.
        """
        alvo_inimigo = random.choice(inimigos)

        # Atacar
        return ("atacar", self.habilidades[0], alvo_inimigo)
        