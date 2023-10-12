import math

def fcd(fck: float) -> float:
    return fck / 1.4

def fyd(fy: float) -> float:
    return fy / 1.15

def area_bitola(bitola: float) -> float:
    return math.pi * bitola**2 / 4

def dominio(epslon: float) -> str:
    dominio = None
    if epslon <= 0:
        dominio = 1
    elif 0 < epslon <= 0.259:
        dominio = 2
    elif 0.259 < epslon <= 0.450:
        dominio = '3a'
    elif 0.450 < epslon <= 0.628:
        dominio = '3b'
    elif 0.628 < epslon <= 1:
        dominio = 4
    elif 1 < epslon:
        dominio = 5
    else:
        raise Exception('Intervalo do domínio não definido.')
    return str(dominio)

def As(Md: float, fyd: float, d: float, x: float) -> float:
    return Md / (fyd * (d - 0.4 * x))

def As_min(taxa_de_armadura: float, tw: float, d: float, d_linha: float) -> float:
    return taxa_de_armadura * tw * (d + d_linha)

def calcula_viga(
    b1,
    b2,
    tw,
    d1,
    d2,
    d3,
    d4,
    d5,
    recobrimento,
    fck,
    fy,
    Mg,
    Mq,
    Vsg,
    Vsq,
    diametro_bitola,
    diametro_pele,
    diametro_estribo
):
    Md = 1.35 * Mg + 1.5 * Mq
    Vsd = 1.35 * Vsg + 1.5 * Vsq

    d = (d1 + d2 + d3 + d4 + d5) - recobrimento
    # Equação x/d
    a = 0.4
    b = -1
    c = Md / (0.68 * b1 * (d**2) * fcd)

    delta = b**2 - 4 * a * c

    if delta < 0:
        raise Exception('Dimensões da viga não válidas.')

    raiz1 = (-b + math.sqrt(delta)) / (2 * a)
    raiz2 = (-b - math.sqrt(delta)) / (2 * a)

    epslon = min(raiz1, raiz2)
    x = epslon * d
    y = 0.8 * x

    # Condição definida no programa
    # Não se calcula a viga nessa situação
    if y > d1 and not (b1 == b2 == tw):
        raise Exception('Linha neutra fora da mesa.')

    print(f'x/d={epslon} x={x} y={y} Domínio {dominio(epslon)}')


if __name__ == '__main__':
    # Seção AA - Armadura positiva
    calcula_viga(
        b1=0.8,
        b2=0.8,
        tw=0.8,

        d1=0.2,
        d2=0.22,
        de=1.63,
        d4=0,
        d5=0,

        recobrimento=0.03,
        fck=20e6,
        fy=500e6,

        Mg=1304.017e3,
        Mq=2808.184e3
    )
