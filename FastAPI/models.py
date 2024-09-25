from uuid import uuid4, UUID
from pydantic import BaseModel
from typing import Optional, List
from enum import Enum

class Gender(str, Enum):
    male = "male"
    female = "female"
class Role(str, Enum):
    admin = "admin"
    user = "user"
    student = "student"
class User(BaseModel):
    id: Optional[UUID] = uuid4()
    f_name: str 
    l_name: str 
    m_name: Optional[str]
    gender: Gender
    roles: List[Role]
class UserUpdate(BaseModel):
    f_name: Optional[str] = None
    l_name: Optional[str] = None
    m_name: Optional[str] = None
    gender: Optional[Gender] = None
    roles: Optional[List[Role]] = None

    