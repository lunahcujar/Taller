from sqlmodel import SQLModel, create_engine, Session
from dotenv import load_dotenv

DATABASE_URL = "sqlite:///database.db"

engine = create_engine(DATABASE_URL, echo=True)

# Inicializar la base de datos
def init_db():
    SQLModel.metadata.create_all(engine)

# Obtener una sesión
def get_session():
    with Session(engine) as session:
        yield session
