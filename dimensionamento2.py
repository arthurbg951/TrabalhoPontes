import math
from Secoes import GirderSection
from carregamentos import main as calcula_pp
from funcoes import (
    to_red as re,
    to_yellow as ye,
    to_blue as bl,
    arredonda_pra_cima,
    arredonda_pra_baixo
)

# Formulas

def calcular_epslon(Md: float, b1: float, d: float, fcd: float) -> tuple[float, float]:
    '''
    Equação que retorna epslon (x/d).
    '''
    a = 0.4
    b = -1
    c = Md / (0.68 * b1 * (d**2) * fcd)

    delta = b**2 - 4 * a * c

    if delta < 0:
        raise Exception('Dimensões da viga não válidas.')

    raiz1 = (-b + math.sqrt(delta)) / (2 * a)
    raiz2 = (-b - math.sqrt(delta)) / (2 * a)
    return raiz1, raiz2

def verifica_dominio(epslon: float) -> str:
    '''
    Verifica o domínio com base em um epslon (x/d).
    '''
    if epslon < 0:
        return '1'
    elif 0 <= epslon <= 0.259:
        return '2'
    elif 0.259 < epslon <= 0.450:
        return '3a'
    elif 0.450 < epslon <= 0.628:
        return '3b'
    elif 0.628 < epslon <= 1:
        return '4'
    elif 1 < epslon:
        return '5'
    else:
        raise Exception('Intervalo do domínio não definido.')

def fcd(fck: float) -> float:
    return fck / 1.4

def fyd(fy: float) -> float:
    return fy / 1.15

def area_bitola(bitola: float) -> float:
    return math.pi * bitola**2 / 4

def As_min(taxa_de_armadura: float, tw: float, d: float, d_linha: float) -> float:
    return taxa_de_armadura * tw * (d + d_linha)

def As_pele(tw: float, h: float) -> float:
    if h >= 0.6:
        return (0.1 / 100) * tw * h
    else:
        return 0

def taxa_minima_armadura(fck: int) -> float:
    if 20 <= fck <= 30:
        return 0.15 / 100
    elif fck == 35:
        return 0.164 / 100
    elif fck == 40:
        return 0.179 / 100
    elif fck == 35:
        return 0.164 / 100
    elif fck == 45:
        return 0.194 / 100
    elif fck == 50:
        return 0.208 / 100
    elif fck == 55:
        return 0.211 / 100
    elif fck == 60:
        return 0.219 / 100
    elif fck == 65:
        return 0.226 / 100
    elif fck == 70:
        return 0.233 / 100
    elif fck == 75:
        return 0.239 / 100
    elif fck == 80:
        return 0.245 / 100
    elif fck == 85:
        return 0.251 / 100
    elif fck == 90:
        return 0.256 / 100
    else:
        raise Exception(f'Não existe concreto para fck={fck}!')

def alfa_v2(fck):
    return 1 - (fck / 1e6) / 250

def Vrd2(alfa_v2, fcd, tw, d):
    return 0.27 * alfa_v2 * fcd * tw * d

def fctd(fck):
    return 0.7 * (0.3 * math.pow(fck / 1e6, 2 / 3)) / 1.4

def Vc(fctd, tw, d):
    return 0.6 * fctd * 1e6 * tw * d

def Asw(Vsd, Vc, d, fyd):
    Vsw = Vsd - Vc
    fywd: int = None
    if fyd <= 435e6:
        fywd = fyd
    else:
        fywd = 435e6
    alfa = math.radians(90)
    return Vsw / (0.9 * d * fywd * (math.sin(alfa) + math.cos(alfa)))

def fctm(fck):
    return 0.3 * math.pow(fck / 1e6, 2 / 3)

def Asw_min(fctm, fywk, tw):
    alfa = math.radians(90)
    return 0.2 * (fctm * 1e6 / fywk) * tw * math.sin(alfa)


# Dimensionamento

