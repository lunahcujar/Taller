from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime
from enum import Enum


# Enumeraciones para los estados
class EstadoTarea(str, Enum):
    pendiente = "Pendiente"
    en_ejecucion = "En ejecución"
    realizada = "Realizada"
    cancelada = "Cancelada"

class EstadoUsuario(str, Enum):
    activo = "Activo"
    inactivo = "Inactivo"
    eliminado = "Eliminado"

# Modelo de Usuario
class Usuario(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    nombre: str
    email: str
    estado: EstadoUsuario
    premium: bool

# Modelo de Tarea
class Tarea(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    nombre: str
    descripcion: str
    fecha_creacion: datetime
    fecha_modificacion: datetime
    estado: EstadoTarea
    usuario_id: int = Field(foreign_key="usuario.id")
