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
    
    def __str__(self):
        """
        Converte a classe em uma string.
        """
        string = f'Nome: {self.nome}, Tipo: {self.tipo}, Nível: {self.nivel}, Experiência: {self.experiencia}, HP Máximo: {self.maxHp}, HP: {self.hp}, ' + \
            f'Mana Máxima: {self.maxMana}, Mana: {self.mana}\n' + \
            f'Ataque: {self.ataque}, Defesa: {self.defesa}, Magia: {self.magia}, Velocidade: {self.velocidade}, Chance de Acerto Crítico: {self.chance_critico}, ' + \
            f'Multiplicador de Dano Crítico: {self.multiplicador_critico}\n' + \
            f'singular_plural: {self.singular_plural}, Gênero: {self.genero}\n' + \
            f'Descrição: {self.descricao}\n'
        string += 'Buffs:\n'
        for i, b in enumerate(self.buffs):
            string += '* ' + str(b)
            if i != len(self.buffs) - 1:
                string += '\n'
        string += 'Debuffs:\n'
        for i, d in enumerate(self.debuffs):
            string += '* ' + str(d)
            if i != len(self.debuffs) - 1:
                string += '\n'
        string += 'Habilidades:\n'
        for i, h in enumerate(self.habilidades):
            string += '* ' + str(h)
            if i != len(self.habilidades) - 1:
                string += '\n'
        string += 'Espólios:\n'
        for i, (e0, e1) in enumerate(self.espolios):
            string += f'* {e0}% de chance: {e1}'
            if i != len(self.espolios) - 1:
                string += '\n'

        return string

    def ChecarRecarga(self, habilidade):
        """
        Retorna 1 se o valor de recarga atual da habilidade é igual ao valor da recarga e retorna 0 caso contrário.
        """

        return habilidade.recarga_atual == habilidade.recarga

    def EfeitoPresente(self, efeito_nome):
        """
        Retorna o primeiro efeito com nome <efeito_nome> presente na criatura, e retorna None caso a
        criatura não esteja sob este efeito.
        """

        for e in self.buffs:
            if e.nome == efeito_nome:
                return e
        for e in self.debuffs:
            if e.nome == efeito_nome:
                return e
        return None
    
    def HabilidadePresente(self, habilidade_nome):
        """
        Retorna a habilidade com nome <habilidade_nome> presente na criatura, e retorna None caso a
        criatura não possua aquela habilidade.
        """

        for h in self.habilidades:
            if h.nome == habilidade_nome:
                return h
        return None

    def HabilidadeIndice(self, habilidade_nome):
        """
        Retorna o índice da habilidade com nome <habilidade_nome> presente na criatura, e retorna None caso a
        criatura não possua aquela habilidade.
        """

        for indice, h in enumerate(self.habilidades):
            if h.nome == habilidade_nome:
                return indice
        return None
    
    def ContarEfeitos(self, buff_debuff, efeito_nome = ""):
        """
        Retorna uma lista de índices dos efeitos de buff ou debuff que a criatura está sob.

        Parâmetros:
        - buff_debuff: tipo de efeito cujos inídices serão retornados. Os valores possíveis são 'buff' e
        'debuff'.

        Parâmetros Opcionais:
        - efeito_nome: se o nome de um efeito for passado, retornará apenas os índices dos efeitos que tenham
        o mesmo nome.
        """

        lista_indices = []
        lista_efeitos = None

        if buff_debuff == "buff":
            lista_efeitos = self.buffs
        else:
            lista_efeitos = self.debuffs

        indice = 0
        for e in lista_efeitos:
            if (e.nome == efeito_nome) or (efeito_nome == ""):
                lista_indices.append(indice)
            indice += 1

        return lista_indices
    
    def ContarEfeitosImprimiveis(self, buff_debuff):
        """
        Retorna a quantidade de buffs ou debuffs que uma criatura está sob que podem ser impressos.
        """

        if buff_debuff == "buff":
            lista_efeitos = self.buffs
        else:
            lista_efeitos = self.debuffs

        tamanho = len(lista_efeitos)
        for e in lista_efeitos:
            if e.nome == "Resistência Veneno":
                tamanho -= 1

        return tamanho
    
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
            efeito = self.EfeitoPresente(efeito_nome)
        else:
            lista_efeitos = self.buffs
            efeito = self.EfeitoPresente(efeito_nome)

        indice = 0

        if efeito is not None:

            for e in lista_efeitos:
                
                # Efeitos com nome <efeito_nome> presentes na criatura que não são o primeiro
                if e.nome == efeito_nome and e != efeito:
                    combinou = 1

                    # Combinando os efeitos
                    if efeito_nome == "Veneno":
                        if e.valor > efeito.valor:
                            efeito.valor = e.valor
                    
                    if efeito_nome == "Veneno" or efeito_nome == "Atordoamento":
                        if e.duracao > efeito.duracao:
                            efeito.duracao = e.duracao
                    
                    elif efeito_nome == "Lentidão":
                        efeito.duracao += (e.duracao - 1)

                    # Removendo efeitos com nome <efeito_nome> duplicados
                    lista_efeitos.remove(e)

                indice += 1
        
        return combinou
