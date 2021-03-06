from . import basico

class Criatura(basico.Base):
    """
    Esta classe serve para criaturas.
    """
    def __init__(self, buffs = [], debuffs = [], habilidades = [], espolios = [], nome = "default",
                descricao = "default", tipo = "default", nivel = 0, experiencia = 0, maxHp = 0, hp = 0, maxMana = 0,
                mana = 0, ataque = 0, defesa = 0, magia = 0, velocidade = 0, singular_plural = "default",
                genero = "default", chance_critico = 0.0, multiplicador_critico = 1.0):
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
            defesa, magia, velocidade, singular_plural, genero, chance_critico, multiplicador_critico)
    
    def ChecarRecarga(self, habilidade):
        """
        Retorna 1 se o valor de recarga atual da habilidade é igual ao valor da recarga e retorna 0 caso contrário.
        """

        return habilidade.recarga_atual == habilidade.recarga

    def EfeitoPresente(self, buff_debuff, efeito_nome):
        """
        Retorna o índice da lista de buffs ou debuffs correspondente ao nome do efeito passado por parâmetro se
        a criatura está sob aquele efeito e -1 caso contrário.
        """

        valor = -1
        indice = 0
        lista_efeitos = None

        if buff_debuff == "buff":
            lista_efeitos = self.buffs
        else:
            lista_efeitos = self.debuffs

        for e in lista_efeitos:
            if e.nome == efeito_nome:
                valor = indice
                break
            indice += 1

        return valor
    
    def ContarEfeitos(self, buff_debuff, efeito_nome):
        """
        Retorna os índices dos efeitos de buff ou debuff que a criatura está sob que tenha o mesmo nome do
        passado por parâmetro.
        """

        lista_indices = []
        lista_efeitos = None

        if buff_debuff == "buff":
            lista_efeitos = self.buffs
        else:
            lista_efeitos = self.debuffs

        indice = 0
        for e in lista_efeitos:
            if e.nome == efeito_nome:
                lista_indices.append(indice)
            indice += 1

        return lista_indices
    
    def MaiorEfeito(self, buff_debuff, efeito_nome, criterio):
        """
        Retorna o índice e o valor do maior critério (decaimento, duracao, etc.) dentre os buffs ou debuffs que
        a criatura está sob que tenha o mesmo nome do passado por parâmetro.
        """

        maior = -9999999
        lista_efeitos = None

        if buff_debuff == "buff":
            lista_efeitos = self.buffs
        else:
            lista_efeitos = self.debuffs

        indice = 0
        for e in lista_efeitos:
            if e.nome == efeito_nome:
                if criterio == "valor" and e.valor > maior:
                    maior = e.valor

                elif criterio == "decaimento" and e.decaimento > maior:
                    maior = e.decaimento

                elif criterio == "duracao" and e.duracao > maior:
                    maior = e.duracao
            
            indice += 1

        return indice, maior
    
    def HabilidadePresente(self, habilidade_nome):
        """
        Retorna o índice da lista de habilidades correspondente ao nome da habilidade passado por parâmetro se
        a criatura possui aquela habilidade e -1 caso contrário.
        """

        valor = -1
        indice = 0

        for h in self.habilidades:
            if h.nome == habilidade_nome:
                valor = indice
                break
            indice += 1

        return valor

    def CombinarEfeito(self, efeito_nome):
        """
        Se a criatura estiver sob mais de um efeito de <efeito_nome>, eles serão combinados e será retornado 1.
        Caso contrário, será retornado 0.

        Debuffs:
        * Veneno: maior valor e maior duração
        * Atordoamento: maior duração
        * Lentidão: soma das durações
        """

        combinou = 0

        # Definindo a lista de efeitos
        if efeito_nome == "Veneno" or efeito_nome == "Atordoamento" or efeito_nome == "Lentidão":
            lista_efeitos = self.debuffs
            primeiro_indice = self.EfeitoPresente("debuff", efeito_nome)
        else:
            lista_efeitos = self.buffs
            primeiro_indice = self.EfeitoPresente("buff", efeito_nome)

        indice = 0

        if primeiro_indice != -1:

            for e in lista_efeitos:
                
                # Efeitos com nome <efeito_nome> presentes na criatura que não são o primeiro
                if e.nome == efeito_nome and indice != primeiro_indice:
                    combinou = 1

                    # Combinando os efeitos
                    if efeito_nome == "Veneno":
                        if e.valor > lista_efeitos[primeiro_indice].valor:
                            lista_efeitos[primeiro_indice].valor = e.valor
                    
                    if efeito_nome == "Veneno" or efeito_nome == "Atordoamento":
                        if e.duracao > lista_efeitos[primeiro_indice].duracao:
                            lista_efeitos[primeiro_indice].duracao = e.duracao
                    
                    elif efeito_nome == "Lentidão":
                        lista_efeitos[primeiro_indice].duracao += (e.duracao - 1)

                    # Removendo efeitos com nome <efeito_nome> duplicados
                    lista_efeitos.remove(e)

                indice += 1
        
        return combinou
