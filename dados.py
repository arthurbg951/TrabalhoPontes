# Dimensões da viga (Seção T) OBS: Verificar secao.png
b1 = 2.92
b2 = 1
tw = 0.8

d1 = 0.2
d2 = 0
d3 = 0.5
d4 = 0
d5 = 0.4
d_linha = 0.05

d = 0.925
# d = (d1 + d2 + d3 + d4 + d5) - d_linha

# Concreto
bitola_agregado = (3 / 4) * 2.54e-2
fck = 30e6
fcd = fck / 1.4

# Aço
diametro_bitola = 25  # mm
diametro_bitola_pele = 10  # mm
diametro_estribo = 12.5  # mm
num_ramos = 2
fy = 500e6
fyd = fy / 1.15
