# Program will display a table of lbs to kilos conversion from 100-300
# 7/8/19
# CTI-110 P4HW2 - Pounds to Kilos Table
# Veronica Kildare

# Value will be given to variable. Using the for loop and long with range,
# program will convert pounds to kilos from 100 to 300 lbs, in 10 lbs
# increments. Lastly, the conversion will be shown using a table.

def main():
    starting_lbs = 100
    ending_lbs = 310
    step_value = 10
    conversion = 2.2046

    print('Pounds\tKilos')
    print('-------------')

    for pounds in range(starting_lbs, ending_lbs, step_value):
        kilos = pounds / conversion
        print(pounds, '\t', format(kilos, '.2f'))

main()
    
