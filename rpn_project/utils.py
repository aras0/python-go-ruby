from __future__ import unicode_literals

import datetime
import os.path
import io
from cgi import escape

from rpn_project import settings

TEMPLATE_DIR = os.path.join(settings.BASEDIR, 'templates')

TEMPLATE_CACHE = {}

def load_template(name):
    template_path = os.path.join(TEMPLATE_DIR, name)
    with io.open(template_path, 'r', encoding='utf-8') as template:
        template_string = template.read()
    return template_string

def render_template(name, **context):
    if name not in TEMPLATE_CACHE:
        TEMPLATE_CACHE[name] = load_template(name)
    template_string = TEMPLATE_CACHE[name]
    text = template_string.format(**context)
    return text.encode('utf-8')

def handle_404(environ, start_response):
    start_response(b'404 NOTFOUND', [(b'Content-Type', b'text/plain')])
    yield b'404 Not found'
