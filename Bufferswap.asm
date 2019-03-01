;fibbonachi sequence

;step one: check locations of buffers
lea rdi, [0] ;1st buffer
lea rsi, [1] ;2nd buffer
;step two: do the logic
;the logic for fibonacci is that you take the previous number, add it to the current, to get the next digit
cmp rsi, rdi ;compare source to destination
jb .backwards ;if above, swap backwards
ja .forwards 

.backwards
mov ecx, length_of_buffer
lea rsi, length_of_buffer
lea rdi, length_of_buffer
loop 
mov rsi, rdi ;overwrite current value with value stored in 2nd buffer
lea rsi-1, length_of_buffer
lea rdi-1, length_of_buffer

.forwards
rep movsb rsi, rdi ;move byte from source to destination. this varies from loop as it automatically increments forward
;essentially this does the same thing as .backwards, but does not require us to specify where the address it pointed

;step three: do the swap (backwards swap or forwards swap)
;this depends on the way the buffers overlap. if the second buffer is before the first, swap backwards for example.