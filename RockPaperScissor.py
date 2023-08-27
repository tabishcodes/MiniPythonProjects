import random

def play():
    user = input("'r' for rock, 'p' for paper & 's' for scissor ? ")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        print(f"Tie ! You both choose {user}")
    if is_win(user, computer):
        return 'You won ! ' + user + ' beats ' + computer
    
    return 'Computer won ! ' + computer + ' beats ' + user

def is_win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p')\
    or (player == 'p' and opponent == 'r'):
        return True

print(play())