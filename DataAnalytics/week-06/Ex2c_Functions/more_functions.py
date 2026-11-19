# Function 1 Mailing Label
def display_mailing_label(name, address, city, state, zip):
    print(name)
    print(address)
    print(f'{city}, {state} {zip}')

# Function 2 add any number of values
def add_numbers(*numbers): 
    total = sum(numbers)
    text = '+'.join(str(n) for n in numbers)
    print(f'{text} = {total}')

# Function 3 Receipt
def display_receipt(total_due, amount_paid):
    print(f'Total Due: ${total_due:.2f}')
    print(f'Amount Paid: ${amount_paid:.2f}')
    if amount_paid >= total_due:
        change = amount_paid - total_due 
        print(f'Change Due: ${change:.2f}')
    else:
        remaining = total_due - amount_paid 
        print(f'Remaining balance to be paid: ${remaining:.2f}')

# Step 5.A Call the label function twice
display_mailing_label('Genesa Alvarez', '398 Day Lane', 'Philadelphia', 'PA', '19093')
print()
display_mailing_label('Sam Lee', '12 Oak Street', 'Camden', 'NJ', '08101')
print()

# Step 5.B Call add_numbers 3 times
add_numbers(5)
add_numbers(3, 4)
add_numbers(10, 20, 30, 40)
print()

# Step 5.C Overpay, Exact, Underpay
display_receipt(40.00, 50.00)
print()
display_receipt(40.00, 40.00)
print()
display_receipt(40.00, 25.00)