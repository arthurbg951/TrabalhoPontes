import ezdxf

# Cria o ambiente
doc = ezdxf.new()
msp = doc.modelspace()

# Linha
msp.add_line(start=(0, 0), end=(5, 5))

# Polilinha
points = [(0, 0), (5, 0), (5, 5), (0, 5)]  # Corrija as coordenadas aqui
msp.add_lwpolyline(points=points, close=True)

# Círculo
msp.add_circle(center=(5,5), radius=5)

doc.saveas("teste.dxf")
