#Define known values
food_cost = 79.25
tax = 6.54
tip = 12.00

#Calculate the unknown
total_due = food_cost + tax + tip

#Display the results
#print(f'The total due is ' + str(total_due))

#Due to the fact that the total_due being a float and we want to display it as a text so we use string conversion to convert the float to a string.

print('Food cost is ' + str(food_cost) + ' and tax is' + str(tax))
#print('Tip is ' + str(tip))
print('Total due is ' + str(total_due))
print('Tip is ' + format(tip, '.2f'))