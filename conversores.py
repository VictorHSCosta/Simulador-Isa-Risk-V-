import numpy as np
import Memoria as mem

# converte hex para ascii
def hex_to_ascii(hex_string):
    # Remove o prefixo '0x' se estiver presente
    if hex_string.startswith("0x"):
        hex_string = hex_string[2:]

    # Garante que a string tenha um número par de dígitos hexadecimais
    if len(hex_string) % 2 != 0:
        hex_string = "0" + hex_string

    # Converte cada par de dígitos hexadecimais em ASCII e junta os caracteres
    ascii_string = ""
    for i in range(0, len(hex_string), 2):
        ascii_string += chr(int(hex_string[i:i+2], 16))

    return ascii_string

# converte de decimal para hex

def decToHex(number):
    number = hex(number)
    return number