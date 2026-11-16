name_1 = 'PRIYA SHARMA'
name_2 = 'bob NGUYEN'
name_3 = "LaTonya Williams"
salary_1 = '82,500'
salary_2 = '74,000'

# Print name variables in lowercase
print(name_1.lower(), name_2.lower(), name_3.lower())

# Print name variables in title case
print(name_1.title(), name_2.title(), name_3.title())

# Print salary variables with commas and $removed and their types
print(salary_1.replace(',', ''), salary_2.replace(',', ''))
print(type(salary_1.replace(',', '')), type(salary_2.replace(',', '')))

# Chain .replace() and int() in a single line
salary_1_int = int(salary_1.replace(',', ''))
salary_2_int = int(salary_2.replace(',', ''))
print(salary_1_int, salary_2_int)
print(type(salary_1_int), type(salary_2_int))