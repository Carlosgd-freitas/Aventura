import math
import random
from colorama import Fore, Back, Style

from . import mecanicas

def AlvoUnico(atacante, alvo, habilidade):
    """
    Utiliza uma habilidade em um único alvo e retorna o dano infligido.
    """

    dano = mecanicas.CalcularDano(atacante, alvo, habilidade)

    if not habilidade.nao_causa_dano:
        alvo.hp -= dano

    # Custos da habilidade
    for c in habilidade.custo:
        if c[0] == "Mana":
            atacante.mana -= c[1]

        elif c[0] == "HP":
            atacante.hp -= c[1]
    
    # Adicionando efeitos ao ataque normal temporariamente
    for h in atacante.habilidades:
        if h.nome == "Envenenamento":
            efeito = h.efeitos[0]
            atacante.habilidades[0].efeitos.append(efeito)
    
    # Aplicando Debuffs no Alvo
    AplicarEfeitos(atacante, alvo, habilidade)
    
    # Removendo os efeitos temporários do ataque normal
    atacante.habilidades[0].efeitos = []

    # Zerando a recarga atual da habilidade
    habilidade.recarga_atual = -1

    return dano

def AlvoMultiplo(atacante, alvos, habilidade):
    """
    Utiliza uma habilidade em múltiplos alvos e retorna uma lista contendo o dano infligido em cada um.
    """

    # Custos da habilidade
    for c in habilidade.custo:
        if c[0] == "Mana":
            atacante.mana -= c[1]

        elif c[0] == "HP":
            atacante.hp -= c[1]
    
    # Adicionando efeitos ao ataque normal temporariamente
    for h in atacante.habilidades:
        if h.nome == "Envenenamento":
            efeito = h.efeitos[0]
            atacante.habilidades[0].efeitos.append(efeito)

    danos = []

    for alvo in alvos:
        dano = mecanicas.CalcularDano(atacante, alvo, habilidade)
        danos.append(dano)

        if not habilidade.nao_causa_dano:
            alvo.hp -= dano

        # Aplicando Debuffs no Alvo
        AplicarEfeitos(atacante, alvo, habilidade)
        
    # Removendo os efeitos temporários do ataque normal
    atacante.habilidades[0].efeitos = []

    # Zerando a recarga atual da habilidade
    habilidade.recarga_atual = -1

    return danos

def AlvoProprio(criatura, habilidade):
    """
    Utiliza uma habilidade em si próprio.
    """

    # Custos da habilidade
    for c in habilidade.custo:
        if c[0] == "Mana":
            criatura.mana -= c[1]

        elif c[0] == "HP":
            criatura.hp -= c[1]

    # Aplicando Buffs em si próprio
    AplicarEfeitos(criatura, criatura, habilidade)
                
    # Zerando a recarga atual da habilidade
    habilidade.recarga_atual = -1

def AplicarEfeitos(usuario, alvo, habilidade):
    """
    Aplica efeitos de buffs e debuffs de uma habilidade, utilizada por um usuario, em uma criatura alvo.
    """

    for e in habilidade.efeitos:
        chance = random.randint(1, 100)

        # Efeitos de Buff
        if e.nome == "Defendendo" and chance <= e.chance:
            defendendo = e.ClonarEfeito()
            alvo.buffs.append(defendendo)
            print(f'{alvo.nome} está defendendo.')
        
        elif e.nome == "Aumento Defesa" and chance <= e.chance:
            aumento = e.ClonarEfeito()

            valor_aumento = e.valor # Valor Base
            for m in habilidade.modificadores: # Modificadores
                if m[0] == "ataque":
                    valor_aumento += usuario.ataque * (m[1] / 100)
                elif m[0] == "magia":
                    valor_aumento += usuario.magia * (m[1] / 100)
            
            valor_aumento = math.floor(valor_aumento)
            aumento.valor = valor_aumento

            # Se a criatura já está sob o efeito de aumento de defesa
            if alvo.EfeitoPresente("buff", "Aumento Defesa") != -1:
                indice = alvo.EfeitoPresente("buff", "Aumento Defesa")
                alvo.defesa += math.floor(0.25 * alvo.buffs[indice].valor)
                alvo.buffs[indice].duracao += 1
                alvo.buffs[indice].valor += math.floor(0.25 * alvo.buffs[indice].valor)
                print(f'{alvo.nome} teve seu aumento de defesa melhorado em 25% e a duração do efeito extendida em 1 turno.')

            # Se a criatura não está sob o efeito de aumento de defesa
            else:
                alvo.buffs.append(aumento)
                alvo.defesa += valor_aumento
                print(f'{alvo.nome} aumentou sua defesa em {valor_aumento} por {e.duracao} turnos.')

        # Efeitos de Debuff
        elif e.nome == "Veneno" and chance <= e.chance:
            veneno = e.ClonarEfeito()
            alvo.debuffs.append(veneno)
            print(f'{usuario.nome} ' + Fore.GREEN + 'envenenou' + Style.RESET_ALL + f' {alvo.nome}!')
            alvo.CombinarEfeito("Veneno")
        
        elif e.nome == "Atordoamento" and chance <= e.chance:
            atordoamento = e.ClonarEfeito()
            alvo.debuffs.append(atordoamento)
            print(f'{usuario.nome} atordoou {alvo.nome}!')
            alvo.CombinarEfeito("Atordoamento")

        elif e.nome == "Diminuição Defesa" and chance <= e.chance:
            diminuicao = e.ClonarEfeito()

            valor_diminuicao = e.valor # Valor Base
            for m in habilidade.modificadores: # Modificadores
                if m[0] == "ataque":
                    valor_diminuicao += usuario.ataque * (m[1] / 100)
                elif m[0] == "magia":
                    valor_diminuicao += usuario.magia * (m[1] / 100)
            
            valor_diminuicao = math.floor(valor_diminuicao)
            diminuicao.valor = valor_diminuicao

            # Se a criatura alvo já está sob o efeito de diminuição de defesa
            if alvo.EfeitoPresente("debuff", "Diminuição Defesa") != -1:
                indice = alvo.EfeitoPresente("debuff", "Diminuição Defesa")
                alvo.defesa -= math.floor(0.25 * alvo.debuffs[indice].valor)
                alvo.debuffs[indice].duracao += 1
                alvo.debuffs[indice].valor += math.floor(0.25 * alvo.debuffs[indice].valor)
                print(f'{alvo.nome} teve sua dimimuição de defesa piorada em 25% e a duração do efeito extendida em 1 turno.')

            # Se a criatura não está sob o efeito de diminuição de defesa
            else:
                alvo.debuffs.append(diminuicao)
                alvo.defesa -= valor_diminuicao
                print(f'{alvo.nome} teve sua defesa diminuída em {valor_diminuicao} por {e.duracao} turnos.')
