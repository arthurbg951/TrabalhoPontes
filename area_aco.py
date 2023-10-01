import math

# Dimensões da viga
base_viga = 0.20
altura_viga = 0.52
d_linha = 0.03
d = altura_viga - d_linha

# Concreto
fck = 20e6
fct = fck / 1.4

# Aço
fy = 500e6
fyd = fy / 1.15

# Carregamento e dimensões
L = 8
q = 15e3
Mk = q * L**2 / 8
Md = 1.4 * Mk

# Equação x/d
a = 0.4
b = -1
c = Md / (0.68 * base_viga * math.pow(d, 2) * fct)

raiz1, raiz2 = None, None

try:
    raiz1 = (-b + math.sqrt(b**2 - 4 * a * c)) / (2 * a)
except:
    ...


try:
    raiz2 = (-b - math.sqrt(b**2 - 4 * a * c)) / (2 * a)
except:
    ...

epslon = min(raiz1, raiz2)
x = epslon / d

# Domínios
dominio = None
if epslon <= 0.167:
    dominio = 1
elif 0.167 < epslon <= 0.259:
    dominio = 2
elif 0.259 < epslon <= 0.450:
    dominio = '3a'
elif 0.450 < epslon <= 0.628:
    dominio = '3b'
elif 0.628 < epslon:
    dominio = '4/5'

print(f'x/d={epslon:.2f} x={x:.2f} Domínio {dominio}')

# Area de aço
As = Md / (fyd * (d - 0.4 * x))
bitola = 20
area_bitola = math.pi * (bitola / 1e3)**2 / 4
num_bitolas = round(As / area_bitola)

print(f'Area de aço={As*1e4:.2f} cm² {num_bitolas} Ø {bitola}mm')
