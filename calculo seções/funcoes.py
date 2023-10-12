import math
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os

def mostrar_secao():
    # Carregue a imagem usando matplotlib.image
    imagem = mpimg.imread(os.path.join('..', 'secao.png'))

    # Exiba a imagem
    plt.imshow(imagem)

    # Personalize a exibição, se desejar
    plt.axis('off')  # Desabilita os eixos

    # Mostra a imagem na janela
    plt.show()

def check_bitola(area_aco: float, *args: tuple[int, float]) -> None:
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

def arredonda_pra_cima(valor: float) -> int:
    resto = valor % 1
    arredondado_pra_cima = int(valor + (1 - resto))
    return arredondado_pra_cima
