import matplotlib.pyplot as plt
from dados import b1, b2, tw, d1, d2, d3, d4, d5

# Seção Girder
# b1 = 1
# b2 = 0.6
# tw = 0.5

# d1 = 0.1
# d2 = 0.0
# d3 = 0.9
# d4 = 0
# d5 = 0.3

# Defina manualmente os pontos x e y para as retas
x1 = [-b2 / 2, b2 / 2]
y1 = [0, 0]

x2 = [b2 / 2, b2 / 2]
y2 = [0, d5]

x3 = [b2 / 2, tw / 2]
y3 = [d5, d5 + d4]

x4 = [tw / 2, tw / 2]
y4 = [d5 + d4, d5 + d4 + d3]

x5 = [tw / 2, b1 / 2]
y5 = [d5 + d4 + d3, d5 + d4 + d3 + d2]

x6 = [b1 / 2, b1 / 2]
y6 = [d5 + d4 + d3 + d2, d5 + d4 + d3 + d2 + d1]

x7 = [b1 / 2, -b1 / 2]
y7 = [d5 + d4 + d3 + d2 + d1, d5 + d4 + d3 + d2 + d1]

x8 = [-b1 / 2, -b1 / 2]
y8 = [d5 + d4 + d3 + d2, d5 + d4 + d3 + d2 + d1]

x9 = [-tw / 2, -b1 / 2]
y9 = [d5 + d4 + d3, d5 + d4 + d3 + d2]

x10 = [-tw / 2, -tw / 2]
y10 = [d5 + d4, d5 + d4 + d3]

x11 = [-b2 / 2, -tw / 2]
y11 = [d5, d5 + d4]

x12 = [-b2 / 2, -b2 / 2]
y12 = [0, d5]

# Crie um gráfico
plt.figure(figsize=(8, 6))

# Plote as retas
for x, y in [(x1, y1), (x2, y2), (x3, y3), (x4, y4), (x5, y5), (x6, y6), (x7, y7), (x8, y8), (x9, y9), (x10, y10), (x11, y11), (x12, y12)]:
    plt.plot(x, y, color='purple')

# Sombrear a área dentro da forma
x = []
x.extend([x1[1], x2[1], x3[1], x4[1], x5[1], x6[1], x7[1], x8[1], x9[1], x10[1], x11[1], x12[1]])
y = []
y.extend([y1[1], y2[1], y3[1], y4[1], y5[1], y6[1], y7[1], y8[1], y9[1], y10[1], y11[1], y12[1]])
plt.fill_between(
    x=x,
    y1=y,
    color='lightgray')

# Adicione rótulos aos eixos e um título
plt.title('Seção Girder')

# Remova as marcações dos eixos x e y
plt.xticks([])
plt.yticks([])

# Exiba o gráfico
plt.show()
