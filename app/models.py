from sqlalchemy import ForeignKey, Column, Integer, String, MetaData, Table, DateTime
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}
metadata = MetaData(naming_convention=convention)

Base = declarative_base(metadata=metadata)

class Restaurant(Base):
    # defining table name
    __tablename__='restaurants'

    # defining table attributes
    id = Column(Integer(), primary_key=True)
    name = Column(String())
    price = Column(Integer())

    # customizing the '__repr__() method to return a human readable output
    def __repr__(self):
        return f"Restaurant(id={self.id}," + \
            f"name={self.name}, " + \
            f"price={self.price})"