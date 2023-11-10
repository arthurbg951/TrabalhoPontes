import numpy as np
import matplotlib.pyplot as plt
from funcoes import integrate_linear_function


n = 6  # número de longarinas
E = 2.43  # distância entre eixos
# n = 5  # número de longarinas
# E = 3.24  # distância entre eixos
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
# coordenada_x_do_comeco_trem_tipo = 0.4
coordenada_x_do_comeco_trem_tipo = 2.5
# coordenada_x_do_comeco_trem_tipo = 2.5
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

# comprimento_sem_trem_tipo = 9.965
comprimento_sem_trem_tipo = 3.4
print(f'Trem tipo:')
for i, (a, y1, y2, b) in enumerate(pontos_de_analise):
    a = abs(a)
    y1 = abs(y1)
    y2 = abs(y2)
    b = abs(b)
    A1 = integrate_linear_function(equacoes[i][0], equacoes[i][1], pontos[0], pontos[len(pontos) - 1], desired_error=0.0001)
    A2 = integrate_linear_function(equacoes[i][0], equacoes[i][1], pontos[len(pontos) - 1], pontos[len(pontos) - 1] + comprimento_sem_trem_tipo, desired_error=0.0001)
    Q1 = 75 * (y1 + y2)
    q1 = 5 * (A1 + A2)
    q2 = 5 * A2
    print(f'Viga {i+1}: Q1={Q1:.2f} q1={q1:.2f} q2={q2:.2f} A1={A1} A2={A2}')

# Plot das equações
comprimento_tabuleiro = 14.6
x = np.linspace(0, comprimento_tabuleiro, 100)  # Gere 100 pontos entre 0 e comprimento_tabuleiro para o eixo x
plt.figure()

for i, equacao in enumerate(equacoes):
    a, b = equacao
    y = a * x + b
    plt.plot(x, y, label=f'n{i+1}(x)={a:.3f}x + {b:.3f}')

# linha da viga
plt.plot([0, comprimento_tabuleiro], [0, 0], label='transversina', color='black')

# linhas do trem tipo
# a, y1, y2, b = pontos_de_analise[0]
# a1, y11, y21, b1 = pontos_de_analise[len(pontos_de_analise) - 1]
# x1, x2, x3, x4 = pontos
# plt.plot([x1, x1], [a1, a], linestyle='--', color='gray')
# plt.plot([x2, x2], [y11, y1], linestyle='--', color='gray')
# plt.plot([x3, x3], [y21, y2], linestyle='--', color='gray')
# plt.plot([x4, x4], [b1, b], linestyle='--', color='gray')
# x5 = x4 + comprimento_sem_trem_tipo
# ultima_equacao = equacoes[len(equacoes) - 1]
# a, b = ultima_equacao
# y5 = a * x5 + b
# primeira_equacao = equacoes[0]
# a, b = primeira_equacao
# y6 = a * x5 + b if a * x5 + b < 0 else 0
# plt.plot([x5, x5], [y5, y6], linestyle='--', color='gray')

plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title('Gráfico das Equações de Engesser-Courbon')
plt.grid(True)
plt.savefig('equações_engesser-courbon.png')
plt.show()
