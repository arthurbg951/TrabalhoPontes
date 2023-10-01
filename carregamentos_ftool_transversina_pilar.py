from codigo_SMATH_em_PYTHON import (
    q_guarda_roda,
    q_pavimento,
    q_tabuleiro,
    q_transversina_pilar,
    comprimento_tranversina,
    comprimento_tranversina_pilar
)
from ABNT_NBR_7188 import q_passeio, p

# CARREGAMENTOS FTOOL
print(f'### CARREGAMENTOS FTOOL ###')
# CARGAS NODAIS
print(f' --> CARGAS NODAIS')
# GUARDA RODA
q_guarda_roda
print(f'guarda roda: {q_guarda_roda:.3f} kN')

# CARGAS DISTRIBUIDAS
print(f' --> CARGAS DISTRIBUIDAS')
# PAVIMENTO
q_pavimento *= 2
print(f'pavimento: {q_pavimento:.3f} kN/m')
# TABULEIRO
q_tabuleiro *= 2
print(f'tabuleiro: {q_tabuleiro:.3f} kN/m')
# TRANSVERSINA
q_transversina_pilar /= comprimento_tranversina_pilar
print(f'tranversina: {q_transversina_pilar:.3f} kN/m')
# SOMATÓRIO DISTRIBUÍDAS
q_distribuída = q_pavimento + q_tabuleiro + q_transversina_pilar
print(f'soma carga distribuída: {q_distribuída:.3f} kN/m')

# TREM TIPO
print(f' --> LIVE LOAD')
# EXTERNO
q_externo = p * comprimento_tranversina
print(f'externo: {q_externo:.3f} kN/m')
# INTERNO
q_interno = q_passeio * comprimento_tranversina
print(f'interno: {q_interno:.3f} kN/m')
