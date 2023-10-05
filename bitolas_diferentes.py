from area_aco import As
import math

def check_bitola(area_aco: float, *args: tuple[int, float]) -> None:
    aco_total = 0
    qtd_total_bitolas = 0
    for qtd_bitolas, bitola in args:
        area_bitola = math.pi * (bitola / 1e3)**2 / 4
        aco_total += area_bitola * qtd_bitolas
        qtd_total_bitolas += qtd_bitolas

    print(f'Calculo de aço com bitolas diferentes:')

    print(f'    quantitativo:')
    for qtd_bitolas, bitola in args:
        print(f'        {qtd_bitolas} bitolas de {bitola}mm')

    print(f'    total:\n        {qtd_total_bitolas} bitolas')

    if aco_total < area_aco:
        print(f'Area de aço insuficiente. {aco_total}<{area_aco}')
    else:
        print(f'Quantidade de bitolas={qtd_total_bitolas}, Area de aço calculado={aco_total}')


if __name__ == '__main__':
    check_bitola(As, (7, 16), (24, 20))
