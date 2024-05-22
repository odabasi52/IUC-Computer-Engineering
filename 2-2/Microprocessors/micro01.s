@ 15 ve 30 sayıları R1 ve R2 registerlarında bulunmaktadır. R3 registerı
@ R1 ve R2 registerında tutulan değerlerin toplamını tutmaktadır.
@ Bellekteki 0x1000 adresine R3 registerındaki değeri gönderiniz,
@ ardından aynı bellek adresindeki değeri R5 registerına yazınız

.global _start
_start:
	MOV R1, #15 
	MOV R2, #30 
	ADD R3, R1, R2 
	MOV R4, #0x1000 
	STR R3, [R4] 
	LDR R5, [R4]
_end:

