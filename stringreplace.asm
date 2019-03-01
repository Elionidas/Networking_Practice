;alright kiddos, time to get you some assembly pratice

;so, here seems to be our backup info. the code is running in x64 assembly, 
;it's running a global main function, and has the external command printf
bits 64
global main
extern printf

section .text
main:
;function setup
push rbp
mov rbp, rsp ;what this means is we are copying the data from a stack pointer to a base pointer,
             ; the 'r' stating it is a FRAME POINTER. we are doing this because rbp allows up to take a snapshot of rsp,
             ; while we change the values of the original rsp
sub rsp, 32 ;this means we are subtracting 32 from the value of rsp
;
lea rdi, [rel message] ; this is lea, which means "load effective address of source into destination" 
                       ;in this case, load [rel message] with data from rdi
mov al, 0 ;copy data from al (8-bit register), make it 0
call printf ;just like it would in C, call the function printf
;
;print source message
lea rdi, [rel source] ; load effective address of [rel source] with info from rdi
mov al, 0 ;copy data from al and make it 0
call printf ;use printf command
;
;print target message
lea rdi, [rel target] ;load effective address of [rel target] with info from rdi
mov al, 0
call printf
;
lea rdi, [rel target]
lea rdi, [rel source]
cld ;this means clear it out effectively

Loop: ;we have made a loop function
lodsb ;load byte at address RSI into AL
stosb ;store AL at address RDI

cmp al, 'c' ;compare c to value of AL
jne LoopBack ;if they dont match, swap to function loopback

lodsb
stosb
cmp al, 'a' ;compare a to the value of AL
jne LoopBack

lodsb
stosb
cmp al, 't'
jne LoopBack

sub rdi, 3 ;subtract 3 from rdi
mov byte [rdi], 'd' ;replace the value of rdi with d
inc rdi ;increment rdi by 1
mov byte [rdi], 'o' ;replace value of rdi with o
inc rdi
mov byte [rdi], 'g'
inc rdi

LoopBack:
cmp al, 0
jne Loop ;if they arent 0, go back to the loop function

;print new version of target
lea rdi, [rel target]
mov al, 0
call printf

;function return
mov eax, 0
add rsp, 32 ;here is where we return the 32 we subtracted at the beginning
pop rbp ;pop rbp off the stack, setting the value back to its new value
ret

section .data
message: db 'Project:',0x0d,0x0a,'Author:',0x0D,0x0a,0x0D,0x0a,0

source: db "The cat chased the bird",0x0a,0x0D,0
target: db '0000000000000000000000000000000000000000',0x0D,0x0a,0

success: db "Success",0