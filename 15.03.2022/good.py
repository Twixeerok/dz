

from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship


engine = create_engine("sqlite:///sql/testsssas.db", echo=True)
Base = declarative_base()


class Student(Base):
    __tablename__ = 'student'
    id = Column(Integer, primary_key=True)
    student = Column(String)
    ball = Column(Integer)



class Diary(Base):    
    __tablename__ = 'diary'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    student_id = Column(Integer, ForeignKey('student.id'), nullable=False)
    student = relationship('Student', foreign_keys='Diary.student_id', uselist=False, backref='student')
    
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()


st = Student(name = 'maxim', ball = 5)
diary = Diary(name='one', student = st)
session.add_all([diary, st])
session.commit()


