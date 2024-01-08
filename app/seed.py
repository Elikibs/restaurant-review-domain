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

    fake = Faker()

    restaurants = []
    for i in range(50):
        restaurant = Restaurant(
            name = fake.unique.name(),
            price = random.random(100, 500),
        )
        # add and commit to session, individually to get their IDs back
        session.add(restaurant)
        session.commit()

        restaurants.append(restaurant)

    customers = []
    for i in range(25):
        customer = Customer(
            first_name = fake.name(),
            second_name = fake.name(),
        )
        # add and commit to session, individually to get their IDs back
        session.add(customer)
        session.commit()

        customers.append(customer)
    
    reviews = []
    for restaurant in restaurants:
        for i in range(random.randint(1,3)):
            review = Review(
                rating = random.randint(1, 5),
                comment = fake.sentence()
            )

            reviews.append(review)

    session.bulk_save_objects(reviews)
    session.commit()
    session.close()
