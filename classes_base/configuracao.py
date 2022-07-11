import pickle

class Configuracao():
    """
    Esta classe serve para armazenar configurações preferenciais do jogador.
    """

    def __init__(self):
        """
        Inicializador da classe.
        """
        self.confirmacao_sair = True
        self.npc_fala_delay = 0.03
    
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
