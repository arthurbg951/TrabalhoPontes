from ABNT_NBR_7188 import P, p, CNF, CIA, CIV
from dados import b1, b2, tw, d1, d2, d3, d4, d5

'''
  Entrada de dados:
'''
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
area_secao_longarina = (
    b1 * d1 +
    (tw + b1) * d2 / 2 +
    tw * d3 + (tw + b2) * d4 / 2 +
    d5 * b2
)

# Guarda_roda
area_guarda_roda = 0.218  # m²

# Guarda_corpo
q_guarda_corpo = 0.157  # kN/m

# Transversinas
area_septo_pilar = 0.7 * 0.35  # altura x base
comprimento_septo_pilar = b1  # m

# Recapeamento
q_recapeamento = 2  # kN/m²

# Comprimentos adotados
espessura_de_asfalto = 0.04  # m
altura_passeio = 0.04  # m

# CARREGAMENTOS FTOOL
# Distribuído
ppV1 = area_secao_longarina * peso_especifico_concreto
ppV1 += q_guarda_corpo
ppV1 += 2 * 0.04 * peso_especifico_pavimento
ppV1 += 2 * q_recapeamento
ppV1 += area_guarda_roda * peso_especifico_concreto

ppV2 = area_secao_longarina * peso_especifico_concreto
ppV2 += 2.36 * 0.04 * peso_especifico_pavimento
ppV2 += 2.36 * q_recapeamento

ppV3 = area_secao_longarina * peso_especifico_concreto
ppV3 += b1 * 0.04 * peso_especifico_pavimento
ppV3 += b1 * q_recapeamento

ppV4 = area_secao_longarina * peso_especifico_concreto
ppV4 += area_guarda_roda * peso_especifico_concreto
ppV4 += (b1 - 0.4) * 0.04 * peso_especifico_pavimento
ppV4 += (b1 - 0.4) * q_recapeamento

ppV5 = area_secao_longarina * peso_especifico_concreto
ppV5 += q_guarda_corpo
ppV5 += (b1 - 0.1) * 0.04 * peso_especifico_pavimento
ppV5 += (b1 - 0.1) * q_recapeamento

ppV6 = area_secao_longarina * peso_especifico_concreto
ppV6 += q_guarda_corpo
ppV6 += (b1 - 0.1) * 0.04 * peso_especifico_pavimento
ppV6 += (b1 - 0.1) * q_recapeamento

# Concentrado
concentrada = area_septo_pilar * comprimento_septo_pilar * peso_especifico_concreto

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
