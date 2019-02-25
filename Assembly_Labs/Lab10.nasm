;Project: Lab 10
;
; vim: filetype=nasm :

bits 64

global first_func, second_func, third_func

first_func:
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;    Using the rdtsc instruction,
;  1.) Obtain the current timestamp
;  2.) Combine the low 32 bits (from RAX)
;     and the high 32 bits (RDX), and
;     return them.
;
;  BEGIN student code
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
rdtsc
shl rdx, 32
or rax, rdx
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;  END student code
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
    ret

second_func:
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;   Using CPUID, get the vendor
;  string, and copy each chunk
;  returned into the buffer
;  passed to your function.
;  The buffer should be the
;  first (and only) argument.
; 
;  BEGIN student code
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
xor eax, eax
xor ebx, ebx
xor ecx, ecx
xor edx, edx
cpuid
;mov [rdi], ebx
;mov [rdi + 4], edx
;mov [rdi + 8], ecx
mov eax, ebx
stosd
mov eax, edx
stosd
mov eax, ecx
stosd
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;  END student code
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
    ret