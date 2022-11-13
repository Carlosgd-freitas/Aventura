import sys

sys.path.append("..")
from base import criatura, utils
from habilidades import ativas_alvo_unico, ativas_alvos_multiplos
from itens import espolios, consumiveis

class Ervagora(criatura.Criatura):
    """
    Classe para a criatura Ervágora.
    """

    def __init__(self, nivel):
        """
        Cria e retorna uma Ervágora de um determinado nível.
        """
        # Atributos base da criatura
        maxHp = 1
        maxMana = 2
        ataque = 0
        defesa = 0
        magia = 1
        velocidade = 1
        experiencia = 0
        ouro = 0
        chance_critico = 0.0
        multiplicador_critico = 1.0

        # Aumentado os atributos por nivel
        i = 1
        while i <= nivel:
            maxHp += 1
            maxMana += 1
            experiencia += 1
            ouro += 1

            # A cada 3 níveis
            if i % 3 == 0:
                magia += 1
                velocidade += 1
            
            i += 1

        # Habilidades da Criatura
        habilidades = []

        atacar = ativas_alvo_unico.Atacar("Normal")
        habilidades.append(atacar)

        grito_estremecedor = ativas_alvos_multiplos.GritoEstremecedor(2, 3, 2, 100)
        habilidades.append(grito_estremecedor)

        # Espolios da Criatura
        grana = espolios.Ouro(ouro)
        erva = consumiveis.ErvaCurativa(1, 1)

        esp = [(100, grana), (40, erva)]

        # Criando a Criatura
        super(Ervagora, self).__init__([], [], habilidades, esp, "Ervágora", tipo = "Terrestre", maxHp = maxHp,
            hp = maxHp, maxMana = maxMana, mana = maxMana, ataque = ataque, defesa = defesa, magia = magia,
            velocidade = velocidade, nivel = nivel, experiencia = experiencia, singular_plural = "singular",
            genero = "F", chance_critico = chance_critico, multiplicador_critico = multiplicador_critico,
            descricao = "Uma planta ambulante que possui um rosto em seu fruto e utiliza suas raízes para correr" +
            " das batalhas. É facilmente caçada por alquimistas e bruxas por possuir poder mágico em suas folhas" +
            ", embora seja mais fraco que sua parente mais conhecida, a Mandrágora.")

    def EscolherAcao(self, aliados, inimigos, jogador):
        """
        Qual ação a criatura irá tomar.
        """

        # Grito Estremecedor -> 50% de chance da Ervágora usar
        if self.mana >= 3 and super().ChecarRecarga(self.habilidades[1]):
            if utils.CalcularChance(0.5):
                return ("habilidade", self.habilidades[1], inimigos)

        # Correr da Batalha
        return ("correr", "A Ervágora corre aos prantos da batalha.", None)
