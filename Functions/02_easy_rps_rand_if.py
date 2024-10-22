import random

# Super simple Rock, Paper, Scissors game...

# User choosees R P S
user_choice = input("Enter r, p, or s for rock paper or scisors: ")

# Computer choice is set by programmer...
computer_choice = random.choice("r", "p", "s")

# Programmer must code the tie, win lose messages based on his choice...
if user_choice == computer_choice:
    print("You tied!")
if user_choice == 's':
    print("You lose!")
if user_choice == 'p' and computer_choice == "s" or user_choice == 'p' and computer_choice == "r" or user_choice == 'p':
    print("You win!")