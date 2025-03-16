from sqlalchemy import create_engine, Column, Integer, String, Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Инициализация базы данных
engine = create_engine('sqlite:///calories.db', connect_args={'check_same_thread': False})
Base = declarative_base()

class UserData(Base):
    __tablename__ = 'user_data'
    id = Column(Integer, Sequence('user_data_id_seq'), primary_key=True)
    user_id = Column(Integer)
    food = Column(String(50))
    calories = Column(Integer)

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

def get_user_data(user_id):
    session = Session()
    data = session.query(UserData).filter_by(user_id=user_id).all()
    session.close()
    return data

def clear_user_data(user_id):
    session = Session()
    session.query(UserData).filter_by(user_id=user_id).delete()
    session.commit()
    session.close()

def delete_food_entry(user_id, food):
    session = Session()
    entry = session.query(UserData).filter_by(user_id=user_id, food=food).first()
    if entry:
        session.delete(entry)
        session.commit()
        session.close()
        return True
    session.close()
    return False
