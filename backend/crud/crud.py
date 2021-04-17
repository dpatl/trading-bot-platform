from sqlalchemy.orm import Session
import models.models as models, schemas.schemas as schemas
from typing import List
from models.enums import Roles
import bcrypt

def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()

def get_users(db: Session):
    return db.query(models.User).all()

def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = bcrypt.hashpw(user.password.encode('utf-8'), bcrypt.gensalt())
    db_user = models.User(username=user.username, password=hashed_password, email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def check_username_password(db: Session, user: schemas.UserAuthenticate):
    db_user: models.User = get_user_by_username(db, username=user.username)
    return bcrypt.checkpw(user.password.encode('utf-8'), db_user.password.encode('utf-8'))


def check_user_roles(db: Session, user: schemas.User, roleIds: List[Roles]):
    db_user: models.User = get_user_by_username(db, username=user.username)
    return db.query(models.User_Role).filter(models.User_Role.user_id == db_user.id, models.User_Role.role_id in roleIds).first() is not None



def create_new_bot(db: Session, bot: schemas.BotMetadataBase):
    db_bot = models.BotMetadata(owner_id=bot.owner_id, bot_name=bot.bot_name)
    db.add(db_bot)
    db.commit()
    db.refresh(db_bot)
    return db_bot


def get_all_bots(db: Session):
    return db.query(models.BotMetadata).all()

def get_bot_by_id(db: Session, bot_id: int):
    return db.query(models.BotMetadata).filter(models.BotMetadata.id == bot_id).first()

def get_bots_by_user_id(db: Session, user_id: int):
    return db.query(models.BotMetadata).filter(models.BotMetadata.owner_id == user_id).all()