# Program will add the sum of positive numbers entered by user.
# 7/9/19
# CTI-110 P4HW3 - Sum of Numbers
# Veronica Kildare
#

# Program will ask the user to enter positive numbers.
# Program will calculate positive numbers until user enter a negative number.
# Program will display the total of all numbers entered.


def main():
    total = 0
    print('Please enter a positive number to calculate.')
    print('The program will conclude when a negative number is entered.')
    number = int(input('Enter positive number: '))

    while number >= 0:
        total += number 
        print('The total is', total)
        number = int(input('Enter positive number: '))

main()
    
