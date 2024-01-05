from database import BaseClass
from sqlalchemy import Column, Integer, ForeignKey, Text, String
from sqlalchemy.orm import relationship

class User(BaseClass):

    __tablename__ = 'users'
    id = Column(Integer,primary_key=True)
    username = Column(String(25),unique=True)
    email= Column(String,unique=True)
    password = Column(Text)
    orders= relationship('Order',back_populates='user')




class Order(BaseClass):

    __tablename__='orderdetails'
    id = Column(Integer,primary_key=True)
    quantity = Column(Integer,nullable=False)
    product = Column(String)
    user_id = Column(Integer,ForeignKey('users.id'))
    user = relationship('User',back_populates='orders')