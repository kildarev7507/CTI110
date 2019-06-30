# CTI-110 
# P3HW2 - MealTipTax 
# Veronica Kildare 
# 6/30/19
#
# User will enter total charge of their meal, and choose how much tip they
# would like to leave. The tip along with the 7% tax sales will be calculated
# and display. All the charges will be displayed separately.


meal_cost = float(input('Please enter your meal total: '))
tip = int(input('Enter if you would like to leave a 15, 18, or 20 percent tip: '))
tax = meal_cost * .07
tip_total = meal_cost * (tip * .01)
meal_total = tax + tip_total + meal_cost

if tip == 15:
    print('Tip amount is $', format(tip_total, '.2f'))
    print('You tax total is $', format(tax, '.2f'))
    print('Your total is $', format(meal_total, '.2f'))
elif tip == 18:
    print('Tip amount is $', format(tip_total, '.2f'))
    print('You tax total is $', format(tax, '.2f'))
    print('Your total is $', format(meal_total, '.2f'))
elif tip == 20:
    print('Tip amount is $', format(tip_total, '.2f'))
    print('You tax total is $', format(tax, '.2f'))
    print('Your total is $', format(meal_total, '.2f'))
else:
    print('Please enter appropriate tip percentage.')
