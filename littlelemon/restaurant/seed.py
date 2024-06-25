from faker import Faker
import random
from .models import *


def seed_df(n=10):

    """
    Generates and saves a specified number of Menu objects with random titles, prices, and inventory.

    Args:
        n (int): The number of Menu objects to generate and save.

    Returns:
        None
    """

    fake = Faker()

    food_names = [
        'Spaghetti Carbonara', 'Margherita Pizza', 'Caesar Salad', 'Chicken Alfredo',
        'Beef Tacos', 'Grilled Cheese Sandwich', 'Chicken Noodle Soup', 'Veggie Burger',
        'Lemon Chicken', 'Fish and Chips', 'Beef Stroganoff', 'Chicken Parmesan',
        'Shrimp Scampi', 'BBQ Ribs', 'Eggplant Parmesan', 'Turkey Sandwich',
        'French Onion Soup', 'Pulled Pork Sandwich', 'Buffalo Wings', 'Garlic Bread',
        'Pancakes', 'Waffles', 'French Toast', 'Omelette', 'Quiche Lorraine',
        'Banana Split', 'Chocolate Cake', 'Cheesecake', 'Apple Pie', 'Brownies'
    ]

    menu_items = [
        Menu(
            title=random.choice(food_names), 
            price=round(random.uniform(5.00, 100.00), 2),  
            inventory=random.randint(1, 100)
        )
        for _ in range(n)
    ]
    Menu.objects.bulk_create(menu_items)
