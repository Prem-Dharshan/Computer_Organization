.data
prompt1: .asciiz "Enter first number: "
prompt2: .asciiz "Enter second number: "
result: .asciiz "Result: "

.text
.globl main

main:
    # Display prompt1 and read first number
    li $v0, 4
    la $a0, prompt1
    syscall
    
    li $v0, 5
    syscall
    move $t0, $v0
    
    # Display prompt2 and read second number
    li $v0, 4
    la $a0, prompt2
    syscall
    
    li $v0, 5
    syscall
    move $t1, $v0
    
    # Call recursive subroutine to perform arithmetic operations
    move $a0, $t0
    move $a1, $t1
    jal arithmetic_op
    
    # Display result
    li $v0, 4
    la $a0, result
    syscall
    
    li $v0, 1
    move $a0, $v0
    syscall
    
    # Exit program
    li $v0, 10
    syscall
    
# Subroutine to perform arithmetic operations recursively
# Inputs: $a0 - first operand, $a1 - second operand
# Outputs: $v0 - result of operation
arithmetic_op:
    # Check if second operand is 0 (to prevent division by zero)
    beq $a1, $0, exit_division
    
    # Perform addition
    add $v0, $a0, $a1
    j exit_op
    
    # Perform subtraction
    sub $v0, $a0, $a1
    j exit_op
    
    # Perform multiplication
    mult $a0, $a1
    mflo $v0
    j exit_op
    
    # Perform division
    div $a0, $a1
    mflo $v0
    j exit_op
    
    # Perform modulo operation
mod_op:
    div $a0, $a1
    mfhi $v0
    j exit_op
    
    # Exit recursive subroutine
exit_op:
    jr $ra
    
    # Exit division operation (if second operand is 0)
exit_division:
    li $v0, 0xffffffff # Set result to -1 to indicate division by zero error
    jr $ra

