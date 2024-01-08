from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Restaurant, Customer, Review

if __name__ == '__main__':
    engine = create_engine('sqlite:///freebies.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    import ipdb; ipdb.set_trace()