def dimensionar_armadura_longitudinal(
    secao: GirderSection,
    d,
    cobrimento,
    Mg,
    Mq,
    diametro_bitola,
    fck,
    fy,
):
    Md = 1.35 * Mg + 1.5 * Mq

    fcd_calc = fcd(fck)
    raiz1, raiz2 = calcular_epslon(Md, secao.b1, d, fcd_calc)
    epslon = min(raiz1, raiz2)
    x = epslon * d
    y = 0.8 * x

    is_retangular_section = (secao.b1 == secao.b2 == secao.tw)
    Md1 = 0.85 * fcd_calc * (secao.b1 - secao.tw) * secao.d1 * (d - 0.5 * secao.d1)
    if y > secao.d1 and not is_retangular_section:
        Md2 = Md - Md1
        Md = Md2
        raiz1, raiz2 = calcular_epslon(Md2, secao.b1, d, fcd_calc)
        epslon = min(raiz1, raiz2)
        x = epslon * d
        y = 0.8 * x

    dominio = verifica_dominio(epslon)

    As1 = 0.85 * fcd_calc * (girder.b1 - girder.tw) * girder.d1 / fyd(fy)
    As2 = 0.68 * girder.b1 * d * epslon * fcd_calc / fyd(fy)
    # formula vista em sala
    # As2 = Md / (fyd * (d - 0.4 * x))  # Area de aço calculado
    As_calculado = As2
    if epslon <= 0.45:
        # Se a linha neutra passar da mesa
        if y > girder.d1 and not is_retangular_section:
            As_calculado += As1

    elif epslon > 0.45:
        print(ye(f"Necessita de armadura dupla."))
        print(ye(f'Verificar diferença do d". O cálculo não foi automatizado para isso.'))
        d_duas_linhas = cobrimento  # necessário verificar a porcentagem de diferença
        As_linha1 = Md - 0.68 * girder.b1 * d**2 * 0.45 * fcd_calc * (1 - 0.4 * 0.45) / (fyd(fy) * (d - d_duas_linhas))

        # Caso 1: linha neutra dentro da mesa
        if y <= girder.d1:
            As_calculado += As_linha1
        # Caso 2: linha neutra fora da mesa
        elif y > girder.d1:
            Md2 = 0.68 * girder.tw * d**2 * 0.45 * fcd_calc * (1 - 0.4 * 0.45)
            Md_linha = Md - Md1 - Md2
            As_linha2 = Md_linha / (fyd(fy) * (d - d_duas_linhas))
            As_calculado += As1 + As_linha2

    aco_minimo = As_min(taxa_minima_armadura(fck / 1e6), secao.tw, d, cobrimento)

    if As_calculado < aco_minimo:
        As_adotado = aco_minimo
    else:
        As_adotado = As_calculado

    num_bitolas = arredonda_pra_cima(As_adotado / area_bitola(diametro_bitola))

    return epslon, x, y, dominio, As_adotado, num_bitolas

def dimensionar_armadura_de_pele(secao: GirderSection, diametro_bitola_pele: float):
    As_pele_calculado = As_pele(secao.tw, (secao.d1 + secao.d2 + secao.d3 + secao.d4 + secao.d5))
    num_bitolas_pele = arredonda_pra_cima(As_pele_calculado / area_bitola(diametro_bitola_pele))

    return As_pele_calculado, num_bitolas_pele

def dimensionar_armadura_transversal(
        secao: GirderSection,
        diametro_estribo,
        num_ramos,
        d,
        fck,
        fy,
        Vsg,
        Vsq
):
    Vsd = 1.35 * Vsg + 1.5 * Vsq
    alfa_v2_calc = alfa_v2(fck)
    Vrd2_calc = Vrd2(alfa_v2_calc, fcd(fck), secao.tw, d)
    if Vsd < Vrd2_calc:
        # Não ocorre ruptura das diagonais de compressão. (Vsd<Vrd2)
        # Resistência a compressão do concreto
        Vc_calc = Vc(fctd(fck), secao.tw, d)
        As_w_calc = Asw(Vsd, Vc_calc, d, fyd(fy))
        As_min_calc = Asw_min(fctm(fck), fywk=fy, tw=secao.tw)
        if As_w_calc < As_min_calc:
            As_adotado = As_min_calc
        else:
            As_adotado = As_w_calc
        area_estribo = area_bitola(diametro_estribo)
        num_estribos = arredonda_pra_cima(As_adotado / (area_estribo * num_ramos))

        return Vrd2_calc, As_adotado, num_estribos

    else:
        raise Exception(re(f'Ocorre ruptura das diagonais de compressão. Vsd/Vrd2={Vsd/Vrd2_calc * 100:.2f}%'))


