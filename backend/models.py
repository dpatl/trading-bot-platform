from sqlalchemy import create_engine, MetaData, Table, Integer, String, \
    Column, DateTime, ForeignKey, Numeric, PrimaryKeyConstraint, UniqueConstraint, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class BotMetadata(Base):
    __tablename__ = "bot_metadata"
    bot_id = Column(Integer, primary_key=True, index=True)
    owner_id = Column(Integer, ForeignKey('users.id'))
    bot_name = Column(String, nullable = False)
    created_date = Column(DateTime(), default = datetime.now, unique=False, nullable = False)
    last_modified_date = Column(DateTime(), default = datetime.now, unique = False, nullable = False, onupdate = datetime.now)
    owner = relationship("User")

    __table_args__ = (
        PrimaryKeyConstraint('bot_id', name='bot_pk')
    )

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer)
    username = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False)    
    password = Column(String(200), nullable=False)
    bots = relationship("BotMetadata")
    
    __table_args__ = (
        PrimaryKeyConstraint('id', name='user_pk'),
        UniqueConstraint('username'),
        UniqueConstraint('email'),
    )