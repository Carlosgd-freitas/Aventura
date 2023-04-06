import sys
import math
from copy import deepcopy
from colorama import Fore, Back, Style

from . import invocar_criaturas, batalha_chefao

sys.path.append("..")
from base import imprimir, utils
from itens import espolios

def InicioBatalha(criatura, verbose = True):
    """
    Esta função é chamada no início da batalha.
    """

    # Ativando o efeito de certas habilidades passivas
    if criatura.HabilidadePresente("Regeneração") is not None:
        habilidade = criatura.HabilidadePresente("Regeneração")
        efeito_regen = deepcopy(habilidade.efeitos[0])
        criatura.buffs.append(efeito_regen)

def InicioTurno(criatura, verbose = True):
    """
    Esta função é chamada no início do turno da criatura e retorna 0 caso a criatura esteja atordoada.
    """

    # Flags
    consciente = 1

    if criatura.hp > 0:

        # Aplicando efeitos de buff
        if criatura.EfeitoPresente("Regeneração HP") is not None:
            buff = criatura.EfeitoPresente("Regeneração HP")
            buff.Processar(criatura, criatura, append = False)
        elif criatura.EfeitoPresente("Regeneração HP %") is not None:
            buff = criatura.EfeitoPresente("Regeneração HP %")
            buff.Processar(criatura, criatura, append = False)

        # Aplicando efeitos de debuff
        criatura.CombinarEfeito("Veneno")
        criatura.CombinarEfeito("Atordoamento")
        criatura.CombinarEfeito("Lentidão")

        if criatura.EfeitoPresente("Veneno") is not None:
            debuff = criatura.EfeitoPresente("Veneno")
            valor = debuff.valor
            criatura.hp -= valor
            print(f'{criatura.nome} sofreu {valor} de dano do ' + Fore.GREEN + 'envenenamento' + Style.RESET_ALL + '!')
        
        elif criatura.EfeitoPresente("Atordoamento") is not None:
            debuff = criatura.EfeitoPresente("Atordoamento")

            if debuff.duracao != 0:
                consciente = 0
                
                if criatura.singular_plural == "singular":
                    if criatura.genero == "M":
                        print(f'{criatura.nome} está atordoado e não pode agir!')
                    elif criatura.genero == "F":
                        print(f'{criatura.nome} está atordoada e não pode agir!')

                elif criatura.singular_plural == "plural":
                    if criatura.genero == "M":
                        print(f'{criatura.nome} estão atordoados e não podem agir!')
                    elif criatura.genero == "F":
                        print(f'{criatura.nome} estão atordoadas e não podem agir!')

    return consciente

def AcrescentarRecargas(criatura):
    """
    Acrescenta em 1 a recarga atual de todas as habilidades de uma criatura ou jogador caso ela não seja igual à
    recarga. Se alguma habilidade da criatura foi recarregada, a função retorna 1 e, caso contrário, retorna 0.
    """

    recarregou = 0

    for h in criatura.habilidades:
        if h.recarga_atual < h.recarga:
            h.recarga_atual += 1
            recarregou = 1
    
    return recarregou

