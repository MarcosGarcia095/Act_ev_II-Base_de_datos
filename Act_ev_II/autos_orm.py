from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Configuración de la base de datos
engine = create_engine('sqlite:///example.db', echo=True)
Base = declarative_base()

# Definición de la clase Auto
class Auto(Base):
    __tablename__ = 'autos'
    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    anio_fabricacion = Column(Integer)

# Crear las tablas
Base.metadata.create_all(engine)

# Crear una sesión
Session = sessionmaker(bind=engine)
session = Session()

# Insertar un nuevo auto
nuevo_auto = Auto(nombre='Toyota Corolla', anio_fabricacion=2020)
session.add(nuevo_auto)
session.commit()

# Consultar autos
autos = session.query(Auto).all()
for auto in autos:
    print(f'Auto: {auto.nombre}, Año: {auto.anio_fabricacion}')

# Eliminar el auto
session.delete(nuevo_auto)
session.commit()

# Verificar si fue eliminado
autos = session.query(Auto).all()
for auto in autos:
    print(f'Auto: {auto.nombre}, Año: {auto.anio_fabricacion}')