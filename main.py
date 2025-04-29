from fastapi import FastAPI, APIRouter
from sqlalchemy.orm import sessionmaker

import models
from models import *
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Annotated
from sqlmodel import Session
from operations import *
from db_conection import *
from fastapi import FastAPI, Depends
from db_conection import get_session, init_db
from enum import Enum

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


from db_conection import get_session

@app.post("/Agregar_Tarea", response_model=Tarea)
def Add_tarea(tarea: Tarea):
    nueva_tarea = agregar_tarea(
        nombre=tarea.nombre,
        descripcion=tarea.descripcion,
        estado=tarea.estado,
        usuario_id=tarea.usuario_id
    )
    return nueva_tarea

@app.on_event("startup")
def on_startup():
    init_db()

@app.post("/usuarios", response_model=Usuario)
def create_user(
    nuevo_usuario: Usuario,
    session: Session = Depends(get_session),
):
    user = Usuario(
        nombre=nuevo_usuario.nombre,
        email=nuevo_usuario.email,
        estado=nuevo_usuario.estado,
        premium=nuevo_usuario.premium
    )
    session.add(user)
    session.commit()
    session.refresh(user)
    return user