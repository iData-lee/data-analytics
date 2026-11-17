pay_rate = 30
hours_worked = 45
filing_status = 'joint'

if hours_worked > 40:
    regular_pay = 40 * pay_rate
    overtime_hours = hours_worked - 40
    overtime_pay = overtime_hours * pay_rate * 1.5
    gross_pay = regular_pay + overtime_pay 
else:
    gross_pay = hours_worked * pay_rate
#print(f'Gross pay: {gross_pay:.2f}')

annual_gross = gross_pay * 52
#print(annual_gross)

if filing_status == 'single':
    if annual_gross < 12000:
        tax_rate = 0.05
    elif annual_gross < 25000:
        tax_rate = 0.10
    elif annual_gross < 75000:
        tax_rate = 0.15
    else: 
        tax_rate = 0.20
else: 
    if filing_status == 'joint':
        if annual_gross < 12000:
            tax_rate = 0.00
        elif annual_gross < 25000:
            tax_rate = 0.06
        elif annual_gross < 75000:
            tax_rate = 0.11
        else:
            tax_rate = 0.20 

tax_withheld = gross_pay * tax_rate 
net_pay = gross_pay - tax_withheld 

print(f'You worked {hours_worked} hours this period.')
print(f'Because you earn ${pay_rate} per hour, your gross weekly pay is ${gross_pay:.2f}.')
print(f'Your filing status is {filing_status}')
print(f'Your tax withholding for the week is ${tax_withheld:.2f}')
print(f'Your net pay is ${net_pay:.2f}')
