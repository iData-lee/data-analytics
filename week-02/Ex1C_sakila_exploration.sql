/*
a) In the actor/column Table the information that is included is: actor Id, First Name, Last Name, and the last update. 
b) In the film/coum Table the information that is included is: film ID, title, description, release year, langauge ID, original language ID, rental duration, rental rate, length, replacement cost, rating, special features, and the last update. 
c) The table to include actor_id and film_id is the film_actor table.
d) In the rental table it provides all information pertaining to the rentals. Date, Inventory Id, Customer Id, the return date of the rental, the staff Id who sold the rental, and the last update of the rental. I would say the information is fairly easy to understand as long as you understand what rows you are looking at, but it is a rather large amount of information to collect. 
e) In the inventory table it provides the Inventory Id, Film Id, Store Id, and the last update. 
f) The rental table contains information about when a movie was rented, including the rental_date and inventory_id. The inventory table connects each rental to a specific film using the inventory_id and film_id columns. Finally, the film table contains the names of the movies in the title column.

SELECT rental_date, inventory_id FROM rental;
SELECT inventory_id, film_id FROM inventory;
SELECT film_id, title FROM film;


*/