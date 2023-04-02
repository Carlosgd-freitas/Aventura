import sys

sys.path.append("..")
from base import utils

class Receita():
    """
    Esta classe é utilizada para receitas de fabricação.
    """

    def __init__(self, nome = "default", entrada = [], saida = [], preco = 0, nivel = 0,
                singular_plural = "default", genero = "default"):
        """
        Inicializador da classe.
        """
        self.nome = nome
        self.entrada = entrada
        self.saida = saida
        self.preco = preco
        self.nivel = nivel

        self.singular_plural = singular_plural
        self.genero = genero

    def __str__(self):
        """
        Converte a classe em uma string.
        """
        string = f'Nome: {self.nome}\n'
        string += 'Entrada:\n'
        string += utils.ListaEmString(self.entrada) + '\n'
        string += 'Saída:\n'
        string += utils.ListaEmString(self.saida) + '\n'
        string += f'Preço: {self.preco}\n'
        string += f'Nível: {self.nivel}\n'
        string += f'singular_plural: {self.singular_plural}\n'
        string += f'Gênero: {self.genero}\n'
        return string
    
    def MateriaisNecessarios(self, materiais, quantidade = 1):
        """
        Retorna se cada um dos itens presentes na entrada da receita também estão presentes na lista de itens
        passadas por parâmetro.

        Parâmetros:
        * materiais: lista de itens onde a checagem será realizada.
        
        Parâmetros opcionais:
        * quantidade: vezes em que a saída será gerada ao final da fabricação.
        """
        for item in self.entrada:
            check = False

            for material in materiais:
                if material.nome == item.nome and material.quantidade >= item.quantidade * quantidade:
                    check = True
                    break

            if not check:
                return False

        return check
        