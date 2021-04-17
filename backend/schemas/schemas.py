from pydantic import BaseModel


class UserBase(BaseModel):
    username: str


class UserCreate(UserBase):
    email: str
    password: str


class UserAuthenticate(UserBase):
    password: str


class User(UserBase):
    id: int

    class Config:
        orm_mode = True


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str


class BotMetadataBase(BaseModel):
    bot_name: str
    owner_id: int
    created_date: str
    last_modified_date: str


class BotMetadata(BotMetadataBase):
    id: int

    class Config:
        orm_mode = True

class RoleId(BaseModel):
    id: int 

class Role(RoleId):
    role_name: str

    class Config:
        orm_mode = True

class User_Role(BaseModel):
    user_id:int
    role_id:int

    class Config:
        orm_mode = True