
try:
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




class UserControllerSchema(Schema):
    name = fields.String(required=True, description="name is required")
    age = fields.Number(required=True, description="age is required")



class UserController(MethodResource, Resource):

    @doc(description='This API add User', tags = ['add_User'])
    @use_kwargs(UserControllerSchema, location=('json'))
    def post(self,**kwargs):
        global users
        _mes_name = kwargs.get("name")
        _mes_age = kwargs.get("age")
        user = {"name": _mes_name, "age": _mes_age}
        users.append(user)
        return {
            'message': 'Insert user success',
            'user': user
        }
    
    @doc(description='This API delete User', tags = ['delete_User'])
    @use_kwargs(UserControllerSchema, location=('json'))
    def delete(self, **kwargs):
        global users
        _mes_name = kwargs.get("name")
        users = [item for item in users if item['name'] != _mes_name]
        return {
            'message': 'Delete done!'
        }
            
    @doc(description='This API List Users', tags = ['list_User'])
    def get(self):
        return {
            'message': '',
            'users': users
        }
    
    @doc(description='This API update User', tags = ['update_User'])
    @use_kwargs(UserControllerSchema, location=('json'))
    def put(self, **kwargs):
        global users
        _mes_name = kwargs.get("name")
        find = [item for item in users if item['name'] == _mes_name]
        if len(find) == 0:
            return {
                'message': 'username not exist!'
            }, 403
        user = find[0]
        user['age'] = kwargs.get("age")
        return {
            'message': 'Update user success',
            'user': user
        }