def DecairBuffsDebuffs(criatura, nao_decair = [], verbose = 1, terminar = False):
    """
    Aplica o decaimento no valor de cada buff e debuff presente na criatura. Se houve algum decaimento de buff ou
    debuff na criatura, a função retorna 1 e, caso contrário, retorna 0.

    Parâmetros:
    - criatura: criatura que terá os efeitos de buff e debuff decaídos.

    Parâmetros opcionais:
    - nao_decair: lista de nomes de efeitos que não serão decaídos da criatura. O valor padrão é uma lista vazia.
    - verbose: se igual a 0, a função não imprime quaisquer mensagens. O valor padrão é 1.
    """

    # Se não há buffs ou debuffs presentes na criatura
    if (not criatura.buffs) and (not criatura.debuffs):
        return 0

    # Se há apenas buffs e debuffs na criatura que não devem decair
    buff_nao = 1
    debuff_nao = 1

    for b in criatura.buffs:
        if b.nome not in nao_decair:
            buff_nao = 0

    if buff_nao == 1:
        for d in criatura.debuffs:
            if d.nome not in nao_decair:
                debuff_nao = 0

        if debuff_nao == 1:
            return 0

    # Flags
    efeitos_expirados = []
    duracao_pre_termino = 0
    
    # Decaindo Buffs
    for indice, buff in enumerate(criatura.buffs):
        if buff.nome not in nao_decair:

            if not terminar:
                buff.duracao -= buff.decaimento
            else:
                duracao_pre_termino = buff.duracao
                buff.duracao -= 9999
            
            if buff.duracao <= 0 and criatura.hp > 0:
                efeitos_expirados.append(indice)

                # Defendendo
                if buff.nome == "Defendendo" and verbose == 1:
                    print(f'{criatura.nome} não está mais defendendo.')
                
                # Aumento de atributo: Ataque, Defesa, Magia, Velocidade, Chance de Crítico
                elif buff.nome == "Aumento Ataque":
                    criatura.ataque -= buff.valor
                    if verbose == 1:
                        print(f'O aumento de ataque de {criatura.nome} terminou.')

                elif buff.nome == "Aumento Defesa":
                    criatura.defesa -= buff.valor
                    if verbose == 1:
                        print(f'O aumento de defesa de {criatura.nome} terminou.')

                elif buff.nome == "Aumento Magia":
                    criatura.magia -= buff.valor
                    if verbose == 1:
                        print(f'O aumento de magia de {criatura.nome} terminou.')

                elif buff.nome == "Aumento Velocidade":
                    criatura.velocidade -= buff.valor
                    if verbose == 1:
                        print(f'O aumento de velocidade de {criatura.nome} terminou.')

                elif buff.nome == "Aumento Chance Crítico":
                    criatura.chance_critico -= buff.valor
                    if verbose == 1:
                        print(f'O aumento de chance de crítico de {criatura.nome} terminou.')

                # Regeneração de HP em um valor definido ou com base no HP máximo
                elif buff.nome == "Regeneração HP" or buff.nome == "Regeneração HP %":

                    # Curando a criatura com o restante do efeito de regeneração de HP
                    if terminar:
                        if buff.nome == "Regeneração HP":
                            criatura.hp += duracao_pre_termino * buff.valor
                        elif buff.nome == "Regeneração HP %":
                            valor = duracao_pre_termino * math.floor(criatura.maxHp * (buff.valor / 100))
                            criatura.hp += valor

                        if criatura.hp > criatura.maxHp:
                            criatura.hp = criatura.maxHp
                            print(f'O ' + Fore.RED + 'HP' + Style.RESET_ALL + f' de {criatura.nome} foi maximizado' +
                                ' pelo restante do efeito de regeneração.')
                        else:
                            print(f'{criatura.nome} recuperou {valor} de ' + Fore.RED + 'HP' + Style.RESET_ALL + 
                                ' pelo restante do efeito de regeneração.')

                        if verbose == 1:
                            print('A regeneração de ' + Fore.RED + 'HP' + Style.RESET_ALL + f' de {criatura.nome} terminou.')
        
                # Resistência a Veneno
                elif buff.nome == "Resistência Veneno" and verbose == 1:
                    print(f'{criatura.nome} não possui mais resistência a ' + Fore.GREEN + 'Veneno' +
                        Style.RESET_ALL + '.')

    # Removendo Buffs expirados
    indice = 0
    for i in efeitos_expirados:
        criatura.buffs.pop(i - indice)
        indice += 1

    # Decaindo Debuffs
    efeitos_expirados = []
    for indice, debuff in enumerate(criatura.debuffs):

        if debuff.nome not in nao_decair:

            if not terminar:
                debuff.duracao -= debuff.decaimento
            else:
                duracao_pre_termino = debuff.duracao
                debuff.duracao -= 9999

            # Atordoamento
            if debuff.nome == "Atordoamento" and debuff.duracao <= -1 and criatura.hp > 0:
                efeitos_expirados.append(indice)

                if verbose == 1:
                    if criatura.singular_plural == "singular":
                        if criatura.genero == "M":
                            print(f'{criatura.nome} não está mais atordoado.')
                        elif criatura.genero == "F":
                            print(f'{criatura.nome} não está mais atordoada.')

                    elif criatura.singular_plural == "plural":
                        if criatura.genero == "M":
                            print(f'{criatura.nome} não estão mais atordoados.')
                        elif criatura.genero == "F":
                            print(f'{criatura.nome} não estão mais atordoadas.')

            # Demais debuffs
            elif debuff.duracao <= 0 and criatura.hp > 0:
                efeitos_expirados.append(indice)

                # Veneno
                if debuff.nome == "Veneno" and verbose == 1:
                    if criatura.singular_plural == "singular":
                        if criatura.genero == "M":
                            print(f'{criatura.nome} não está mais ' + Fore.GREEN + 'envenenado' + Style.RESET_ALL + '.')
                        elif criatura.genero == "F":
                            print(f'{criatura.nome} não está mais ' + Fore.GREEN + 'envenenada' + Style.RESET_ALL + '.')

                    elif criatura.singular_plural == "plural":
                        if criatura.genero == "M":
                            print(f'{criatura.nome} não estão mais ' + Fore.GREEN + 'envenenados' + Style.RESET_ALL + '.')
                        elif criatura.genero == "F":
                            print(f'{criatura.nome} não estão mais ' + Fore.GREEN + 'envenenadas' + Style.RESET_ALL + '.')
            
                # Lentidão
                elif debuff.nome == "Lentidão":
                    criatura.velocidade += debuff.valor
                    if verbose == 1:
                        print(f'{criatura.nome} não está mais sob o efeito de Lentidão.')

                # Diminuição de atributo: Ataque, Defesa, Magia, Velocidade, Chance de Crítico
                elif debuff.nome == "Diminuição Ataque":
                    criatura.ataque += debuff.valor
                    if verbose == 1:
                        print(f'A diminuição de ataque de {criatura.nome} terminou.')

                elif debuff.nome == "Diminuição Defesa":
                    criatura.defesa += debuff.valor
                    if verbose == 1:
                        print(f'A diminuição de defesa de {criatura.nome} terminou.')

                elif debuff.nome == "Diminuição Magia":
                    criatura.magia += debuff.valor
                    if verbose == 1:
                        print(f'A diminuição de magia de {criatura.nome} terminou.')

                elif debuff.nome == "Diminuição Velocidade":
                    criatura.velocidade += debuff.valor
                    if verbose == 1:
                        print(f'A diminuição de velocidade de {criatura.nome} terminou.')

                elif debuff.nome == "Diminuição Chance Crítico":
                    criatura.chance_critico += debuff.valor
                    if verbose == 1:
                        print(f'A diminuição de chance de crítico de {criatura.nome} terminou.')
    
    # Removendo Debuffs expirados
    indice = 0
    for i in efeitos_expirados:
        criatura.debuffs.pop(i - indice)
        indice += 1

    return 1

