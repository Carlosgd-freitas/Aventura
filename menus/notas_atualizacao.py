from colorama import Fore, Back, Style
from classes_base import utils

class NotasAtualizacao():
    """
    Classe utilizada para documentar e imprimir as versões do jogo.
    """
    
    def menuNotas(self):
        """
        Exibe a nota de atualização da versão atual e imprime outras versões do jogo.
        """

        # Imprimindo até 2 versões
        pagina = 0
        anterior = 0
        proximo = 0
        nao_repetir = 0
        op = -1

        while True:

            # Evitando a repetição de impressões da mesma versão
            if nao_repetir == 1:
                nao_repetir = 0

            else:
                # Imprimindo Versão Atual
                if pagina == 0:
                    self.alphaV003(self)
                    print('')
                
                # Imprimindo Outras Versões
                elif pagina == 1:
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

                if pagina != 1:
                    proximo = 1
                    print('[2] Próximo\n')
                else:
                    proximo = 0
                    print(Fore.RED + '[2] Próximo' + Style.RESET_ALL + '\n')
                
                print('[0] Retornar ao menu anterior')

            op = utils.LerNumeroIntervalo('> ', 0, 2)

            if op == 0:
                print('')
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
        self.positivo('O índice do turno e os inimigos em batalha agora são impressos a cada início de turno.')
        self.positivo('Jogadores podem usar alguns itens consumíveis de seu inventário enquanto estão fora de batalha.')
        self.positivo('Ataques e habilidades que causam dano podem causar acertos críticos.')

        print('\nInimigos')
        self.positivo('Ervágora adicionada.')
        
        print('\nOutros')
        self.positivo('Tela de Créditos Adicionada.')
        self.positivo("Campos 'singular/plural' e 'gênero' adicionados aos componentes do jogo, deixando a "+
            "impressão de mensagens mais consistente.")
        self.positivo('Adicionada uma confirmação para sair do jogo.')
        self.positivo('Falas de NPCs possuem um delay durante sua impressão.')

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
        print(Back.BLACK + Fore.YELLOW + '- ' + Fore.WHITE + string + Style.RESET_ALL)
