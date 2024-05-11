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
    elif opcode_bin == '0000011':  # Tipo I_1
        return 2 #Tipo I: operações com dados imediatos pequenos
    elif opcode_bin == '0010011':  # Tipo I_2
        return 3 #Tipo I: operações com dados imediatos pequenos
    elif opcode_bin == '1100111':  # Tipo I_3
        return 4 #Tipo I: operações com dados imediatos pequenos
    elif opcode_bin == '0100011':  # Tipo S
        return 5 #Tipo S: operações de armazenamento 
    elif opcode_bin == '1100011':  # Tipo SB
        return 6 #Tipo SB: operações de salto condicional
    elif opcode_bin == '0010111':  # Tipo U apuic
        return 7 #Tipo U
    elif opcode_bin == '0110111': #tipo lui
        return 8 #Tipo U
    elif opcode_bin == '1101111':  # Tipo UJ
        return 9#jal
    elif opcode_bin == "1110011":
        return 10 #ecall
    else: 
        return None

# funcao que tira o imm12 dos codigos tipo s

def imm12_s_funct(ri):
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
def imm13_funct(imm12_s):
    
    bit_0 = imm12_s & 1  # Extrai o bit 0

    # Trocar o valor do bit 11 pelo valor do bit 0
    imm12_s = (imm12_s & ~(1 << 11)) | (bit_0 << 11)
    imm12_s = (imm12_s & ~(1))  # Zera o último bit

    return imm12_s

def imm21(ri):
    
    #primeira parte extende o sinal com base no bit msis significativo
    
    imm21 = 0x00000000
    
    bit20 = ri >> 31 & 1
    
    if bit20 == 1:
        imm21 = 0xFFF00000
        
    # extrai os 8 bits do meio [19:12]

    temp = ri & 0xff000
    
    #extrai os primeiros 12 bits [20 |10:1 | 11]
    
    primeiros12 = ri & 0xFFF00000
    
    primeiros12 = (primeiros12 >> 20)
    
    # faz um a mesma coisa que o imm13 por isso podemos chamar a funcao aqui
    
    primeiros12 = imm13_funct(primeiros12)
    
    imm21 = imm21 | temp | primeiros12
    
    return imm21


#funcao instrucao tabela 

def gerarCodigoDeInstrucao(funct7,funct3,opcode):
    
    tipo = get_instr_format(opcode)

    if(tipo == 1):#se for do tipo R
        
        funct = (funct7 << 3) | funct3
        
        #agora vamos procurat qual dos tipo r ela é
        
        print(funct)
        
        #funct = bin(funct)
        
        if funct == 0:
            return (0x0 , 1 , "add") #retorna que é o add 
        if funct == 256:
            return (0x1 , 1, "sub") # instrucao que retorna o sub
        if funct == 2 :
            return (0x2 , 1 , "slt") # instrucao que retorna slt
        if funct == 3 :
            return (0x3 , 1 , "sltu" ) # retorna o sltu
        if funct == 4:
            return (0x4 , 1 , "xor") # retorna xor
        if funct == 6 :
            return (0x5 , 1 , "or") # retorna or
        if funct == 7:
            return (0x6 , 1 , "and")#retorna o and
        
    if(tipo == 2): #tipo I parte 1
        
        if funct3 == 0:
            return (0x0 , 2 , "lb") #retorna o lb
        if funct3 == 2:
            return (0x1 , 2 , "lw") # retorna lw
        if funct3 == 4:
            return (0x2 , 2 , "lbu")#retorna o lbu
    
    if (tipo == 3): #tipo I parte 2
        if funct3 == 0:
            return (0x0 , 3 , "addi") # retorna addi
        if funct3 == 6:
            return (0x1 , 3 , "ori") # retorna ori
        if funct3 == 7:
            return (0x2 , 3 , "andi") # retorna andi
        
        funct = (funct7 << 3) | funct3
        
        if funct == 1:
            return (0x3 , 3 , "slli") #retorna  slli
        if funct == 5:
            return (0x4 , 3 , "srli") #retorna srli
        if funct == 261:
            return(0x5  , 3 , "srai")#srai
    
    if(tipo == 4):
        return (0x0 , 4 , "jalr")# retorna o jalr
    
    if(tipo == 5):
        if funct3 == 0:
            return(0x0 , 5 , "sb") #retorna o valor de sb
        if funct3 == 2:
            return(0x1 , 5 , "sw") # retorna o valor de sw
        
    if(tipo == 6):
        if funct3 == 0:
            return(0x0 , 6 ,"beq") # retorna beq
        if funct3 == 1:
            return(0x1 , 6 ,"bne") # retorna o valor de bne
        if funct3 == 4:
            return(0x2 , 6 ,"blt") # retorna o valor de blt
        if funct3 == 5 :
            return(0x3, 6 , "bge") #retorna bge
        if funct3 == 6:
            return(0x4 ,6 , "bltu") # retorna bltu
        if funct3 == 7:
            return(0x5 ,6 , "bgeu")# retorna bgeu
    
    if(tipo == 7):
        return(0x0 ,7 ,"auipc") #retorna uipc
    
    if(tipo == 8):
        return(0x0 ,8, "lui")
    
    if(tipo == 9):
        return(0x0 , 9, "jal")
    
    if(tipo == 10):#tipo i
        return(0x0, 10 , "ecall")
    
    return None


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
    imm12_s = imm12_s_funct(ri)
    imm13 = imm13_funct(imm12_s)
    imm21_uj = imm21(ri)
    
    #padrao que nem dos slide 
    #tipo r (tipo ,func7,rs2,rs1,funct3,rd,opcode)
    #tipo i (tipo ,imm12_i,rs1,funct3,rd,opcode,shamt para as funcoes como slii)
    #tipo s (tipo ,imm12_s ,rs2,rs1,funct3,opcode)
    #tipo sB (tipo ,imm13 ,rs2,rs1,opcode)
    #tipo U (tipo ,imm21,rd,opcode)
    #tipo UJ (tipo,imm21 ,rd,opcode)
    

def exculte(tipo,lista):  
    
    # vai ser um grande switch and case que chama as instrucoes e exceculta
    
    #primeiro passo separar por tipo
    
    pass
    



#testes feitos durante a confexao do programa

mem.carregarCodigo()
"""
for i in range(0,22):
    print("-------------------------------------------------------------------------")
    fetch()
    print(decode())
    

for i in range(0,22):
    print("-------------------------------------------------------------------------")
    fetch()
    decode()
    
    

numero_hexadecimal = 0x11cdefff
resultado = imm21(numero_hexadecimal)


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



print(gerarCodigoDeInstrucao(0b0100000,0b010,0b1101111))




"""
