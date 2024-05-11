def int_neg_to_uint(val):
    # Adiciona 2^32 ao valor negativo para obter seu equivalente sem sinal de 32 bits
    return val & 0xFFFFFFFF

# Exemplo de uso:
valor_negativo = -40
valor_sem_sinal = int_neg_to_uint(valor_negativo)
print(hex(valor_sem_sinal))  # Saída: 4294967295