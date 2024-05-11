.text

principal:

	addi t1,t1,-1
	
	addi t2,zero,-5
	
	bgeu t1,t2,igual

seder:
	
	addi t3,zero,100
	
igual:

	bge t2,t1,principal
	
	beq t1,t2,seder	
	
	