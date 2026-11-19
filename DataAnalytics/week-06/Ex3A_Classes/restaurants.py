class Restaurant: 
    '''A restaurant with a name and a type of food.'''

    def __init__(self, rest_name, food_type):
        self.rest_name = rest_name
        self.food_type = food_type

    def describe_rest(self):
        print(f'{self.rest_name} serves {self.food_type}.')

    def rest_open(self):
        print(f'{self.rest_name} is open.')

restaurant_1 = Restaurant('Sumo', 'Hibachi Food')
restaurant_2 = Restaurant('Island Breeze', 'Jamaican Food')
restaurant_3 = Restaurant('Mi Casa', 'Mexican Food') 

restaurant_1.describe_rest()
restaurant_1.rest_open()

restaurant_2.describe_rest()
restaurant_2.rest_open()

restaurant_3.describe_rest()
restaurant_3.rest_open()

