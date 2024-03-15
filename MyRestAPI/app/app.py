from dotenv import load_dotenv
load_dotenv()
from API import (app,
                     api,
                     HeathController,
                     UserController,
                     InsertUsersController,
                     docs

                     )

# try:
#     from API import (app,
#                      api,
#                      HeathController,docs

#                      )
# except Exception as e:
#     print("Modules are Missing : {} ".format(e))

api.add_resource(HeathController, '/health_check')
docs.register(HeathController)

api.add_resource(UserController, '/greet_user')
docs.register(UserController)

api.add_resource(InsertUsersController, '/insert_csv')
docs.register(InsertUsersController)