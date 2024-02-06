# Python program to divide two
# unsigned integers using
# Non-Restoring Division Algorithm

def binTodeci(n):
    decimal = 0
    power = 1
    while n > 0:
        rem = n % 10
        n = n//10
        decimal += rem*power
        power *= 2

    return decimal

# Function to add two binary numbers
def add(A, M):
	carry = 0
	Sum = ''

	# Iterating through the number
	# A. Here, it is assumed that
	# the length of both the numbers
	# is same
	for i in range (len(A)-1, -1, -1):

		# Adding the values at both
		# the indices along with the
		# carry
		temp = int(A[i]) + int(M[i]) + carry

		# If the binary number exceeds 1
		if (temp>1):
			Sum += str(temp % 2)
			carry = 1
		else:
			Sum += str(temp)
			carry = 0

	# Returning the sum from
	# MSB to LSB
	return Sum[::-1]

# Function to find the compliment
# of the given binary number
def compliment(m,A):
	M = ''

	# Iterating through the number
	for i in range (0, len(m)):

		# Computing the compliment
		M += str((int(m[i]) + 1) % 2)

	# Adding 1 to the computed
	# value
	M = add(M, (len(A)-1)*'0'+'1')
	return M
	
# Function to find the quotient
# and remainder using the
# Non-Restoring Division Algorithm
def nonRestoringDivision(Q, M, A):
	
	# Computing the length of the
	# number
	count = len(M)


	comp_M = compliment(M,A)

	# Variable to determine whether
	# addition or subtraction has
	# to be computed for the next step
	flag = 'successful'

	# Printing the initial values
	# of the accumulator, dividend
	# and divisor
	print ('Initial Values: A:', A,
		' Q:', Q, ' M:', M)
	
	# The number of steps is equal to the
	# length of the binary number
	while (count):

		# Printing the values at every step
		print ("\nstep:", len(M)-count + 1,
			end = '')
		
		# Step1: Left Shift, assigning LSB of Q
		# to MSB of A.
		print (' Left Shift and ', end = '')
		A = A[1:] + Q[0]

		# Choosing the addition
		# or subtraction based on the
		# result of the previous step
		if (flag == 'successful'):
			A = add(A, comp_M)
			print ('subtract: ')
		else:
			A = add(A, M)
			print ('Addition: ')
			
		print('A:', A, ' Q:',
			Q[1:]+'_', end ='')
		
		if (A[0] == '1'):


			# Step is unsuccessful and the
			# quotient bit will be '0'
			Q = Q[1:] + '0'
			print (' -Unsuccessful')

			flag = 'unsuccessful'
			print ('A:', A, ' Q:', Q,
				' -Addition in next Step')
			
		else:

			# Step is successful and the quotient
			# bit will be '1'
			Q = Q[1:] + '1'
			print (' Successful')

			flag = 'successful'
			print ('A:', A, ' Q:', Q,
				' -Subtraction in next step')
		count -= 1
	print ('\nQuotient(Q):', Q,
		' Remainder(A):', A)
	print(binTodeci(int((Q))), binTodeci(int(A)), "\n")

# Driver code
if __name__ == "__main__":

	dividend = '10000'
	divisor = '00101'
	print(binTodeci(int((dividend))), binTodeci(int(divisor)), "\n")

	accumulator = '0' * len(dividend)

	nonRestoringDivision(dividend,
						divisor,
						accumulator)
