import Memoria as mem 
import Registradores as reg
from time import sleep
from os import system

mem.carregarCodigo()
mem.carregarData()

registradores = ['zero', 'ra', 'sp', 'gp', 'tp', 't0', 't1', 't2', 's0', 's1', 'a0', 'a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 's2', 's3', 's4', 's5', 's6', 's7', 's8', 's9', 's10', 's11', 't3', 't4', 't5', 't6']


# faz passo a passo pressionando enter caso queira sair pressione 0


option = 1

while(option != "0"):
    
    system("Cls")
    
    print("Presione Enter para o proximo passo")
    print("Pressione 0 para sair")
    
    print(f"Pc:{reg.pc} Ri:{reg.ri}")
    
    reg.step()

    print('='*20)
    
    for i in range(0,32):
        
        print(f"0x{i}    ||  {registradores[i]}  ||  {mem.getRegister(i)}")

    print('='*20)
    
    if reg.pc >= 0x2000:
        print("\n-- program is finished running (dropped off bottom) --")
        break
    
    if reg.FlagInterruption == True:
        print("\n-- program is finished running (0) --")
        break
    
    option = (input())
    