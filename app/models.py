from sqlalchemy import ForeignKey, Column, Integer, String, MetaData, Table, DateTime
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}
metadata = MetaData(naming_convention=convention)

Base = declarative_base(metadata=metadata)

# restaurant_customer (many-many) relationship
restaurant_customer = Table(
    'restaurant_customers',
    Base.metadata,
    Column('restaurant_id', ForeignKey('restaurants.id'), primary_key=True),
    Column('customer_id', ForeignKey('customers.id'), primary_key=True),
    extend_existing=True

)

class Restaurant(Base):
    # defining table name
    __tablename__='restaurants'

    # defining restaurants table attributes
    id = Column(Integer(), primary_key=True)
    name = Column(String())
    price = Column(Integer())

    # defining restaurant-review relationship
    reviews = relationship('Review', backref=backref('restaurants'))
    # defining restaurant-customer relationship
    customers = relationship('Customer', secondary=restaurant_customer, back_populates='restaurants')

    # customizing the '__repr__() method to return a human readable output
    def __repr__(self):
        return f"Restaurant(id={self.id}," + \
            f"name={self.name}, " + \
            f"price={self.price})"


class Customer(Base):
    # defining table name
    __tablename__='customers'

    # defining customers table attributes
    id = Column(Integer(), primary_key=True)
    first_name = Column(String())
    second_name = Column(String())

    # defining customer-review relationship
    reviews = relationship('Review', backref=backref('customers'))
    # defining restaurant-customer relationship
    restaurants = relationship('Restaurant', secondary=restaurant_customer, back_populates='customers')

     # customizing the '__repr__() method to return a human readable output
    def __repr__(self) -> str:
        return f"Customer(id={self.id}, " + \
            f"first_name={self.first_name}, " + \
            f"second_name={self.second_name})"


class Review(Base):
    # defining table name
    __tablename__='reviews'

    # defining reviews table attributes
    id = Column(Integer(), primary_key=True)
    rating = Column(Integer())
    comment = Column(Integer())

    restaurant_id = Column(Integer(), ForeignKey('restaurants.id'))
    customer_id = Column(Integer(), ForeignKey('customers.id'))

    # customizing the '__repr__() method to return a human readable output
    def __repr__(self) -> str:
        return f"Review(id={self.id}, " + \
            f"rating={self.rating}, " + \
            f"comment={self.comment})"

