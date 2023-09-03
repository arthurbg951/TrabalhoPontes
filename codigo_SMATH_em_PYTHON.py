# DADOS DO PROJETO
print(f'### DADOS DO PROJETO ###')
# DEIXAR SEMPRE OS DADOS NO SI
fck = 20  # MPa
peso_especifico_concreto = 25  # kN/m³
peso_especifico_asfalto = 24  # kN/m³
print(f'fck: {fck} MPa')
print(f'peso especifico concreto: {peso_especifico_concreto} kN/m³')
print(f'peso especifico asfalto: {peso_especifico_asfalto} kN/m³')

# CALCULOS DEFINIDOS EM REUNIÃO
print(f'\n### CALCULOS DEFINIDOS EM REUNIÃO ###')
# ÁREA DA LONGARINA (completa)
area_longarina = 1.833  # m²
q_longarina = peso_especifico_concreto * area_longarina
print(f'Carregamento da longarina: {q_longarina:.3f} kN/m²')

# ÁREA MÁXIMA DE ACRESCIMO NO PILAR (carga triangular) (valor máximo do triangulo)
altura_longarina = 2.05  # m
base_transversina = 0.40  # m
q_max_triangulo = altura_longarina * base_transversina * peso_especifico_concreto + q_longarina
print(f'Carregamento máximo do triangulo: {q_max_triangulo:.3f} kN/m²')

# ÁREA DO TABULEIRO (metade do tabuleiro)
area_tabuleiro = 0.395  # m²
q_tabuleiro = peso_especifico_concreto * area_tabuleiro
print(f'Carregamento do tabuleiro: {q_tabuleiro:.3f} kN/m')

# ÁREA DO GUARDA RODA (1 lado do guarda roda)
area_guarda_roda = 0.218  # m²
q_guarda_roda = peso_especifico_concreto * area_guarda_roda
print(f'Carregamento da guarda roda: {q_guarda_roda:.3f} kN/m')

# ÁREA PAVIMENTO (completo - dividido por 2 depois)
area_pavimento = 0.657 / 2   # m²
q_pavimento = area_pavimento * peso_especifico_asfalto
print(f'Carregamento do pavimento: {q_pavimento:.3f} kN/m')

# ÁREA TRANSVERSINA FORA DO PILAR (completa)
altura_tranversina = 0.42  # m
base_transversina = 0.40  # m
comprimento_tranversina = 5.60  # m
q_transversina = peso_especifico_concreto * altura_tranversina * base_transversina * comprimento_tranversina
print(f'Carregamento da transversina fora do pilar: {q_transversina:.3f} kN')

# ÁREA TRANSVERSINA DO PILAR (completa)
altura_tranversina_pilar = 0.42  # m
base_transversina_pilar = 0.30  # m
comprimento_tranversina_pilar = 4.80  # m
q_transversina_pilar = peso_especifico_concreto * altura_tranversina_pilar * base_transversina_pilar * comprimento_tranversina_pilar
print(f'Carregamento da transversina do pilar: {q_transversina_pilar:.3f} kN')

# ÁREA DA CORTINA (somente 1 cortina)
area_cortina = 0.713  # m²
comprimento_cortina = 10.20  # m
q_cortina = peso_especifico_concreto * area_cortina * comprimento_cortina
print(f'Carregamento da cortina: {q_cortina:.3f} kN')
