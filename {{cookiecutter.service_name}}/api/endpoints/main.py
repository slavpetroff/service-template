from fastapi import FastAPI, HTTPException
from schemas import UserCreate, User

app = FastAPI()

# Dummy database
fake_db = []


@app.get("/")
async def read_root():
    return {"message": "Welcome to the Microservice API"}


@app.post("/users", response_model=User, status_code=201)
async def create_user(user: UserCreate):
    user_dict = user.dict()
    user_dict["id"] = len(fake_db) + 1
    fake_db.append(user_dict)
    return user_dict


@app.get("/users/{user_id}", response_model=User)
async def read_user(user_id: int):
    for user in fake_db:
        if user["id"] == user_id:
            return user
    raise HTTPException(status_code=404, detail="User not found")


@app.put("/users/{user_id}", response_model=User)
async def update_user(user_id: int, user: UserCreate):
    for stored_user in fake_db:
        if stored_user["id"] == user_id:
            stored_user.update(user.dict())
            return stored_user
    raise HTTPException(status_code=404, detail="User not found")


@app.delete("/users/{user_id}", status_code=204)
async def delete_user(user_id: int):
    for index, stored_user in enumerate(fake_db):
        if stored_user["id"] == user_id:
            del fake_db[index]
            return
    raise HTTPException(status_code=404, detail="User not found")
