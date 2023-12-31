import math
from funcoes import arredonda_pra_cima, arredonda_pra_baixo
from funcoes import (
    to_red as re,
    to_yellow as ye
)
from carregamentos import main as calcula_pp


def calcular_epslon(Md: float, b1: float, d: float, fcd: float) -> tuple[float, float]:
    '''
    Equação que retorna epslon (x/d).
    '''
    a = 0.4
    b = -1
    c = Md / (0.68 * b1 * (d**2) * fcd)

    delta = b**2 - 4 * a * c

    if delta < 0:
        raise Exception('Dimensões da viga não válidas.')

    raiz1 = (-b + math.sqrt(delta)) / (2 * a)
    raiz2 = (-b - math.sqrt(delta)) / (2 * a)
    return raiz1, raiz2


def verifica_dominio(epslon: float) -> str:
    '''
    Verifica o domínio com base em um epslon (x/d).
    '''
    if epslon < 0:
        return '1'
    elif 0 <= epslon <= 0.259:
        return '2'
    elif 0.259 < epslon <= 0.450:
        return '3a'
    elif 0.450 < epslon <= 0.628:
        return '3b'
    elif 0.628 < epslon <= 1:
        return '4'
    elif 1 < epslon:
        return '5'
    else:
        raise Exception('Intervalo do domínio não definido.')

# Dimensões da viga (Seção T) OBS: Verificar secao.png
b1=1
b2=0.2
tw=0.2

d1=0.2
d2=0
d3=0.4
d4=0
d5=0.2

d_linha = 0.04

# d = 0.6875000000000001
d = (d1 + d2 + d3 + d4 + d5) - d_linha


# Concreto
bitola_agregado = (3 / 4) * 2.54e-2
fck = 20e6
fcd = fck / 1.4

# Aço
diametro_bitola = 40  # mm
diametro_bitola_pele = 6.3  # mm
diametro_estribo = 6.3  # mm
num_ramos = 1
fy = 500e6
fyd = fy / 1.15

# Comprimento ponte
L = 25

# Carregamentos
PP = max(*calcula_pp(b1, b2, tw, d1, d2, d3, d4, d5))
print(f'Peso próprio = {PP} kN/m')

# Momento Fletor
# Mg = (PP * L**2 / 8) * 1e3
# Mq = 3443.9e3
# Md = 1.35 * Mg + 1.5 * Mq
MPP = PP * 14.6**2 / 8 # Nm
MR = 5815.4e3 # Nm
Md = 7e3 # Nm

# Esforço cortante
# Vsg = (PP * L) * 1e3 / 2
# Vsq = 571.1e3
# Vsd = 1.35 * Vsg + 1.5 * Vsq
VPP = (PP * 14.6) * 1e3 / 2 # Nm
VR = 1594e3 # N
Vsd = 8.4e3 # N

raiz1, raiz2 = calcular_epslon(Md, b1, d, fcd)
epslon = min(raiz1, raiz2)
x = epslon * d
y = 0.8 * x

if y > d1 and not (b1 == b2 == tw):
    Md1 = 0.85 * fcd * (b1 - tw) * d1 * (d - 0.5 * d1)
    Md2 = Md - Md1
    Md = Md2
    raiz1, raiz2 = calcular_epslon(Md2, b1, d, fcd)
    epslon = min(raiz1, raiz2)
    x = epslon * d
    y = 0.8 * x

if epslon > 0.45:
    print(y(f'Necessita armadura dupla. O calculo não considera isso.'))

dominio = verifica_dominio(epslon)
print(f'x/d={epslon} x={x} y={y} Domínio {dominio}')

# Area de aço
As_calculado = Md / (fyd * (d - 0.4 * x))
As = As_calculado
taxa_armadura = 0.150 / 100
As_min = taxa_armadura * tw * (d + d_linha)

if As_min > As_calculado:
    As = As_min

area_bitola = math.pi * (diametro_bitola / 1e3)**2 / 4
num_bitolas = arredonda_pra_cima(As / area_bitola)
print(f'Area de aço calculado={As_calculado}; Area de aço min={As_min} -> {num_bitolas} Ø {diametro_bitola}mm')

# Armadura de pele
if d1 + d2 + d3 + d4 + d5 >= 0.6:
    As_pele = (0.1 / 100) * tw * (d1 + d2 + d3 + d4 + d5)
    area_bitola = math.pi * (diametro_bitola_pele / 1e3)**2 / 4
    num_bitolas_pele = arredonda_pra_cima(As_pele / area_bitola)

    print(f'Area de aço pele={As_pele} -> {num_bitolas_pele} Ø {diametro_bitola_pele}mm')

