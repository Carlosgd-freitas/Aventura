from . import criatura, item, efeito, habilidade

class Jogador(criatura.Criatura):
    """
    Esta classe serve para o jogador.
    """
    def __init__(self, classe = "default", nome = "default"):
        """
        Cria um jogador novo.
        """
        # Classe do Jogador (Guerreiro, Mago, etc.)
        self.classe = classe

        # Quantidade inicial de ouro do Jogador
        self.ouro = 50

        # O jogador irá começar com 2 Poções de Cura Pequenas
        pocao_efeito = [efeito.Efeito("Cura HP % ou valor", [25, 5], 0, -1, 100)]
        pocao = item.Item(pocao_efeito, [], 5, 2, "Poção de Cura Pequena",
            "Cura 25% do HP máximo ou 5 de HP, o que for maior.")
        self.inventario = [("Consumivel", pocao)]

        # Atacar normalmente é possível para todas as classes
        habilidades = []
        atacar = habilidade.Habilidade("Atacar", "Alvo único: Um ataque normal.", "Normal", "inimigo", "ativa", 0, [], 0, 0,
            [("ataque", 100)], [])
        habilidades.append(atacar)

        if self.classe == "Guerreiro":
            maxHp = 20
            maxMana = 10
            magia = 0
            velocidade = 1
        
            # Arma inicial do Guerreiro
            espada = item.Item([], [], 5, 1, "Espada Enferrujada", "Uma espada velha que se enferrujou com o tempo.",
                "Normal", 1, ataque = 1)
            equipados = [("Uma mao", espada)]
        
        elif self.classe == "Mago":
            maxHp = 15
            maxMana = 20
            magia = 1
            velocidade = 1

            # Um Mago começará com 1 Poção de Mana Pequena
            pocao_efeito = [efeito.Efeito("Cura Mana % ou valor", [25, 5], 0, -1, 100)]
            pocao = item.Item(pocao_efeito, [], 4, 1, "Poção de Mana Pequena",
                "Cura 25% da Mana máxima ou 5 de Mana, o que for maior.")
            self.inventario.append(("Consumivel", pocao))

            # Arma inicial do Mago
            cajado = item.Item([], [], 5, 1, "Cajado de Iniciante", nivel = 1, tipo = "Normal", magia = 1, 
                descricao = "Um cajado de madeira imbuído com uma pequena quantidade de mana. Este tipo de cajado" +
                " é normalmente utilizado por magos iniciantes.")
            equipados = [("Duas maos", cajado)]

            projetil = habilidade.Habilidade("Projétil de Mana", "Alvo único: Concentra e dispara uma pequena" + 
            "quantidade de mana, causando dano igual à sua magia.", "Normal", "inimigo", "ativa", 0,
            [("Mana", 2)], 1, 1, [("magia", 100)], [])
            habilidades.append(projetil)

        # Equipamentos iniciais do Jogador
        self.equipados = equipados

        super(Jogador, self).__init__([], [], habilidades, [], nome, "default", "Normal", 1, 0, maxHp, maxHp,
                                    maxMana, maxMana, 1, 0, magia, velocidade)
                                    