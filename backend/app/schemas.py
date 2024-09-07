from pydantic import BaseModel, EmailStr
from typing import List, Optional

# User schemas
class UserBase(BaseModel):
    username: str
    email: EmailStr

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True

# Token schemas
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None

# ArmyList schemas
class ArmyListBase(BaseModel):
    name: str
    faction: str
    points: int
    list_data: str

class ArmyListCreate(ArmyListBase):
    pass

class ArmyList(ArmyListBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True

# Campaign schemas
class CampaignBase(BaseModel):
    name: str
    description: str

class CampaignCreate(CampaignBase):
    pass

class Campaign(CampaignBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True
