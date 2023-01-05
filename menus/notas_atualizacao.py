from colorama import Fore, Back, Style
from base import utils

class NotasAtualizacao():
    """
    Classe utilizada para documentar e imprimir as versões do jogo.
    """
    
    def menuNotas(self):
        """
        Exibe a nota de atualização da versão atual e imprime outras versões do jogo.
        """

        pagina = 0
        anterior = 0
        proximo = 0
        nao_repetir = 0
        op = -1

        print('')

        while True:

            # Evitando a repetição de impressões da mesma versão
            if nao_repetir == 1:
                nao_repetir = 0

            else:
                # Imprimindo Versão Atual
                if pagina == 0:
                    self.alphaV004(self)
                    print('')
                
                # Imprimindo Outras Versões
                if pagina == 1:
                    self.alphaV003(self)
                    print('')
                    
                elif pagina == 2:
                    self.alphaV002(self)
                    print('')
                    self.alphaV001(self)
                    print('')

                # Opções do menu
                if pagina != 0:
                    anterior = 1
                    print('[1] Anterior')
                else:
                    anterior = 0
                    print(Fore.RED + '[1] Anterior' + Style.RESET_ALL + '')

                if pagina != 2:
                    proximo = 1
                    print('[2] Próximo\n')
                else:
                    proximo = 0
                    print(Fore.RED + '[2] Próximo' + Style.RESET_ALL + '\n')
                
                print('[0] Retornar ao menu anterior\n')

            op = utils.LerNumeroIntervalo('> ', 0, 2)

            if op == 0:
                break
            
            elif op == 1 and anterior == 1:
                print('')
                pagina -= 1
            
            elif op == 2 and proximo == 1:
                print('')
                pagina += 1
            
            elif op == 1 or op == 2:
                nao_repetir = 1

    def alphaV001(self):
        """
        Notas de atualização referente à versão Alpha 0.0.1.
        """
    
        self.titulo('----------------------------------- Alpha Versão 0.0.1 -----------------------------------')
        print('\nJogabilidade')
        self.positivo('Jogadores podem atacar, defender, usar consumíveis, usar habilidades e correr em batalha.')
        self.positivo('Classes Guerreiro e Mago adicionadas.\n')

        print('Inimigos')
        self.positivo('Slime adicionado.\n')

        print('Habilidades')
        self.positivo('Projétil de Mana, Regeneração e Cuspe Ácido adicionados.\n')

        print('Itens')
        self.positivo('Espada Enferrujada e Cajado de Iniciante adicionados.')
        self.positivo('Poção de Cura Pequena e Poção de Mana Pequena adicionadas.')

    def alphaV002(self):
        """
        Notas de atualização referente à versão Alpha 0.0.2.
        """

        self.titulo('----------------------------------- Alpha Versão 0.0.2 -----------------------------------')
        print('\nJogabilidade')
        self.positivo('Fora de batalha, jogadores podem explorar a área, ver seu status, inventário, habilidades' +
            ', equipamentos e sair do jogo')
        self.positivo('Loja e evento de descanso adicionados.')
        self.positivo('Jogadores também podem equipar e desequipar itens em batalha.')
        self.positivo('Jogadores ganham espólios (ouro, experiência e chance de itens) ao derrotarem criaturas ' +
            'inimigas.')
        self.positivo('Jogadores podem subir de nível até o nível 5.\n')

        print('Inimigos')
        self.positivo('Cobra Venenosa, Slime Gigante e Tortuga adicionados.\n')

        print('Habilidades')
        self.positivo('Picada Venenosa, Envenenamento, Subdivisão, Esconder no Casco, Impacto Atordoante e ' +
            'Escudo Mágico adicionados.\n')
        
        print('Itens')
        self.positivo('Espada e Cajado de Aprendiz adicionados.')
        self.positivo('Broquel de Madeira, Chapéu de Couro, Peitoral de Couro, Robe de Algodão e Botas de couro ' +
            'adicionados.')
        self.positivo('Antídoto e Bomba Inferior adicionados.')

    def alphaV003(self):
        """
        Notas de atualização referente à versão Alpha 0.0.3.
        """

        self.titulo('----------------------------------- Alpha Versão 0.0.3 -----------------------------------')
        print('\nJogabilidade')
        self.positivo('O índice do turno agora é impresso a cada início de turno.')
        self.positivo('Os inimigos em batalha agora são impressos no início da vez do jogador.')
        self.positivo('Jogadores podem usar alguns itens consumíveis de seu inventário enquanto estão fora de batalha.')
        self.positivo('Ataques e habilidades que causam dano podem causar acertos críticos.')
        self.positivo("Em batalha, criaturas com o mesmo nome agora aparecerão com nomes únicos. (Ex.: 'Slime A', 'Slime B'...)")

        print('\nLojas e Estalagens')
        self.positivo('Lojas e estalagens agora contam com NPCs únicos que falam com o jogador.')
        self.positivo('NPCs podem dar dicas e explicar algumas mecânicas do jogo para o jogador.')
        self.neutro('Lojas e estalagens só serão encontradas dentro de vilas ou cidades.')

        print('\nInimigos')
        self.positivo('Ervágora e Slime de Mel adicionados.')
        self.positivo('Chefão da primeira área adicionado.')

        print('\nHabilidades')
        self.positivo('Grito Estremecedor, Cuspe de Mel e Cura Inferior adicionados.')

        print('\nItens')
        self.positivo('Erva Curativa, Mel de Abelhóide e Bomba Grudenta Inferior adicionados.')
        
        print('\nOutros')
        self.positivo('Tela de créditos adicionada.')
        self.positivo('Tela de configurações adicionada.')
        self.positivo("Campos 'singular/plural' e 'gênero' adicionados aos componentes do jogo, deixando a "+
            "impressão de mensagens mais consistente.")
        self.positivo('Adicionada uma confirmação para sair do jogo.')
        self.positivo('Perder o jogo retorna o jogador para o menu principal em vez de fechá-lo.')
        self.neutro('Falas de NPCs possuem um delay durante sua impressão.')
    
    def alphaV004(self):
        """
        Notas de atualização referente à versão Alpha 0.0.4.
        """

        self.titulo('----------------------------------- Alpha Versão 0.0.4 -----------------------------------')
        print('\nJogabilidade')
        self.positivo('Um jogo pode ser salvo e carregado manualmente.')
        self.positivo("O jogo, por padrão, salva automaticamente quando a ação 'Sair do Jogo' é escolhida.")
        self.positivo('O jogador pode acessar seu status, inventário, habilidades e equipamento quando ' +
            'estiver em uma vila.')
        self.positivo('O local em que o jogador está é impresso antes das ações disponíveis quando este está ' +
            'fora de combate.')
        self.positivo('Jogadores podem usar itens consumíveis que dão regeneração de seu inventário enquanto ' +
            'estão fora de batalha.')
        self.positivo('Evento de vendedor ambulante adicionado.')
        self.positivo('Jogadores podem subir de nível até o nível 10.')
        self.positivo('Habilidades que curam HP ou Mana podem causar acertos críticos.')
        self.positivo('As lojas são reestocadas a cada certo número de batalhas ganhas.')
        self.negativo('Eventos na exploração de uma área agora possuem uma menor chance de acontecer.')
        self.negativo('O debuff de envenenamento persiste após a batalha.')
        self.negativo('Quando o jogador vai até uma vila ou cidade, há uma pequena chance de uma emboscagem ocorrer.')

        print('\nInimigos')
        self.positivo('Larva de Abelhóide e Abelhóide adicionadas.')

        print('\nHabilidades')
        self.positivo('Disparo Elétrico e Vingança adicionados.')

        print('\nItens')
        self.positivo('Poção Pequena de Regeneração adicionada.')
        self.positivo('Elixires Pequenos de Ataque, Defesa, Magia e Velocidade adicionados.')
        self.neutro('Poções de Cura e Mana Pequenas renomeadas para Poções Pequenas de Cura e Mana.')

        print('\nOutros')
        self.positivo('As configurações são salvas e permanecem com as alterações feitas pelos jogadores.')
        self.positivo('O mapeamento das teclas de algumas ações pode ser alterado.')
        self.positivo("Utilização de tabelas mais organizadas em alguns aspectos do jogo.")

    def alphaV005(self):
        """
        Notas de atualização referente à versão Alpha 0.0.5.
        """

        self.titulo('----------------------------------- Alpha Versão 0.0.5 -----------------------------------')
        print('\nOutros')
        self.neutro('As descrições dos itens consumíveis foi refeita.')

    def titulo(string):
        """
        Utilizado para imprimir o título de uma versão. Impime a string em preto com fundo branco.
        """
        print(Fore.BLACK + Back.WHITE + string + Style.RESET_ALL)

    def positivo(string):
        """
        Imprime um '+' verde e uma string em branco, ambos com fundo preto.
        """
        print(Back.BLACK + Fore.GREEN + '+ ' + Fore.WHITE + string + Style.RESET_ALL)
    
    def negativo(string):
        """
        Imprime um '-' vermelho e uma string em branco, ambos com fundo preto.
        """
        print(Back.BLACK + Fore.RED + '- ' + Fore.WHITE + string + Style.RESET_ALL)
    
    def neutro(string):
        """
        Imprime um '*' amarelo e uma string em branco, ambos com fundo preto.
        """
        print(Back.BLACK + Fore.YELLOW + '* ' + Fore.WHITE + string + Style.RESET_ALL)
