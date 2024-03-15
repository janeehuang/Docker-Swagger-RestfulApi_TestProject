
try:
    import argparse
    from flask import Flask
    from flask_restful import Resource, Api
    from apispec import APISpec
    from marshmallow import Schema, fields
    from apispec.ext.marshmallow import MarshmallowPlugin
    from flask_apispec.extension import FlaskApiSpec
    from flask_apispec.views import MethodResource
    from flask_apispec import marshal_with, doc, use_kwargs

    print("All imports are ok............")
except Exception as e:
    print("Error: {} ".format(e))

users = [{
    'name': 'kiki',
    'age': 3
}]




class InsertUsersController(MethodResource, Resource):

    @doc(description='This API Insert multiple Users', tags = ['insert_multifple_Users'])
    def interface():
        parser = argparse.ArgumentParser(description='data import')
        parser.add_argument('-o', '--override_warning', action='store_true',
                        help='override warnings and continue importing')
        parser = parser.parse_args()
        return parser
