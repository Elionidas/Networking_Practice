;lets do it, fibonacci to the nth number
;recieves ecx as input "n"
;returns EAX as nth fibonacci number calculated

;alright first off, think of this as if it was a C program
.data
    previous DWORD ?
    current DWORD ?

;we use EAX to store the result without using a :next: variable
;we cant use mov for memory to memory, so we will pass it through EDX for the assignment previous = current
;alright so in assembly this looks like this
FibonacciByMemory PROC
    mov eax, 1 ;set a counter
    mov previous, 0 ;initialize previous variable
    mov current, 0 ;initialize current variable
L1:
    add eax,previous ;add the previous number to EAX register
    mov edx, current ;change the EDX register to hold the current number
    mov previous, current ;make current the previous number
    mov current, eax ;place the current number EAX calculated into the current variable
loop L1 ;loop the function over and over until we get to the 'n'th number
    ret
FibonacciByMemory ENDP

;now this is utilizing memory and variables. to do this purely with registers it looks like this
;using the mov command...
FibonacciByRegMOV PROC
    mov eax, 1 ;once again assign the counter
    xor ebx, ebx ;XOR the ebx register to create previous
    xor edx, edx ;xor the edx register to create current
L1:
    add eax, ebx ;effectively += in this instance
    mov ebx, edx ;create a new current number
    mov edx, eax ;create a new previous number
loop L1 ;loop the function
    ret ;return the EAX nth number
FibonacciByRegMOV ENDP

;now if you want to do this even easier with the XCHG command...
FibonacciByRegXCHG PROC
    xor eax,eax ;make eax 1
    mov ebx, 1 ;assign ebx to hold 1
L1:
    xchg eax, ebx ;change out eax for ebx (previous for current)
    add eax, ebx ;add them together, making a new current number
loop L1 ;loop function
    ret ;return eax as the nth number
FibonacciByRegXCHG ENDP

;theres also an even easier way using something called an atomic instruction
FibonacciByRegXADD PROC
    xor eax, eax ;make your counter, setting eax to 1
    mov ebx, 1 ;create your current number
L1:
    xadd eax, ebx ;so this command actually xchanges the two registers and then adds the sum of the two, 
    ;storing it in the destination register
loop L1 ;loop the xadd command
    ret ;return the eax as nth number
FibonacciByRegXADD ENDP

;now if we are to perform fibonacci using the stack it would look more like this
FibonacciByStack PROC
    mov eax, 1
    mov previous, 0
    mov current, 0
L1:
    add eax, previous
    push current
    pop previous
    mov current, eax
loop L1
    ret
FibonacciByStack ENDP

;