from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field
from models import Usuario, TipoUsuario
from marshmallow_enum import EnumField

class RegistroSerializer(SQLAlchemyAutoSchema):
    
    password = auto_field(required=True)
    tipoUsuario = EnumField(TipoUsuario)
    
    class Meta:
        model = Usuario