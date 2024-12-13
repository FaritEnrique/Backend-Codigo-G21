from flask_restful import Resource, request
from instancias import conexion
from models import Categoria
from .serializers import CategoriaSerializer
from marshmallow.exceptions import ValidationError


class CategoriasController(Resource):
    serilizador = CategoriaSerializer()
    def post(self):
        data = request.get_json()
        try:
            data_serializada = self.serilizador.load(data)
            nueva_categoria = Categoria(**data_serializada)
            conexion.session.add(nueva_categoria)
            conexion.session.commit()
            
            resultado = self.serilizador.dump(nueva_categoria)
            
            return{
                'mesaje': 'Categoria creada Exitosamente',
                'content': resultado
            }
        
        except ValidationError as error:
            return{
                'mesaje': 'Error al crear categoría',
                'content': error.args
            }
    
    def get(self):
        categorias = conexion.session.query(Categoria).all()
        
        return{
            'content': self.serilizador.dump(categorias, many=True)
        }
