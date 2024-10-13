from app import app
from models import db, Restaurant, Pizza, RestaurantPizza

with app.app_context():
    db.drop_all()
    db.create_all()

    # Create Restaurants
    restaurant1 = Restaurant(name="Karen's Pizza Shack", address="address1")
    restaurant2 = Restaurant(name="Sanjay's Pizza", address="address2")
    restaurant3 = Restaurant(name="Kiki's Pizza", address="address3")

    # Create Pizzas
    pizza1 = Pizza(name="Emma", ingredients="Dough, Tomato Sauce, Cheese")
    pizza2 = Pizza(name="Geri", ingredients="Dough, Tomato Sauce, Cheese, Pepperoni")
    pizza3 = Pizza(name="Melanie", ingredients="Dough, Sauce, Ricotta, Red peppers, Mustard")

    # Add RestaurantPizza associations
    rp1 = RestaurantPizza(price=10, restaurant=restaurant1, pizza=pizza1)
    rp2 = RestaurantPizza(price=15, restaurant=restaurant2, pizza=pizza2)
    rp3 = RestaurantPizza(price=8, restaurant=restaurant3, pizza=pizza3)

    # Add to session and commit
    db.session.add_all([restaurant1, restaurant2, restaurant3, pizza1, pizza2, pizza3, rp1, rp2, rp3])
    db.session.commit()
