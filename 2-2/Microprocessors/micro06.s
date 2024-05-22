@ first_number etiketli bellek biriminde yer alan sayı 8’den küçükse,
@ kendisinden 0’a kadar 1’er eksilterek ekrana yazdıran (0’ı
@ yazdırmayacak) programı yazınız. Döngü mantığıyla çözünüz.
.section .data
	first_number: .word 5
.section .text
.global _start
_start:
	LDR R0, =first_number
	LDR R1, [R0]
loop:
	CMP R1, #8
	BGT exit
	CMP R1, #0
	BLE exit
	ADD R2, R1, #48
	STRB R2, [R0], #1
	SUB R1, R1, #1
	B loop
	
exit:
	MOV R1, #0
_end:
	