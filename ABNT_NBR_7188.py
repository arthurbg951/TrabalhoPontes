print(f'\n### ABNT NBR 7188 ###')
'''5 Ações em pontes e viadutos'''
'''
5.1 Cargas móveis

Q = P*CIV*CNF*CIA
q = p*CIV*CNF*CIA

P = 75 kN
p = 5 kN/m²

Para obras de estradas vicinais municipais:
P = 40 kN
p = 4 kN/m²
'''
def get_Q(P, CIV, CNF, CIA):
    return P * CIV * CNF * CIA
def get_q(p, CIV, CNF, CIA):
    return p * CIV * CNF * CIA


P = 75
p = 5
print(f'P: {P} kN')
print(f'p: {p} kN')
'''
5.1.1 Cargas nos passeios
Nos passeios para pedestres das pontes e viadutos, adotar carga uniformemente distribuída
de 3 kN/m² na posição mais desfavorável concomitante com a carga móvel rodoviária, para verificações
e dimensionamentos dos diversos elementos estruturais, assim como para verificações globais.
'''
q_passeio = 3
print(f'Carga no passeio: {q_passeio} kN')
