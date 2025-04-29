from sqlmodel import SQLModel, create_engine, Session
from dotenv import load_dotenv
import os

# Cargar las variables de entorno
load_dotenv()

# Configurar la conexión a Clever Cloud
DATABASE_URL = (
    f"postgresql://{os.getenv('CLEVER_USER')}:"
    f"{os.getenv('CLEVER_PASSWORD')}@"
    f"{os.getenv('CLEVER_HOST')}:"
    f"{os.getenv('CLEVER_PORT')}/"
    f"{os.getenv('CLEVER_DATABASE')}"
)

# Crear el motor de base de datos
engine = create_engine(DATABASE_URL, echo=True)

# Inicializar la base de datos
def init_db():
    SQLModel.metadata.create_all(engine)

# Obtener una sesión
def get_session():
    with Session(engine) as session:
        yield session
