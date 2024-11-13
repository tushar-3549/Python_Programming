# Day: 01
'''
from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
  name: str
  price: int
  is_offer: Union[bool, None] = None


class ItemUpdate(BaseModel):
  name: Union[str, None] = None
  price: Union[int, None] = None
  is_offer: Union[bool, None] = None


@app.get('/')
def home():
  return {"message": "Hello World"}


@app.get('/items/{item_id}')
def read_item(item_id: int, q: Union[str, None] = None):
  return {"item_id": item_id, "q": q}


@app.post('/items')
def create_item(item: Item):
  return {
      "item_name": item.name,
      "item_price": item.price,
      "is_offer": item.is_offer
  }


@app.put('/items/{item_id}')
# def update_item(item_id: int, v: str):
#   return {"item_id": item_id, "v": v}
def update_item(item_id: int, item: Item):
  return {"item_id": item_id, "item_name": item.name, "item_price": item.price}


@app.delete('/items/{item_id}')
def delete_item(item_id: int):
  return {"message": f"Item with id {item_id} has been deleted"}


@app.patch('/items/{item_id}')
def patch_item(item_id: int, item_update: ItemUpdate):
  return {
      "item_id": item_id,
      "updated_fields": item_update.dict(exclude_unset=True)
  }
'''

# Day: 02
'''
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()


class Student(BaseModel):
  name: str
  dept: str
  varsity: str


STUDENTS = [{
    "id": 1,
    "name": "tushar",
    "dept": "cse",
    "varsity": "diu"
}, {
    "id": 2,
    "name": "sakib",
    "dept": "eee",
    "varsity": "aiub"
}, {
    "id": 3,
    "name": "tamim",
    "dept": "bba",
    "varsity": "nsu"
}]


@app.get('/')
def root():
  return {"message": "Welcome to our API"}


@app.get('/students/')
async def read_students(varsity: Optional[str] = None,
                        dept: Optional[str] = None):
  std_to_return = []
  for std in STUDENTS:
    if dept and std.get('dept').casefold() != dept.casefold():
      continue
    if varsity and std.get('varsity').casefold() != varsity.casefold():
      continue
    std_to_return.append(std)
    return std_to_return


@app.get('/students/{id}')
async def read_student(id: int):
  for std in STUDENTS:
    if std.get('id') == id:
      return std
  raise HTTPException(status_code=404, detail="Student not found")


@app.post('/students/')
async def create_student(student: Student):
  new_id = max(std['id'] for std in STUDENTS) + 1
  new_student = {"id": new_id, **student.dict()}
  STUDENTS.append(new_student)
  return new_student


@app.put('/students/{id}')
async def update_student(id: int, student: Student):
  for i, std in enumerate(STUDENTS):
    if std.get('id') == id:
      STUDENTS[i] = {**std, **student.dict()}
      return STUDENTS[i]
  raise HTTPException(status_code=404, detail="Student not found")


@app.delete('/students/{id}')
async def delete_student(id: int):
  for i, std in enumerate(STUDENTS):
    if std.get('id') == id:
      STUDENTS.pop(i)
      return {"message": "Student deleted successfully"}

'''

# Day : 03

from fastapi import FastAPI, HTTPException, Response
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Student(BaseModel):
    id: int
    name: str
    dept: str
    course: Optional[str]

my_students = [
    {
        "id": 1,
        "name": "tushar",
        "dept": "cse",
        "course": "python"
    },
    {
        "id": 2,
        "name": "hemal",
        "dept": "swe",
        "course": "basic programming"
    }
]

def find_post(id):
    for p in my_students:
        if p['id'] == id:
            return p

def find_index(id):
    for i, str in enumerate(my_students):
        if str['id'] == id:
            return i

@app.get("/")
def root():
    return {"message": "Welcome to my API"}

@app.get("/students")
def get_students():
    return my_students

@app.get('/students/{id}')
def read_student(id: int):
    for std in my_students:
        if std.get('id') == id:
            return std
    raise HTTPException(status_code=404, detail="student not found")

@app.post("/posts")
def create_posts(post: Student):
    post_dict = post.dict()
    my_students.append(post_dict)
    # print(post_dict)
    return post_dict

@app.get("/posts/latest")
def get_latest_post():
    post = my_students[len(my_students)-1]
    return {"last_data": post}

@app.get("/posts/{id}")
def get_posts(id: int, response : Response):
    # print(id)
    # print(type(id))
    post = find_post(int(id))
    # print(post)
    if not post:
        response.status_code = 404
    return {"post_detail": post}

@app.delete("/delete/{id}")
def delete_student(id: int):
    for i, std in enumerate(my_students):
        if std.get('id') == id:
            my_students.pop(i)
            return {"message": "student deleted successfully"}
    

@app.put("/posts/{id}")
def update_post(id: int, post: Student):
    ind = find_index(id)
    post_dict = post.dict()
    post_dict['id'] = id 
    my_students[ind] = post_dict
    
    # return {"message": "student updated successfully"}
    return {"data": post_dict}

