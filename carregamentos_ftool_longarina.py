from codigo_SMATH_em_PYTHON import (
    q_longarina,
    q_guarda_roda,
    q_pavimento,
    q_tabuleiro,
    q_max_triangulo,
    q_transversina,
    q_transversina_pilar,
    q_cortina
)

# CARREGAMENTOS FTOOL
print(f'\n### CARREGAMENTOS FTOOL ###')
# CARGAS DISTRIBUIDAS
print(f' --> CARGAS DISTRIBUIDAS')
# SUBINDO
q_subindo_pyi = q_longarina + q_guarda_roda + q_pavimento + q_tabuleiro
q_subindo_pyj = q_subindo_pyi + (q_max_triangulo - q_longarina)
print(f'subindo: Pyi: {q_subindo_pyi:.3f} kN/m² Pyj: {q_subindo_pyj:.3f} kN/m²')
# DESCENDO
q_descendo_pyi = q_subindo_pyi + (q_max_triangulo - q_longarina)
q_descendo_pyj = q_longarina + q_guarda_roda + q_pavimento + q_tabuleiro
print(f'descendo: Pyi: {q_descendo_pyi:.3f} kN/m² Pyj: {q_descendo_pyj:.3f} kN/m²')
# LONGARINA
q_longarina = q_subindo_pyi
print(f'longarina: {q_longarina:.3f} kN/m')

# CARGAS NODAIS
print(f' --> CARGAS NODAIS')
# TABULEIRO
q_tabuleiro
print(f'tabuleiro: {q_tabuleiro:.3f} kN')
# TRANSVERSINA PILAR
q_transversina_pilar /= 2
print(f'transversina pilar: {q_transversina_pilar:.3f} kN')
# TRANSVERSINA VÃO
q_transversina /= 2
print(f'transversina vão: {q_transversina:.3f} kN')
# CORTINA
q_cortina
print(f'cortina: {q_cortina:.3f} kN')
