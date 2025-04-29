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

@app.post("/db", response_model=Tarea)
def create_task(
    nueva_tarea: Tarea,
    session: Session = Depends(get_session),
):
    new_task = Tarea(
        nombre=nueva_tarea.nombre,
        descripcion=nueva_tarea.descripcion,
        fecha_creacion=datetime.now(),
        fecha_modificacion=datetime.now(),
        estado=nueva_tarea.estado,
        usuario_id=nueva_tarea.usuario_id,
    )
    session.add(new_task)
    session.commit()
    session.refresh(new_task)
    return new_task

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