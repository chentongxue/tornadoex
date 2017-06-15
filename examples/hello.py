# coding=utf-8
from tornadoex import Route, Application, Form
from tornado.web import RequestHandler
from wtforms.fields import IntegerField
from wtforms import validators


class TestForm(Form):
    age = IntegerField('age', [validators.DataRequired(u'不能为空')])


@Route('/')
class Test(RequestHandler):
    def get(self):
        form = TestForm(self)
        if form.validate():
            print 'allow'
        else:
            print form.errors
        return self.write('hello')

app = Application('config.cfg')


if __name__ == '__main__':
    app.run()
