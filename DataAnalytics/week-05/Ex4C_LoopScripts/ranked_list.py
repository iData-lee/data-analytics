favs = ['Sushi', 'Rollerskating', 'Painting', 'Music', 'Dancing']

for number, fav in enumerate(favs, start=1):
    if number == 1:
        print(f'{number}. {fav} <- top pick!')
    else: 
        print(f'{number}. {fav}') 


for number, fav in enumerate(reversed(favs), start=1): # Bonus question
    if number == 1:
        print(f'{number}. {fav} <- top pick!')
    else: 
        print(f'{number}. {fav}')