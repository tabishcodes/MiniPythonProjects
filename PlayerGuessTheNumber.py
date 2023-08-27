import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0

    while guess != random_number:
        guess = int(input(f"Guess a number between 1 to {x}: "))

        if guess < random_number:
            print("Too Low")
        elif guess > random_number:
            print("Too High")

    print(f"You got it. It's {random_number}")
    
guess(10)