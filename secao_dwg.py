from dados import b1, b2, tw, d1, d2, d3, d4, d5, d_linha
import ezdxf
import os

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
