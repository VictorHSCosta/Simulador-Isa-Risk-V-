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
        
        
        
    def removeComplementoDe2_tipoI(self):
        complemento =self.imm12_i
        
        if complemento & (1 << 11):
            return complemento | ~((1 << 12) - 1)
        else:
            return complemento
        
        
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