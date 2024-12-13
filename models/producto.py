from instancias import conexion
from sqlalchemy import Column, types, ForeignKey
from datetime import datetime

class ProductoModel(conexion.Model):
    id = Column(type_=types.Integer, autoincrement=True,
                primary_key=True, nullable=False)
    nombre=Column(type_=types.Text, nullable=False)
    descripcion=Column(type_=types.Text, nullable=True)
    precio=Column(type_=types.Float, nullable=False)
    disponibilidad=Column(type_=types.Boolean, default=True)
    
    categoriaId=Column(ForeignKey(column='categorias.id'), type_=types.Integer, nullable=False)
    
    __tablename__ = 'productos'
    __bind_key__ = 'postgres'