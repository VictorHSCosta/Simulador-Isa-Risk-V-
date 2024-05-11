import Memoria as mem
import Registradores

    #padrao que nem dos slide 
    #tipo r (tipo ,func7,rs2,rs1,funct3,rd,opcode)
    #tipo i (tipo ,imm12_i,rs1,funct3,rd,opcode,shamt para as funcoes como slii)
    #tipo s (tipo ,imm12_s ,rs2,rs1,funct3,opcode)
    #tipo sB (tipo ,imm13 ,rs2,rs1,opcode)
    #tipo U (tipo ,imm21,rd,opcode)
    #tipo UJ (tipo,imm21 ,rd,opcode)

def lw(lista):#tipo i (tipo ,imm12_i,rs1,funct3,rd,opcode,shamt para as funcoes como slii)
    constante  = lista[1]
    
    registradorEndereço = lista[2]
    
    dados = mem.lw(registradorEndereço,constante)
    
    mem.setRegister(hex(list[4]),dados)