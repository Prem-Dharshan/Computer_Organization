# MIPS 32 program to take input number first and then asks for operator, computes and ends program at '='

.data
  op: .asciiz "\nEnter the operator (+, -, *, /)(Enter = to print result): "
  num: .asciiz "\nEnter a number: "
  result: .asciiz "\n\nResult: "

.text
.globl main
main:
  # Prompt for a number
  li $v0, 4
  la $a0, num
  syscall
    
  # Read a number
  li $v0, 5
  syscall
  move $t2, $v0
    
  # Loop until the input is '='
  Loop:
    # Prompt for the operator
    li $v0, 4
    la $a0, op
    syscall
  
    # Read the operator
    li $v0, 12
    syscall
    move $t0, $v0
    
    # Check if the input is '='
    beq $t0, '=', End
    
    # Prompt for a number
    li $v0, 4
    la $a0, num
    syscall
    
    # Read a number
    li $v0, 5
    syscall
    move $t1, $v0
    
    # Perform the operation
    beq $t0, '+', Add
    beq $t0, '-', Sub
    beq $t0, '*', Mul
    beq $t0, '/', Div
    
  Add:
    add $t2, $t2, $t1
    j Next
  
  Sub:
    sub $t2, $t2, $t1
    j Next
  
  Mul:
    mul $t2, $t2, $t1
    j Next
  
  Div:
    div $t2, $t2, $t1
    j Next
  
  # Prompt for the next operator
  Next:
    j Loop
  
  # Print the result
  End:
    li $v0, 4
    la $a0, result
    syscall
    
    li $v0, 1
    move $a0, $t2
    syscall
    
    # Exit the program
    li $v0, 10
    syscall
