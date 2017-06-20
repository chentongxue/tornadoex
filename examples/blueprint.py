# coding=utf-8
from tornadoex.app import Application
from tornadoex.blueprint import Blueprint
from tornadoex.handler import BaseRequestHandler

app = Application('config.cfg')

frontend_blueprint = Blueprint('frontend')


@frontend_blueprint.route('/', name='frontend.index')
class FrontendHandler(BaseRequestHandler):
    def get(self):
        return self.write('hello world')


user_blueprint = Blueprint('user', url_prefix='/user')


@user_blueprint.route('', name='user.index')
class UserHandler(BaseRequestHandler):
    def get(self):
        return self.write('user')


app.register_blueprint(frontend_blueprint)
app.register_blueprint(user_blueprint)

if __name__ == '__main__':
    app.run()
