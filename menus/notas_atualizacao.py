from colorama import Fore, Back, Style

class NotasAtualizacao():
    """
    Exibe o que foi adicionado, removido ou balanceado nas versões lançadas do jogo.
    """
    def exibir(self):
        """
        Exibe as notas de atualização.
        """

        self.titulo('\n----------------------------------- Alpha Versão 0.0.1 -----------------------------------')
        print('\nJogabilidade')
        self.positivo('Jogadores podem atacar, defender, usar consumíveis, usar habilidades e correr em batalha.')
        self.positivo('Classes Guerreiro e Mago adicionadas.\n')

        print('Inimigos')
        self.positivo('Slime adicionado.\n')

        print('Habilidades')
        self.positivo('Projétil de Mana, Regeneração e Cuspe Ácido adicionados.\n')

        print('Itens')
        self.positivo('Espada Enferrujada e Cajado de Iniciante adicionados.')
        self.positivo('Poção de Cura Pequena e Poção de Mana Pequena adicionadas.\n')

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
        self.positivo('Antídoto e Bomba Inferior adicionados.\n')

        input('Aperte [ENTER] para sair.')
        return

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