# Espaçamentos

def espacamento_max_estribos(Vsd, Vrd2, d):
    # Espaçamento de estribos - item 18.3.3.2 da NBR 6118 (2014)
    if Vsd <= 0.67 * Vrd2:
        if 0.6 * d >= 0.3:
            return 0.3
        else:
            return 0.6 * d
    elif Vsd > 0.67 * Vrd2:
        if 0.3 * d >= 0.3:
            return 0.2
        else:
            return 0.3 * d
    else:
        raise Exception(re('Ocorreu um erro no espaçamento de estribos.'))

def espacamento_armadura_transversal(num_estribos, espacamento_max_entre_estribos):
    espacamento_estribos = 100 / (num_estribos - 1)
    espacamento_estribos /= 100
    if espacamento_estribos > espacamento_max_entre_estribos:
        raise Exception(re(f'Não cabe {num_estribos} estribos em 1m.'))
    if espacamento_estribos < 3.5 * 1e-2:
        raise Exception(re(f'Espaçamento entre estribos não suporta 1 vibrador.'))
    return espacamento_estribos

def espacamento_armadura_longitudinal(
    secao: GirderSection,
    diametro_estribo,
    bitola_agregado,
    diametro_bitola,
    num_bitolas_longitudinal,
    num_ramos,
    cobrimento,
    d
):
    espacamento_min_horizontal = max(1.2 * bitola_agregado, 0.02, diametro_bitola)
    espacamento_min_vertical = max(0.5 * bitola_agregado, 0.02, diametro_bitola)

    num_max_de_bitolas_por_camada = arredonda_pra_baixo(
        ((secao.b2 - cobrimento * 2 - num_ramos * diametro_estribo * 2) + espacamento_min_horizontal) /
        (diametro_bitola + espacamento_min_horizontal)
    )

    if num_bitolas_longitudinal <= num_max_de_bitolas_por_camada:
        num_de_camadas = 1
        num_max_de_camadas = 1
        d_real = (secao.d1 + secao.d2 + secao.d3 + secao.d4 + secao.d5 - cobrimento - diametro_estribo - diametro_bitola / 2)
    else:
        num_de_camadas = arredonda_pra_cima(num_bitolas_longitudinal / num_max_de_bitolas_por_camada)
        num_max_de_camadas = arredonda_pra_baixo(
            ((secao.d5 - diametro_estribo - cobrimento) + espacamento_min_vertical) /
            (diametro_bitola + espacamento_min_vertical)
        )
        if num_de_camadas > num_max_de_camadas:
            raise Exception(re(f'Não existe seção suficiente para a quantidade de bitolas.'))
        d_real = secao.d1 + secao.d2 + secao.d3 + secao.d4
        d_real += (
            secao.d5 - cobrimento - diametro_estribo -
            (num_de_camadas * diametro_bitola + (num_de_camadas - 1) * espacamento_min_vertical)
        )  # Folga
        d_real += (num_de_camadas * (diametro_bitola) + (num_de_camadas - 1) * espacamento_min_vertical) / 2  # Metade da area bitolas com espaçamento

    # Condição de até no max 10% de diferença
    if (d - d_real) / (secao.d1 + secao.d2 + secao.d3 + secao.d4 + secao.d5) > 0.1:
        raise Exception(re(f'(d-d_real)/h > 10%'))

    return espacamento_min_horizontal, espacamento_min_vertical, num_max_de_bitolas_por_camada, num_de_camadas, num_max_de_camadas, d_real


