import math

# Dados da Geometria Aparelho de apoio.
a = 400  # dimensão a (mm).
b = 500  # dimensão b (mm).
n = 4  # Numero de camadas de elastômeros.
ts = 4  # Espessura da chapa de aço (mm).
te = 12  # Espessura do Elastômero (mm).
camadaex = 2.5  # Espessura da camada externa de Elastômero (mm).
Borda_externa = 4

# Dados de Entrada.

Vxd = 38.28  # deslocamento (mm)
Vyd = 7.36  # deslocamento (mm)
Fzk = 2140e3  # Força (N) - Reações da longarina
Fzd = Fzk * 1.4
Fzdmin = 800e3  # Força (N)
Fxd = 130e3  # Força (N) - Força no eixo x (vento)
Fyd = 25e3  # Força (N) - Força no eixo x (frenagem)
Alfa_ad = 0.001
Alfa_bd = 0
G = 0.9e6  # Normativo - Módulo de cisalhamento
Fy = 210e6  # Tensão do aço
t1 = 12  # Espessura do elastometro (mm)
t2 = 12  # Espessura do elastometro (mm)


# Verificação 1: Máxima Deformação Total de Calculo.
print(f'Verificação 1: Máxima Deformação Total de Calculo.')
Eud = 7
Kl = 1.5

a_linha = a - 2 * Borda_externa
print(f'a_linha: {a_linha}')
b_linha = b - 2 * Borda_externa
print(f'b_linha: {b_linha}')
A1 = a_linha * b_linha
print(f'A1:{A1}')
Ar = A1 * (1 - (Vxd / (a - 2 * Borda_externa)) - (Vyd / b)) / 1000000
print(f'Ar:{Ar}')

Ip = 2 * (a_linha + b_linha)
print(f'Ip:{Ip}')

S = A1 / (Ip * te)
print(f'S:{S}')

Ecd = 1.5 * Fzd / (G * Ar * S)
print(f'Ecd:{Ecd}')

Vxyd = math.sqrt((Vxd**2) + (Vyd**2))
print(f'Vxyd:{Vxyd}')

tq = (n * te) + 2 * camadaex
print(f'tq:{tq}')

Eqd = (Vxyd / tq)
print(f'Eqd:{Eqd}')

Ealfa_d = ((((a_linha**2) * Alfa_ad) + ((b_linha**2) * Alfa_bd)) * te) / (2 * n * te**3)
print(f'Ealfa_d:{Ealfa_d}')

Etd = Kl * (Ecd + Eqd + Ealfa_d)
print(f'Etd:{Etd}')

# Máxima Deformação Total de Calculo.
print(f'Máxima Deformação Total de Calculo.')
if Etd < Eud:
    print("okay")
else:
    print("Não Okay")


# Verificação 2: Expessura da Chapa de Aço.
print(f'Verificação 2: Expessura da Chapa de Aço.')
Kh = 1
Kp = 1.3
Gama_m = 1


ts_linha = (Kp * Fzd * (t1 + t2) * Kh * Gama_m) / (Ar * Fy)
print(f'ts_linha:{ts_linha}')

if ts_linha < ts:
    print("okay")
else:
    print("Não Okay")

# Verificação 3: Condição limite - Rotação
print(f'Verificação 3: Condição limite - Rotação')
Krd = 3
Vzd = 3.7
Clr = ((a_linha * Alfa_ad) + (b_linha * Alfa_bd)) / Krd
print(f'Clr:{Clr}')


# Verificação 4: Condição limite - Estabilidade a Flanbagem
print(f'Verificação 4: Condição limite - Estabilidade a Flanbagem')
Ef = Fzd / (Ar * 1000000)
print(f'Ef:{Ef}')

Ef2 = (2 * a_linha * G * S) / (3 * tq * 1000000)
print(f'Ef2:{Ef2}')

if Ef < Ef2:
    print("okay")
else:
    print("Não Okay")


# Verificação 5: Condição limite - Estabilidade ao Deslizamento
print(f'Verificação 5: Condição limite - Estabilidade ao Deslizamento')
# sob cargas permanentes
print(f'sob cargas permanentes')

Sigma_cdmin = Fzdmin / (Ar * 1000000)
print(f'Sigma_cdmin:{Sigma_cdmin}')

if Sigma_cdmin >= 3:
    print("okay")
else:
    print("Não Okay")


# sob cargas totais
print(f'sob cargas totais')
Kf = 0.6

sigma_m = Fzdmin / (Ar * 1000000)
print(f'Sigma_m:{sigma_m}')

Ue = 0.1 + ((1.5 * Kf) / sigma_m)
print(f'Ue:{Ue}')

Fxyd = math.sqrt((Fxd**2) + (Fyd**2))
print(f'Fxyd:{Fxyd}')

Verificacao = Fxyd - (Ue * Fzdmin)
print(f'verificacao:{Verificacao}')

if Verificacao < 0:
    print("okay")
else:
    print("Não Okay")
