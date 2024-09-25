from fastapi import FastAPI, HTTPException
from models import User, Gender, Role, UserUpdate
from typing import Optional, List
from uuid import uuid4, UUID
app = FastAPI()

db: List[User] = [
    User(
        # id=uuid4(),
        id= "db996432-a35f-4168-b423-cca0f33ad869",
        f_name="Tushar",
        m_name = "",
        l_name="Ahmed",
        gender=Gender.male,  
        roles=[Role.student]
    ),
    User(
        # id=uuid4(),
        id= "16fba926-330a-4075-b1b3-ca8e2bc8ce03",
        f_name="Sakib",
        m_name="",
        l_name="Al Hasan",
        gender=Gender.male,  
        roles=[Role.user, Role.admin]
    )
]


@app.get("/")
def root():
    return {"message": "welcome to our API"}

@app.get("/api/v1/users")
async def fetch_users():
    return db

'''
@app.post("/api/v1/users")
async def register_users(user: User):
    db.append(user)
    # return {"id": user.id}
'''
@app.post("/api/v1/users", response_model=User)
async def register_users(user: User):
    if not user.id:
        user.id = str(uuid4())  
    db.append(user)
    return user 
@app.delete("/api/v1/users/{u_id}")
async def delete_user(u_id: UUID):
    for user in db:
        if user.id == u_id:
            db.remove(user)
            return
        raise HTTPException (
            status_code = 404,
            detail = f"User with id: {u_id} does not Exist."
        )

@app.put("/api/v1/users/{u_id}")
async def update_user(user_update: UserUpdate, u_id: UUID):
    for user in db:
        if user.id == u_id:
            if user_update.f_name is not None:
                user.f_name = user_update.f_name
            if user_update.l_name is not None:
                user.l_name = user_update.l_name
            if user_update.m_name is not None:
                user.m_name = user_update.m_name
            if user_update.gender is not None:
                user.gender = user_update.gender
            if user_update.roles is not None:
                user.roles = user_update.roles
            return user  
    raise HTTPException(
        status_code=404,
        detail=f"User with id: {u_id} does not exist."
    )

        
