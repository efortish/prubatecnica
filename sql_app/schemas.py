from datetime import date

from pydantic import BaseModel





class ProfileBase(BaseModel):
    id:int
    name: str 
    address:str
    user_id:int


class HospitalProfile(ProfileBase):
    medical_services: str
    
    class Config:
        orm_mode = True
    

class PatientProfile(ProfileBase):
    date_of_birth: date
    
    class Config:
        orm_mode = True




class UserBase(BaseModel):
    email:str
    phone_number:str
    profile:str
    
    class Config:
        orm_mode = True

class UserCreate(UserBase):
    password:str

class LoginUser(BaseModel):
    email:str
    password:str


class User(UserBase):
    id:int

    
    class Config:
        orm_mode = True



class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None

    