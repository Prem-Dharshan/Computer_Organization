# data section
.data
prompt1: .asciiz "Enter the first number: "
prompt2: .asciiz "Enter the second number: "
prompt3: .asciiz "Enter the operator (+, -, *, or /): "
result: .asciiz "\n\nThe result is: "
error_message: .asciiz "Invalid operator. Please try again.\n"

# text section
.text
# main function
main:
    # prompt user for first number
    li $v0, 4
    la $a0, prompt1
    syscall
    
    # read in first number
    li $v0, 5
    syscall
    move $s0, $v0
    
    # prompt user for second number
    li $v0, 4
    la $a0, prompt2
    syscall
    
    # read in second number
    li $v0, 5
    syscall
    move $s1, $v0
    
    # prompt user for operator
    li $v0, 4
    la $a0, prompt3
    syscall
    
    # read in operator
    li $v0, 12
    syscall
    move $s2, $v0
    
    # perform operation based on operator
    beq $s2, 43, add_op # if operator is '+', jump to add_op label
    beq $s2, 45, sub_op # if operator is '-', jump to sub_op label
    beq $s2, 42, mul_op # if operator is '*', jump to mul_op label
    beq $s2, 47, div_op # if operator is '/', jump to div_op label
    j error # if operator is invalid, jump to error label
    
add_op:
    add $t0, $s0, $s1 # add the two numbers
    j print_result # jump to print_result label
    
sub_op:
    sub $t0, $s0, $s1 # subtract the two numbers
    j print_result # jump to print_result label
    
mul_op:
    mul $t0, $s0, $s1 # multiply the two numbers
    j print_result # jump to print_result label
    
div_op:
    div $s0, $s1 # divide the two numbers
    mflo $t0 # move quotient to $t0
    j print_result # jump to print_result label
    
error:
    li $v0, 4
    la $a0, error_message
    syscall
    j exit # jump to exit label
    
print_result:
    li $v0, 4
    la $a0, result
    syscall
    li $v0, 1
    move $a0, $t0 # display result in $t0
    syscall
    
exit:
    li $v0, 10
    syscall
