

from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship


engine = create_engine("sqlite:///sql/testssss.db", echo=True)
Base = declarative_base()


class Group(Base):
    __tablename__ = 'person'
    id = Column(Integer, primary_key=True)
    name = Column(String)



class Student(Base):
    __tablename__ = 'student'
    id = Column(Integer, primary_key=True)
    firstname = Column(String)
    lastname = Column(String)
    group_id = Column(Integer, ForeignKey('person.id'), nullable=False)
    group = relationship('Group', foreign_keys='Student.group_id', backref='albums')
    
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

gr = Group(name='Z65')
st = Student(firstname = 'maxim', lastname = 'Kh', group = gr)
session.add_all([gr, st])
session.commit()


