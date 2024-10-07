from fastapi import FastAPI, Body, Depends 
from models import PostSchema
from models import PostSchema, UserSchema, UserLoginSchema
from auth.jwt_handler import signJWT
from auth.jwt_bearer import jwtBearer

posts = [
    {
        "id": 1,
        "title": "title number one",
        "text": "text number one"
    },
    {
        "id": 2,
        "title": "title number two",
        "text": "text number two"
    },
    {
        "id": 3,
        "title": "title number three",
        "text": "text number three"
    }
]

users = []

app = FastAPI()
@app.get("/", tags = ["test"])
def home():
    return {"message": "welcome to fastapi authentication"}

@app.get("/posts", tags=["posts"]) 
def get_posts():
    return {"data": posts}
@app.get("/posts/{id}", tags=["posts"])
def get_one_posts(id: int):
    if id > len(posts):
        return {
            "post with this id does not exist."
        }
    for post in posts:
        if post["id"] == id:
            return {
                "data": post
            }
@app.post("/posts", dependencies=[Depends(jwtBearer())] ,tags=["posts"])
def add_post(post: PostSchema):
    post.id = len(posts)+1
    posts.append(post.dict())
    return {
        "info": "post added."
    }
    
@app.post("/user/signup", tags=["user"])
def user_signup(user: UserSchema = Body(default=None)):
    users.append(user)
    return signJWT(user.email)

def check_user(data: UserLoginSchema):
    for user in users:
        if user.email == data.email and user.password == data.password:
            return True
        return False

@app.post("/user/login", tags=["user"])
def user_login(user: UserLoginSchema = Body(default=None)):
    if check_user(user):
        return signJWT(user.email)
    else:
        return {
            "error": "invalid login details"
        }