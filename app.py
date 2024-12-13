from flask import Flask
from instancias import conexion
from os import environ
from dotenv import load_dotenv
from flask_migrate import Migrate
from flask_restful import Api
from models import *
from controllers import *

load_dotenv()

app = Flask(__name__)
api = Api(app)
#print(environ.get('DATABASE_URL'))
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DATABASE_URL')
app.config['SQLALCHEMY_BINDS'] = {
    'postgres': environ.get('DATABASE_URL2')
}

conexion.init_app(app)

Migrate(app, conexion)

api.add_resource(CategoriaController, '/categorias')
api.add_resource(ManejoCategoriaController, '/categoria/<id>')
api.add_resource(ProductosController, '/productos')

if __name__ == '__main__':
    app.run(debug=True)