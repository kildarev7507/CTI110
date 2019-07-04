# This program asks user to enter amount of bugs caught on a daily basis,
# and displays the total number of bugs collected.
# 7/3/19
# CTI-110 P4T2 - Bug Collector
# Veronica Kildare
#

total = 0
for day in range(1,6):
    print('How many bugs were collected on day', day)
    bugs = int(input())
    total += bugs
print('You caught a total of', total)
