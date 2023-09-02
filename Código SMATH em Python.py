# DADOS DO PROJETO
# DEIXAR SEMPRE OS DADOS NO SI
fck = 20e6  # MPa
peso_especifico_concreto = 25  # kN/m³
peso_especifico_asfalto = 24  # kN/m³

# ÁREA DA LONGARINA
area_longarina = 1.833  # m²
q_longarina = peso_especifico_concreto * area_longarina
print(f'Carregamento da longarina: {q_longarina:.3f} kN/m')

# ÁREA MÁXIMA DE ACRESCIMO NO PILAR (carga triangular)
altura_longarina = 2.05  # m
base_transversina = 0.4  # m
q_max_triangulo = altura_longarina * base_transversina * peso_especifico_concreto + q_longarina
1.340  # Valor esrito em sala (possivelmente errado)
print(f'Carregamento máximo do triangulo: {q_max_triangulo:.3f} kN/m')

# ÁREA DO TABULEIRO
area_tabuleiro = 0.395  # m² - área da metade do tabuleiro
q_tabuleiro = peso_especifico_concreto * area_tabuleiro
print(f'Carregamento da tabuleiro: {q_tabuleiro:.3f} kN/m')

# ÁREA DO GUARDA RODA
area_guarda_roda = 0.218  # m²
q_guarda_roda = peso_especifico_concreto * area_guarda_roda
print(f'Carregamento da guarda roda: {q_guarda_roda:.3f} kN/m')


# ÁREA PAVIMENTO
'''
Faltando retirar
'''
