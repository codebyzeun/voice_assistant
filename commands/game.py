import random

def play_rps(player_choice):
    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)
    if player_choice == computer_choice:
        return f"It's a tie! We both chose {player_choice}."
    elif (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "scissors" and computer_choice == "paper") or \
         (player_choice == "paper" and computer_choice == "rock"):
        return f"You win! {player_choice} beats {computer_choice}."
    else:
        return f"You lose! {computer_choice} beats {player_choice}."
