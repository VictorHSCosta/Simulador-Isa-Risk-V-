.text

principal:

	addi t1,t1,-1
	
	addi t2,zero,6
	
	jal voltar
	
	bltu t1,t2,principal

seder:
	
	addi t3,zero,100
	
	add t3,t3,t3
	
igual:

	bgeu t1,t2,principal
	
	beq t1,t2,seder	
voltar:
	ret	
	