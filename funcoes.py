import math

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
