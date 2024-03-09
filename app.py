from controllers.HomeController import home_bp
from controllers.UserController import user_bp
from appconfig import config
from DBInit import  app

#DB Setup
#Controller Registration
app.register_blueprint(home_bp, url_prefix='/home')
app.register_blueprint(user_bp, url_prefix='/users')



if __name__ == '__main__':
    app.run(host=config['HOST'], port=config['PORT'])



