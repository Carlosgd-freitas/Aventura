from . import basico

class Criatura(basico.Base):
    """
    Esta classe serve para criaturas.
    """
    def __init__(self, buffs = [], debuffs = [], habilidades = [], espolios = [], nome = "default",
                descricao = "default", tipo = "default", nivel = 0, experiencia = 0, maxHp = 0, hp = 0, maxMana = 0,
                mana = 0, ataque = 0, defesa = 0, magia = 0, velocidade = 0):
        """
        Inicializador da classe.
        """
        # Uma lista de efeitos positivos que estão atuando na Criatura
        self.buffs = buffs

        # Uma lista de efeitos negativos que estão atuando na Criatura
        self.debuffs = debuffs

        # Habilidades da Criatura
        self.habilidades = habilidades

        # Uma lista de tuplas (X, Y), onde X é um Item e Y é a chance em % daquele Item ser dropado quando a
        # Criatura for destruída
        self.espolios = espolios

        super(Criatura, self).__init__(nome, descricao, tipo, nivel, experiencia, maxHp, hp, maxMana, mana, ataque,
                                    defesa, magia, velocidade)
    
    def ChecarRecarga(self, habilidade):
        """
        Retorna 1 se o valor de recarga atual da habilidade é igual ao valor da recarga e retorna 0 caso contrário.
        """

        return habilidade.recarga_atual == habilidade.recarga
