; Project: Lab2

; vim: set filetype=nasm :

bits 64

extern value
global first_func, second_func

first_func:
    mov rax, -1
    mov rcx, -1
    mov cl,; Name: Robert John Graham III
; Date: 10 Oct 18
; Project: Lab1 0x04
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;  For this task, you must move
;  the first byte of RCX into
;  RAX, using zero extend.
;
;
;  BEGIN student code
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
movzx rax, cl
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;  END student code
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
    ret


second_func:
	xor rax, rax
	mov ah, 0x42
	mov al, 0x41
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;	For this task, you must swap
;  the contents of the first two
;  bytes of RAX (ah/al).
;
;  BEGIN student code
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
xchg ah, al
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;  END student code
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
	ret