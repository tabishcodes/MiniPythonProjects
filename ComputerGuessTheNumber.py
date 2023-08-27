import random

def guess(x):
    player_random_number = int(input(f"Now it's your game, choose a number \
between 1 to {x}: "))
    computer_guess = 0

    while computer_guess != player_random_number:
        computer_guess = random.randint(1,x)

        if computer_guess < player_random_number:
            print("Too Low")
        elif computer_guess > player_random_number:
            print("Too High")

    print(f"You got it. It's {player_random_number}")
    
guess(100)