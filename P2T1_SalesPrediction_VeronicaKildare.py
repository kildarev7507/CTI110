#Get the projected total sales.
#06/18/19
#CTI-110 P2T1 - Sales Prediction
#Veronica Kildare
#
total_sales = float(input('Enter the projected sales: '))

#Calculate the profit as 23 percent of total sales.
profit = total_sales * 0.23

#Display the profit.
print('The profit is $', format(profit, ',.2f'))
