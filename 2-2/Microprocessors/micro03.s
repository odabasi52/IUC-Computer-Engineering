@ 3 sayının toplama işleminin sonucunu result_sum isimli bir bellek
@ adresinde, çarpım sonucunu result_mul isimli bir bellek adresinde
@ tutan bir program yazınız.
.section .data
	result_sum: .word 0 
	result_mul: .word 0
.section .text
.global _start
_start:
	MOV R1, #10 
	MOV R2, #20 
	MOV R3, #30 
	ADD R4, R1, R2 
	ADD R4, R4, R3 
	MUL R5, R1, R2 
	MUL R5, R5, R3
	LDR R6, =result_sum 
	STR R4, [R6] 
	LDR R6, =result_mul 
	STR R5, [R6] 
_end: