from __future__ import print_function, unicode_literals

from wsgiref.validate import validator
from wsgiref.simple_server import make_server

from rpn_project import app, settings

def main():
    # This is the application wrapped in a validator
    validator_app = validator(app.application)

    httpd = make_server(settings.HOST, settings.PORT, validator_app)
    print("Listening on {}:{}....".format(settings.HOST, settings.PORT))
    httpd.serve_forever()

if __name__ == '__main__':
    main()
