import math

# Dimensões da viga (Seção T) OBS: Verificar secao.png
b1 = 0.40
b2 = 0.40
tw = 0.40

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
bitola = 20  # mm
fy = 500e6
fyd = fy / 1.15

# Carregamento
# Md = 6_521.597e3  # Seção A-A Momento negativo
# Md = 9_031.429e3 # Seção B-B Momento positivo
Md = 6300e3

# Equação x/d
a = 0.4
b = -1
c = Md / (0.68 * b1 * (d**2) * fcd)

raiz1, raiz2 = None, None
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
if epslon < 0:
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
As = Md / (fyd * (d - 0.4 * x))
taxa_armadura = 0.208 / 100
As_min = taxa_armadura * tw * (d + d_linha)

if As_min > As:
    As = As_min

area_bitola = math.pi * (bitola / 1e3)**2 / 4
num_bitolas = round(As / area_bitola)

print(f'Area de aço calculado={As}; Area de aço min={As_min} -> {num_bitolas} Ø {bitola}mm')
