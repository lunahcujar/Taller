# operación lógica
from sqlmodel import Session
from datetime import datetime
from models import Tarea
from db_conection import engine


def agregar_tarea(nombre, descripcion, estado, usuario_id):
    nueva_tarea = Tarea(
        nombre=nombre,
        descripcion=descripcion,
        fecha_creacion=datetime.now(),
        fecha_modificacion=datetime.now(),
        estado=estado,
        usuario_id=usuario_id
    )
    with Session(engine) as session:
        session.add(nueva_tarea)
        session.commit()
        session.refresh(nueva_tarea)
        return nueva_tarea


