# favorite movies list
fav_films = ["The Matrix", "The Godfather", "The Conjuring", "Pulp Fiction", "Forrest Gump", "Grave of the Fireflies", "Wall-E", "Coco", "Joker", "The Truman Show"]

print(len(fav_films))

print(f'The list includes my top {len(fav_films)} favorite films')

print(sorted(fav_films)) # This sorts the films in alphabetical order
print(fav_films) # This keeps the films in the format I orginally implemented

fav_films.sort() # change the list around itself
print(fav_films) # it is now permanently sorted

# Add at least one more film
fav_films.append("Up")
print(fav_films)
