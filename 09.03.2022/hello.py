from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker



engine = create_engine("sqlite:///sql/testssss.db", echo=True)
Base = declarative_base()


class Person(Base):
    __tablename__ = 'person'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    lastname = Column(String)
    age = Column(Integer)
    pet = Column(String)
    
    def __init__(self, name, lastname, age , pet):
        self.name = name
        self.lastname = lastname
        self.age = age
        self.pet = pet
        Base.metadata.create_all(engine)


Session = sessionmaker(bind=engine)
session = Session()
session.add(Person('Alex', 'Varkalov', 15, 'dog'))
session.commit()


result = session.query(Person).filter(Person.name == 'Alex', Person.age<25)
result2 = session.query(Person).filter(Person.age>14, Person.age<19)

for i in result2:
    print('ID:', i.id, 'name:', i.name, 'lastname:', i.lastname, 'age:', i.age, 'pet:', i.pet)