import math
from funcoes import arredonda_pra_cima


# Dimensões da viga (Seção T) OBS: Verificar secao.png
b1 = 0.80
b2 = 0.80
tw = 0.80

d1 = 0.20
d2 = 0.22
d3 = 1.63
d4 = 0
d5 = 0

d_linha = 0.03
d = (d1 + d2 + d3 + d4 + d5) - d_linha

# Concreto
fck = 20e6
fcd = fck / 1.4

# Aço
diametro_bitola = 22  # mm
diametro_bitola_pele = 10  # mm
diametro_estribo = 12.5  # mm
fy = 500e6
fyd = fy / 1.15

# Carregamentos
# Seção A-A
# Momento negativo
Mg = 1.35 * 2661.168e3
Mq = 1.5 * 2808.184e3
Md = Mg + Mq
# Momento positivo
# Mg = 1.35 * 0e3
# Mq = 1.5 * 0e3
# Md = Mg + Mq

# Seção B-B
# Momento positivo
# Mg = 1.35 * 1639.392e3
# Mq = 1.5 * 3676.279e3
# Md = Mg + Mq

# Seção B-B
# Momento negativa
# Mg = 1.35 * 0
# Mq = 1.5 * 1445.278e3
# Md = Mg + Mq


# Cortante
# Seção AA
Vsg = 1.35 * 880.122e3
Vsq = 1.5 * 1041.702e3
Vsd = Vsg + Vsq


# Seção BB
# Vsg = 1.35 * 687.624e3
# Vsq = 1.5 * 920.743e3
# Vsd = Vsg + Vsq


# sEÇÃO DOIDA
# Vsg = 1.35 * 96.199e3
# Vsq = 1.5 * 483.761e3
# Vsd = Vsg + Vsq
print(f'Md={Md}')

# Equação x/d
a = 0.4
b = -1
c = Md / (0.68 * b1 * (d**2) * fcd)

delta = b**2 - 4 * a * c

if delta < 0:
    raise Exception('Dimensões da viga não válidas.')

raiz1 = (-b + math.sqrt(delta)) / (2 * a)
raiz2 = (-b - math.sqrt(delta)) / (2 * a)


epslon = min(raiz1, raiz2)
x = epslon * d
y = 0.8 * x

if y > d1 and not (b1 == b2 == tw):
    raise Exception('Linha neutra fora da mesa.')

# Domínios
dominio = None
if epslon <= 0:
    dominio = 1
elif 0 < epslon <= 0.259:
    dominio = 2
elif 0.259 < epslon <= 0.450:
    dominio = '3a'
elif 0.450 < epslon <= 0.628:
    dominio = '3b'
elif 0.628 < epslon <= 1:
    dominio = 4
elif 1 < epslon:
    dominio = 5
else:
    raise Exception('Intervalo do domínio não definido.')

print(f'x/d={epslon} x={x} y={y} Domínio {dominio}')

# Area de aço
As_calculado = Md / (fyd * (d - 0.4 * x))
As = As_calculado
taxa_armadura = 0.208 / 100
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
    num_bitolas = arredonda_pra_cima(As_pele / area_bitola)

    print(f'Area de aço pele={As_pele} -> {num_bitolas} Ø {diametro_bitola_pele}mm')

# Verificação do esforço cortante
alfa_v2 = 1 - (fck / 1e6) / 250
Vrd2 = 0.27 * fcd * tw * d
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
    Asw_min = 0.2 * (fctm / fywk) * tw * math.sin(alfa)

    if Asw < Asw_min:
        Asw = Asw_min

    area_estribo = math.pi * (diametro_estribo / 1e3)**2 / 4
    num_estribos = arredonda_pra_cima(Asw / area_estribo)
    # Espaçamento de estribos
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
        raise Exception('Ocorreu um erro no espaçamento de estribos.')

    print(f'Area de aço estribos={Asw}/m; Area de aço min={Asw_min}/m -> {num_estribos} Ø {diametro_estribo}mm')
    print(f'Espaçamento máximo entre estribos={espacamento_max_estribos}')
else:
    raise Exception('Ocorre ruptura das diagonais de compressão.')
