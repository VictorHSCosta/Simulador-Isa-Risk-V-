# Trabalho-de-OAC

todos os teste feitos no arquivo memoria.py 


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


funcoes testadas no programa Registradores 

   
    
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

codigos testados no codigo registradores.py


"""

for i in range(0,40):
    print("-------------------------------------------------------------------------")
    step()
    print((mem.getRegister(6)),"x6")
    print((mem.getRegister(7)),"x7")
    print((mem.getRegister(28)),"x28")
    print((mem.getRegister(29)),"x29")
    print((mem.getRegister(17)),"x17")
    print((mem.getRegister(10)),"x10")
    print((mem.getRegister(5)),"x5")
    print((mem.getRegister(28)),"x28")
    
"""