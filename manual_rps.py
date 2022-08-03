import random

def get_computer_choice():
    list  = ['Rock', 'Paper', 'Scissors']
    return random.choice(list)

def get_user_choice():
    user_input = input("Enter your input: ")
    return(user_input)

def get_winner(computer_choice, user_choice):
    computer_win = (computer_choice == 'Rock' and user_choice == 'Scissor') or (computer_choice == 'Scissors' and user_choice == 'Paper') or (computer_choice == 'Paper' and user_choice == 'Rock')
    if computer_win:
        return 'Computer Wins'
    elif computer_choice == user_choice:
        return 'draw'
    else:
        return 'User Wins'

def play():
    computer_choice = get_computer_choice()
    user_choice = get_user_choice()
    print(get_winner(computer_choice, user_choice))

play()
