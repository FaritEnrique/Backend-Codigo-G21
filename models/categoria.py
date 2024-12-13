from instancias import conexion
from sqlalchemy import Column, types
from datetime import datetime

class CategoriaModel(conexion.Model):
    id = Column(type_=types.Integer, autoincrement=True,
                primary_key=True, nullable=False)
    nombre=Column(type_=types.Text, nullable=False)
    fechaCreacion=Column(name='fecha_creacion', type_=types.TIMESTAMP,
                         default=datetime.now)
    disponibilidad=Column(type_=types.Boolean, default=True)
    __tablename__ = 'categorias'
    __bind_key__ = 'postgres'