def main(gider: GirderSection, Mg, Mq, Vsg, Vsq, fck, fy, cobrimento, diametro_bitola, diametro_bitola_pele, diametro_estribo, bitola_agregado, num_ramos):
    print(bl(f'PRIMEIRA ITERAÇÃO: Considerando d = h - cobrimento'))
    d = (gider.d1 + gider.d2 + gider.d3 + gider.d4 + gider.d5) - cobrimento
    epslon, x, y, dominio, As_longitudinal, num_bitolas_longitudinal = dimensionar_armadura_longitudinal(
        secao=gider,
        fck=fck,
        fy=fy,
        diametro_bitola=diametro_bitola,
        d=d,
        cobrimento=cobrimento,
        Mg=Mg,
        Mq=Mq,
    )
    print(f'x/d={epslon} x={x} y={y} Domínio {dominio}')
    print(f'Area de aço adotado={As_longitudinal*1e4:.2f}cm² -> {num_bitolas_longitudinal} Ø {diametro_bitola*1e3:.1f}mm')

    As_pele, num_bitolas_pele = dimensionar_armadura_de_pele(
        secao=gider,
        diametro_bitola_pele=diametro_bitola_pele
    )
    print(f'Area de aço pele={As_pele*1e4:.2f}cm² -> {num_bitolas_pele} Ø {diametro_bitola_pele*1e3:.1f}mm')

    Vrd2_calc, As_estribo, num_estribos = dimensionar_armadura_transversal(
        secao=gider,
        diametro_estribo=diametro_estribo,
        num_ramos=num_ramos,
        d=d,
        fck=fck,
        fy=fy,
        Vsg=Vsg,
        Vsq=Vsq,
    )
    Vsd = 1.35 * Vsg + 1.5 * Vsq

    print(f'Area de aço estribos={As_estribo*1e4:.2f}cm²/m -> {num_estribos}x{num_ramos} Ø {diametro_estribo*1e3:.1f}mm/m')
    print(f'Consumo esforço cortante = {Vsd/Vrd2_calc * 100:.2f}%')

    espacamento_max_estribos_calc = espacamento_max_estribos(Vsd, Vrd2_calc, d)
    # print(f'Espaçamento máximo entre estribos={espacamento_max_estribos_calc*1e2:.2f}cm')

    espacamento_estribos = espacamento_armadura_transversal(num_estribos, espacamento_max_estribos_calc)
    print(f'Espaçamento estribos={espacamento_estribos*1e2:.2f}cm')

    espacamento_min_horizontal, espacamento_min_vertical, num_max_de_bitolas_por_camada, num_de_camadas, num_max_de_camadas, d_real = espacamento_armadura_longitudinal(
        secao=gider,
        diametro_estribo=diametro_estribo,
        bitola_agregado=bitola_agregado,
        diametro_bitola=diametro_bitola,
        num_bitolas_longitudinal=num_bitolas_longitudinal,
        num_ramos=num_ramos,
        cobrimento=cobrimento,
        d=d
    )
    if num_bitolas_longitudinal <= num_max_de_bitolas_por_camada:
        print(f'1 camada com {num_bitolas_longitudinal} Ø de {diametro_bitola}mm')
        print(f'Diferença d_real e d utilizado = {math.fabs(d_real - d) * 100:.2f}%')
    else:
        print(f'Precisa de mais de uma camada. 1 camada suporta apenas {num_max_de_bitolas_por_camada} Ø de {diametro_bitola*1e3:.0f}mm c/ {espacamento_min_horizontal*1e2}cm')
        print(f'Numero de camadas: {num_de_camadas}. Descrição:')
        for i in range(num_de_camadas):
            if i < (num_de_camadas - 1):
                print(f'    {i+1} possui {num_max_de_bitolas_por_camada} Ø c/ {espacamento_min_horizontal*1e2}cm')
            else:
                qtd_ultima_camada = num_bitolas_longitudinal - (num_de_camadas - 1) * num_max_de_bitolas_por_camada
                print(f'    {i+1} possui {qtd_ultima_camada} Ø c/ pelo menos {espacamento_min_horizontal*1e2}cm')

    print(f'd={d} d_real={d_real} {((d - d_real) / (gider.d1 + gider.d2 + gider.d3 + gider.d4 + gider.d5)*100):.2f}% de diferença.')
    print()

    iteracao = 1
    while d != d_real:
        print(bl(f'EXECUTANDO {iteracao} ITERAÇÃO DA CORREÇÃO DO CENTROIDE DAS ARMADURAS.'))
        iteracao += 1
        d = d_real
        epslon, x, y, dominio, As_longitudinal, num_bitolas_longitudinal = dimensionar_armadura_longitudinal(
            secao=gider,
            fck=fck,
            fy=fy,
            diametro_bitola=diametro_bitola,
            d=d,
            cobrimento=cobrimento,
            Mg=Mg,
            Mq=Mq,
        )
        print(f'x/d={epslon} x={x} y={y} Domínio {dominio}')
        print(f'Area de aço adotado={As_longitudinal*1e4:.2f}cm² -> {num_bitolas_longitudinal} Ø {diametro_bitola*1e3:.1f}mm')

        As_pele, num_bitolas_pele = dimensionar_armadura_de_pele(
            secao=gider,
            diametro_bitola_pele=diametro_bitola_pele
        )
        print(f'Area de aço pele={As_pele*1e4:.2f}cm² -> {num_bitolas_pele} Ø {diametro_bitola_pele*1e3:.1f}mm')

        Vrd2_calc, As_estribo, num_estribos = dimensionar_armadura_transversal(
            secao=gider,
            diametro_estribo=diametro_estribo,
            num_ramos=num_ramos,
            d=d,
            fck=fck,
            fy=fy,
            Vsg=Vsg,
            Vsq=Vsq,
        )
        Vsd = 1.35 * Vsg + 1.5 * Vsq

        print(f'Area de aço estribos={As_estribo*1e4:.2f}cm²/m -> {num_estribos}x{num_ramos} Ø {diametro_estribo*1e3:.1f}mm/m')
        print(f'Consumo esforço cortante = {Vsd/Vrd2_calc * 100:.2f}%')

        espacamento_max_estribos_calc = espacamento_max_estribos(Vsd, Vrd2_calc, d)
        # print(f'Espaçamento máximo entre estribos={espacamento_max_estribos_calc*1e2:.2f}cm')

        espacamento_estribos = espacamento_armadura_transversal(num_estribos, espacamento_max_estribos_calc)
        print(f'Espaçamento estribos={espacamento_estribos*1e2:.2f}cm')

        espacamento_min_horizontal, espacamento_min_vertical, num_max_de_bitolas_por_camada, num_de_camadas, num_max_de_camadas, d_real = espacamento_armadura_longitudinal(
            secao=gider,
            diametro_estribo=diametro_estribo,
            bitola_agregado=bitola_agregado,
            diametro_bitola=diametro_bitola,
            num_bitolas_longitudinal=num_bitolas_longitudinal,
            num_ramos=num_ramos,
            cobrimento=cobrimento,
            d=d
        )
        if num_bitolas_longitudinal <= num_max_de_bitolas_por_camada:
            print(f'1 camada com {num_bitolas_longitudinal} Ø de {diametro_bitola}mm')
            print(f'Diferença d_real e d utilizado = {math.fabs(d_real - d) * 100:.2f}%')
        else:
            print(f'Precisa de mais de uma camada. 1 camada suporta apenas {num_max_de_bitolas_por_camada} Ø de {diametro_bitola*1e3:.0f}mm c/ {espacamento_min_horizontal*1e2}cm')
            print(f'Numero de camadas: {num_de_camadas}. Descrição:')
            for i in range(num_de_camadas):
                if i < (num_de_camadas - 1):
                    print(f'    {i+1}ª possui {num_max_de_bitolas_por_camada} Ø c/ {espacamento_min_horizontal*1e2}cm')
                else:
                    qtd_ultima_camada = num_bitolas_longitudinal - (num_de_camadas - 1) * num_max_de_bitolas_por_camada
                    print(f'    {i+1}ª possui {qtd_ultima_camada} Ø c/ pelo menos {espacamento_min_horizontal*1e2}cm')

        print(f'd={d} d_real={d_real} {((d - d_real) / (gider.d1 + gider.d2 + gider.d3 + gider.d4 + gider.d5)*100):.2f}% de diferença.')
        print()


