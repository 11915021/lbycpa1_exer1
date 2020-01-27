##################################################
# Author: DOMINGO, Florenz Howard F - 11915021
# Date: January 25, 2020
# Course: LBYCPA1

# Program Description
""" 
    You can pick a formula
    Input for a variable that needs to be found
    Input the given variables
    Shows the variable the user is looking for
"""
##################################################

def fss_Print(): # for printing - no operation
    print("\n===== FORMULA SELECTION SCREEN =====\n")
    print("[1] Ideal Gas Law")
    print("[2] Dilution")
    print("[3] Quit")
    return
def vss1_Print(): # for printing - no operation
    print("\n===== VARIABLE SELECTION SCREEN =====\n")
    print("PV=nRT\n")
    print("[1] Pressure in atm")
    print("[2] Volume in L")
    print("[3] Amount of substance in mol")
    print("[4] Temperature in Kelvin")
    print("[5] Return to Formula Selection Screen")
def vss2_Print(): # for printing - no operation
    print("\n===== VARIABLE SELECTION SCREEN =====\n")
    print("MiVi = MfVf\n")
    print("[1] Initial Concentration in M")
    print("[2] Initial Volume in L")
    print("[3] Final Concentration in M")
    print("[4] Final Volume in L")
    print("[5] Return to Formula Selection Screen")

def type_Check(number):
    try:
        float(number)
    except ValueError:
        return 0
    return 1

def calculate_PV(third_Var, n, T):
    third_Var = float(third_Var)
    if third_Var == 0:
        print("\nUndefined.\n")
        input("Press any key to continue...")
        return "undef"
    n = float(n)
    T = float(T)
    answer = ( R * n * T ) / third_Var
    return answer
def calculate_nT(P, V, third_Var):
    third_Var = float(third_Var)
    if third_Var == 0:
        print("\nUndefined.\n")
        input("Press any key to continue...")
        return "undef"
    P = float(P)
    V = float(V)
    answer = ( P * V ) / ( R * third_Var )
    return answer
def calculate_Dil(num1, num2, den):
    den = float(den)
    if den == 0:
        print("\nUndefined.\n")
        input("Press any key to continue...")
        return "undef"
    num1 = float(num1)
    num2 = float(num2)
    answer = ( num1 * num2 ) / den
    return answer

R = 0.0821

