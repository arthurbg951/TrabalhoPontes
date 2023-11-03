import math
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os

def mostrar_imagem(imagem):
    # Carregue a imagem usando matplotlib.image
    imagem = mpimg.imread(os.path.join(imagem))

    # Exiba a imagem
    plt.imshow(imagem)

    # Personalize a exibição, se desejar
    plt.axis('off')  # Desabilita os eixos

    # Mostra a imagem na janela
    plt.show()

def arredonda_pra_cima(valor: float) -> int:
    '''
    Arredonda um valor para cima. Ex: 7.15 -> 8
    '''
    return int(valor + (1 - valor % 1))

def arredonda_pra_baixo(valor: float) -> int:
    '''
    Arredonda um valor para baixo. Ex: 7.15 -> 7
    '''
    return int(valor - (valor % 1))

def check_bitola(area_aco: float, *args: tuple[int, float]) -> None:
    '''
    Verifica multiplas bitolas para um mesmo As. 
    *args pode conter várias tuplas no formato:
    (num_bitolas1, bitola1), (num_bitolas2, bitola2) ...
    '''
    aco_total = 0
    qtd_total_bitolas = 0
    for qtd_bitolas, bitola in args:
        area_bitola = math.pi * (bitola / 1e3)**2 / 4
        aco_total += area_bitola * qtd_bitolas
        qtd_total_bitolas += qtd_bitolas

    print(f'Testando aço com bitolas diferentes:')

    print(f'    quantitativo:')
    for qtd_bitolas, bitola in args:
        print(f'        {qtd_bitolas} bitolas de {bitola}mm')

    print(f'    total:\n        {qtd_total_bitolas} bitolas')

    if aco_total < area_aco:
        print(f'Area de aço insuficiente. {aco_total}<{area_aco}')
    else:
        print(f'Quantidade de bitolas={qtd_total_bitolas}, Area de aço calculado={aco_total}')


# ANSI code colors python
# Converte um texto para a cor definida

""" ANOTHER COLORS NOT IMPLEMENTED. """

# BLACK = "\033[0;30m"
# RED = "\033[0;31m"
# GREEN = "\033[0;32m"
# BROWN = "\033[0;33m"
# BLUE = "\033[0;34m"
# PURPLE = "\033[0;35m"
# CYAN = "\033[0;36m"
# LIGHT_GRAY = "\033[0;37m"
# DARK_GRAY = "\033[1;30m"
# LIGHT_RED = "\033[1;31m"
# LIGHT_GREEN = "\033[1;32m"
# YELLOW = "\033[1;33m"
# LIGHT_BLUE = "\033[1;34m"
# LIGHT_PURPLE = "\033[1;35m"
# LIGHT_CYAN = "\033[1;36m"
# LIGHT_WHITE = "\033[1;37m"
# BOLD = "\033[1m"
# FAINT = "\033[2m"
# ITALIC = "\033[3m"
# UNDERLINE = "\033[4m"
# BLINK = "\033[5m"
# NEGATIVE = "\033[7m"
# CROSSED = "\033[9m"

__reset_color_text = '\u001b[0m'


def to_red(text: str) -> str:
    return '\u001b[31m' + str(text) + __reset_color_text


def to_green(text: str) -> str:
    return '\u001b[32m' + str(text) + __reset_color_text


def to_yellow(text: str) -> str:
    return '\u001b[33m' + str(text) + __reset_color_text


def to_blue(text: str) -> str:
    return '\u001b[34m' + str(text) + __reset_color_text
