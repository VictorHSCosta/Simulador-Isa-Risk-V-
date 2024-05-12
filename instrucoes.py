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
        self.numeroAux = 0
        
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
    def removeComplementoDe2_tipoJ(self):
        
        complemento = self.imm21_uj
        
        if complemento & (1 << 31):
            valor_decimal = -((1 << 32) - complemento)
        else:
            valor_decimal = complemento
        return valor_decimal
    def removeComplementoDe2_tipoS(self):
        
        complemento = self.imm12_s
        
        if complemento & (1 << 31):
            valor_decimal = -((1 << 32) - complemento)
        else:
            valor_decimal = complemento
        return valor_decimal
    def removerComplementoDe2(self):
        numero = self.numeroAux
        
        bits = bin(numero & 0xffffffff)[2:]

        if bits[0] == '1':
            bits_complemento_2 = ''
            for bit in bits:
                bits_complemento_2 += '1' if bit == '0' else '0'
            
            bits_complemento_2 = bin(int(bits_complemento_2, 2) + 1)[2:]
            
            return -int(bits_complemento_2, 2)
        else:
            return int(bits, 2)

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
        
        imm21_uj = self.removeComplementoDe2_tipoJ()
        
        return pc + imm21_uj -4
    def jalr(self,pc):
        
        imm12_i = self.removeComplementoDe2_tipoI()
        
        endereco = mem.getRegister(self.rs1) + imm12_i 
        
        mem.setRegister(0x1,pc)#seta o valor de pc para ra
        
        mem.setRegister(self.rd,pc)#seta o valor de pc para rd
        
        return endereco
    def Funct_Or(self):
        rs1 = mem.getRegister(self.rs1)
        rs2 = mem.getRegister(self.rs2)
        
        dado = rs1 | rs2
        
        mem.setRegister(self.rd, dado)

    def ori(self):
        
        imm12_i = self.removeComplementoDe2_tipoI()
        
        rs1 = mem.getRegister(self.rs1)
        
        dado = rs1 | imm12_i
        
        mem.setRegister(self.rd ,dado)
        
    def xor(self):
        rs1 = mem.getRegister(self.rs1)
        rs2 = mem.getRegister(self.rs2)
        
        dado = rs1 ^ rs2
        
        mem.setRegister(self.rd, dado)
    def lb(self):
        
        imm12_i = self.removeComplementoDe2_tipoI()
        
        endereco = mem.getRegister(self.rs1)
        
        self.numeroAux = mem.lb(endereco,imm12_i)
        
        dado  = self.removerComplementoDe2()
        
        mem.setRegister(self.rd,dado)
    def lbu(self):
        
        imm12_i = self.removeComplementoDe2_tipoI()
        
        endereco = mem.getRegister(self.rs1)
        
        dado = mem.lbu(endereco,imm12_i)
        
        mem.setRegister(self.rd,dado)
    def lw(self):
        
        imm12_i = self.removeComplementoDe2_tipoI()
        
        endereco = mem.getRegister(self.rs1)
        
        dado = mem.lw(imm12_i,endereco)
        
        mem.setRegister(self.rd,dado)
    def lui(self):
        
        dado = self.imm20_u
        
        mem.setRegister(self.rd ,dado)
    def slt(self):
        
        rs1 = mem.getRegister(self.rs1)
        rs2 = mem.getRegister(self.rs2)
        
        if rs1 < rs2:
            dado = 1
        else:
            dado = 0 
        
        mem.setRegister(self.rd , dado)
    def sltu(self):
        
        rs1 = mem.getRegister(self.rs2)
        rs2 = mem.getRegister(self.rs1)
        
        if rs1 < rs2:  # Comparação sem sinal
            dado = 1
        else:
            dado = 0 
            
        mem.setRegister(self.rd, dado)
    def sb(self):
        
        imm12 = self.removeComplementoDe2_tipoS()
        
        endereco = mem.getRegister(self.rs2)
        
        dado = mem.getRegister(self.rs1)
        
        mem.sb(endereco, imm12 ,dado)
    def sw(self):
        
        imm12 = self.removeComplementoDe2_tipoS()
        
        endereco = mem.getRegister(self.rs1)
        
        dado = mem.getRegister(self.rs2)
        
        mem.sw(endereco, imm12 ,dado)
    def ecall(self):
        
        registrador1 = mem.getRegister(17)
        
        registrador2 = mem.getRegister(10)
        
        if(registrador1 == 1):
            print(registrador2 , end= " ")
            
            return False
        
        if (registrador1 == 10):
            
            return True
        if(registrador1 == 4):
            
            endereco = mem.getRegister(10)
            
            i = 0
            
            while(True):
                
                letra = mem.lb(endereco,i) & 0xFF
                
                letra = chr(letra)
                
                print(letra ,end = '')
                
                if letra == '\x00':
                    return False
                
                i += 1
    def  slli(self):
        imm12_i = self.removeComplementoDe2_tipoI()
        
        rs1 = mem.getRegister(self.rs1)
        
        dado = rs1 << imm12_i
        
        mem.setRegister(self.rd,dado)
    
    def srai():
        pass
    
    def srli():
        pass





































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