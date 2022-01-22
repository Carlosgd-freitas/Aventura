import math
import random
from colorama import Fore, Back, Style

from . import mecanicas

def AlvoUnico(atacante, alvo, habilidade):
    """
    Utiliza uma habilidade em um único alvo e retorna o dano infligido.
    """

    dano = mecanicas.CalcularDano(atacante, alvo, habilidade)
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
    for e in habilidade.efeitos:
        chance = random.randint(1, 100)

        if e.nome == "Veneno" and chance <= e.chance:
            veneno = e.ClonarEfeito()
            alvo.debuffs.append(veneno)
            print(f'{atacante.nome} ' + Fore.GREEN + 'envenenou' + Style.RESET_ALL + f' {alvo.nome}!')
            alvo.CombinarEfeito("Veneno")
        
        if e.nome == "Atordoamento" and chance <= e.chance:
            atordoamento = e.ClonarEfeito()
            alvo.debuffs.append(atordoamento)
            print(f'{atacante.nome} atordoou {alvo.nome}!')
            alvo.CombinarEfeito("Atordoamento")
    
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
        alvo.hp -= dano

        # Aplicando Debuffs no Alvo
        for e in habilidade.efeitos:
            chance = random.randint(1, 100)

            if e.nome == "Veneno" and chance <= e.chance:
                veneno = e.ClonarEfeito()
                alvo.debuffs.append(veneno)
                print(f'{atacante.nome} ' + Fore.GREEN + 'envenenou' + Style.RESET_ALL + f' {alvo.nome}!')
                alvo.CombinarEfeito("Veneno")
            
            if e.nome == "Atordoamento" and chance <= e.chance:
                atordoamento = e.ClonarEfeito()
                alvo.debuffs.append(atordoamento)
                print(f'{atacante.nome} atordoou {alvo.nome}!')
                alvo.CombinarEfeito("Atordoamento")
        
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
    for e in habilidade.efeitos:
        chance = random.randint(1, 100)

        if e.nome == "Defendendo" and chance <= e.chance:
            defendendo = e.ClonarEfeito()
            criatura.buffs.append(defendendo)
            print(f'{criatura.nome} está defendendo.')
        
        elif e.nome == "Aumento Defesa" and chance <= e.chance:
            aumento = e.ClonarEfeito()

            valor_aumento = e.valor # Valor Base
            for m in habilidade.modificadores: # Modificadores
                if m[0] == "ataque":
                    valor_aumento += criatura.ataque * (m[1] / 100)
                elif m[0] == "magia":
                    valor_aumento += criatura.magia * (m[1] / 100)
            
            valor_aumento = math.floor(valor_aumento)
            aumento.valor = valor_aumento

            # Se a criatura já está sob o efeito de aumento de defesa
            if criatura.EfeitoPresente("buff", "Aumento Defesa") != -1:
                indice = criatura.EfeitoPresente("buff", "Aumento Defesa")
                criatura.defesa += math.floor(0.25 * criatura.buffs[indice].valor)
                criatura.buffs[indice].duracao += 1
                criatura.buffs[indice].valor += math.floor(0.25 * criatura.buffs[indice].valor)
                print(f'{criatura.nome} teve seu aumento de defesa melhorado em 25% e a duração do efeito extendida em 1 turno.')

            # Se a criatura não está sob o efeito de aumento de defesa
            else:
                criatura.buffs.append(aumento)
                criatura.defesa += valor_aumento
                print(f'{criatura.nome} aumentou sua defesa em {valor_aumento} por {e.duracao} turnos.')
                
    # Zerando a recarga atual da habilidade
    habilidade.recarga_atual = -1
