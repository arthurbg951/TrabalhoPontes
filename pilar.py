import math
from funcoes import interpolar
from Secoes import CircularSection

'''
EFEITOS DE 1ª ORDEM
'''
# Velocidade Básica
Vo = 30

# Fator Topográfico - Terreno plano ou fracamente acidentado
S1 = 1

# Fator de Rugosidade e Dimensão
# Classe B + Categoria I
h = 7  # m
z = h / 2
S2 = interpolar(5, 10, 1.04, 1.09, z)

# Fator Estatístico
# Ruína total ou parcial pode afetar a segurança ou possibilidade de
# socorro a pessoas após uma tempestade destrutiva
S3 = 1.1

# Velocidade Característica
Vk = Vo * S1 * S2 * S3
print(f'Vo={Vo}m/s S1={S1} S2={S2} S3={S3} Vk={Vk:.2f}m/s')

b = 14.6  # comprimento tabuleiro
a = 25  # comprimento ponte

# caso1 0°
l2 = a
l1 = b
print(f'Vento a 0°: l1/l2={l1/l2:.2f} h/l1={h/l1:.2f} isopleta={0.88}')
# caso2 90°
l1 = a
l2 = b
print(f'Vento a 90°: l1/l2={l1/l2:.2f} h/l1={h/l1:.2f} isopleta="fora da isopleta"')

Ca = 0.88
qw = Ca * 0.613 * Vk**2
print(f'Ca={Ca} qw={qw:.2f}N/m²')

n_pilares = 2
altura_pilar = 5.40
raio_pilar = 0.8  # m
comprimento = raio_pilar / math.pi
Ae = (comprimento / 2) * altura_pilar * 2
Ae += 1.20 * b
Ae += 0.8 * b
# Ae += # Adicionar área da seção da transversina do pilar
Mvento_k = qw * Ae * z / n_pilares
print(f'Mvento_k={Mvento_k/1e3:.2f}kNm')

Nd = 266.83e3  # kN
Nk = Nd / 1.4
eg1v = Mvento_k / Nk
print(f'Excentricidade global de 1ª ordem: eg1v={eg1v*1e2:.2f}cm')

'''
EFEITOS DE 2ª ORDEM
'''
# secao = CircularSection(raio_pilar)
# print(f'Inercia pilar circular = {secao.inercia():.2f}m4 pilar={secao.pilar_equivalente():.2f}')
# Estrutura de nós fixos
eg2v = 0


'''
IMPERFEIÇÕES GEOMÉTRICAS
'''
teta1 = 1 / (100 * math.sqrt(h))

if teta1 > 1 / 200:
    teta1 = 1 / 200
elif teta1 < 1 / 300:
    teta1 = 1 / 300

tetaa = teta1 * math.sqrt((1 + 1 / n_pilares) / 2)

deltacg = z * tetaa

Mimp_geom_k = Nk * deltacg / n_pilares
eig = Mimp_geom_k / Nk
print(f'Excentricidade de imperfeição geométrica: eig={eig*1e2:.2f}cm')


'''
RELAÇÃO VENTO - DESAPRUMO
'''
e2g = 0
print(f'Excentricidade de vento segunda ordem: e1g={e2g*1e2:.2f}cm')


'''
COMPRIMENTO DE FLAMBAGEM
'''
altura_transversina = 1
lo = altura_pilar + altura_transversina
le = min(lo + raio_pilar, altura_pilar)
# seção 1
ea_secao1 = le / 200
# seção 2
ea_secao2 = le / 400
print(f'Excentricidade de imperfeição geométrica local: ea1={ea_secao1*1e2:.2f}cm ea2={ea_secao2*1e2:.2f}cm')


'''
TRANSFERÊNCIA DE MOMENTO DE VIGA PARA PILAR 
'''
L = a
q = 0  # Carregamento da transversina do pilar
Meng = -q * L**2 / 12
rsup = Isup/Lsup
rinf = Iinf/Linf
rvig = Iviga/Lviga
Msup = Meng * rsup / (rinf + rsup + rvig)
