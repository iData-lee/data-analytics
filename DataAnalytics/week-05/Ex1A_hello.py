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

#Ask the user to find the average of three numbers
name = input('Enter your name:')
num1 = eval(input('Enter the first number:'))
num2 = eval(input('Enter the second number:'))
num3 = eval(input('Enter the third number:'))

print(f'The average of {num1}, {num2}, and {num3} is {(num1 + num2 + num3) / 3:.2f}')

name = input('Enter your name:')
salary = int(input('Enter your salary:'))

if salary >= 50000:
   print ((f'{name}, you are eligible for a bonus'))     

print('Done!')

score = int(input('Enter your score:'))
if score >= 80: 
   print (f'Excellent pwrformance!')
else:
    print(f'Needs improvement.')

