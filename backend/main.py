import uvicorn
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jwt import PyJWTError
from sqlalchemy.orm import Session
from fastapi import Depends, FastAPI, HTTPException
from starlette import status
import models.models as models
import schemas.schemas as schemas
import crud.crud as crud
from utils.utils import decode_access_token
from crud.crud import get_user_by_username
from database.database import engine, SessionLocal
from schemas.schemas import User, TokenData
from datetime import timedelta
from utils.utils import create_access_token
from models.enums import Roles
from typing import List

models.Base.metadata.create_all(bind=engine)

ACCESS_TOKEN_EXPIRE_MINUTES = 30

app = FastAPI()


def get_db():
    db = None
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/authenticate")


async def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = decode_access_token(data=token)
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except PyJWTError as jwterr:
        print(jwterr)
        raise credentials_exception
    user = get_user_by_username(db, username=token_data.username)
    if user is None:
        raise credentials_exception
    return user


def check_user_has_permissions(db: Session, user: schemas.User, roleIds: List[Roles]):
    if (not (crud.check_user_roles(db=db, user=user, roleIds=roleIds))):
            raise HTTPException(status_code=403, detail="Forbidden")
    return True

def check_user_has_permissions_or_same_user(db: Session, user: schemas.User, roleIds: List[Roles], user_id: int):
    if (not (user.id != user_id or crud.check_user_roles(db=db, user=user, roleIds=roleIds))):
            raise HTTPException(status_code=403, detail="Forbidden")
    return True

@app.get("/")
def healthcheck():
    return "im alive"
    
@app.get("/users")
def get_users(db: Session = Depends(get_db)):
    db_users = crud.get_users(db)
    return db_users


@app.post("/user", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_username(db, username=user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    return crud.create_user(db=db, user=user)


@app.post("/authenticate", response_model=schemas.Token)
def authenticate_user(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = schemas.UserAuthenticate(username=form_data.username, password=form_data.password)
    db_user = crud.get_user_by_username(db, username=user.username)
    if db_user is None:
        raise HTTPException(status_code=400, detail="Username does not exist")
    else:
        is_password_correct = crud.check_username_password(db, user)
        if is_password_correct is False:
            raise HTTPException(status_code=401, detail="Password is incorrect")
        else:
            access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
            access_token = create_access_token(
                data={"sub": user.username}, expires_delta=access_token_expires)
            return {"access_token": access_token, "token_type": "Bearer"}


@app.post("/bot", response_model=schemas.BotMetadata)
async def create_new_bot(bot: schemas.BotMetadataBase, current_user: User = Depends(get_current_user)
                          , db: Session = Depends(get_db)):
    return crud.create_new_bot(db=db, bot=bot)


@app.get("/bots")
async def get_all_bots(current_user: User = Depends(get_current_user)
                        , db: Session = Depends(get_db)):

    check_user_has_permissions(db=db, user=current_user, roleIds=[Roles.ADMIN,Roles.DEVELOPER,Roles.TEST])                
    return crud.get_all_bots(db=db)


@app.get("/bots/{bot_id}")
async def get_bot_by_id(bot_id, current_user: User = Depends(get_current_user)
                         , db: Session = Depends(get_db)):
    return crud.get_bot_by_id(db=db, bot_id=bot_id)

@app.get("/bots/byUser/{user_id}")
async def get_bots_by_user_id(user_id, current_user: User = Depends(get_current_user)
                         , db: Session = Depends(get_db)):
    

    return crud.get_bots_by_user_id(db=db, user_id=user_id)  


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)