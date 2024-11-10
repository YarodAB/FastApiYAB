from fastapi import FastAPI #Importo fastAPI
from pydantic import BaseModel

app = FastAPI() #Llamo al contexto de la libreria a través de una variable

# Entidad user

class User(BaseModel):
    id: int
    name: str
    surname: str
    url: str
    age: int

users_list = [User(id=1,name="Yarod", surname="Aliaga" , url="https//yarod.aliaga", age=23),
              User(id=2,name="Martin", surname="Sepulveda" , url="https//yarod.aliaga", age=27),
              User(id=3,name="Christian", surname="Andrade" , url="https//yarod.aliaga", age=30)]

@app.get("/usersjeson")
async def users():
    return [{"name": "Yaord", "surname": "Aliaga", "url": "https//yarod.aliaga", "age": 23},
            {"name": "Martin", "surname": "Sepulveda", "url": "https//mar.sep", "age": 27},
            {"name": "Christian", "surname": "Andrade", "url": "https//ch.andr", "age": 30}]
    
@app.get("/users")
async def users():
    return users_list

@app.get("/userquery/")
async def user(id: int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return {"error": "Usuario no encontrado"}