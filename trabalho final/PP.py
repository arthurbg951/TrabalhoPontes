# DIMENSIONAMENTO VIGA 3 Seção T
b = 4.867
d = 0.8
tw = 0.4
tf = 0.2

area = b * tf + (d - tf) * tw

p1 = area * 25
p2 = 3 * 0.205 * 25
p3 = (b - 3) * 0.1 * 24
PP = p1 + p2 + p3
print(PP)

# DIMENSIONAMENTO SECAO GIRDER
b1 = 14.6 / 3
b2 = 0.5
tw = 0.5

d1 = 0.1
d2 = 0.0
d3 = 0
d4 = 0
d5 = 0.7

area = b1 * d1 + (tw + b1) * d2 / 2 + tw * d3 + (tw + b2) * d4 / 2 + d5 * b2
p1 = area * 25
p2 = 3 * 0.205 * 25
comprimento_total_asfalto = (b1 - 3) if (b1 - 3) < 2.4 else None

if comprimento_total_asfalto == None:
    raise Exception(f'Comprimento de asfalto maior que 2.4m.')

p3 = comprimento_total_asfalto * 0.1 * 24
PP = p1 + p2 + p3
print(PP)
