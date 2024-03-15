from flask import Flask
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
from apispec import APISpec
from marshmallow import Schema, fields
from flask_cors import CORS
from flask_marshmallow import Marshmallow
from apispec.ext.marshmallow import MarshmallowPlugin
from flask_apispec.extension import FlaskApiSpec
from flask_apispec.views import MethodResource
from flask_apispec import marshal_with, doc, use_kwargs
import datetime

from API.ClusterHealth.views import HeathController
from API.User.views import UserController
from API.User.views2 import InsertUsersController


app = Flask(__name__)# Flask app instance initiated
api = Api(app)  # Flask restful wraps Flask app around it.
app.config.update({
    'APISPEC_SPEC': APISpec(
        title='Test Project',
        version='v1',
        plugins=[MarshmallowPlugin()],
        openapi_version='2.0.0'
    ),
    'APISPEC_SWAGGER_URL': '/swagger/',  # URI to access API Doc JSON
    'APISPEC_SWAGGER_UI_URL': '/swagger-ui/'  # URI to access UI of API Doc
})
docs = FlaskApiSpec(app)