def dados():
    # Seção Girder
    girder = GirderSection(
        b1=2.43,
        b2=0.8,
        tw=0.4,

        d1=0.2,
        d2=0,
        d3=0.4,
        d4=0,
        d5=0.2,
    )

    # Comprimento Ponte
    L = 25

    # Peso próprio das vigas
    PP = max(*calcula_pp(girder.b1, girder.b2, girder.tw, girder.d1, girder.d2, girder.d3, girder.d4, girder.d5))

    # Solicitações
    Mg = (PP * L**2 / 8) * 1e3
    Mq = 3443.9e3
    Vsg = (PP * L) * 1e3 / 2
    Vsq = 571.1e3

    # Concreto
    fck = 30e6

    # Aço
    fy = 500e6

    cobrimento = 0.04

    diametro_bitola = 25e-3
    diametro_bitola_pele = 10e-3
    diametro_estribo = 10e-3

    bitola_agregado = (3 / 4) * 2.54e-2

    num_ramos = 2

    data = {
        'girder': girder,
        'L': L,
        'PP': PP,
        'Mg': Mg,
        'Mq': Mq,
        'Vsg': Vsg,
        'Vsq': Vsq,
        'fck': fck,
        'fy': fy,
        'cobrimento': cobrimento,
        'diametro_bitola': diametro_bitola,
        'diametro_bitola_pele': diametro_bitola_pele,
        'diametro_estribo': diametro_estribo,
        'bitola_agregado': bitola_agregado,
        'num_ramos': num_ramos
    }

    return data


