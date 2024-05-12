.data
primos: .word 1, 3, 5, 7, 11, 13, 17, 19
size: .word 8
msg: .asciz "Os oito primeiros numeros primos sao : "
space: .ascii " "
.text
	la t1,primos
	
	addi t2,zero,0xab
	
	sw t2,0(t1)
	
	sw t2,4(t1)
	
	lw t3,0(t1)
	
	lb t3,0(t1)
	
	lb t3,1(t1)

	