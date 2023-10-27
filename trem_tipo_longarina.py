'''
O código a seguir desconsidera pontes com balanço na seção transversal
'''
from ABNT_NBR_7188 import P, p, CNF, CIA, CIV

# Entrada de dados:
# Trem tipo intermediário
distancia_1o_vao = 2.92
distancia_2o_vao = 2.92
# Trem tipo canto
distancia_entre_pilares = 2.92


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
Q1 = Q * (y1 + 1 + y2)
q1 = q * (A1 + A2 + A3)
q2 = q * (A1 + A2)

print(f'TREM TIPO LONGARINAS INTERMEDIÁRIAS:')
print(f'    Carga concentrada: {Q1:.1f}')
print(f'    Externo: {q1:.2f}')
print(f'    Interno: {q2:.2f}')


# TREM TIPO LONGARINAS DE CANTO
fator_de_impacto = CNF(2) * CIA('concreto') * CIV(20)

# Método por linha de fluência - Longarinas intermediárias
comprimento_trem_tipo = 3
if distancia_entre_pilares < comprimento_trem_tipo:
    print('\u001b[33m' + 'Trem tipo maior que a distancia entre pilares. Considerando vão=3m' + '\u001b[0m')
    distancia_entre_pilares = 3
distancia_entre_rodas = 2
Q = P
q = p
a = 1
y1 = a * (distancia_entre_pilares - 0.5) / distancia_entre_pilares
y2 = a * (distancia_entre_pilares - (0.5 + distancia_entre_rodas)) / distancia_entre_pilares
b = a * (distancia_entre_pilares - (2 * 0.5 + distancia_entre_rodas)) / distancia_entre_pilares
A2 = (distancia_entre_pilares - comprimento_trem_tipo) * b / 2
A1 = distancia_entre_pilares * a / 2 - A2
Q1 = Q * (y1 + y2)
q1 = q * (A1 + A2)
q2 = q * A2

print(f'TREM TIPO LONGARINAS CANTOS:')
print(f'    Carga concentrada: {Q1:.1f}')
print(f'    Externo: {q1:.2f}')
print(f'    Interno: {q2:.2f}')

print(f'FATOR DE IMPACTO={fator_de_impacto:.2f}')
