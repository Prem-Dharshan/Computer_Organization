from prettytable import PrettyTable


def int_to_bin(n):
    n = bin(n)
    return n[2:]


def shift_left(C, AC, Q):

    C = AC[0]

    temp_AC = list(AC)
    for i in range(1, len(AC)):
        temp_AC[i-1] = temp_AC[i]
    temp_AC[len(AC)-1] = Q[0]
    AC = ''
    AC = AC.join(temp_AC)

    temp_Q = list(Q)
    for i in range(1, len(Q)):
        temp_Q[i-1] = temp_Q[i]
    temp_Q[len(Q)-1] = '_'
    Q = ''
    Q = Q.join(temp_Q)

    return (C, AC, Q)


def operation(C, AC, M):

    temp = C + AC
    temp = bin(int(temp, 2)+int(M, 2)).replace("0b", "")

    if (len(temp) > len(M)):
        temp = temp[1::]

    return (temp[0], temp[1::])

def main():

    AC = ''
    Sign_Bit = '0'

    dividend = input("Enter the dividend(Q)  : ")
    divisor = input("Enter the divisor(M)   : ")

    Q = int_to_bin(int(dividend))
    M = int_to_bin(int(divisor))

    if (len(Q) > len(M)):
        for i in range(len(Q)):
            AC += '0'
    else:
        for i in range(len(M)):
            AC += '0'

    for i in range(len(Q)-len(M)):
        M = '0' + M

    M = '0' + M

    M_arr = list(M)

    for i in range(len(M)):
        if (M[i] == '0'):
            M_arr[i] = '1'
        if (M[i] == '1'):
            M_arr[i] = '0'

    comp_M = ''.join(M_arr)
    comp_M = bin(int(comp_M, 2)+int('1', 2))
    comp_M = comp_M.replace("0b", "")

    table = PrettyTable()
    table.field_names = ["Step No.", "Sign Bit", "Accumulator", "Qutient", "Operartion done"]
    table.add_row(["", Sign_Bit, AC, Q, "Initial Values"])
    table.add_row(["-----------", "----------", "-------------", "------------", "----------------------------"])

    for i in range(len(Q)):

        Sign_Bit, AC, Q = shift_left(Sign_Bit, AC, Q)

        table.add_row([f"Step {i+1}", Sign_Bit, AC, Q, "After shift left operation"])

        if (Sign_Bit == '0'):
            Sign_Bit, AC = operation(Sign_Bit, AC, comp_M)
            
            table.add_row(["", Sign_Bit, AC, Q, "AC = AC - M"])
            table.add_row(["-----------", "----------", "-------------",
                          "------------", "----------------------------"])

        else:
            Sign_Bit, AC = operation(Sign_Bit, AC, M)
            table.add_row(["", Sign_Bit, AC, Q, "AC = AC + M"])
            table.add_row(["-----------", "----------", "-------------",
                          "------------", "----------------------------"])

        if (Sign_Bit == '1'):
            temp_Q = list(Q)
            temp_Q[len(Q)-1] = '0'
            Q = ''
            Q = Q.join(temp_Q)

        else:
            temp_Q = list(Q)
            temp_Q[len(Q)-1] = '1'
            Q = ''
            Q = Q.join(temp_Q)

    if (Sign_Bit == '1'):
        
        Sign_Bit, AC = operation(Sign_Bit, AC, M)
        table.add_row(["Last Step", Sign_Bit, AC, Q, "Since, AC < 0\nAC = AC + M"])
        table.add_row(["", Sign_Bit, AC, Q, ""])
    
    else:
        
        print("No final step as AC is positive.")
        table.add_row([f"Last Step", Sign_Bit, AC, Q, "No Operation since AC > 0"])
    
    print(table)

    print("\nInitial AC value is    : ", AC)
    print("Initial Q value is     : ", Q)
    print("Value of M is          : ", M)
    print("Two's complement of M  : ", comp_M)
    print()
    print("Remainder              : ", int(Sign_Bit+AC, 2))
    print("Quotient               : ", int(Q, 2))

if __name__ == "__main__":
    main()