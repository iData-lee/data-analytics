# Experiments with the random, math, and statistics modules

import random 
import math 
import statistics 

# Starting variables
vals_1_100 = range(1,100)
vals_sample = random.sample(vals_1_100, 75)
vals_choices = random.choices(vals_1_100, k = 200)
radius = random.randint(3,10)
pi = math.pi 

# Calculations for the 75 value sample
sample_sum = sum(vals_sample)
sample_mean = statistics.mean(vals_sample)
sample_median = statistics.median(vals_sample)

# Calculations for the 200 value set
choices_mean = statistics.mean(vals_choices)
choices_median = statistics.median(vals_choices)
choices_mode = statistics.mode(vals_choices)
choices_stdev = statistics.stdev(vals_choices)
choices_variance = statistics.variance(vals_choices)

# Circle: area = pi * radius squared
area = pi * radius ** 2
area_up = math.ceil(area)   # round up to the next interger
area_down = math.floor(area)   # rounds down to the integer below

#Output
print(f'Experimenting with a subset of intergers 1-100:')
print(f'Sum of 75 sample values from 1 to 100: {sample_sum}')
print(f'Average of 75 sample values: {sample_mean:.2f}')
print(f'Median of 75 sample values: {sample_median}')
print('\n')

print(f'Experimenting with a superset of 200 values, intergers 1-100:')
print(f'Average of 200 values: {choices_mean:.2f}')
print(f'Median of 200 values: {choices_median}')
print(f'Mode of 200 values: {choices_mode}')
print(f'Standard Deviation of 200 values: {choices_stdev:.2f}')
print(f'Variance of 200 values: {choices_variance:.2f}')
print('\n')

print('_Modeling a random circle:')
print(f'Radius = {radius}, area = {area_up} (rounded up to the nearest interger)')
print(f'Radius = {radius}, area = {area_down} (rounded down to the nearest interger)')
