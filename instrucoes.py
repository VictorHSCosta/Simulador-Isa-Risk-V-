import Memoria as mem
import numpy as np
#codigo, rs2,rs1,rd,shamt,imm20_u,imm12_i,imm12_s,imm13,imm21_uj
class instrucao():
    
    def __init__(self):
        self.codigo = tuple()
        self.rs2 = 0x0
        self.rs1 = 0x0
        self.rd = 0x0
        self.shamt = 0x0
        self.imm20_u = 0x0
        self.imm12_i = 0x0
        self.imm12_s = 0x0
        self.imm13 = 0x0
        self.imm21_uj = 0x0
        
    #nessas funcoes podemos remover o complemento de 2 e obter os numeros negativos     
        
    def removeComplementoDe2_tipoI(self):
        complemento =self.imm12_i
        
        if complemento & (1 << 11):
            return complemento | ~((1 << 12) - 1)
        else:
            return complemento
    def removeComplementoDe2_tipoSb(self):
        
        complemento = self.imm13
        
        if complemento & (1 << 31):
            valor_decimal = -((1 << 32) - complemento)
        else:
            valor_decimal = complemento
        return valor_decimal
    
    def SignalParaUnsignal(self,number):
        
        return number & 0xFFFFFFFF
        
    #instrucoes
        
    def add(self):
        registrador1 = mem.getRegister(self.rs1)
        registrador2 = mem.getRegister(self.rs2)
        resustado = registrador1 + registrador2
        
        mem.setRegister(self.rd ,resustado)
    def addi(self):#testada e aprovada
        
        imm12_i = self.removeComplementoDe2_tipoI()
        
        resultado = imm12_i + mem.getRegister(self.rs1)
        
        mem.setRegister(self.rd,resultado)
    def Funct_And(self):
        
        rs1 = mem.getRegister(self.rs1)
        rs2 = mem.getRegister(self.rs2)
        
        dado = rs1 & rs2
        
        mem.setRegister(self.rd ,dado)
    def andi(self):
        
        imm12_i = self.removeComplementoDe2_tipoI()
        
        rs1 = mem.getRegister(self.rs1)
        
        dado = rs1 & imm12_i
        
        mem.setRegister(self.rd ,dado)
    def auipc(self,pc):
        
        dado = pc  + self.imm20_u - 4
        
        mem.setRegister(self.rd,dado) 
    def beq(self,pc):
        
        rs1 = mem.getRegister(self.rs1)
        rs2 = mem.getRegister(self.rs2)
        
        imm13 = self.removeComplementoDe2_tipoSb()
        
        if rs1 == rs2:
            return pc + imm13 -4
        else:
            return pc
    def bne(self,pc):
        
        rs1 = mem.getRegister(self.rs1)
        rs2 = mem.getRegister(self.rs2)
        
        imm13 = self.removeComplementoDe2_tipoSb()
        
        if rs1 != rs2:
            return pc + imm13 -4
        else:
            return pc
    def bge(self,pc):
        
        rs1 = mem.getRegister(self.rs1)
        rs2 = mem.getRegister(self.rs2)
        
        imm13 = self.removeComplementoDe2_tipoSb()
        
        if ((rs1 > rs2) or (rs1 == rs2)):
            return pc + imm13 -4
        else:
            return pc
    def bgeu(self,pc):
        
        rs1 = mem.getRegister(self.rs1)
        rs2 = mem.getRegister(self.rs2)
        
        rs1 = self.SignalParaUnsignal(rs1)
        rs2 = self.SignalParaUnsignal(rs2)
        
        
        imm13 = self.removeComplementoDe2_tipoSb()
        
        if ((rs1 > rs2) or (rs1 == rs2)):
            return pc + imm13 -4
        else:
            return pc
    def blt(self,pc):
        
        rs1 = mem.getRegister(self.rs1)
        rs2 = mem.getRegister(self.rs2)
        
        imm13 = self.removeComplementoDe2_tipoSb()
        
        if (rs1 < rs2):
            return pc + imm13 -4
        else:
            return pc
    def bltu(self,pc):
        
        rs1 = mem.getRegister(self.rs1)
        rs2 = mem.getRegister(self.rs2)
        
        rs1 = self.SignalParaUnsignal(rs1)
        rs2 = self.SignalParaUnsignal(rs2)
        
        
        imm13 = self.removeComplementoDe2_tipoSb()
        
        if rs1 < rs2:
            return pc + imm13 -4
        else:
            return pc
    def sub(self):
        registrador1 = mem.getRegister(self.rs1)
        registrador2 = mem.getRegister(self.rs2)
        resustado = registrador1 - registrador2
        
        mem.setRegister(self.rd ,resustado)
    def jal(self,pc):
        
        mem.setRegister(0x1,pc)
        
        mem.setRegister(self.rd,pc)
        
        print(self.imm21_uj,(pc + self.imm21_uj -4))
        
        return pc + self.imm21_uj -4
    def jalr(self,pc):
        
        imm12_i = self.removeComplementoDe2_tipoI()
        
        print(imm12_i)
        
        print(mem.getRegister(self.rs1))
        
        endereco = mem.getRegister(self.rs1) + imm12_i 
        
        print(endereco)
        
        mem.setRegister(0x1,pc)#seta o valor de pc para ra
        
        mem.setRegister(self.rd,pc)#seta o valor de pc para rd
        
        return endereco




































"""    
    def achaInstucao(self):
        
        codigo = self.codigo[2]
        
        if codigo == "add":
            self.add()
        if codigo == "addi":
            self.addi()
        if codigo == "and":
            self.Funct_And()
        if codigo == "andi":
            self.andi()
            
            
            
    
def lw(lista):#tipo i (tipo ,imm12_i,rs1,funct3,rd,opcode,shamt para as funcoes como slii)
    constante  = lista[1]
    
    registradorEndereço = lista[2]
    
    dados = mem.lw(registradorEndereço,constante)
    
    mem.setRegister(hex(list[4]),dados)
""" 