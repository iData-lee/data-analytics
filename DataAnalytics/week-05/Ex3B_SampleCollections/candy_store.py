candies = ('Starburst', 'Airheads', 'Skittles')
flavors = ('Mango', 'Pineapple', 'Lime')

combo = set()
combo.add(f'{candies[0]} {flavors[1]}')
combo.add(f'{candies[1]} {flavors[2]}')
combo.add(f'{candies[2]} {flavors[0]}')
print("Today's candy options include, ", combo) # The order continues to change throughout the created tuples.
