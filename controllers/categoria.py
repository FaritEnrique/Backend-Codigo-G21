from flask_restful import Resource, request
from models import CategoriaModel
from instancias import conexion
from .serializers import CategoriaSerializer
from marshmallow.exceptions import ValidationError


class CategoriaController(Resource):
    def get(self):
        data = conexion.session.query(CategoriaModel).all()
        serializador = CategoriaSerializer()
        resultado = serializador.dump(data, many=True)
        return {
            'message': 'Las categorias son',
            'result': resultado
        }
    
    def post(self):
        data = request.get_json()
        serializador = CategoriaSerializer()
        try:
            data_serializada = serializador.load(data)
            
            nueva_categoria = CategoriaModel(**data_serializada)
            
            conexion.session.add(nueva_categoria)
            
            conexion.session.commit()
            
            resultado = serializador.dump(nueva_categoria)
            
            return {
                'message': 'Categoria creada exitosamente',
                'content': resultado
            }
            
        except ValidationError as error:
            return {
                'message': 'Error al crear categoria',
                'content': error.args
            }

class ManejoCategoriaController(Resource):
    def validarCategoria(self, id):
        categoria_encontrada = conexion.session.query(CategoriaModel).filter(
            CategoriaModel.id == int(id)).first()
        
        return {'message': 'Categoria no existe'} if categoria_encontrada is None else categoria_encontrada
    
    def get(self, id):
        
        categoria_encontrada = self.validarCategoria(id)
        
        if type(categoria_encontrada) == dict:
            return categoria_encontrada

        serializador = CategoriaSerializer()
        
        resultado = serializador.dump(categoria_encontrada)
        
        return {
            'content': resultado
        }

    def put(self, id):
        
        categoria_encontrada = self.validarCategoria(id)
        
        if type(categoria_encontrada) == dict:
            return categoria_encontrada
        
        data = request.get_json()
        serializador = CategoriaSerializer()
        try:
            data_validada = serializador.load(data)
            categoria_encontrada.nombre = data_validada.get('nombre')
            categoria_encontrada.disponibilidad = data_validada.get('disponibilidad') if data_validada.get(
                'disponibilidad') is not None else categoria_encontrada.disponibilidad
            
            conexion.session.commit()
            
            resultado = serializador.dump(categoria_encontrada)
            
            return {
                'message': 'Categoria actualizada exitosamente',
                'content': resultado
            }
            
        except ValidationError as error:
            return {
                'message': 'Error al actualizar categoria',
                'content': error.args
            }

    def delete(self, id):
        categoria_encontrada = self.validarCategoria(id)
        
        if type(categoria_encontrada) == dict:
            return categoria_encontrada
        
        conexion.session.delete(categoria_encontrada)
        
        conexion.session.commit()
        
        return {
            'message': 'Categoria eliminada exitosamente'
        }