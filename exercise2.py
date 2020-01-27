#Laboratory Activity - 2
#Framework Copied from idnumber_1.py
#By DOMINGO - 11915021

def type_Check(number):
    try:
        float(number)
    except ValueError:
        return 0
    return 1

c = 0
while c==0:
    number = input("Input ID Number: ")
    if len(number) == 8:
        check = type_Check(number)
        if check == 1:
            break
        else:
            print("ID number must only have digits. Please try again.\n")
    else:
        print("ID number needs to have 8 digits. Please try again.\n")

#code for getting the total
x = 0
total = 0
while x < 8:
    current = int(number[x])
    current = current * (8-x)
    #for checking if working - 1/2
    #print(current)
    total = total + current
    x+=1

#for checking if working - 2/2
#print("The total is: ", total)

split = total // 11

if split < 16:
    print("STUDENT")
elif split >= 16:
    print("FACULTY")
else:
    print("INVALID")