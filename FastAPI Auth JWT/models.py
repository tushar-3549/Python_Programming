
from pydantic import BaseModel, Field, EmailStr

class PostSchema(BaseModel):
    id: int = Field(default=None)
    title: str = Field(default=None)
    content: str = Field(default=None)

    class Config:  
        json_schema_extra = {
            "post_demo": {  
                "title": "this is title",
                "content": "this is content"
            }
        }

class UserSchema(BaseModel):
    fullname: str = Field(default=None)
    email: EmailStr = Field(default=None)
    password: str = Field(default=None)
    
    class Config:
        json_schema_extra = {
            "user_demo": {
                "fullname": "tushar",
                "email": "tushar3549@gmail.com",
                "password": "tushar3549"
            }
        }
        
class UserLoginSchema(BaseModel):
    email: EmailStr = Field(default=None)
    password: str = Field(default=None)
    
    class Config:
        json_schema_extra = {
            "user_demo": {
                "email": "tushar3549@gmail.com",
                "password": "tushar3549"
            }
        }
