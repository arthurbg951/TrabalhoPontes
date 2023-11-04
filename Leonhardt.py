import math

# Para transversinas e longarinas de seção constante
'''
J_barra: Inércia da transversina
J: Inércia da longarina
E: afastamento recíproco das longarinas
L: vão
'''
ni = J_barra / J
lambd = E / L
zeta = ni / (2 * lambd)**3

# Para transversinas e longarinas com seções variáveis
'''
L: comprimento do tabuleiro
l: largura do tabuleiro
n: número de longarinas
t: número de transversinas
{E: módulo de elasticidade}
Pl: rigidez média das longarinas (EJ)
Pt: rigidez média das transversinas (EJ_barra)
'''
lambd = (l / 2 * L) * (math.pow(L * n * Pl / (l * t * Pt, 2)))
