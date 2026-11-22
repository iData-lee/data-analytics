import math 

# ValueError, way 1: converting bad text to a number
try: 
    num = int('abc')
except ValueError:
    print("ValueError: Oops, that text can't be converted to an interger")
else: 
    print(num)
finally: 
    print("Let's try another one ... ")

# ValueError, way 2: Square Root of a negative number
try: 
    root = math.sqrt(-1)
except ValueError: 
    print("ValueError: Oops, you can't take the square root of a negative number")
else: 
    print(root)
finally: 
    print("Let's try another one ... ")

# NameError, way 1: Assigning an undefined object
try:
    m = banana 
except NameError:
    print("NameError: Oops, looks like you tried to assign an undefined object to a variable")
else:
    print(m)
finally: 
    print("Let's try another one ...")

# NameError, way 2: Printing an undefined varaible
try: 
    print(undefined_var)
except NameError: 
    print("NameError: Oops, that variable was never created")
else:
    print('No error')
finally: 
    print("Let's try another one ... ")

# TypeError, way 1: adding text and a number 
try:
    total = '5' + 5 
except TypeError: 
    print("TypeError: Oops, you can't add a string and an interger")
else: 
    print(total)
finally: 
    print("Let's try another one ... ")

# TypeError, way 2: len() of a number
try: 
    size = len(5)
except TypeError: 
    print("TypeError: Oops, a number has no length")
else: 
    print(size)
finally:
    print("Let's try another one ... ")

# SyntaxError, way 1: Broken code inside a string 
try: 
    result = eval("5 +")
except SyntaxError: 
    print("SyntaxError: Oops, that code isn't written correctly")
else: 
    print(result)
finally: 
    print("Let's try another one ... ")

# SyntaxError, way 2: missing closing parenthesis 
try: 
   exec("print('hi'")
except SyntaxError: 
    print('SyntaxError: Oops, a parenthesis was never closed')
else: 
    print('No error')
finally: 
    print("Let's try another one ...")