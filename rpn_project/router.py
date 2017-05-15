from __future__ import unicode_literals

from rpn_project import utils

class Router(object):

    def __init__(self):
        self.prefixes = []
        self.matches = []

    def add_prefix(self, prefix, app):
        self.prefixes.append((prefix, app))

    def add_exact(self, path, app):
        self.matches.append((path, app))

    def __call__(self, environ, start_response):
        path = environ['PATH_INFO']

        for prefix, app in self.prefixes:
            if path.startswith(prefix):
                return app(environ, start_response)

        for match_path, app in self.matches:
            if match_path == path:
                return app(environ, start_response)

        return utils.handle_404(environ, start_response)
