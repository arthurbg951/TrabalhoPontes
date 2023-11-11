from dimensionamento import Mg, Mq, Vsg, Vsq, As, d
from dimensionamento2 import dados
from numpy import power

# Seção Girder
data = dados()
secao = data['girder']

b1 = secao.b1
b2 = secao.b2
tw = secao.tw

d1 = secao.d1
d2 = secao.d2
d3 = secao.d3
d4 = secao.d4
d5 = secao.d5

'''
Considera-se apenas a ponte bi apoioada.
Não considera momentos fletores negativos.
'''

Vsd_max = Vsg + 0.5 * Vsq
Vsd_min = Vsg
delta_Vsd = Vsd_max - Vsd_min

Md_max_positiva = Mg + 0.5 * Mq
Md_min_positiva = Mg
delta_M_positiva = Md_max_positiva - Md_min_positiva

Md_max_negativa = Mg / 3 + 0.5 * Mq / 3
Md_min_negativa = Mg / 3
delta_M_negativa = Md_max_negativa - Md_min_negativa


# Verificação das armaduras negativas
alfa_e = 10  # dúvida
As_ef = As
bf = b2

x11 = (
    (-alfa_e * As_ef +
     power(
         power(alfa_e * As_ef, 2) +
         2 * bf * alfa_e * As_ef * d,
         1 / 2)
     ) /
    bf
)

print(f'Posição da linha neutra: {x11}')

hf = d1
if x11 > hf:
    ...
