from models import User, Order
from database import engine, BaseClass


BaseClass.metadata.create_all(bind=engine)