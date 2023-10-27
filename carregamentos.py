from ABNT_NBR_7188 import P, p, CNF, CIA, CIV
from dados import b1, b2, tw, d1, d2, d3, d4, d5

# Entrada de dados:
# Trem tipo intermediário
distancia_1o_vao = b1
distancia_2o_vao = b1
# Trem tipo canto
distancia_entre_longarinas = b1


# Pesos específicos Materiais
peso_especifico_concreto = 25  # kN/m³
peso_especifico_pavimento = 24  # kN/m³

# AREAS DO PROJETO CAD
# Longarina
area_secao_intermediaria = (
    b1 * d1 +
    (tw + b1) * d2 / 2 +
    tw * d3 + (tw + b2) * d4 / 2 +
    d5 * b2
)
area_secao_canto = (
    tw * (d1 + d2 + d3 + d4 + d5) +
    ((d1 + d2) + d1) * (b1 - tw) / 2 +
    ((d4 + d5) + d5) * (b2 - tw) / 2
)

# Guarda_roda
area_guarda_roda = 0.218  # m²

# Transversinas
area_tranversina_pilar = 0.7 * 0.35  # altura x base
area_tranversina_vao = 0  # altura x base
comprimento_transversina_pilar = 2.92  # m
comprimento_metade_transversina_vao = 0  # m

# Recapeamento
q_recapeamento = 2  # kN/m²

# Comprimentos adotados
espessura_de_asfalto = 0.1  # m
altura_passeio = 0.205  # m

# CARREGAMENTOS FTOOL
# Distribuído
ppV1 = area_secao_canto * peso_especifico_concreto
ppV1 += (comprimento_transversina_pilar / 2) * altura_passeio * peso_especifico_concreto
ppV1 += area_guarda_roda * peso_especifico_concreto

ppV2 = area_secao_intermediaria * peso_especifico_concreto
ppV2 += 1.04 * altura_passeio * peso_especifico_concreto
ppV2 += (0.42 + comprimento_transversina_pilar / 2) * espessura_de_asfalto * peso_especifico_pavimento
ppV2 += (0.42 + comprimento_transversina_pilar / 2) * q_recapeamento

ppV3 = area_secao_intermediaria * peso_especifico_concreto
ppV3 += comprimento_transversina_pilar * espessura_de_asfalto * peso_especifico_pavimento
ppV3 += comprimento_transversina_pilar * q_recapeamento

ppV4 = area_secao_intermediaria * peso_especifico_concreto
ppV4 += 0.3 * altura_passeio * peso_especifico_concreto
ppV4 += 1.02 * espessura_de_asfalto * peso_especifico_pavimento
ppV4 += 1.02 * q_recapeamento
ppV4 += ((comprimento_transversina_pilar / 2) + 0.14) * espessura_de_asfalto * peso_especifico_pavimento
ppV4 += ((comprimento_transversina_pilar / 2) + 0.14) * q_recapeamento

ppV5 = area_secao_intermediaria * peso_especifico_concreto
ppV5 += 1.38 * espessura_de_asfalto * peso_especifico_pavimento
ppV5 += 1.38 * q_recapeamento
ppV5 += ((comprimento_transversina_pilar / 2) + 0.08) * altura_passeio * peso_especifico_concreto

ppV6 = area_secao_canto * peso_especifico_concreto
ppV6 += (comprimento_transversina_pilar / 2) * altura_passeio * peso_especifico_concreto
ppV6 += area_guarda_roda * peso_especifico_concreto

# Concentrado
concentrada = area_tranversina_pilar * comprimento_transversina_pilar * peso_especifico_concreto

# Fator de impacto
fator_de_impacto = CNF(2) * CIA('concreto') * CIV(20)

# Método por linha de fluência - Longarinas intermediárias
# TREM TIPO LONGARINAS INTERMEDIÁRIAS
comprimento_trem_tipo = 3
distancia_entre_rodas = 2
Q = P
q = p
y1 = (distancia_1o_vao - distancia_entre_rodas / 2) / distancia_1o_vao
a = (distancia_1o_vao - (distancia_entre_rodas / 2 + 0.5)) / distancia_1o_vao
y2 = (distancia_2o_vao - distancia_entre_rodas / 2) / distancia_2o_vao
b = (distancia_2o_vao - (distancia_entre_rodas / 2 + 0.5)) / distancia_2o_vao
A1 = (distancia_1o_vao - (distancia_entre_rodas / 2 + 0.5)) * a / 2
A3 = (distancia_2o_vao - (distancia_entre_rodas / 2 + 0.5)) * b / 2
A2 = distancia_1o_vao * 1 / 2 - A1 + distancia_2o_vao * 1 / 2 - A3
Q1_INTERMEDIARIO = Q * (y1 + 1 + y2)
q1_INTERMEDIARIO = q * (A1 + A2 + A3)
q2_INTERMEDIARIO = q * (A1 + A2)

# Método por linha de fluência - Longarinas intermediárias
comprimento_trem_tipo = 3
if distancia_entre_longarinas < comprimento_trem_tipo:
    distancia_entre_longarinas = 3
distancia_entre_rodas = 2
Q = P
q = p
a = 1
y1 = a * (distancia_entre_longarinas - 0.5) / distancia_entre_longarinas
y2 = a * (distancia_entre_longarinas - (0.5 + distancia_entre_rodas)) / distancia_entre_longarinas
b = a * (distancia_entre_longarinas - (2 * 0.5 + distancia_entre_rodas)) / distancia_entre_longarinas
A2 = (distancia_entre_longarinas - comprimento_trem_tipo) * b / 2
A1 = distancia_entre_longarinas * a / 2 - A2
Q1_CANTOS = Q * (y1 + y2)
q1_CANTOS = q * (A1 + A2)
q2_CANTOS = q * A2

if __name__ == '__main__':
    print(f'TREM TIPO LONGARINAS CANTOS:')
    if distancia_entre_longarinas == comprimento_trem_tipo:
        print('\u001b[33m' + 'Trem tipo maior que a distancia entre pilares. Considerando vão=3m.' + '\u001b[0m')
    print(f'    Carga concentrada: {Q1_CANTOS:.1f}')
    print(f'    Externo: {q1_CANTOS:.2f}')
    print(f'    Interno: {q2_CANTOS:.2f}')

    print(f'TREM TIPO LONGARINAS INTERMEDIÁRIAS:')
    print(f'    Carga concentrada: {Q1_INTERMEDIARIO:.1f}')
    print(f'    Externo: {q1_INTERMEDIARIO:.2f}')
    print(f'    Interno: {q2_INTERMEDIARIO:.2f}')

    print(f'CARGAS DISTRIBUÍDAS:')
    print(f'    V1: {ppV1:.2f}')
    print(f'    V2: {ppV2:.2f}')
    print(f'    V3: {ppV3:.2f}')
    print(f'    V4: {ppV4:.2f}')
    print(f'    V5: {ppV5:.2f}')
    print(f'    V6: {ppV6:.2f}')

    print(f'CARGAS CONCENTRADAS:')
    print(f'    Transversina no pilar: {concentrada:.2f}')

    print(f'FATOR DE IMPACTO={fator_de_impacto:.2f}')