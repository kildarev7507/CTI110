# Program will convert kilometers into miles.
# 7/15/19
# CTI-110 P5T1_KilometerConverter 
# Veronica Kildare
#
CONVERSION_FACTOR = 0.6214
def main():
    kilometers = float(input('Enter distance in kilometers: '))
    show_miles(kilometers)
    
def show_miles(km):
    miles = km * CONVERSION_FACTOR
    print(km, 'kilometers equals', miles, 'miles')

main()
    