if __name__ == '__main__':

    data = dados()

    girder = data['girder']
    Mg = data['Mg']
    Mq = data['Mq']
    Vsg = data['Vsg']
    Vsq = data['Vsq']
    fck = data['fck']
    fy = data['fy']
    cobrimento = data['cobrimento']
    diametro_bitola = data['diametro_bitola']
    diametro_bitola_pele = data['diametro_bitola_pele']
    diametro_estribo = data['diametro_estribo']
    bitola_agregado = data['bitola_agregado']
    num_ramos = data['num_ramos']

    print(ye(f'Hipótese 1:'))
    main(girder, Mg, Mq, Vsg, Vsq, fck, fy, cobrimento, diametro_bitola, diametro_bitola_pele, diametro_estribo, bitola_agregado, num_ramos)

    girder = GirderSection(
        # b1=1.07893,
        b1=1.079,
        b2=0.5,
        tw=0.2,

        d1=0.2,
        d2=0,
        d3=0.5,
        d4=0,
        d5=0.5,
    )

    print(ye(f'Hipótese 2:'))
    main(girder, 6_000e3, 0, 0, 0, fck, fy, cobrimento, 25 * 1e-3, 6.3 * 1e-3, 6.3 * 1e-3, bitola_agregado, 1)

    girder = GirderSection(
        b1=0.5,
        b2=0.5,
        tw=0.5,

        d1=0,
        d2=0,
        d3=0,
        d4=0,
        d5=0.5,
    )

    print(ye(f'Hipótese 3:'))
    main(girder, 500e3, 0, 0, 0, fck, fy, cobrimento, 40 * 1e-3, 6.3 * 1e-3, 6.3 * 1e-3, bitola_agregado, 1)