def EscolherAlvo(criaturas):
    """
    Imprime as possíveis criaturas que o jogador pode atacar ou usar uma habilidade de alvo único e retorna
    o índice da lista de criaturas correspondente ao alvo escolhido.
    """

    print('\nEscolha quem deseja atacar:')
    imprimir.InimigosPresentes(criaturas)

    print('[0] Retornar e escolher outra ação.\n')

    alvo = utils.LerNumeroIntervalo('> ', 0, len(criaturas))
    return alvo

def GerarEspolios(criatura):
    """
    Retorna uma lista contendo os espólios de uma criatura derrotada.
    """

    lista_espolios = []

    # Ouro e Itens que o jogador irá ganhar por ter derrotado a criatura
    for e in criatura.espolios:
        if utils.CalcularChance(e[0] / 100):
            lista_espolios.append(e[1])
    
    # Experiência que o jogador irá ganhar por ter derrotado a criatura
    exp = espolios.Experiencia(criatura.experiencia)
    lista_espolios.append(exp)

    return lista_espolios

def AbaterCriaturas(lista_criaturas, lista_espolios, criatura = None, gerar_espolios = True, nomes = None, nomes_zerados = None, conf = None, chefao = 0):
    """
    Remove quaisquer criaturas que possuam 0 ou menos de HP da lista de criaturas. Retorna 1 caso <criatura> for
    removida da lista de criaturas ou 0 caso contrário.

    Parâmetros:
    - lista_criaturas: lista que contém as possíveis criaturas a serem derrotadas;
    - lista_espolios: lista contendo os espólios ganhos durante uma batalha.
    
    Parâmetros opcionais:
    - criatura: criatura que pode morrer enquanto realiza seu turno. Por padrão, nenhuma criatura é passada por
    parâmetro;
    - gerar_espolios: se for igual a True, adiciona os espólios gerados a lista de espólios caso uma criatura
    seja abatida. O valor padrão é True;
    - nomes: dicionário gerado pelo sistema de adicionar sufixos aos nomes das criaturas. Por padrão, nenhum
    dicionário é passado por parâmetro.
    - nomes_zerados: dicionário gerado pelo sistema de adicionar sufixos aos nomes das criaturas. Por padrão,
    nenhum dicionário é passado por parâmetro.
    - conf: configurações do usuário relativas ao jogo. Por padrão, nenhuma configuração é passada por parâmetro;
    - chefao: número da batalha contra um chefão. O valor padrão é 0 (a batalha não é contra um chefão).
    """

    morreu = 0
    indice = 0
    criaturas_derrotadas = []

    for c in lista_criaturas:
        if c.hp <= 0:

            if chefao == 0:
                if c.singular_plural == "singular":
                    if c.genero == "M":
                        print(f'{c.nome} foi derrotado!')
                    elif c.genero == "F":
                        print(f'{c.nome} foi derrotada!')

                elif c.singular_plural == "plural":
                    if c.genero == "M":
                        print(f'{c.nome} foram derrotados!')
                    elif c.genero == "F":
                        print(f'{c.nome} foram derrotadas!')
            
            elif chefao != 0:
                batalha_chefao.DialogoChefaoDerrotado(chefao, lista_criaturas, c, conf)
                batalha_chefao.ChefaoDerrotado(chefao, lista_criaturas, c, conf)

            # Adicionando os espólios gerados à lista de espólios passada por parâmetro
            if gerar_espolios:
                espolios_gerados = GerarEspolios(c)
                for e in espolios_gerados:
                    lista_espolios.append(e)

            # Criatura passada por parâmetro foi derrotada
            if criatura is not None and c == criatura:
                morreu = 1
            
            # Habilidades que ativam quando a criatura é derrotada
            for h in c.habilidades:
                if h.alvo == "Invocação":
                    lista_criaturas = invocar_criaturas.InvocarCriaturas(c, h, lista_criaturas, nomes, nomes_zerados)

            criaturas_derrotadas.append(indice)

            # Ativando habilidades de outras criaturas alidas
            for c2 in lista_criaturas:
                if c2.hp > 0 and c2 != c:

                    for h in c2.habilidades:
                        if h.nome == "Vingança":
                            efeito = deepcopy(h.efeitos[0])
                            conteudo = efeito.nome.split(":") # ["Vingança", "Larva de Abelhóide", "Aumento Ataque", "F"]
                            derrotada = conteudo[1]

                            if utils.CompararNomes([c.nome, derrotada]):

                                if c2.singular_plural == 'singular':
                                    if c2.genero == 'M':
                                        print(f'{c2.nome} se sente vingativo!')
                                    elif c2.genero == 'F':
                                        print(f'{c2.nome} se sente vingativa!')

                                elif c2.singular_plural == 'plural':
                                    if c2.genero == 'M':
                                        print(f'{c2.nome} se sentem vingativos!')
                                    elif c2.genero == 'F':
                                        print(f'{c2.nome} se sentem vingativas!')

                                efeito.nome = conteudo[2]
                                efeito.Processar(c2, c2, habilidade = h)
        
        indice += 1
    
    # Removendo criaturas derrotadas
    indice = 0
    for i in criaturas_derrotadas:
        lista_criaturas.pop(i - indice)
        indice += 1

    # Compactando lista de espólios
    indice_1 = 0
    for espolio_1 in lista_espolios:

        indice_2 = 0
        for espolio_2 in lista_espolios:

            if espolio_1.nome == espolio_2.nome and indice_1 != indice_2:
                espolio_1.quantidade += espolio_2.quantidade
                lista_espolios.remove(espolio_2)
            
            indice_2 += 1
        
        indice_1 += 1

    return morreu

def TerminarBuffsDebuffs(criatura, nao_terminar = ['Veneno']):
    """
    Processa cada um dos buffs e debuffs ainda presentes na criatura ao fim de uma batalha.
    
    Parâmetros:
    - criatura: criatura presente no fim da batalha que terá os efeitos de buff e debuff terminados.

    Parâmetros opcionais:
    - nao_terminar: lista de nomes de efeitos que não serão removidos da criatura. O valor padrão é uma lista
    contendo o efeito 'Veneno'.
    """

    while True:
        decaiu = DecairBuffsDebuffs(criatura, nao_decair = nao_terminar, verbose = 0, terminar = True)

        if decaiu == 0:
            break

def AcrescentarRecargasMaximo(criatura):
    """
    Recarrega completamente todas as habilidades de uma criatura.

    Parâmetros:
    - criatura: criatura que terá as habilidades recarregadas.
    """

    while True:
        recarregou = AcrescentarRecargas(criatura)

        if recarregou == 0:
            break
