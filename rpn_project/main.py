from __future__ import unicode_literals, division
from ctypes import cdll

import json
import cgi
import os

from rpn_project import utils


def in_run(environ, start_response):

    text = utils.render_template('index.html')
    start_response(b'200 OK', [(b'Content-Type', b'text/html')])
    yield text


def out_run(environ, start_response):
    file = open("in.txt", 'w')

    try:
        request_body_size = int(environ.get('CONTENT_LENGTH', 0))
    except (ValueError):
        request_body_size = 0

    request_body = environ['wsgi.input'].read(request_body_size)
    count = int(cgi.parse_qs(request_body)['input_n'][0])
    file.write(str(count) + "\n")

    for i in range(count):
        exp = cgi.parse_qs(request_body)['exp'+str(i)]
        print(exp[0])

        file.write(exp[0] + "\n")

    file.close()

    run_script()

    filename = "out.txt"
    file = open(filename, 'r')
    listOut = ""

    for li in file:
        value = li.split()
        listOut = listOut + value[0] + u' '  + value[1] + u'</br>'

    file.close()
    os.remove(filename)

    text = utils.render_template('out_form.html', text=listOut)

    start_response(b'200 OK', [(b'Content-Type', b'text/html')])

    yield text


def run_script():
    lib = cdll.LoadLibrary('./command.so')

    print "Loaded go script"
    print lib.run()
