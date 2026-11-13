# Description: This script tests various numeric
#             conversion techniques
# Author: Idasha A Lee

# Variables
a = " 101.1 "
b = '55'
c = "402 Stevens"
d = 'Number 5 ' 

# ---- Variable a ----
# int(a): ValueError - the string has a decimal point, which int() won't accept
# a_int = int(a)  # ValueError
# float(a): works. float() ignores the leading/trailing spaces -> 101.1
a_float = float(a)
# int(float(a)): works. float gives 101.1, then int() drops the decimal part -> 101
a_int_float = int(float(a))

# ---- Variable b ----
# int(b): works -> 55
b_int = int(b)
# float(b): works -> 55.0
b_float = float(b)

# ---- Variable c ----
# int(c): ValueError - "Stevens" is not numeric
# c_int = int(c)  # ValueError
# float(c): ValueError - "Stevens" is not numeric
# c_float = float(c)  # ValueError

# ---- Variable d ----
# int(d): ValueError - "Number" is not numeric
# d_int = int(d)  # ValueError
# float(d): ValueError - "Number" is not numeric
# d_float = float(d)  # ValueError

# ---- Print each variable and its type ----
print(a, type(a))
print(b, type(b))
print(c, type(c))
print(d, type(d))
print(a_float, type(a_float))
print(a_int_float, type(a_int_float))
print(b_int, type(b_int))
print(b_float, type(b_float)) 

a_sliced = float(a[1:6])  
c_sliced = int(c[0:3]) 
d_sliced = int(d[7:8])     

print(a.strip()) 
print(d.strip())  