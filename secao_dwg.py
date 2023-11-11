from dimensionamento2 import dados
import ezdxf
import os

# Seção Girder
data = dados()
secao = data['girder']

b1 = secao.b1
b2 = secao.b2
tw = secao.tw

d1 = secao.d1
d2 = secao.d2
d3 = secao.d3
d4 = secao.d4
d5 = secao.d5

# Defina manualmente os pontos x e y para as retas
pontos = [
    (-b2 / 2, 0),
    (b2 / 2, 0),
    (b2 / 2, d5),
    (tw / 2, d5 + d4),
    (tw / 2, d5 + d4 + d3),
    (b1 / 2, d5 + d4 + d3 + d2),
    (b1 / 2, d5 + d4 + d3 + d2 + d1),
    (-b1 / 2, d5 + d4 + d3 + d2 + d1),
    (-b1 / 2, d5 + d4 + d3 + d2 + d1),
    (-b1 / 2, d5 + d4 + d3 + d2),
    (-tw / 2, d5 + d4 + d3),
    (-tw / 2, d5 + d4),
    (-b2 / 2, d5)
]

# Cria o ambiente
doc = ezdxf.new()
msp = doc.modelspace()

# viga
msp.add_lwpolyline(points=pontos, close=True)

doc.saveas(os.path.join('dxf', 'SecaoVigaGirder.dxf'))
