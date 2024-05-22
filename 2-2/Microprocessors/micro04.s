@ first_number, second_number, third_number ve fourth number isimli
@ 4 değişken olsun. Sırasıyla 100, 50, 200, 300
@ result_rsb ve result_add değişken tanımları yapılsın.
@ ilk sayı R1, ikinci sayı R2, üçüncü sayı R3 ve dördüncü sayı R4
@ registerına yüklensin.
@ komutta R1, R2 sırasıyla belirtilip R2'den R1'i çıkarın, bu işlem sonrası
@ flag güncellemesi olsun. Sonuç result_rsb isminde tanımlı belleğe
@ gönderilsin.
@ R3 ve R4 toplansın R7'ye kaydedilsin, işlem sonrası flag güncellemesi
@ olsun. Sonuç result_add isminde tanımlı belleğe yüklensin.
.section .data
	first_number: .word 100
	second_number: .word 50
	third_number: .word 200
	fourth_number: .word 300
	result_rsb: .word 0
	result_add: .word 0
.section .text
.global _start
_start:
	LDR R0,=first_number
	LDR R1, [R0]
	LDR R0,=second_number
	LDR R2, [R0]
	LDR R0,=third_number
	LDR R3, [R0]
	LDR R0,=fourth_number
	LDR R4, [R0]
	RSBS R5, R1, R2
	LDR R0,=result_rsb
	STR R5, [R0]
	ADDS R7, R3, R4
	LDR R0,=result_add
	STR R7, [R0]
_end: