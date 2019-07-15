# This program will convert the input number of inches to feet.
# 7/15/19
# CTI-110 P5T2_FeetToInches 
# Veronica Kildare
#
INCHES_PER_FOOT = 12

def main():
    feet = int(input('Enter a number of feet: '))
    print(feet, 'equals', feet_to_inches(feet), 'inches.')
    
def feet_to_inches(feet):
    return feet * INCHES_PER_FOOT

main()
