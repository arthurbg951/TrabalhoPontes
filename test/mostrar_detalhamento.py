import sys
from PyQt5.QtWidgets import QApplication, QGraphicsView, QGraphicsScene, QGraphicsLineItem
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QTransform  # Importe a classe QPainter e QTransform
import ezdxf
import os

class DXFViewer(QGraphicsView):
    def __init__(self):
        super().__init__()
        self.setScene(QGraphicsScene())
        self.setSceneRect(0, 0, 100, 100)
        self.setRenderHint(QPainter.Antialiasing)  # Use QPainter.Antialiasing
        self.setRenderHint(QPainter.SmoothPixmapTransform)  # Use QPainter.SmoothPixmapTransform

        self.dxf_lines = []
        self.zoom_factor = 1.0

    def load_dxf_file(self, filename):
        doc = ezdxf.readfile(filename)
        modelspace = doc.modelspace()
        self.dxf_lines = [(line.dxf.start, line.dxf.end) for line in modelspace.query('LINE')]

    def draw_dxf(self):
        self.scene().clear()
        for start, end in self.dxf_lines:
            line_item = QGraphicsLineItem(start.x, start.y, end.x, end.y)
            self.scene().addItem(line_item)

    def wheelEvent(self, event):
        # Implement zoom in and out using the mouse wheel
        delta = event.angleDelta().y()
        if delta > 0:
            self.zoom_factor *= 1.1
        else:
            self.zoom_factor /= 1.1

        self.setTransform(QTransform().scale(self.zoom_factor, self.zoom_factor))

def main():
    app = QApplication(sys.argv)
    view = DXFViewer()
    view.load_dxf_file(os.path.join('..', 'dxf', 'PROJETO ARQUITETÔNICO - CASA l38.dxf'))  # Substitua 'exemplo.dxf' pelo caminho do seu arquivo DXF.
    view.draw_dxf()
    view.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
