from ABNT_NBR_7188 import P, p, CNF, CIA, CIV

# Trem tipo
fator_de_impacto = CNF(2) * CIA('concreto') * CIV(20)

# Método por linha de fluência
distancia_1o_vao = 25 / 2
distancia_2o_vao = 25 / 2

comprimento_trem_tipo = 6
distancia_entre_rodas = 1.5
Q = P
q = p
y1 = (distancia_1o_vao - distancia_entre_rodas) / distancia_1o_vao
a = (distancia_1o_vao - 2 * distancia_entre_rodas) / distancia_1o_vao
y2 = (distancia_2o_vao - distancia_entre_rodas) / distancia_2o_vao
b = (distancia_2o_vao - 2 * distancia_entre_rodas) / distancia_2o_vao
A1 = (distancia_1o_vao - 2 * distancia_entre_rodas) * a / 2
A3 = (distancia_2o_vao - 2 * distancia_entre_rodas) * b / 2
A2 = distancia_1o_vao * 1 / 2 - A1 + distancia_2o_vao * 1 / 2 - A3

Q1 = fator_de_impacto * Q * (y1 + 1 + y2)
q1 = fator_de_impacto * q * (A1 + A2 + A3)
q2 = fator_de_impacto * q * (A1 + A2)

print(f'TREM TIPO:')
print(f'    Carga concentrada: {Q1}')
print(f'    Externo: {q1:.3f}')
print(f'    Interno: {q2:.3f}')

print(f'FATOR DE IMPACTO={fator_de_impacto:.3f}')
