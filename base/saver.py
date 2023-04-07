import os
import pickle
from . import imprimir
from datetime import datetime

def Salvar(caminho, jogador, estatisticas, area, local):
    """
    Salva o jogo em um arquivo binário com o nome do jogador.

    Parâmetros:
    - caminho: caminho relativo a pasta que contém os saves;
    - jogador: objeto do jogador;
    - estatisticas: estatísticas relacionadas ao jogador e ao jogo;
    - area: area em que o jogador estava quando salvou o jogo;
    - local: nome do local em que o jogador estava quando salvou o jogo.
    """
    estatisticas.data_jogo_salvo = datetime.now()
    estatisticas.ContabilizarTempoJogado()

    save = {
        "valido": "Arquivo de jogo salvo do Aventura",
        "jogador": jogador,
        "estatisticas": estatisticas,
        "area": area,
        "local": local,
    }
    
    caminho_save = os.path.join(caminho, jogador.nome + '.bin')
    f = open(caminho_save, 'wb')
    f.write(pickle.dumps(save))
    f.close()
    imprimir.MensagemSistema('O jogo foi salvo com sucesso.')

def Carregar(caminho):
    """
    Retorna um jogo salvo no formato de um dicionário. Se o save não puder ser carregado, uma mensagem é
    impressa e o jogo fecha.

    Parâmetros:
    - caminho: caminho relativo ao save em questão.
    """
    save = pickle.loads(open(caminho, "rb").read())

    # Campo de validação do arquivo binário
    if 'valido' in save:
        valido = save['valido']

        if valido == 'Arquivo de jogo salvo do Aventura':
            return save

        else:
            imprimir.MensagemErro('O arquivo não pode ser carregado corretamente.')
            os._exit(0)

def ListarSaves(caminho):
    """
    Lista todos os saves em um diretório.

    Parâmetros:
    - caminho: caminho relativo a pasta que contém os saves.
    """
    saves = []
    saves_nomes = []

    i = 0
    for arquivo in os.listdir(caminho):
        f = os.path.join(caminho, arquivo)

        if arquivo.endswith('.bin'):
            save = pickle.loads(open(f, "rb").read())

            if 'valido' in save and save['valido'] == "Arquivo de jogo salvo do Aventura":
                saves.append(save)
                saves_nomes.append(save['jogador'].nome + '.bin')
    
    if saves:
        print(imprimir.RetornarTabelaSaves(saves), end = '\n\n')

    if i != 0:
        print('\n[0] Voltar ao menu principal\n')

    return saves_nomes
