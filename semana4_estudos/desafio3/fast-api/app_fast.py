from fastapi import FastAPI, HTTPException
from uuid import UUID
from typing import List
from models import User, Role

app = FastAPI()

db: List[User] = [
    User(
      id=UUID("56b4ede7-e8ac-43ed-b176-bea60ebd2f43"),
      first_name="Nathalia", 
      last_name="Andrade", 
      email="nath@andrade.com.br", 
      role=[Role.role_1]
    ),
    User(
      id=UUID("6f3282e3-e0cc-41cb-bcc8-2ea16b7fe226"),
      first_name="Juliana", 
      last_name="Almeida", 
      email="ju@almeida.com.br", 
      role=[Role.role_2]
    ),
        User(
      id=UUID("3aa1a3f5-9d36-43a5-9e46-2e266aabc58c"),
      first_name="Zelita", 
      last_name="Camargo", 
      email="zelita@camargo.com.br", 
      role=[Role.role_3]
    )
]

@app.get("/")
async def root():
    return {"message": "Olá Terráqueos!!"}

@app.get("/api/users")
async def get_users():
    return db

@app.get("/api/users/{id}")
async def get_user(id: UUID):
    for user in db:
      if user.id == id:
        return user
    return {"message": "Ops! Usuário não encontrado"}    

@app.post("/api/users")
async def add_user(user: User):
    """
    Adiciona um usuário na base de dados:
    - **id**: UUID
    - **first_name**: string
    - **last_name**: string
    - **email**: string
    - **role**: Role
    """
    db.append(user)
    return {"id": user.id}


@app.put("/api/users/{id}")
async def update_user(id:UUID, updated_user:User):
  for user in db:
    if user.id == id:
        user.first_name = updated_user.first_name
        user.last_name = updated_user.last_name
        user.email = updated_user.email
        user.role = updated_user.role
        return {"Usuário atualizado com sucesso, id": user.id} 
  raise HTTPException(
    status_code=404,
    detail=f"Usuário com o id {id} não encontrado"
  )  


@app.delete("/api/users/{id}")
async def remove_user(id: UUID):  
    for user in db:
      if user.id == id:
        db.remove(user)
        return 
    raise HTTPException(
        status_code=404,
        detail=f"Usuário com o id {id} não encontrado"
    )    
