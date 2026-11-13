# A savings account worth X to double in value based on interst rate of IR (RULE of 72)
# Rule of 72 - formula used to calculate how long an investment will need to double in value, given its annual rate of return 

savings = 8500
interest_rate = .05
years = 72 / (interest_rate * 100)
doubled_balance = savings * 2 

print(f'Your current savings is', format(savings,'.2f') +'.')
print(f'At a', format(interest_rate, '.0%'),' interest rate, your savings account will be') 
print(f' worth', format(doubled_balance, '.2f'), 'in', format(years, '.1f'), 'years')