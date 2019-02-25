;Project: Lab 6
;
; vim: filetype=nasm : 

bits 64

global first_func, second_func, third_func

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
; INSTRUCTIONS
; -Set the flags via by arithmetic operation
; -Then set the flags manually*
; *You will need to comment out the previous solution 


first_func:
    push rbp
    mov rbp, rsp
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
; Set the carry flag.
;
;  BEGIN student code
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;mov al, 128
;rol al, 1
pushf
pop rax
or rax, 1
push rax
popf
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;  END student code
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
    pop rbp
    ret

second_func:
    push rbp
    mov rbp, rsp
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;  Set the overflow flag.
;
;  BEGIN student code
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;mov al, -128
;sub al, 2
pushf
pop rax
mov rcx, 1
shl rcx, 11
or rax, rcx
push rcx
popf
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;  END student code
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
    pop rbp
    ret

third_func:
    push rbp
    mov rbp, rsp
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;  Set both the carry and overflow
;  flags.
;
;  BEGIN student code
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;mov al, -128
;add al, -128
pushf
pop rax
mov rcx, 1
shl rcx, 11
inc rcx
or rax, rcx
push rcx
popf
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;  END student code
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
    pop rbp
    ret