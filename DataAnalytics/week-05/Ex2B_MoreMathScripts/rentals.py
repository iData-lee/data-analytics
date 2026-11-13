# X people on a tour
# Charter vans seat 15 passengers each
# Van cost $250 per day (including driver's pay)
# 38 tourist 

import math

tourists = 38 
van_cap = 15
van_cost = 250

vans = math.ceil(tourists / van_cap) # round up so there are no partial vans
total_cost = vans * van_cost
per_person = total_cost / tourists

print(f'Number of vans needed are {vans} vans.')
print(f'The total rental cost is ${total_cost:.2f}.')
print(f'The cost split per person is ${per_person:.2f}.')