# Verificação do esforço cortante
alfa_v2 = 1 - (fck / 1e6) / 250
Vrd2 = 0.27 * alfa_v2 * fcd * tw * d
if Vsd <= Vrd2:
    # Não ocorre ruptura das diagonais de compressão. (Vsd<Vrd2)
    # Resistência a compressão do concreto
    fctd = 0.7 * (0.3 * math.pow(fck / 1e6, 2 / 3)) / 1.4
    Vc = 0.6 * fctd * 1e6 * tw * d
    Vsw = Vsd - Vc
    fywd: int = None
    if fyd <= 435e6:
        fywd = fyd
    else:
        fywd = 435e6
    alfa = math.radians(90)
    Asw = Vsw / (0.9 * d * fywd * (math.sin(alfa) + math.cos(alfa)))
    fctm = 0.3 * math.pow(fck / 1e6, 2 / 3)
    fywk = fy
    Asw_min = 0.2 * (fctm * 1e6 / fywk) * tw * math.sin(alfa)

    if Asw < Asw_min:
        Asw = Asw_min

    area_estribo = num_ramos * math.pi * (diametro_estribo / 1e3)**2 / 4
    num_estribos = arredonda_pra_cima(Asw / area_estribo)
    # Espaçamento de estribos - item 18.3.3.2 da NBR 6118 (2014)
    espacamento_max_estribos: float = None
    if Vsd <= 0.67 * Vrd2:
        if 0.6 * d >= 0.3:
            espacamento_max_estribos = 0.3
        else:
            espacamento_max_estribos = 0.6 * d
    elif Vsd > 0.67 * Vrd2:
        if 0.3 * d >= 0.3:
            espacamento_max_estribos = 0.2
        else:
            espacamento_max_estribos = 0.3 * d
    else:
        raise Exception(re('Ocorreu um erro no espaçamento de estribos.'))

    print(f'Area de aço estribos={Asw}/m; Area de aço min={Asw_min}/m -> {num_estribos} Ø {diametro_estribo}mm')
    print(f'Consumo esforço cortante = {Vsd/Vrd2 * 100:.2f}%')
    # print(f'Espaçamento máximo entre estribos={espacamento_max_estribos}')
else:
    raise Exception(re(f'Ocorre ruptura das diagonais de compressão. Vsd/Vrd2={Vsd/Vrd2 * 100:.2f}%'))

espacamento_min_horizontal = max(1.2 * bitola_agregado, 0.02, diametro_bitola * 1e-3)
# print(f'Espacamento min horizontal={espacamento_min_horizontal}')

espacamento_min_vertical = max(0.5 * bitola_agregado, 0.02, diametro_bitola * 1e-3)
# print(f'Espacamento min vertical={espacamento_min_vertical}')

num_max_de_bitolas_por_camada = arredonda_pra_baixo(
    ((b2 - d_linha * 2 - num_ramos * diametro_estribo * 2e-3) + espacamento_min_horizontal) /
    (diametro_bitola * 1e-3 + espacamento_min_horizontal)
)

if num_bitolas <= num_max_de_bitolas_por_camada:
    print(f'1 camada com {num_bitolas} Ø de {diametro_bitola}mm')
    d_real = (d1 + d2 + d3 + d4 + d5 - d_linha - diametro_estribo * 1e-3 - diametro_bitola * 1e-3 / 2)
    print(f'Diferença d_real e d utilizado = {math.fabs(d_real - d) * 100:.2f}%')
else:
    print(f'Precisa de mais de uma camada. 1 camada suporta apenas {num_max_de_bitolas_por_camada} Ø de {diametro_bitola}mm c/ {espacamento_min_horizontal}')
    num_de_camadas = arredonda_pra_cima(num_bitolas / num_max_de_bitolas_por_camada)
    print(f'Numero de camadas: {num_de_camadas}')
    num_max_de_camadas = arredonda_pra_baixo(
        ((d5 - diametro_estribo * 1e-3 - d_linha) + espacamento_min_vertical) /
        (diametro_bitola * 1e-3 + espacamento_min_vertical)
    )
    if num_de_camadas > num_max_de_camadas:
        raise Exception(f'Não existe seção suficiente para a quantidade de bitolas.')
    d_real = d1 + d2 + d3 + d4
    d_real += (
        d5 - d_linha - diametro_estribo * 1e-3 -
        (num_de_camadas * diametro_bitola * 1e-3 + (num_de_camadas - 1) * espacamento_min_vertical)
    )  # Folga
    d_real += (num_de_camadas * (diametro_bitola * 1e-3) + (num_de_camadas - 1) * espacamento_min_vertical) / 2  # Metade da area bitolas com espaçamento
    if d_real != d:
        print(f'd={d} d_real={d_real} {((d - d_real) / (d1 + d2 + d3 + d4 + d5)*100):.2f}% de diferença.')

if (d - d_real) / (d1 + d2 + d3 + d4 + d5) > 0.1:
    raise Exception(f'(d-d_real)/h > 10%')
