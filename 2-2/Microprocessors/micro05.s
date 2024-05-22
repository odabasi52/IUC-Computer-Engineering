@ 0’dan 15’e kadar olan sayıları 101f1000 adresinden başlayarak
@ Memory’de Hexadecimal karşılıklarını ekrana yazdırınız.
.global _start
_start:
	LDR R4, =0x101f1000
	MOV R0, #0
my_loop:
	CMP R0, #15
	BGT my_exit
	CMP R0, #10
	ADDLT R1, R0, #48
	ADDGE R1, R0, #55
	STRB R1, [R4], #1
	ADD R0, R0, #1
	B my_loop
my_exit:
	MOV R0, #0
_end: