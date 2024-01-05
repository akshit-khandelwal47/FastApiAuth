from pydantic import BaseModel
from typing import Optional


class SignUpModel(BaseModel):
    id:Optional[int] =None
    username: str
    email: str
    password: str

    class Config:
        from_attributes= True
        json_schema_extra = {
            'example':{
                "username":"string",
                "email":"string",
                "password": "string"
            }
        }


class Settings(BaseModel):
    secret_key: str='7c3a5bd62aadf4058429328a0ef5fe1a4c4cff5eba5dce71f5e8e2502e5642cc'

class LoginModel(BaseModel):
    username:str
    password:str


class OrderModel(BaseModel):
    quantity:int
    product:str

    class Config:
        from_attributes = True
        json_schema_extra={
            'example':{
                "quantity":"integer",
                "product":"string"

            }
        }


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None

