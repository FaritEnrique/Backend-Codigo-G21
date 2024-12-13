from instancias import conexion
from sqlalchemy import Column, types

class PruebaModel(conexion.Model):
    id = Column(type_=types.Integer, autoincrement=True,
                primary_key=True)
    nombre=Column(type_=types.Text)
    descripcion=Column(type_=types.Text, nullable=True)
        
    __tablename__ = 'pruebas'