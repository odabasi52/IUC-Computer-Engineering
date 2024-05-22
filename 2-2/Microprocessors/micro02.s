@ 3 sayının toplamını hesaplayan, sonucu bir bellek konumuna(0x3000)
@ kaydeden ve ardından bu değeri bir başka registere yükleyen ARM
@ Assembly uygulaması yazınız.
@ • Sayılar 5, 15, 25
.global _start
_start:
	MOV R1, #5
	MOV R2, #15
	ADD R2, R2, R1
	ADD R3, R2, #25
	MOV R4, #0x3000
	STR R3, [r4]
_end: