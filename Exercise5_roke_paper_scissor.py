import random
def check_win(player, computer):
    if player == computer:
        return "It's a tie!"
    elif (player == "rock" and computer == "scissors") or (player=="scissors" and computer =="paper" ) or (player=="paper" and computer =="rock" ):
        return "You win!"
    else:
        return "You Lose!"

choices = ["rock", "paper", "scissors"]
print("Welocome to Rock-Paper_Scissors Game!")
print("Enter your choice (rock/paper/scissor): ")

player_choice = input().lower()
if player_choice not in choices:
    print("Invalid input! Please choose only rock, paper, or scissors.")
else:
    computer_chooice = random.choice(choices)
    print(f"\nYou Chose: {player_choice}")
    print(f"Computer Chose: {computer_chooice}")

    res = check_win(player_choice, computer_chooice)
    print(f"\nResult: {res}")