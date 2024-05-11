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
        
    def achaInstucao(self):
        
        codigo = self.codigo[2]
        
        if codigo == "add":
            self.add()
        if codigo == "addi":
            self.addi()
            
    def sign_extend_tipoI(self):
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
    def addi(self):
        
        imm12_i = self.sign_extend_tipoI()
        
        print(imm12_i)
        
        resultado = imm12_i + mem.getRegister(self.rs1)
        
        mem.setRegister(self.rd,resultado)
        
        print("parte interna",self.imm12_i,self.rs1,self.rd,resultado)
        












def lw(lista):#tipo i (tipo ,imm12_i,rs1,funct3,rd,opcode,shamt para as funcoes como slii)
    constante  = lista[1]
    
    registradorEndereço = lista[2]
    
    dados = mem.lw(registradorEndereço,constante)
    
    mem.setRegister(hex(list[4]),dados)
    
