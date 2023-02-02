import pickle
from colorama import Fore, Back, Style
from . import imprimir

class Configuracao():
    """
    Esta classe serve para armazenar configurações preferenciais do jogador.
    """

    def __init__(self):
        """
        Inicializador da classe.
        """
        self.confirmacao_sair = True
        self.salvar_sair = True

        self.npc_fala_delay = 0.025

        self.tecla_status = 'S'
        self.tecla_inventario = 'I'
        self.tecla_habilidades = 'H'
        self.tecla_equipamentos = 'E'
        self.tecla_salvar_jogo = 'P'
    
    def Atualizar(self):
        """
        Se uma configuração não possui um dos atributos da classe, então um atributo é criado com o valor
        padrão.
        """
        if not hasattr(self, 'confirmacao_sair'):
            self.confirmacao_sair = True
        
        if not hasattr(self, 'salvar_sair'):
            self.salvar_sair = True

        if not hasattr(self, 'npc_fala_delay'):
            self.npc_fala_delay = 0.025
        
        if not hasattr(self, 'tecla_status'):
            self.tecla_status = 'S'
        
        if not hasattr(self, 'tecla_inventario'):
            self.tecla_inventario = 'I'
        
        if not hasattr(self, 'tecla_habilidades'):
            self.tecla_habilidades = 'H'
        
        if not hasattr(self, 'tecla_equipamentos'):
            self.tecla_equipamentos = 'E'
        
        if not hasattr(self, 'tecla_salvar_jogo'):
            self.tecla_salvar_jogo = 'P'
    
    def ImprimirAcoes(self):
        """
        Imprime as ações de status, inventário, habilidades, equipamentos e de salvar o jogo, cada uma com sua
        tecla correspondente e separadas por quebra de linha.
        """
        print(f'[{self.tecla_status}] Status')
        print(f'[{self.tecla_inventario}] Inventário')
        print(f'[{self.tecla_habilidades}] Habilidades')
        print(f'[{self.tecla_equipamentos}] Equipamentos')
        print(f'[{self.tecla_salvar_jogo}] Salvar Jogo')
    
def SalvarConfiguracao(conf, caminho_conf):
    """
    Salva as configurações em um arquivo binário 'conf'.

    Parâmetros:
    - conf: configurações do usuário relativas ao jogo;
    - caminho_conf: caminho relativo ao arquivo que será salvo.
    """

    dados = {}
    dados['valido'] = 'Arquivo de configuração do Aventura'
    dados['conf'] = conf

    f = open(caminho_conf, "wb")
    f.write(pickle.dumps(dados))
    f.close()

def ImprimirConfiguracaoLigadoDesligado(conf):
    """
    Imprime a mensagem 'LIGADO' em verde caso a configuração seja igual a True e a mensagem 'DESLIGADO' em vermelho
    caso contrário. Uma quebra de linha também será impressa em ambos os casos.

    Parâmetros:
    - conf: uma configuração que possua valor True ou False.
    """

    if conf == True:
        print(Fore.GREEN + 'LIGADO' + Style.RESET_ALL)
    else:
        print(Fore.RED + 'DESLIGADO' + Style.RESET_ALL)

def ImprimirConfiguracaoValor(conf):
    """
    Imprime o valor de uma configuração em branco e negrito, no fundo preto. Uma quebra de linha também será
    impressa.

    Parâmetros:
    - conf: uma configuração.
    """

    if isinstance(conf, str):
        print(Style.BRIGHT + Fore.WHITE + Back.BLACK + conf + Style.RESET_ALL)
    else:
        print(Style.BRIGHT + Fore.WHITE + Back.BLACK + str(conf) + Style.RESET_ALL)

def DefinirConfiguracaoValor(conf, c):
    """
    Define o valor de uma configuração como um caractere não numérico.

    Parâmetros:
    - conf: configurações do usuário relativas ao jogo;
    - conf: configuração que está sendo alterada.
    """

    print('')

    while True:
        print('> Nova tecla: ', end = '')
        valor = input()

        if (len(valor) > 1) or (not valor.isalpha()):
            imprimir.MensagemErro('Apenas uma tecla, não numérica, pode ser definida como uma ação do jogador.')

        else:

            if (CompararAcao(valor, conf.tecla_status) and conf.tecla_status != c) or \
                (CompararAcao(valor, conf.tecla_inventario) and conf.tecla_inventario != c) or \
                (CompararAcao(valor, conf.tecla_habilidades) and conf.tecla_habilidades != c) or \
                (CompararAcao(valor, conf.tecla_equipamentos) and conf.tecla_equipamentos != c) or \
                (CompararAcao(valor, conf.tecla_salvar_jogo) and conf.tecla_salvar_jogo != c):
                imprimir.MensagemErro('Outra ação já foi definida com esta tecla.')

            else:
                if conf.tecla_status == c:
                    conf.tecla_status = valor.upper()

                elif conf.tecla_inventario == c:
                    conf.tecla_inventario = valor.upper()

                elif conf.tecla_habilidades == c:
                    conf.tecla_habilidades = valor.upper()

                elif conf.tecla_equipamentos == c:
                    conf.tecla_equipamentos = valor.upper()

                elif conf.tecla_salvar_jogo == c:
                    conf.tecla_salvar_jogo = valor.upper()

                break

def CompararAcao(valor, conf):
    """
    Compara um valor com o valor de uma configuração.

    Parâmetros:
    - valor: valor a ser comparado;
    - conf: configuração com que será comparada.
    """

    if valor == conf or valor == conf.lower():
        return True
    else:
        return False
