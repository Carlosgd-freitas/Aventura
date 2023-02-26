import math
from . import utils
from copy import deepcopy
from colorama import Fore, Back, Style

class Efeito():
    """
    Esta classe é utilizada para efeitos de buff e debuff.
    """

    def __init__(self, nome = "default", valor = 0, decaimento = 0, duracao = 0, chance = 100,
        singular_plural = "default", genero = "default"):
        """
        Inicializador da classe.
        """
        # Nome do Efeito
        self.nome = nome

        # Valor do Efeito
        self.valor = valor

        # Quanto o valor irá decair a cada turno
        self.decaimento = decaimento
        
        # Quantos turnos o efeito irá perdurar. Se igual a -1, o efeito é instantâneo.
        self.duracao = duracao

        # Qual é chance deste efeito acontecer, em %
        self.chance = chance

        # Se o nome do efeito é em singular ou plural
        self.singular_plural = singular_plural

        # Se o nome do efeito é masculino ou feminino
        self.genero = genero
    
    def __str__(self):
        """
        Converte a classe em uma string.
        """
        string = f'Nome: {self.nome}\n'
        string += f'Valor: {self.valor}\n'
        string += f'Decaimento: {self.decaimento}\n'
        string += f'Duração: {self.duracao}\n'
        string += f'Chance: {self.chance}\n'
        string += f'singular_plural: {self.singular_plural}\n'
        string += f'Gênero: {self.genero}'
        return string

    def Processar(self, usuario, alvo, item = None, habilidade = None, fora_combate = False, append = True):
        """
        Processa um efeito de buff/debuff de um item ou habilidade, utilizado por um usuário em um alvo. Apenas um
        dos parâmetros 'item' ou 'habilidade' deve receber um argumento, enquanto o outro permanece com None.
        
        Parâmetros:
        - usuario: qual criatura (ou jogador) está causando o efeito;
        - efeito: efeito a ser processado;
        - alvo: alvo do efeito;
        - item: item que irá causar o efeito;
        - habilidade: habilidade que irá causar o efeito.

        Parâmetros opcionais:
        - fora_combate: se igual a True, o efeito sendo processado não foi causado em combate. O valor padrão é False;
        - append: se igual a False, o efeito sendo processado não será adicionado a lista de buffs/debuffs da
        criatura. O valor padrão é True.
        """

        # Alguns efeitos terão sua chance calculada posteriormente
        if self.nome == "Veneno":
            pass
        # Se o efeito veio de uma habilidade e possui uma % de acontecer
        elif (habilidade is not None) and (not utils.CalcularChance(self.chance / 100)):
            return

        # Flags para efeitos de item
        sobrecura_hp = 0
        sobrecura_mana = 0

        # Melhora das mensagens de uso de itens
        mensagem = None
        if item is not None:
            artigo = item.RetornarArtigo()
            contracao_por = item.RetornarContracaoPor().lower()

        ## Efeitos de Buff ##

        # Cura o HP em um valor definido, com base no HP máximo ou o que for maior dentre estas opções
        if self.nome == "Cura HP" or self.nome == "Cura HP %" or self.nome == "Cura HP % ou valor":
            valor = 0

            if self.nome == "Cura HP":
                valor = self.valor
            elif self.nome == "Cura HP %":
                valor = math.floor(alvo.maxHp * (self.valor / 100))
            else:
                valor1 = math.floor(alvo.maxHp * (self.valor[0] / 100))
                valor2 = self.valor[1]
                if valor1 > valor2:
                    valor = valor1
                else:
                    valor = valor2
            
            if habilidade is not None:
                valor = habilidade.ContabilizarModificadores(valor, usuario)

                # Acerto Crítico
                chance_critico = usuario.chance_critico + habilidade.chance_critico
                multiplicador_critico = usuario.multiplicador_critico * habilidade.multiplicador_critico

                if utils.CalcularChance(chance_critico / 100):
                    valor = math.ceil(valor * multiplicador_critico)
                    print(Fore.GREEN + 'CRÍTICO!' + Style.RESET_ALL + ' ', end = '')

            alvo.hp += valor

            # Buff foi causado através de um item
            if item is not None:
                mensagem = f'{artigo} {item.nome} recuperou {valor} de ' + Fore.RED + 'HP' + Style.RESET_ALL + f' de {alvo.nome}.'
            # Buff foi causado através de uma habilidade ou outra fonte
            else:
                mensagem = f'{alvo.nome} recuperou {valor} de ' + Fore.RED + 'HP' + Style.RESET_ALL + '.'

            sobrecura_hp = 1

        # Cura a Mana em um valor definido, com base na Mana máxima ou o que for maior dentre estas opções
        elif self.nome == "Cura Mana" or self.nome == "Cura Mana %" or self.nome == "Cura Mana % ou valor":
            valor = 0

            if self.nome == "Cura Mana":
                valor = self.valor
            elif self.nome == "Cura Mana %":
                valor = math.floor(alvo.maxMana * (self.valor / 100))
            else:
                valor1 = math.floor(alvo.maxMana * (self.valor[0] / 100))
                valor2 = self.valor[1]
                if valor1 > valor2:
                    valor = valor1
                else:
                    valor = valor2
            
            if habilidade is not None:
                valor = habilidade.ContabilizarModificadores(valor, usuario)

                # Acerto Crítico
                chance_critico = usuario.chance_critico + habilidade.chance_critico
                multiplicador_critico = usuario.multiplicador_critico * habilidade.multiplicador_critico

                if utils.CalcularChance(chance_critico / 100):
                    valor = math.ceil(valor * multiplicador_critico)
                    print(Fore.GREEN + 'CRÍTICO!' + Style.RESET_ALL + ' ', end = '')

            alvo.mana += valor

            # Buff foi causado através de um item
            if item is not None:
                mensagem = f'{artigo} {item.nome} recuperou {valor} de ' + Fore.BLUE + 'Mana' + Style.RESET_ALL + f' de {alvo.nome}.'
            # Buff foi causado através de uma habilidade ou outra fonte
            else:
                mensagem = f'{alvo.nome} recuperou {valor} de ' + Fore.BLUE + 'Mana' + Style.RESET_ALL + '.'

            sobrecura_mana = 1

        # Regenera o HP em um valor definido ou com base no HP máximo durante vários turnos
        elif self.nome == "Regeneração HP" or self.nome == "Regeneração HP %":
            valor = 0

            if self.nome == "Regeneração HP":
                valor = self.valor
            elif self.nome == "Regeneração HP %":
                valor = math.floor(alvo.maxHp * (self.valor / 100))
            
            # Se o efeito de regeneração foi causado fora de combate: recuperar todo o HP de uma vez
            if fora_combate:
                valor *= self.duracao

            alvo.hp += valor

            # Buff foi causado através de um item
            if item is not None:
                mensagem = f'{artigo} {item.nome} recuperou {valor} de ' + Fore.RED + 'HP' + Style.RESET_ALL + f' de {alvo.nome}.'
            # Buff foi causado através de uma habilidade ou outra fonte
            else:
                mensagem = f'{alvo.nome} recuperou {valor} de ' + Fore.RED + 'HP' + Style.RESET_ALL + '.'

            if not fora_combate:
                regen = deepcopy(self)
                regen.duracao -= regen.decaimento
                if append:
                    alvo.buffs.append(regen)
            
            sobrecura_hp = 1
        
        # Aumento de Atributo
        elif self.nome == "Aumento Ataque" or self.nome == "Aumento Defesa" or \
            self.nome == "Aumento Magia" or self.nome == "Aumento Velocidade" or \
            self.nome == "Aumento Chance Crítico":

            aumento = deepcopy(self)
            valor_aumento = self.valor
            if habilidade is not None:
                valor_aumento = habilidade.ContabilizarModificadores(valor_aumento, usuario)
            aumento.valor = valor_aumento

            # Se a criatura já está sob o efeito de aumento do atributo
            if alvo.EfeitoPresente(self.nome) is not None:
                efeito_presente = alvo.EfeitoPresente(self.nome)
                efeito_presente.duracao += 1
                efeito_presente.valor += math.floor(0.25 * efeito_presente.valor)

                if self.nome == "Aumento Ataque":
                    alvo.ataque += math.floor(0.25 * efeito_presente.valor)
                    print(f'{alvo.nome} teve seu aumento de ataque melhorado em 25% e a duração do efeito extendida em 1 turno.')
                elif self.nome == "Aumento Defesa":
                    alvo.defesa += math.floor(0.25 * efeito_presente.valor)
                    print(f'{alvo.nome} teve seu aumento de defesa melhorado em 25% e a duração do efeito extendida em 1 turno.')
                elif self.nome == "Aumento Magia":
                    alvo.magia += math.floor(0.25 * efeito_presente.valor)
                    print(f'{alvo.nome} teve seu aumento de magia melhorado em 25% e a duração do efeito extendida em 1 turno.')
                elif self.nome == "Aumento Velocidade":
                    alvo.velocidade += math.floor(0.25 * efeito_presente.valor)
                    print(f'{alvo.nome} teve seu aumento de velocidade melhorado em 25% e a duração do efeito extendida em 1 turno.')
                elif self.nome == "Aumento Chance Crítico":
                    alvo.chance_critico += math.floor(0.25 * efeito_presente.valor)
                    print(f'{alvo.nome} teve seu aumento de chance de crítico melhorado em 25% e a duração do efeito extendida em 1 turno.')

            # Se a criatura não está sob o efeito de aumento do atributo
            else:
                if append:
                    alvo.buffs.append(aumento)
                
                if self.nome == "Aumento Ataque":
                    alvo.ataque += valor_aumento
                    if self.duracao >= 999:
                        print(f'{alvo.nome} teve seu ataque aumentado em {valor_aumento} até o fim da batalha.')
                    else:
                        print(f'{alvo.nome} teve seu ataque aumentado em {valor_aumento} por {self.duracao} turnos.')

                elif self.nome == "Aumento Defesa":
                    alvo.defesa += valor_aumento
                    if self.duracao >= 999:
                        print(f'{alvo.nome} teve sua defesa aumentada em {valor_aumento} até o fim da batalha.')
                    else:
                        print(f'{alvo.nome} teve sua defesa aumentada em {valor_aumento} por {self.duracao} turnos.')

                elif self.nome == "Aumento Magia":
                    alvo.magia += valor_aumento
                    if self.duracao >= 999:
                        print(f'{alvo.nome} teve sua magia aumentada em {valor_aumento} até o fim da batalha.')
                    else:
                        print(f'{alvo.nome} teve sua magia aumentada em {valor_aumento} por {self.duracao} turnos.')

                elif self.nome == "Aumento Velocidade":
                    alvo.velocidade += valor_aumento
                    if self.duracao >= 999:
                        print(f'{alvo.nome} teve sua velocidade aumentada em {valor_aumento} até o fim da batalha.')
                    else:
                        print(f'{alvo.nome} teve sua velocidade aumentada em {valor_aumento} por {self.duracao} turnos.')

                elif self.nome == "Aumento Chance Crítico":
                    alvo.chance_critico += valor_aumento
                    if self.duracao >= 999:
                        print(f'{alvo.nome} teve sua chance de crítico aumentada em {valor_aumento}% até o fim da batalha.')
                    else:
                        print(f'{alvo.nome} teve sua chance de crítico aumentada em {valor_aumento}% por {self.duracao} turnos.')

        # Criatura está defendendo
        elif self.nome == "Defendendo":
            defendendo = deepcopy(self)
            if append:
                alvo.buffs.append(defendendo)
            print(f'{alvo.nome} está defendendo.')
        
        # Cura debuff de envenenamento
        elif self.nome == "Cura Veneno":
            debuff = alvo.EfeitoPresente("Veneno")
            if debuff is not None:
                alvo.debuffs.remove(debuff)

                # Buff foi causado através de um item
                if item is not None:
                    mensagem = f'{artigo} {item.nome} curou o ' + Fore.GREEN + 'envenenamento' + Style.RESET_ALL + f' de {alvo.nome}.'
                # Buff foi causado através de uma habilidade ou outra fonte
                else:
                    mensagem = f'O ' + Fore.GREEN + 'envenenamento' + Style.RESET_ALL + f' de {alvo.nome} foi curado.'

        # Caso o HP ou Mana estrapole o valor máximo
        if sobrecura_hp == 1 and alvo.hp >= alvo.maxHp:
            alvo.hp = alvo.maxHp

            if item is not None:
                mensagem = f'{artigo} {item.nome} maximizou o ' + Fore.RED + 'HP' + Style.RESET_ALL + f' de {alvo.nome}.'
            elif habilidade is not None:
                mensagem = f'O ' + Fore.RED + 'HP' + Style.RESET_ALL + f' de {alvo.nome} foi maximizado.'

        if sobrecura_mana == 1 and alvo.mana >= alvo.maxMana:
            alvo.mana = alvo.maxMana

            if item is not None:
                mensagem = f'{artigo} {item.nome} maximizou a ' + Fore.BLUE + 'Mana' + Style.RESET_ALL + f' de {alvo.nome}.'
            elif habilidade is not None:
                mensagem = f'A ' + Fore.BLUE + 'Mana' + Style.RESET_ALL + f' de {alvo.nome} foi maximizada.'

        if mensagem is not None:
            print(mensagem)

        ## Efeitos de Debuff ##

        # Dá dano em todos os inimigos
        if self.nome == "Dano":
            if item is not None:
                dano, acerto_critico = utils.CalcularDano(usuario, alvo, item = item)
            elif habilidade is not None:
                dano, acerto_critico = utils.CalcularDano(usuario, alvo, habilidade = habilidade)

            alvo.hp -= dano
            if alvo.hp < 0:
                alvo.hp = 0
            
            if item is not None:
                print(f'{artigo} {item.nome} infligiu {dano} de dano em {alvo.nome}.')
            elif habilidade is not None:
                print(f'{habilidade.nome} infligiu {dano} de dano em {alvo.nome}.')

        elif self.nome == "Veneno":

            chance_veneno = self.chance
            chance_resistencia = 0

            # Calculando a chance de resistir ao veneno
            buff = alvo.EfeitoPresente('Resistência Veneno')
            if buff is not None:
                chance_resistencia += buff.valor
            
            if chance_resistencia > 1:
                chance_resistencia = 1

            chance = chance_veneno * (1 - chance_resistencia)

            if utils.CalcularChance(chance):
                veneno = deepcopy(self)
                if append:
                    alvo.debuffs.append(veneno)
                print(f'{usuario.nome} ' + Fore.GREEN + 'envenenou' + Style.RESET_ALL + f' {alvo.nome}!')
                alvo.CombinarEfeito("Veneno")
        
        elif self.nome == "Atordoamento":
            atordoamento = deepcopy(self)
            if append:
                alvo.debuffs.append(atordoamento)
            print(f'{usuario.nome} atordoou {alvo.nome}!')
            alvo.CombinarEfeito("Atordoamento")
        
        elif self.nome == "Lentidão":
            debuff_ja_presente = alvo.EfeitoPresente("Lentidão")

            lentidao = deepcopy(self)
            lentidao.nome = "Lentidão"
            lentidao.valor = alvo.velocidade
            alvo.velocidade = 0
            if append:
                alvo.debuffs.append(lentidao)

            # Debuff foi causado através de um item
            if item is not None:
                if debuff_ja_presente is None:
                    if lentidao.duracao > 1:
                        print(f'{artigo} {item.nome} infligiu Lentidão em {alvo.nome} por {self.duracao} turnos.')
                    else:
                        print(f'{artigo} {item.nome} infligiu Lentidão em {alvo.nome} por {self.duracao} turno.')
                else:
                    if lentidao.duracao > 1:
                        print(f'{artigo} {item.nome} infligiu Lentidão em {alvo.nome} por mais {self.duracao} turnos.')
                    else:
                        print(f'{artigo} {item.nome} infligiu Lentidão em {alvo.nome} por mais {self.duracao} turno.')
            
            # Debuff foi causado através de uma habilidade
            elif habilidade is not None:
                if debuff_ja_presente is None:
                    if lentidao.duracao > 1:
                        print(f'{usuario.nome} infligiu Lentidão em {alvo.nome} por {lentidao.duracao} turnos.')
                    else:
                        print(f'{usuario.nome} infligiu Lentidão em {alvo.nome} por {lentidao.duracao} turno.')
                else:
                    if lentidao.duracao > 1:
                        print(f'{usuario.nome} infligiu Lentidão em {alvo.nome} por mais {lentidao.duracao} turnos.')
                    else:
                        print(f'{usuario.nome} infligiu Lentidão em {alvo.nome} por mais {lentidao.duracao} turno.')

            alvo.CombinarEfeito("Lentidão")

        # Diminuição de Atributo
        elif self.nome == "Diminuição Ataque" or self.nome == "Diminuição Defesa" or \
            self.nome == "Diminuição Magia" or self.nome == "Diminuição Velocidade" or \
            self.nome == "Diminuição Chance Crítico":

            diminuicao = deepcopy(self)
            valor_diminuicao = self.valor
            if habilidade is not None:
                valor_diminuicao = habilidade.ContabilizarModificadores(valor_diminuicao, usuario)
            diminuicao.valor = valor_diminuicao

            # Se a criatura já está sob o efeito de diminuição do atributo
            if alvo.EfeitoPresente(self.nome) is not None:
                debuff = alvo.EfeitoPresente(self.nome)
                debuff.duracao += 1
                debuff.valor += math.floor(0.25 * debuff.valor)

                if self.nome == "Diminuição Ataque":
                    alvo.ataque -= math.floor(0.25 * debuff.valor)
                    print(f'{alvo.nome} teve sua diminuição de ataque piorada em 25% e a duração do efeito extendida em 1 turno.')
                elif self.nome == "Diminuição Defesa":
                    alvo.defesa -= math.floor(0.25 * debuff.valor)
                    print(f'{alvo.nome} teve sua diminuição de defesa piorada em 25% e a duração do efeito extendida em 1 turno.')
                elif self.nome == "Diminuição Magia":
                    alvo.magia -= math.floor(0.25 * debuff.valor)
                    print(f'{alvo.nome} teve sua diminuição de magia piorada em 25% e a duração do efeito extendida em 1 turno.')
                elif self.nome == "Diminuição Velocidade":
                    alvo.velocidade -= math.floor(0.25 * debuff.valor)
                    print(f'{alvo.nome} teve sua diminuição de velocidade piorada em 25% e a duração do efeito extendida em 1 turno.')
                elif self.nome == "Diminuição Chance Crítico":
                    alvo.chance_critico -= math.floor(0.25 * debuff.valor)
                    print(f'{alvo.nome} teve sua diminuição de chance de crítico piorada em 25% e a duração do efeito extendida em 1 turno.')

            # Se a criatura não está sob o efeito de diminuição do atributo
            else:
                if append:
                    alvo.debuffs.append(diminuicao)
                
                if self.nome == "Diminuição Ataque":
                    alvo.ataque -= valor_diminuicao
                    if self.duracao >= 999:
                        print(f'{alvo.nome} teve seu ataque diminuído em {valor_diminuicao} até o fim da batalha.')
                    else:
                        print(f'{alvo.nome} teve seu ataque diminuído em {valor_diminuicao} por {self.duracao} turnos.')
                
                elif self.nome == "Diminuição Defesa":
                    alvo.defesa -= valor_diminuicao
                    if self.duracao >= 999:
                        print(f'{alvo.nome} teve sua defesa diminuída em {valor_diminuicao} até o fim da batalha.')
                    else:
                        print(f'{alvo.nome} teve sua defesa diminuída em {valor_diminuicao} por {self.duracao} turnos.')
                
                elif self.nome == "Diminuição Magia":
                    alvo.magia -= valor_diminuicao
                    if self.duracao >= 999:
                        print(f'{alvo.nome} teve sua magia diminuída em {valor_diminuicao} até o fim da batalha.')
                    else:
                        print(f'{alvo.nome} teve sua magia diminuída em {valor_diminuicao} por {self.duracao} turnos.')
                
                elif self.nome == "Diminuição Velocidade":
                    alvo.velocidade -= valor_diminuicao
                    if self.duracao >= 999:
                        print(f'{alvo.nome} teve sua velocidade diminuída em {valor_diminuicao} até o fim da batalha.')
                    else:
                        print(f'{alvo.nome} teve sua velocidade diminuída em {valor_diminuicao} por {self.duracao} turnos.')
                
                elif self.nome == "Diminuição Chance Crítico":
                    alvo.chance_critico -= valor_diminuicao
                    if self.duracao >= 999:
                        print(f'{alvo.nome} teve sua chance de crítico diminuída em {valor_diminuicao}% até o fim da batalha.')
                    else:
                        print(f'{alvo.nome} teve sua chance de crítico diminuída em {valor_diminuicao}% por {self.duracao} turnos.')

    def CombinarEfeito(self, efeito):
        """
        Combina os atributos de si mesmo com os de um outro efeito.
        """

        if self.nome == 'Veneno' and efeito.nome == 'Veneno':
            self.valor += efeito.valor
            self.duracao += efeito.duracao
            self.chance += efeito.chance
