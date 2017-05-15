import io
import os.path
import mimetypes
from wsgiref.util import FileWrapper

from rpn_project import settings, utils

STATIC_PATH = os.path.join(settings.BASEDIR, 'static')

def serve_static_file(url, file_obj, environ, start_response):
    type_, encoding = mimetypes.guess_type(url)
    start_response(b'200 OK', [(b'Content-Type', type_)])
    for chunk in FileWrapper(file_obj):
        yield chunk
    file_obj.close()

def static_app(environ, start_response):
    path = environ['PATH_INFO']
    segments = path.split(b'/')[2:] # skip /static
    segments = (segment for segment in segments if not segment.startswith('.'))
    fs_path = os.path.join(STATIC_PATH, *segments)
    try:
        static_file = io.open(fs_path, 'rb')
    except IOError:
        return utils.handle_404(environ, start_response)
    else:
        return serve_static_file(fs_path, static_file, environ, start_response)
