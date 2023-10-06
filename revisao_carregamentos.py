from ABNT_NBR_7188 import p, P, CIA, CIV, CNF

# Pesos específicos Materiais
peso_especifico_concreto = 25  # kN/m³
peso_especifico_pavimento = 24  # kN/m³

# AREAS DO PROJETO CAD
# Longarina
area_secao_t = 1.833  # m²
area_misula_longarina = 2.05 * 0.4  # altura x base

# Guarda_roda
area_guarda_roda = 0.218  # m²

# Transversinas
area_tranversina_pilar = 1.63 * 0.3  # altura x base
area_tranversina_vao = 1.58 * 0.25  # altura x base
comprimento_metade_transversina_pilar = 5.10 - 0.4  # m
comprimento_metade_transversina_vao = 5.10 - 0.8  # m

# Metade do tabuleiro
area_metade_tabuleiro = 0.396  # m²

# Metade do pavimento
area_metade_pavimento = 0.329  # m²

# Cortina
area_cortina_na_secao_longitudinal = 0.713  # m²
comprimento_metade_cortina = 5.10  # m
# OBS: remover do carregamento o volume da longarina que adetra na cortina

# CARREGAMENTOS FTOOL
# Distribuído
q_recapeamento = 2  # kN/m
q_pavimento = area_metade_pavimento * peso_especifico_pavimento
q_longarina = area_secao_t * peso_especifico_concreto
q_tabuleiro = area_metade_tabuleiro * peso_especifico_concreto
q_guarda_roda = area_guarda_roda * peso_especifico_concreto
q_acrescimo_triangulo = area_misula_longarina * peso_especifico_concreto

q_distribuido_continuo = q_recapeamento + q_pavimento + q_longarina + q_tabuleiro + q_guarda_roda
q_max_triangulo = q_distribuido_continuo + q_acrescimo_triangulo

# Concentrado
q_transversina_pilar = area_tranversina_pilar * comprimento_metade_transversina_pilar * peso_especifico_concreto
q_transversina_vao = area_tranversina_vao * comprimento_metade_transversina_vao * peso_especifico_concreto
volume_total_cortina = area_cortina_na_secao_longitudinal * comprimento_metade_cortina
volume_viga_t_na_cortina = 0.25 * area_secao_t
volume_tabuleiro_na_cortina = 0.25 * area_metade_tabuleiro
q_cortina = (volume_total_cortina - volume_viga_t_na_cortina - volume_tabuleiro_na_cortina) * peso_especifico_concreto

# Trem tipo
P = 2 * P  # kN
q_externo = p * (2.1 - 0.4 + 6) / 2
q_interno = p * (2.1 - 0.4 + 6 - 3) / 2
fator_de_impacto = CNF(2) * CIA('concreto') * CIV(20)


print(f'CARGAS DISTRIBUÍDAS:')
print(f'    Carga continua: {q_distribuido_continuo}')
print(f'    Carga máxima triangular: {q_max_triangulo}')

print(f'CARGAS CONCENTRADAS:')
print(f'    Transversina no pilar: {q_transversina_pilar}')
print(f'    Transversina no vao: {q_transversina_vao}')
print(f'    Cortina: {q_cortina}')

print(f'TREM TIPO:')
print(f'    Carga concentrada: {P}')
print(f'    Externo: {q_externo}')
print(f'    Interno: {q_interno}')

print(f'FATOR DE IMPACTO={fator_de_impacto}')
