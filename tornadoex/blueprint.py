# coding=utf-8
from tornado.web import RequestHandler, URLSpec


class Blueprint(object):
    ROUTES = []

    def __init__(self, name, url_prefix=''):
        self.name = name
        self.url_prefix = url_prefix

    def route(self, route, host=".*$", name=None, initialize={}):
        def decorator(handler):
            _name = name or handler.__name__
            spec = URLSpec(self.url_prefix + route, handler, initialize, name='%s.%s' % (self.name, _name))
            self.ROUTES.append({'host': host, 'spec': spec})
            return handler
        return decorator

    def register_route(self, app):
        for route in self.ROUTES:
            app.add_handlers(route['host'], [route['spec']])





