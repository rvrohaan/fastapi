from sqlalchemy import Column, Integer, String
import database

class Blog(database.base):
    __tablename__ = 'blogs'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    body = Column(String)