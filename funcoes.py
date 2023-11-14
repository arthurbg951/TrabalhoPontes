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


def integrate_linear_function(a, b, start, end, desired_error=1e-6):
    num_segments = 2  # Comece com 2 segmentos
    integral_prev = 0.0

    while True:
        h = (end - start) / num_segments
        integral = 0.0

        for i in range(num_segments):
            x0 = start + i * h
            x1 = x0 + h
            y0 = a * x0 + b
            y1 = a * x1 + b
            area = 0.5 * (y0 + y1) * h
            integral += abs(area)

        if abs(integral - integral_prev) < desired_error:
            return integral  # Retorna o valor da integral quando o erro é alcançado

        integral_prev = integral
        num_segments *= 2  # Duplica o número de segmentos na próxima iteração


def show_section(b1, b2, tw, d1, d2, d3, d4, d5):
    # Defina manualmente os pontos x e y para as retas
    x1 = [-b2 / 2, b2 / 2]
    y1 = [0, 0]

    x2 = [b2 / 2, b2 / 2]
    y2 = [0, d5]

    x3 = [b2 / 2, tw / 2]
    y3 = [d5, d5 + d4]

    x4 = [tw / 2, tw / 2]
    y4 = [d5 + d4, d5 + d4 + d3]

    x5 = [tw / 2, b1 / 2]
    y5 = [d5 + d4 + d3, d5 + d4 + d3 + d2]

    x6 = [b1 / 2, b1 / 2]
    y6 = [d5 + d4 + d3 + d2, d5 + d4 + d3 + d2 + d1]

    x7 = [b1 / 2, -b1 / 2]
    y7 = [d5 + d4 + d3 + d2 + d1, d5 + d4 + d3 + d2 + d1]

    x8 = [-b1 / 2, -b1 / 2]
    y8 = [d5 + d4 + d3 + d2, d5 + d4 + d3 + d2 + d1]

    x9 = [-tw / 2, -b1 / 2]
    y9 = [d5 + d4 + d3, d5 + d4 + d3 + d2]

    x10 = [-tw / 2, -tw / 2]
    y10 = [d5 + d4, d5 + d4 + d3]

    x11 = [-b2 / 2, -tw / 2]
    y11 = [d5, d5 + d4]

    x12 = [-b2 / 2, -b2 / 2]
    y12 = [0, d5]

    # Crie um gráfico
    plt.figure(figsize=(8, 6))

    # Plote as retas
    for x, y in [(x1, y1), (x2, y2), (x3, y3), (x4, y4), (x5, y5), (x6, y6), (x7, y7), (x8, y8), (x9, y9), (x10, y10), (x11, y11), (x12, y12)]:
        plt.plot(x, y, color='purple')

    # Sombrear a área dentro da forma
    x = []
    x.extend([x1[1], x2[1], x3[1], x4[1], x5[1], x6[1], x7[1], x8[1], x9[1], x10[1], x11[1], x12[1]])
    y = []
    y.extend([y1[1], y2[1], y3[1], y4[1], y5[1], y6[1], y7[1], y8[1], y9[1], y10[1], y11[1], y12[1]])
    plt.fill_between(
        x=x,
        y1=y,
        color='lightgray')

    # Adicione rótulos aos eixos e um título
    plt.title('Seção Adotada')

    # Remova as marcações dos eixos x e y
    plt.xticks([])
    plt.yticks([])

    # Exiba o gráfico
    plt.show()


def interpolar(sup1, inf1, sup2, inf2, valor):
    delta1 = sup1 - inf1
    delta2 = sup2 - inf2
    return (valor - inf1) / (delta1 / delta2) + inf2

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
