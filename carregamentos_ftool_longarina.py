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
q_recapeamento = 2

# CARREGAMENTOS FTOOL
print(f'### CARREGAMENTOS FTOOL ###')
# CARGAS DISTRIBUIDAS
print(f' --> CARGAS DISTRIBUIDAS')
# SUBINDO
q_subindo_pyi = (q_longarina + q_guarda_roda + q_pavimento + q_tabuleiro + q_recapeamento) * 1.35
q_subindo_pyj = (q_subindo_pyi + (q_max_triangulo - q_longarina) + q_recapeamento) * 1.35
print(f'subindo: Pyi: {q_subindo_pyi:.3f} kN/m² Pyj: {q_subindo_pyj:.3f} kN/m²')
# DESCENDO
q_descendo_pyi = (q_subindo_pyi + (q_max_triangulo - q_longarina) + q_recapeamento) * 1.35
q_descendo_pyj = (q_longarina + q_guarda_roda + q_pavimento + q_tabuleiro + q_recapeamento) * 1.35
print(f'descendo: Pyi: {q_descendo_pyi:.3f} kN/m² Pyj: {q_descendo_pyj:.3f} kN/m²')
# LONGARINA
q_longarina = (q_subindo_pyi + q_recapeamento) * 1.35
print(f'longarina: {q_longarina:.3f} kN/m')

# CARGAS NODAIS
print(f' --> CARGAS NODAIS')
# TABULEIRO
q_tabuleiro = q_tabuleiro * 1.35
print(f'tabuleiro: {q_tabuleiro:.3f} kN')
# TRANSVERSINA PILAR
q_transversina_pilar = (q_transversina_pilar / 2)
q_transversina_pilar = q_transversina_pilar * 1.35
print(f'transversina pilar: {q_transversina_pilar:.3f} kN')
# TRANSVERSINA VÃO
q_transversina = q_transversina / 2
q_transversina = q_transversina * 1.35
print(f'transversina vão: {q_transversina:.3f} kN')
# CORTINA
q_cortina = q_cortina * 1.35
print(f'cortina: {q_cortina:.3f} kN')
