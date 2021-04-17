from sqlalchemy import create_engine, MetaData, Table, Integer, String, \
    Column, DateTime, ForeignKey, Numeric, PrimaryKeyConstraint, UniqueConstraint, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from database.database import Base

class BotMetadata(Base):
    __tablename__ = "bot_metadata"
    bot_id = Column(Integer, primary_key=True, index=True)
    owner_id = Column(Integer, ForeignKey('users.id'))
    bot_name = Column(String, nullable = False)
    created_date = Column(DateTime(), default = datetime.now, unique=False, nullable = False)
    last_modified_date = Column(DateTime(), default = datetime.now, unique = False, nullable = False, onupdate = datetime.now)
    owner = relationship("User")

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(100), nullable=False, unique = True)
    email = Column(String(100), nullable=False, unique = True)    
    password = Column(String(200), nullable=False)
    bots = relationship("BotMetadata")

class Role(Base):
    __tablename__ = 'roles'
    id = Column(Integer, primary_key=True,index=True)
    role_name = Column(String, nullable=False, unique=True)

class User_Role(Base):
    __tablename__ = 'user_roles'
    user_id = Column(Integer, primary_key=True, nullable=False)
    role_id = Column(Integer, primary_key=True, nullable=False)