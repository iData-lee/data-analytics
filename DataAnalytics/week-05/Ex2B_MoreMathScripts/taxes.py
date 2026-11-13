# Federal taxes are 23% of monthly salary. If making X amount of money. How much is withheld?

salary = 4000 # monthly salary
fed_tax = .23

tax_withheld = salary * fed_tax
home_pay = salary - tax_withheld

print(f'Your monthly salary is{salary:.2f}.')
print(f'At a {fed_tax:.0%} tax rate, your withholding will be {tax_withheld:.2f}.')