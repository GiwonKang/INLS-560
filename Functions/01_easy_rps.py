# Super simple Rock, Paper, Scissors game...

# User choosees R P S
user_choice = input("Enter r, p, or s for rock paper or scisors: ")

# Computer choice is set by programmer...
computer_choice = 'r'

# Programmer must code the tie, win lose messages based on his choice...
if user_choice == 'r':
    print("You tied!")
if user_choice == 's':
    print("You lose!")
if user_choice == 'p':
    print("You win!")
