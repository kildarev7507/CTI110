# This program is a virtual game of rock, paper, scissors between
# the user and computer.
# 7/17/19
# CTI-110 P5HW2 - Rock, Paper, Scissors Game
# Veronica Kildare
# Computer will randomly generate a number between 1-3. User will input rock,
# paper, or scissors usin the same numbers respectively.
# Program will compare integers and assess who the winner is.

import random

rock = 1
paper = 2
scissors = 3

def main():
    rules()
    comp_choice = random.randrange(1,3)
    user_choice = int(input('Choose rock (1), paper (2), or scissors (3): '))
    print('You chose: ', user_choice)
    print('Computer chose: ', comp_choice)
    determineWinner(comp_choice, user_choice)
    
def rules():
    print('Let us play Rock, Paper, Scissors! ')
    print('The rules are:')
    print('Enter number 1 for rock.')
    print('Enter number 2 for paper.')
    print('Enter number 3 for scissors.')

def determineWinner(comp_choice, user_choice):
    if comp_choice == user_choice:
        print('You tied!')
    elif comp_choice == rock and user_choice == paper:
        print('You win!')
    elif comp_choice == rock and user_choice == scissors:
        print('Computer wins.')
    elif comp_choice == scissors and user_choice == rock:
       print('You win!')
    elif comp_choice == scissors and user_choice == paper:
        print('Computer wins')
    elif comp_choice == paper and user_choice == scissors:
        print('You win!')
    elif comp_choice == paper and user_choice == rock:
        print('Computer wins.')
    else:
        print('This is not a valid answer.')
    
main()    
