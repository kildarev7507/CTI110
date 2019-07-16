# This program is a game that asks the user to guess whether a randomly 
# generated number between 1 and 100 will be higher or lower than the number
# that was entered.
# 7/16/19
# CTI-110 P5HW1 - Random Number
# Veronica Kildare

# User will enter number. Computer will generate random number, and then 
# compare if number is higher, lower, or equal to number generated. If numbers
# match, the program will restart. 

import random
auto_num = random.randrange(99, 100)

def main():
    entered_num = float(input('Enter a number between 1 and 100: '))
        
    if entered_num > auto_num:
        print(auto_num)
        print('Too high. Try again.')
    elif entered_num < auto_num:
        print(auto_num)
        print('Too low. Try again.')
    elif entered_num == auto_num:
        print(auto_num)
        print('Numbers match! Play again.')
        entered_num = float(input('Enter a number between 1 and 100: '))
main()
        
    
    
