import numpy as np
import Memoria as mem

#Parte do codigo que contem os principais registradores

pc = 0x00000000
ri = 0x00000000

#funcao fech

def fetch():
    global pc ,ri
    ri = mem.lw(pc, 0); # carrega instrução endereçada pelo pc
    pc = pc + 4; # aponta para a próxima instrução

# funcao que descobre o tipo 
def get_instr_format(opcode):
    
    opcode_bin = format(opcode, '07b')

    if opcode_bin == '0110011':  # Tipo R
        return  1 #Tipo R: operações lógico-aritméticas
    elif opcode_bin in ['0010011', '0000011', '1100111']:  # Tipo I
        return 2 #Tipo I: operações com dados imediatos pequenos
    elif opcode_bin == '0100011':  # Tipo S
        return 3 #Tipo S: operações de armazenamento (store)
    elif opcode_bin == '1100011':  # Tipo SB
        return 4 #Tipo SB: operações de salto condicional
    elif opcode_bin in ['0010111', '0110111']:  # Tipo U
        return 5 #Tipo U: operações com dados imediatos grandes
    elif opcode_bin == '1101111':  # Tipo UJ
        return 6#Tipo UJ: operações de salto incondicional
    elif opcode_bin == "1110011":
        return 7 #ecall
    else: 
        return None

# funcao que tira o imm12 dos codigos tipo s

def imm12_s(ri):
    bitsMaisSignificativo = (ri >> 25) & 0x7F
    
    bitsMenosSignificativo = (ri >> 7) & 0x1F
    
    imm12_s_value = (bitsMaisSignificativo<< 5) | bitsMenosSignificativo
    
    sign_bit = imm12_s_value & 0x800  # Bit de sinal
    if sign_bit:  # Se o bit de sinal for 1 (negativo), estende o sinal
        imm12_s_extended = imm12_s_value | 0xFFFFF000
    else:  # Se o bit de sinal for 0 (positivo), não é necessário estender o sinal
        imm12_s_extended = imm12_s_value
        
    return imm12_s_extended

# consegue o valor de imm13 com base no valor de imm12
def imm13(imm12_s):
    
    bit_0 = imm12_s & 1  # Extrai o bit 0

    # Trocar o valor do bit 11 pelo valor do bit 0
    imm12_s = (imm12_s & ~(1 << 11)) | (bit_0 << 11)
    imm12_s = (imm12_s & ~(1))  # Zera o último bit

    return imm12_s

def imm21(ri):
    
    bit20 = ri >> 31 & 1
    
    print(bit20)
    
    

# Exemplo de uso da função
numero_hexadecimal = 0xe0000000
resultado = imm21(numero_hexadecimal)
print("Resultado:", resultado)




# funcao decode 

def decode():
    global ri
    
    ri = int(ri,16)
    
    opcode	= ri & 0x7F
    rs2		= (ri >> 20) & 0x1F
    rs1		= (ri >> 15) & 0x1F
    rd		= (ri >> 7)  & 0x1F
    shamt	= (ri >> 20) & 0x1F
    funct3	= (ri >> 12) & 0x7
    funct7  = (ri >> 25)
    imm20_u = (ri & 0xFFFFF000)
    imm12_i = (ri & 0xFFFFFFFF) >> 20
    imm12_s = imm12_s(ri)
    imm13 = imm13(imm12_s)
    
    
    tipoDeCodigo = get_instr_format(opcode)
    
    


mem.carregarCodigo()



"""
for i in range(0,22):
    print("-------------------------------------------------------------------------")
    fetch()
    decode()
"""



"""
#code = imm12_s(0xABACADAE)
code = imm12_s(0xABCD1111)

print(hex(code))
print(bin(code))

code = imm13(code)

print(hex(code))
print(bin(code))


#print(get_instr_format(opcode))
    
    
    
    
    #print(hex(opcode))
    #print(imm20_u)
    #print(hex(rs1))
    #print(hex(rs2))
    #print(hex(rd))







"""
