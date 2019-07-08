# Program calculates calories burned in a 20, 35, and 45 minute workout.
# 7/7/19
# CTI-110 P4HW1 - Calories Burned
# Veronica Kildare

# The program will calculate how many calories were burned during a 20, 35,
# and 45 minute treadmill workout. It will display the total amount
# of calories burned to the user.

def main():
    for time in [20, 35, 45]:
        calories = 5 * time
        print('In', time, 'minutes you burned: ', calories)
main()
