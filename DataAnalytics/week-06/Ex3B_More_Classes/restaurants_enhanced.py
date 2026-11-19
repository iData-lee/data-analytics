class Restaurant: 
    '''A restaurant with a name, a type of food, a customer count, and a list of customer ratings.'''

    def __init__(self, rest_name, food_type):
        self.rest_name = rest_name
        self.food_type = food_type
        self.number_served = 0
        self.customer_ratings = []

    def describe_rest(self):
        print(f'{self.rest_name} serves {self.food_type}.')

    def rest_open(self):
        print(f'{self.rest_name} is open.')

    def add_num_served(self):
        amount = int(input('How many customers served today?'))
        self.number_served = self.number_served + amount

    def print_num_served(self):
        print(f'{self.rest_name} has served {self.number_served} customers')

    def customer_rating(self): 
        while True:
            rating = input('How would you rate your experience today on a scale of 1-5 (5 being excellent)?')
            if rating.isdigit() and 1 <= int(rating) <= 5:
                break 
            print('Please enter a whole number from 1 to 5')

        rating = int(rating)
        self.customer_ratings.append(rating)
        average = sum(self.customer_ratings) / len(self.customer_ratings)
        print(f'Your rating was {rating}. The average rating for this restaurant is {average:.1f}')

restaurant_1 = Restaurant('Sumo', 'Hibachi Food')
restaurant_2 = Restaurant('Island Breeze', 'Jamaican Food')
restaurant_3 = Restaurant('Mi Casa', 'Mexican Food') 

# Step 6a Tests customers served
restaurant_1.print_num_served()
restaurant_1.add_num_served()
restaurant_1.add_num_served()
restaurant_1.print_num_served()

restaurant_2.print_num_served()
restaurant_2.add_num_served()
restaurant_2.add_num_served()
restaurant_2.print_num_served()

restaurant_3.print_num_served()
restaurant_3.add_num_served()
restaurant_3.add_num_served()
restaurant_3.print_num_served()

# Step 6b and 6c Tests ratings
restaurant_1.customer_rating()
restaurant_1.customer_rating() 
restaurant_1.customer_rating()

restaurant_2.customer_rating() 
restaurant_2.customer_rating() 

restaurant_3.customer_rating() 
restaurant_3.customer_rating()