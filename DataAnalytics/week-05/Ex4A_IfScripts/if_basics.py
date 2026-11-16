x = 100 
y = 20 

# 3.a
if x / y == 5:
    print('Are the variables set up correctly?')
    x = 1
# 3.b
if x * y == 20:
    print('Now x times y is y')
    x = 10
else:
    print(f'Whoops, x equals {x}')
# 3.c 
if x < y:
    print('x is less than y')
    x = x * 2
else:
    print('Uh oh, x is not less than y')
#3.d 
if x > y:
    print('How is x greater than y?')
else:
    print('x is NOT greater than y')
# 3.e
print(f'The final value of x is {x} and the final value of y is {y}')
