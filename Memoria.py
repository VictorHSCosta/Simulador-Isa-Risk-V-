import numpy as np
import time

# memoria e registradores 

mem = np.zeros(16384, dtype=np.uint8)
reg = np.zeros(32,dtype=np.int32)

#Funcoes de leitura e escrita da memoria

def multiplo(reg,kte,numero):
    
    if((reg+kte) % numero != 0): #verifica se o endereço é divisivel por 4
        raise ValueError(f"Endereço de memória não é múltiplo de {numero}")
    else:
        return (reg + kte)

def lw(reg, kte):
    
    endereco = multiplo(reg,kte,2)
    
    byte0 = mem[endereco]
    byte1 = mem[endereco+1]
    byte2 = mem[endereco+2]
    byte3 = mem[endereco+3]

    word	=	(byte3	<<	24)	| (byte2 << 16) | (byte1 << 8) | (byte0) 
    
    word = np.uint32(word)
    
    return word

def sw(reg,	kte, word):  
    
    if(len(bin(word)) > 34):
        raise ValueError("A word atribuida tem um valor maior que 32 bits")    

    endereco = multiplo(reg,kte,4)
    
    byte0	=	word	&	0xFF		#retorna	o	primeiro	byte,	0x04.
    byte1	=	(word	>>		8)	&	0xFF	#produz	o	segundo	byte	de	word,	0x03.
    byte2	=	(word	>>		16)	&	0xFF	#produz	o	terceiro	byte	de	word,	0x02.
    byte3	=	(word	>>		24)	&	0xFF	#produz	o	quarto	byte	de	word,	0x01.
    
    mem[endereco  ] = byte0
    mem[endereco+1] = byte1
    mem[endereco+2] = byte2
    mem[endereco+3] = byte3

def lb(reg, kte):
    
    endereco = multiplo(reg,kte,1)
    
    byte = mem[endereco]
    
    if byte & 0x80: 
        word = (0xFFFFFF00 | byte) 
    else:
        word = byte  
    return word

def lbu(reg, kte):
    
    endereco = multiplo(reg,kte,1)
    
    byte = mem[endereco]
    
    valor_unsigned = byte & 0xFFFFFFFF

    
    return valor_unsigned
    
def sb(reg,	kte, byte):
    
    endereco = multiplo(reg,kte,1)
    
    mem[endereco] = np.uint8(byte)

#carrega o codigo
def carregarCodigo():
    with open('code.bin', 'rb') as f:
        
        dados_binarios = f.read()
        
        # Converter dados binários em array NumPy
        array_np = np.frombuffer(dados_binarios, dtype=np.uint8)
        
        if array_np.shape[0] != mem.shape[0]:
            pass

        for endereco ,dado in enumerate(array_np):
            mem[endereco] = dado
    
#carrega a memoria 
def carregarData():
    with open('data.bin', 'rb') as f:
        
        dados_binarios = f.read()

        # Converter dados binários em array NumPy
        array_np = np.frombuffer(dados_binarios, dtype=np.uint8)
        
        for endereco ,dado in enumerate(array_np):
            mem[8192 + endereco] = dado
            #print(hex(dado))

def iniciaRegistradores():
    global reg
    reg[2] = 0x00003ffc #inicia o sp
    reg[3] = 0x00001800

def getRegister(addr): #pega o valor do registrador e retorna 
    
    try:
        return reg[addr]
    except: 
        raise "Registrador nao existe"

def setRegister(addr,kte): #seta o valor de um registrador
    
    if (addr != 0):
        try:
            reg[addr] = kte
        except:
            raise f"Erro ao preecher o valor do registrador 0x{addr}"




#testes de todas as funcoes

"""

setRegister(0x0,0x400)
setRegister(0x20,0xABACADEF)
print(hex(getRegister(0x0)))
print(hex(getRegister(0x20)))



reg[0] = 0xAAAAA

iniciaRegistradores()

carregar_data()
print(lw(8192,0))
print(lw(8192,4))
print(lw(8192,8))
print(lw(8192,12))
print(lw(8192,16))
print(lw(8192,20))
print(lw(8192,24))
print(lw(8192,28))"""

"""for i in range(8192,8392,4):
    byte_decimal = lb(0,i)
    
    print(conversores.hex_to_ascii(byte_decimal)) """



"""
sw(0,4,0xABCDEF)

print(lw(0,4))

print(lw(0,8))
#print(lb(0,3))"""
"""
#teste das funcoes da memoria
sw(0,	0,	0xABACADEF)
sb(4,	0,	1)
sb(4,	1,	2)
sb(4,	2,	3)
sb(4,	3,	4)

print(lb(0,	0))
print(lb(0,	1))
print(lb(0,	2))
print(lb(0,	3))
print(lbu(0,	0))
print(lbu(0,	1))
print(lbu(0,	2))
print(lbu(0,	3))"""