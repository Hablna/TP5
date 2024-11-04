from fastapi import FastAPI, Depends
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordBearer

class Item(BaseModel):
    name: str
    description: str | None = None
    priority: int

fake_users_db = {
    "user1": {"username": "user1", "todo_count": 0}
}
fake_todo_db = []
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

app = FastAPI(description="TP5 API")

@app.get("/")
def root():
    return {"message": "Hello World!"}

@app.get("/miscellaneous/addition")
def addition(a: int, b: int):
    return {"result": a + b}

#@app.post("/users")
#def create_user(item: Item):
#    return item

@app.get("/users/me")
def get_user_me(token: str = Depends(oauth2_scheme)):
    # Here you would normally verify the token and get the user information
    # For simplicity, we are skipping that part
    user = fake_users_db["user1"]
    user["todo_count"] = len(fake_todo_db)
    return {"username": user["username"], "todo_count": user["todo_count"]}

@app.post("/users/me/todo")
def create_todo(item: Item):
    return item
