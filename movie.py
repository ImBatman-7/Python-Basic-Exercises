user_name = input("Type your name: ")
user_age = int(input("Type your age: "))

if (user_name[0] == 'a' or user_name[0] == 'A') and user_age > 10:
    print("You can watch this movie!!!")
else:
    print("Sorry! You can't watch this movie.")    
