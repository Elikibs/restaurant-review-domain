from faker import Faker 
from datetime import datetime
import random

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Restaurant, Review, Customer

if __name__== "__main__":
    engine = create_engine('sqlite:///restaurants.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    session.query(Restaurant).delete()
    session.query(Review).delete()
    session.query(Customer).delete()

    fake = Faker()

    restaurants = []
    for i in range(50):
        restaurant = Restaurant(
            name = fake.company(),
            price = random.randint(100, 500),
        )
        # add and commit to session, individually to get their IDs back
        session.add(restaurant)
        session.commit()

        restaurants.append(restaurant)

    customers = []
    for i in range(25):
        customer = Customer(
            first_name = fake.first_name(),
            second_name = fake.last_name(),
        )
        # add and commit to session, individually to get their IDs back
        session.add(customer)
        session.commit()

        customers.append(customer)
    
    reviews = []
    for restaurant in restaurants:
        for i in range(random.randint(1,3)):
            customer = random.choice(customers)
            if restaurant not in customer.restaurants:
                customer.restaurants.append(restaurant)
                session.add(customer)
                session.commit()

            review = Review(
                rating = random.randint(1, 5),
                comment = fake.sentence(),
                restaurant_id = restaurant.id,
                customer_id = customer.id,
            )

            reviews.append(review)

    session.bulk_save_objects(reviews)
    session.commit()
    session.close()
