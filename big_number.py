def greatest(num1,num2,num3):
    if num1 > num2 and num3:
        return num1
    elif num2 > num1 and num3:
        return num2
    else:
        return num3    


num1 = int(input("Number 1: "))
num2 = int(input("Number 2: "))
num3 = int(input("Number 3: "))

big = greatest(num1,num2,num3)
print(f"{big} is greater.")