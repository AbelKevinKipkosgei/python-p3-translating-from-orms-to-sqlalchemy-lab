from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Dog

def create_table(base, engine = None):
    if engine is None:
        engine = create_engine("sqlite:///:memory:")
    base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    return session

def save(session, dog):
    session.add(dog)
    session.commit()

def get_all(session):
    return [dog for dog in session.query(Dog).all()]

def find_by_name(session, name):
    return session.query(Dog).filter(Dog.name == name).first()

def find_by_id(session, id):
    return session.query(Dog).filter(Dog.id == id).first()

def find_by_name_and_breed(session, name, breed):
    return session.query(Dog).filter(Dog.name == name, Dog.breed == breed).first()

def update_breed(session, dog, breed):
    dog.breed = breed
    session.commit()

#function calls
if __name__ == "__main__":
    session = create_table(Base)

    dog1 = Dog(
        name = "Joey",
        breed = "Labrador Retriever"
    )

    save(session, dog1)
    find_by_name(session, "Joey")
    find_by_id(session, 1)
    find_by_name_and_breed(session, "Milan", "Beagle")
    update_breed(session, dog1, "Beagle")