loop_First = 0
while loop_First == 0:
    fss_Print()
    fss_Pick = str(input("\nChoose an Option: "))
    loop_Second = 0
    if fss_Pick == "1": # Ideal Gas Law
        while loop_Second == 0:
            vss1_Print()
            vss_Pick = str(input("\nChoose an Option: "))
            print("")
            loop_Third = 0
            while loop_Third == 0: 

                if vss_Pick == "1": #Pressure
                    V = input("Input volume in liters: ")
                    type_Return = type_Check(V)
                    if type_Return == 1:
                        pass
                    else:
                        print("\nInvalid Input. Try again.")
                        input("\nPress any key to continue...")
                        break
                    n = input("Input amount of substance in mol: ")
                    type_Return = type_Check(n)
                    if type_Return == 1:
                        pass
                    else:
                        print("\nInvalid Input. Try again.")
                        input("\nPress any key to continue...")
                        break
                    T = input("Input temperature in Kelvin: ")
                    type_Return = type_Check(T)
                    if type_Return == 1:
                        pass
                    else:
                        print("\nInvalid Input. Try again.")
                        input("\nPress any key to continue...")
                        break
                    answer = calculate_PV(V, n, T)
                    if answer == "undef":
                        loop_Third+=1
                    else:
                        print("\nThe pressure is", "%.2f" %answer, "atm\n")
                        input("Press any key to continue...\n")
                        loop_Third+=1

                elif vss_Pick == "2": # Volume
                    P = input("Input pressure in atm: ")
                    type_Return = type_Check(P)
                    if type_Return == 1:
                        pass
                    else:
                        print("\nInvalid Input. Try again.")
                        input("\nPress any key to continue...")
                        break
                    n = input("Input amount of substance in mol: ")
                    type_Return = type_Check(n)
                    if type_Return == 1:
                        pass
                    else:
                        print("\nInvalid Input. Try again.")
                        input("\nPress any key to continue...")
                        break
                    T = input("Input temperature in Kelvin: ")
                    type_Return = type_Check(T)
                    if type_Return == 1:
                        pass
                    else:
                        print("\nInvalid Input. Try again.")
                        input("\nPress any key to continue...")
                        break
                    answer = calculate_PV(P, n, T)
                    if answer == "undef":
                        loop_Third +=1
                    else:
                        print("\nThe volume is", "%.2f" %answer, "L\n")
                        input("Press any key to continue...\n")
                        loop_Third+=1

                elif vss_Pick == "3": # mol
                    P = input("Input pressure in atm: ")
                    type_Return = type_Check(P)
                    if type_Return == 1:
                        pass
                    else:
                        print("\nInvalid Input. Try again.")
                        input("\nPress any key to continue...")
                        break
                    V = input("Input volume in L: ")
                    type_Return = type_Check(V)
                    if type_Return == 1:
                        pass
                    else:
                        print("\nInvalid Input. Try again.")
                        input("\nPress any key to continue...")
                        break
                    T = input("Input temperature in Kelvin: ")
                    type_Return = type_Check(T)
                    if type_Return == 1:
                        pass
                    else:
                        print("\nInvalid Input. Try again.")
                        input("\nPress any key to continue...")
                        break
                    answer = calculate_nT(P, V, T)
                    if answer == "undef":
                        loop_Third +=1
                    else:
                        print("\nThe amount of substance is", "%.2f" %answer, "mol\n")
                        input("Press any key to continue...\n")
                        loop_Third+=1
                    
                elif vss_Pick == "4": #Temperature

                    P = input("Input pressure in atm: ")
                    type_Return = type_Check(P)
                    if type_Return == 1:
                        pass
                    else:
                        print("\nInvalid Input. Try again.")
                        input("\nPress any key to continue...")
                        break
                    V = input("Input volume in L: ")
                    type_Return = type_Check(V)
                    if type_Return == 1:
                        pass
                    else:
                        print("\nInvalid Input. Try again.")
                        input("\nPress any key to continue...")
                        break
                    n = input("Input amount of substance in mol: ")
                    type_Return = type_Check(n)
                    if type_Return == 1:
                        pass
                    else:
                        print("\nInvalid Input. Try again.")
                        input("\nPress any key to continue...")
                        break
                    answer = calculate_nT(P, V, n)
                    if answer == "undef":
                        loop_Third +=1
                    else:
                        print("\nThe temperature is", "%.2f" %answer, "K\n")
                        input("Press any key to continue...\n")
                        loop_Third+=1
                    
                elif vss_Pick == "5":
                    loop_Second+=1
                    break

                else:
                    print("Invalid. Try again.")
                    input("\nPress any key to continue...")
                    break

    elif fss_Pick == "2": # Dilution
        while loop_Second == 0:
            vss2_Print()
            vss_Pick = str(input("\nChoose an Option: "))
            print("")
            loop_Third = 0
            while loop_Third == 0:

                if vss_Pick == "1": # M initial
                    Vi = input("Input initial volume in L: ")
                    type_Return = type_Check(Vi)
                    if type_Return == 1:
                        pass
                    else:
                        print("\nInvalid Input. Try again.")
                        input("\nPress any key to continue...")
                        break
                    Mf = input("Input final concentration in M: ")
                    type_Return = type_Check(Mf)
                    if type_Return == 1:
                        pass
                    else:
                        print("\nInvalid Input. Try again.")
                        input("\nPress any key to continue...")
                        break
                    Vf = input("Input final volume in L: ")
                    type_Return = type_Check(Vf)
                    if type_Return == 1:
                        pass
                    else:
                        print("\nInvalid Input. Try again.")
                        input("\nPress any key to continue...")
                        break
                    answer = calculate_Dil(Mf, Vf, Vi)
                    if answer == "undef":
                        loop_Third+=1
                    else:
                        print("\nThe initial concentration is", "%.2f" %answer, "M\n")
                        input("Press any key to continue...\n")
                        loop_Third+=1
            
                elif vss_Pick == "2": # V initial
                    Mi = input("Input initial concentraion in M: ")
                    type_Return = type_Check(Mi)
                    if type_Return == 1:
                        pass
                    else:
                        print("\nInvalid Input. Try again.")
                        input("\nPress any key to continue...")
                        break
                    Mf = input("Input final concentration in M: ")
                    type_Return = type_Check(Mf)
                    if type_Return == 1:
                        pass
                    else:
                        print("\nInvalid Input. Try again.")
                        input("\nPress any key to continue...")
                        break
                    Vf = input("Input final volume in L: ")
                    type_Return = type_Check(Vf)
                    if type_Return == 1:
                        pass
                    else:
                        print("\nInvalid Input. Try again.")
                        input("\nPress any key to continue...")
                        break
                    answer = calculate_Dil(Mf, Vf, Mi)
                    if answer == "undef":
                        loop_Third+=1
                    else:
                        print("\nThe initial volume is", "%.2f" %answer, "L\n")
                        input("Press any key to continue...\n")
                        loop_Third+=1
                
                elif vss_Pick == "3": # M final
                    Mi = input("Input initial concentraion in M: ")
                    type_Return = type_Check(Mi)
                    if type_Return == 1:
                        pass
                    else:
                        print("\nInvalid Input. Try again.")
                        input("\nPress any key to continue...")
                        break
                    Vi = input("Input initial volume in L: ")
                    type_Return = type_Check(Vi)
                    if type_Return == 1:
                        pass
                    else:
                        print("\nInvalid Input. Try again.")
                        input("\nPress any key to continue...")
                        break
                    Vf = input("Input final volume in L: ")
                    type_Return = type_Check(Vf)
                    if type_Return == 1:
                        pass
                    else:
                        print("\nInvalid Input. Try again.")
                        input("\nPress any key to continue...")
                        break
                    answer = calculate_Dil(Mi, Vi, Vf)
                    if answer == "undef":
                        loop_Third+=1
                    else:
                        print("\nThe final concentration is", "%.2f" %answer, "atm\n")
                        input("Press any key to continue...\n")
                        loop_Third+=1
                
                elif vss_Pick == "4": # V final
                    Mi = input("Input initial concentraion in M: ")
                    type_Return = type_Check(Mi)
                    if type_Return == 1:
                        pass
                    else:
                        print("\nInvalid Input. Try again.")
                        input("\nPress any key to continue...")
                        break
                    Vi = input("Input initial volume in L: ")
                    type_Return = type_Check(Vi)
                    if type_Return == 1:
                        pass
                    else:
                        print("\nInvalid Input. Try again.")
                        input("\nPress any key to continue...")
                        break
                    Mf = input("Input final concentration in M: ")
                    type_Return = type_Check(Mf)
                    if type_Return == 1:
                        pass
                    else:
                        print("\nInvalid Input. Try again.")
                        input("\nPress any key to continue...")
                        break
                    answer = calculate_Dil(Mi, Vi, Mf)
                    if answer == "undef":
                        loop_Third+=1
                    else:
                        print("\nThe final volume is", "%.2f" %answer, "L\n")
                        input("Press any key to continue...\n")
                        loop_Third+=1
            
                elif vss_Pick == "5":
                    loop_Second+=1
                    break

                else:
                    print("Invalid. Try again.")
                    input("\nPress any key to continue...")
                    break

    elif fss_Pick == "3":
        print("\nThank you. Please come again.\n")
        break

    else:
        print("\nInvalid. Try again.")
        input("\nPress any key to continue...")