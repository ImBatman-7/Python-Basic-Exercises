import random
winning_number = random.randint(1,100)

guess = 1
user = int(input("Guess any number between 1-100: "))

game_over = False


while not game_over:
    if user == winning_number:
       print(f"Congratulations! You guessed the correct number, and you gussed this number in {guess} times.")
       game_over = True 
    else:
        if user < winning_number:
            print("Too low.")
      
 
        else:
            print("too high.")

        guess += 1
        user = int(input("guess again: "))
       

