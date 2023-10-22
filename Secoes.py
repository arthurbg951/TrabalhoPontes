from abc import abstractmethod
from numpy.linalg import det

class ISection:
    @abstractmethod
    def area() -> float:
        '''
        Retorna a área da seção.
        '''
        ...

    @abstractmethod
    def inercia() -> float:
        '''
        Retorna o momento de inercia da seção.
        '''
        ...


class GirderSection(ISection):
    def __init__(self, b1, b2, tw, d1, d2, d3, d4, d5) -> None:
        self.b1 = b1
        self.b2 = b2
        self.tw = tw
        self.d1 = d1
        self.d2 = d2
        self.d3 = d3
        self.d4 = d4
        self.d5 = d5

    def area(self) -> float:
        return (
            self.b1 * self.d1 +
            (self.tw + self.b1) * self.d2 / 2 +
            self.tw * self.d3 +
            (self.tw + self.b2) * self.d4 / 2 +
            self.d5 * self.b2
        )

    def inercia() -> float:
        raise NotImplemented


class TSection(ISection):
    def __init__(self, b, d, tw, tf) -> None:
        self.b = b
        self.d = d
        self.tw = tw
        self.tf = tf

    def area(self) -> float:
        return self.b * self.tf + (self.d - self.tf) * self.tw

    def inercia() -> float:
        raise NotImplemented


class PotatoSection(ISection):
    def __init__(self, *pontos: tuple) -> None:
        self.pontos = list(pontos)

    def area(self) -> float:
        return det(self.pontos) / 2

    def inercia() -> float:
        raise NotImplemented
