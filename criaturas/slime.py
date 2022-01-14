import sys

sys.path.append("..")
from classes_base import criatura, habilidade, efeito, item

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
        atacar = habilidade.Habilidade("Atacar", "Um ataque normal.", "Normal", "inimigo", "ativa", 0, [], 0, 0,
            [("ataque", 100)], [])
        habilidades.append(atacar)

        if nivel >= 3:
            regeneracao = habilidade.Habilidade("Regeneração", "Recupera parte da vida no início do turno.", "Normal",
                "proprio", "passiva", regen, [], 0, 0, [("magia", 50)], [])
            habilidades.append(regeneracao)

        if nivel >= 5:
            perfurante = efeito.Efeito("Perfurante %", 50, 0, -1, 100)
            cuspe = habilidade.Habilidade("Cuspe Ácido", "Um cuspe ácido que ignora 50% da defesa do alvo.", "Normal",
                "inimigo", "ativa", ataque, [("Mana", 4)], 2, 2, [("magia", 50)], [perfurante])
            habilidades.append(cuspe)

        # Espolios da Criatura
        grana = item.Item(nome = "Ouro", quantidade = ouro, descricao = "Peças de ouro aceitas como moeda por todo o mundo.")
        fluido = item.Item(nome = "Fluido de Slime", quantidade = 1,
            descricao = "Uma parte viscosa e um pouco ácida do interior de um Slime derrotado.")

        espolios = [(grana, 100), (fluido, 10)]

        # Criando a Criatura
        super(Slime, self).__init__([], [], habilidades, espolios, "Slime", tipo = "Normal", maxHp = maxHp, hp = maxHp, 
            maxMana = maxMana, mana = maxMana, ataque = ataque, defesa = defesa, magia = magia, velocidade = velocidade,
            nivel = nivel, experiencia = experiencia,
            descricao = "Um monstro verde e gelatinoso que utiliza seu interior ácido para matar suas vítimas lentamente.")

    def EscolherAcao(self):
        """
        Qual ação a criatura irá tomar.
        """
        # Cuspe Ácido
        if self.nivel >= 5 and self.mana >= 4 and super().ChecarRecarga(self.habilidades[2]):
            return ("habilidade", self.habilidades[2])

        # Atacar
        else:
            return ("atacar", self.habilidades[0])
