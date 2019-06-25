# Program will compare the area of two rectagles and tell the user which
# rectangle has the greater area.
# 6/25/19
# CTI-110 P3T1 - Areas of a Rectangle
# Veronica Kildare

# User will enter the length and area of rectangle 1.
# User will enter the length and area of rectangle 2.
# The program will calculate the area of both rectangles.
# The program will display which rectangle has the greater area.

width1 = int(input('Enter the width for reactangle 1: '))
length1 = int(input('Enter the length for rectangle 1: '))
width2 = int(input('Enter the width for rectangle 2: '))
length2 = int(input('Enter the length for rectangle 2: '))

area1 = width1 * length1
area2 = width2 * length2

if area1 > area2:
    print('Rectangle 1 has the greater area.')
  
elif area1 < area2:
    print('Rectangle 2 has the greater area.')
else:
    print('Both rectangles have the same area.')
