winning_number = 25
user = int(input("Write any number between 0 to 50: "))

 
if user == winning_number:
    print("you won!!!") 
else:
    if user < winning_number:
        print("Too low.")
    else:
        print("too high.")        