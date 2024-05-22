@ array_data etiketli bellek biriminde tanımlanmış bir dizi içerisindeki
@ elemanların toplamını hesaplayan bir program yazınız. Programın
@ fonksiyonunu bir dizi elemanı toplamak ve sonucu döndürmek
@ üzerine kurun. Döngü yapısını kullanınız.
@ • Dizi elemanları: 10, 20, 30, 40, 50
@ • Sonuç R2 register’ında yazsın.
.section .data
array_data: .word 10, 20, 30, 40, 50
array_length: .word 5
.section .text
.global _start
_start:
	LDR R0, =array_data 
	LDR R1, =array_length
	LDR R1, [R1]
	BL sum_array @ fonksiyona git ve bu adresi LR de tut
	B _end
sum_array:
	MOV R2, #0
	MOV R3, #0
loop:
	LDR R4, [R0, R3, LSL #2] 
	ADD R2, R2, R4 
	ADD R3, R3, #1
	CMP R3, R1 @ uzunluk ve indexi karşılaştır
	BLT loop @ index uzunluktan küçükse loopa devam et
	MOV PC, LR @ Program Counter' a LR değerini at, fonksiyondan çık
_end: