n = 6  # número de longarinas
E = 2.43  # distância entre eixos
equacoes = []

for i in range(1, n + 1):
    aux = (6 / n) * ((2 * i - n - 1) / ((n**2 - 1) * E))
    a = aux
    b = -aux * 7.05 + 1 / n
    equacoes.append((a, b))

print(f'Equações de Engesser-Courbon:')
for i, equacao in enumerate(equacoes):
    a, b = equacao
    print(f'n{i+1}(x)={a:.3f}x + {b:.3f}')


print(f'Pontos de análise:')
coordenada_x_do_comeco_trem_tipo = 2.5
pontos = [ponto + coordenada_x_do_comeco_trem_tipo for ponto in [0, 0.5, 2.5, 3]]
pontos_de_analise = []
for i, equacao in enumerate(equacoes):
    analise = []
    for ponto in pontos:
        a, b = equacao
        ni = a * ponto + b
        analise.append(ni)
        print(f'n{i+1}({ponto})={ni:.3f}')
    pontos_de_analise.append(analise)
    print()

comprimento_sem_trem_tipo = 3.4
for i, (a, y1, y2, b) in enumerate(pontos_de_analise):
    A1 = (a + b) * 3 / 2
    A2 = b * comprimento_sem_trem_tipo / 2
    Q1 = 75 * (y1 + y2)
    q1 = 5 * (A1 + A2)
    q2 = 5 * A2
    print(f'Viga {i+1}: Q1={Q1:.2f} q1={q1:.2f} q2={q2:.2f}')
