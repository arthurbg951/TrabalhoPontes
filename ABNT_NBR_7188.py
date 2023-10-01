print(f'### ABNT NBR 7188 ###')
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

def get_Q(P: float, CIV: float, CNF: float, CIA: float) -> float:
    return P * CIV * CNF * CIA

def get_q(p: float, CIV: float, CNF: float, CIA: float) -> float:
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


'''
5.1.2 Coeficientes de ponderação de cargas verticais
'''

def CIV(vao_pilares: float) -> float:
    '''
    Coeficiente de impacto vertical
    '''
    if vao_pilares < 10:
        return 1.35
    elif vao_pilares >= 10 and vao_pilares <= 200:
        return 1 + 1.06 * (20 / (vao_pilares + 50))
    else:
        raise Exception(f'Estrutura com vão maior que 200m não é definido na norma.')

def CNF(numero_de_faixas: int) -> float:
    '''
    Coeficiente de número de faixas
    '''
    cnf = 1 - 0.05 * (numero_de_faixas - 2)
    if cnf > 0.9:
        return cnf
    else:
        return 0.9

def CIA(tipo_estrutura: str) -> float:
    '''
    Coeficiente de impacto adicional

    Valores permitidos para tipo_estrutura ['concreto', 'mista', 'aco']
    '''
    if tipo_estrutura == 'concreto' or tipo_estrutura == 'mista':
        return 1.25
    elif tipo_estrutura == 'aco':
        return 1.15
    else:
        raise Exception('O tipo da estrutura definido em norma é apenas concreto,mista ou aço.')


if __name__ == '__main__':
    fator_de_impacto = CIA('concreto') * CNF(2) * CIV(20)
    print(f'Fator de impacto calculado: {fator_de_impacto:.3f}')
