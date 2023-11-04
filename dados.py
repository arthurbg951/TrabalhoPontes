# Dimensões da viga (Seção T) OBS: Verificar secao.png
from funcoes import show_section
b1 = 2.43
b2 = 0.8
tw = 0.4

d1 = 0.2
d2 = 0
d3 = 0.4
d4 = 0
d5 = 0.2

d_linha = 0.04

d = 0.6875000000000001
# d = (d1 + d2 + d3 + d4 + d5) - d_linha


# Concreto
bitola_agregado = (3 / 4) * 2.54e-2
fck = 30e6
fcd = fck / 1.4

# Aço
diametro_bitola = 25  # mm
diametro_bitola_pele = 10  # mm
diametro_estribo = 10  # mm
num_ramos = 2
fy = 500e6
fyd = fy / 1.15

show_section(b1, b2, tw, d1, d2, d3, d4, d5)
