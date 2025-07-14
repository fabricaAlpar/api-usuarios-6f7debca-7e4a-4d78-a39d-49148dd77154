from typing import List
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    id: int
    name: str
    email: str
    password: str

users = []

@app.get("/users", response_model=List[User])
def read_users():
    """Return a list of all users"""
    return users

@app.get("/users/{user_id}", response_model=User)
def read_user(user_id: int):
    """Return a single user by id"""
    for user in users:
        if user.id == user_id:
            return user
    raise HTTPException(status_code=404, detail="User not found")

@app.post("/users", response_model=User)
def create_user(user: User):
    """Create a new user"""
    user.id = len(users) + 1
    users.append(user)
    return user

@app.put("/users/{user_id}", response_model=User)
def update_user(user_id: int, user: User):
    """Update an existing user"""
    for index, existing_user in enumerate(users):
        if existing_user.id == user_id:
            users[index] = user
            return user
    raise HTTPException(status_code=404, detail="User not found")

@app.delete("/users/{user_id}", response_model=User)
def delete_user(user_id: int):
    """Delete a user"""
    for index, existing_user in enumerate(users):
        if existing_user.id == user_id:
            removed_user = users.pop(index)
            return removed_user
    raise HTTPException(status_code=404, detail="User not found")