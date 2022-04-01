class EIT():
    firstName = ''
    lastName = ''
    emailAddress = ''
    phoneNumber = ''
    allergies = []
    preferences = []

class Meal():
    name = ''
    description = ''
    serving_size = ''
    allergens = []
    

class Order(EIT, Meal):
    orderDate = ''
    eitEmail = EIT.emailAddress
    meal = Meal.name
    isTakeaway = False

class Menu(Meal):
    menu_items = []
    day_of_the_week = ''
    meal_time = ''
