def complemento_de_2_para_decimal(numero):
    # Converte o número inteiro para binário e remove o prefixo '0b'
    bits = bin(numero & 0xffffffff)[2:]

    # Verifica se o número é negativo
    if bits[0] == '1':
        # Se for negativo, converte para complemento de 2
        bits_complemento_2 = ''
        for bit in bits:
            bits_complemento_2 += '1' if bit == '0' else '0'
        
        # Adiciona 1 ao complemento de 2
        bits_complemento_2 = bin(int(bits_complemento_2, 2) + 1)[2:]
        
        # Retorna o valor negativo
        return -int(bits_complemento_2, 2)
    else:
        # Se for positivo, retorna diretamente
        return int(bits, 2)

# Exemplo de uso
numero = 16777131
resultado = complemento_de_2_para_decimal(numero)
print(resultado)  # Saída: -85

