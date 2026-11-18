bank_balance = 150
savings_goal = 3000
weekly_savings = 50 

while bank_balance < savings_goal:
    bank_balance = bank_balance + weekly_savings 

    if bank_balance >= savings_goal * 0.75 - 80:
        print(f'So close! After treating myself, my balance is up to {bank_balance}')
    elif bank_balance > savings_goal * 0.5:
       print(f'Almost there! This week my balance went up to {bank_balance}')
    else:
        print(f'This week my balance increased to {bank_balance}')

print(f'Goal met! My current balance is {bank_balance}')