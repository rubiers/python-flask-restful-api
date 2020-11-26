import os
from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flaskext.mysql import MySQL

# Import project structure
from . import configmodule, resources, models, schemas

app = Flask(__name__)

### App environment
app_env = os.environ.get('FLASK_ENV') or 'development'
app.config.from_object(
    configmodule.loadConfig(app_env)
)
api = Api(app)

### Database
models.db.init_app(app)
migrate = Migrate(app, models.db)

### Serializer
ma = schemas.ma.init_app(app)

api.add_resource(resources.Users, '/users', '/users/<string:id>')
