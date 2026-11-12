from operator import sub


print('Hello world!')


message = 'Hello world!'
print(message)
# We made the statement to print off Hello world! twice and that is exactly as the system provided.


#Displaying dollars and cents
dollars = 3
cents = .50
print(dollars + cents) 
# When it added the two variables together it gave us the total of 3.5 which is correct but it also should the value as 3.5 and not 3.50. 
cents = cents + .25
print(dollars + cents) 
d_str = str('3 dollars') 
c_str = str('50 cents')
d_str + c_str
print(d_str + ' and ' + c_str) 

item1 = 25.75
item2 = 45.67
item3 = 45.75 
item4 = 55.67 
item5 = 45.60 

sub_total = item1 + item2 + item3 + item4 + item5

tax = sub_total * .07
Total = sub_total + tax

print(f'sub-total = {sub_total:.2f}')
print(f'      tax = {tax:.2f}')
print(f'Total Cost = {Total:.2f}') 

temp_celsius = 30 
temp_fahrenheit = (temp_celsius * 9/5) + 32 
print(f' {temp_celsius}°C is equal to {temp_fahrenheit}°F')

meal_cost = 65
tip_prcnt = 20 
tax_prcnt = 8.25 
total_cost = meal_cost + (meal_cost * tip_prcnt / 100) + (meal_cost * tax_prcnt / 100)
print(f'Total meal cost = ${total_cost:.2f}')