f = open('about_me.txt', 'r')
#f.close()

#f = open('about_me.txt', 'a')
#f.write('\nPerfect night out: dinner at my favorite spot, then live music.\n')
#f.close 

#f = open('about_me.txt', 'r')
#print(f.read(50))
#print(f.read(50))
#f.close

first_50 = f.read(50)

four_lines = []
for i in range(1, 5):
    four_lines.append(f.readline())

next_lines = f.readlines(100)

print(f'First 50 Characters: {first_50}')
print(f'Next four lines, as list by line: {four_lines}')
print(f'Next 100 characters, as list by line, rounded up to complete lines:{next_lines}')

f.close()